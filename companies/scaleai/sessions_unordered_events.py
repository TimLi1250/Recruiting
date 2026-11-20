# Reconstruct user sessions from unordered events and reconcile charges.

from typing import TypedDict


class Event(TypedDict):
    user_id: str
    timestamp: int
    kind: str  # "login", "logout", or "action"


class Session(TypedDict):
    user_id: str
    start: int
    end: int


class Charge(TypedDict):
    user_id: str
    timestamp: int
    amount: int | float


class Summary(TypedDict):
    number_of_sessions: int
    active_minutes: int


class ReconcileCharges(TypedDict):
    orphan_charges: list[Charge]
    unbilled_sessions: list[Session]


def build_sessions(events: list[Event]) -> dict[str, Summary]:
    # active_sessions should be dict of {user: [int, int, int, etc. ]}
    active_sessions = {}
    completed_sessions = {}
    sorted_events = sorted(events, key = lambda i: (i["user_id"], i["timestamp"]))
    for event in sorted_events:
        user, time, type = event["user_id"], event["timestamp"], event["kind"]
        if type == "login":

            # Three different cases
            # 1. No user is in active_sessions -> add user to active_sessions
            # 2. User in active_sessions -> update user in active_session
            # 3. User in active_sessions is different -> process previous user before adding new user
            if len(active_sessions) == 0:
                active_sessions[user] = [time]
            else:
                if user not in active_sessions:
                    curr = user
                    popped_user = next(iter(active_sessions))
                else:
                    curr = user
                    popped_user = user

                # The same user has already login, and we must close the session based on the last action
                # Last element should be the last action
                current_session = active_sessions.pop(popped_user)
                last_action  = current_session[-1]
                starting_time = current_session[0]

                if last_action != starting_time:
                    if popped_user not in completed_sessions:
                        completed_sessions[popped_user] = Summary(number_of_sessions=1, active_minutes=last_action - starting_time)
                    else:
                        completed_sessions[popped_user]["number_of_sessions"] += 1
                        completed_sessions[popped_user]["active_minutes"] += last_action - starting_time

                # After replacing the old login, we have to start the new session:
                active_sessions[curr] = [time]

        elif type == "action":
            # Here we just need to see if a login is open, if so we append it to the end of the active_sessions dict
            if user in active_sessions:
                active_sessions[user].append(time)
        elif type == "logout":
            # Now we just close previous logins, if previous login DNE, we don't need to do anything
            if user in active_sessions:
                starting_time = active_sessions.pop(user)[0]
                if user not in completed_sessions:
                    completed_sessions[user] = Summary(number_of_sessions=1, active_minutes=time - starting_time)
                else:
                    completed_sessions[user]["number_of_sessions"] += 1
                    completed_sessions[user]["active_minutes"] += time - starting_time

    for user, current_session in active_sessions.items():
        starting_time = current_session[0]
        last_action = current_session[-1]

        if last_action != starting_time:
            if user not in completed_sessions:
                completed_sessions[user] = Summary(
                    number_of_sessions=1,
                    active_minutes=last_action - starting_time,
                )
            else:
                completed_sessions[user]["number_of_sessions"] += 1
                completed_sessions[user]["active_minutes"] += (
                    last_action - starting_time
                )




    return completed_sessions

def reconcile_charges(events: list[Event], ledgers: list[Charge]) -> ReconcileCharges:
    # 1. We need to create a new dict but instead of dict[user, Summary], we want to do dict[user, start_time, end_time]
    # This will be very similar to build_sessions
    active_sessions = {}
    completed_sessions = {}
    sorted_events = sorted(events, key = lambda i: (i["user_id"], i["timestamp"]))
    for event in sorted_events:
        user, time, type = event["user_id"], event["timestamp"], event["kind"]
        if type == "login":

            # Three different cases
            # 1. No user is in active_sessions -> add user to active_sessions
            # 2. User in active_sessions -> update user in active_session
            # 3. User in active_sessions is different -> process previous user before adding new user
            if len(active_sessions) == 0:
                active_sessions[user] = [time]
            else:
                if user not in active_sessions:
                    curr = user
                    popped_user = next(iter(active_sessions))
                else:
                    curr = user
                    popped_user = user

                # The same user has already login, and we must close the session based on the last action
                # Last element should be the last action
                current_session = active_sessions.pop(popped_user)
                last_action  = current_session[-1]
                starting_time = current_session[0]

                if last_action != starting_time:
                    if popped_user not in completed_sessions:
                        completed_sessions[popped_user] = [[starting_time, last_action]]
                    else:
                        completed_sessions[popped_user].append([starting_time, last_action])

                # After replacing the old login, we have to start the new session:
                active_sessions[curr] = [time]

        elif type == "action":
            # Here we just need to see if a login is open, if so we append it to the end of the active_sessions dict
            if user in active_sessions:
                active_sessions[user].append(time)
        elif type == "logout":
            # Now we just close previous logins, if previous login DNE, we don't need to do anything
            if user in active_sessions:
                starting_time = active_sessions.pop(user)[0]
                if user not in completed_sessions:
                    completed_sessions[user] = [[starting_time, time]]
                else:
                    completed_sessions[user].append([starting_time, time])

    for user, current_session in active_sessions.items():
        starting_time = current_session[0]
        last_action = current_session[-1]

        if last_action != starting_time:
            if user not in completed_sessions:
                completed_sessions[user] = [[starting_time, last_action]]
            else:
                completed_sessions[user].append([starting_time, last_action])

    # 2. Now we have a dict of [user, intervals] where intervals are like [[2, 4], [3, 6], etc.]

    orphan_charges = []
    unbilled_sessions = []
    billed = set()

    for charge in ledgers:
        user, time = charge["user_id"], charge["timestamp"]
        # If user is not in completed_sessions -> automatically an orphan charge
        matched = False

        # Otherwise we need to see if the time stamp is within any of that user's sessions
        intervals = completed_sessions.get(user, [])
        for idx, interval in enumerate(intervals):
            start, end = interval[0], interval[1]
            if start <= time < end:
                billed.add((user, idx))
                matched = True
                break

        # If not, it is also added as an orphan charge
        if not matched:
            orphan_charges.append(charge)

    # Whatever is left in completed_sessions should now be the unbilled_sessions
    for user, intervals in completed_sessions.items():
        for idx, interval in enumerate(intervals):
            if (user, idx) not in billed:
                start, end = interval
                unbilled_sessions.append(Session(user_id=user, start=start, end=end))
                
    return ReconcileCharges(orphan_charges=orphan_charges, unbilled_sessions=unbilled_sessions)
