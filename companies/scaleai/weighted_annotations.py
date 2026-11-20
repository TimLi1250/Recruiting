# Annotators assign labels to tasks. Their votes have different weights, and you must identify annotators who
# disagree too often with the task consensus.

# Implement this stateful interface:
#
# class WeightedAnnotations:
#     __init__(trust: dict[annotator_id, float])
#     submit(task_id, annotator_id, label) -> None
#     analyze() -> (consensus, flagged)
#
# `submit()` records one annotator's label for one task. `analyze()` uses all
# submissions recorded on this instance.

# Part A - Consensus. For each task, total the trust weights of annotators choosing each label. Choose the
# label with the highest weight; break exact ties by lexicographically smallest label.

class WeightedAnnotations:
    def __init__(self, trust):
        self.trust = trust
        self.submissions = []
        self.consensus = {}

    def submit(self, task_id, annotator_id, label):
        # Part C, so now instead of appending here we just need to update
        self.update(task_id, annotator_id, label)

    # We want to return a dict: where we have (task, label with highest weight)
    def analyze(self):
        analysis = dict()

        # We should split this up into phases
        # 1. Total each label's vote weight for every task
        for sub in self.submissions:

            task, ann_id, label = sub[0], sub[1], sub[2]
            # We can have a dict of dicts to do this
            if task not in analysis:
                analysis[task] = {label: self.trust[ann_id]}
            else:
                if label in analysis[task]:
                    prev_weight = analysis[task].get(label)
                    analysis[task][label] = prev_weight + self.trust[ann_id]

                else:
                    analysis[task][label] = self.trust[ann_id]

        # 2. Select each task's consensus label
        for task_id, label_weights in analysis.items():
            self.consensus[task_id] = min(label_weights.items(), key = lambda item: (-item[1], item[0]))[0]

        return self.consensus


    # Part B - Outliers. For each annotator, calculate the fraction of their submissions matching that task's
    # consensus. Return IDs whose accuracy is strictly less than 0.60, sorted alphabetically.

    # Here we want to return a dict of {annotator : IDs whose accuracy }
    def outliers(self):
        self.analyze()
        outliers = {}
        for sub in self.submissions:

            task, ann_id, label = sub[0], sub[1], sub[2]

            consensus_label = self.consensus[task]
            if ann_id not in outliers:

                if label == consensus_label:
                    # Store as array not a tuple because we are frequently going to change these numbers
                    outliers[ann_id] = [1, 1]
                else:
                    outliers[ann_id] = [0, 1]
            else:
                if label == consensus_label:
                    outliers[ann_id][0] += 1
                    outliers[ann_id][1] += 1
                else:
                    outliers[ann_id][1] += 1

        # Now outliers should be a dict with items {ann_id: [5, 7]}
        outliers_list = []
        for ann_id, counter in outliers.items():
            if counter[0]/counter[1] < 0.6:
                outliers_list.append(ann_id)

        # This is the same as returning sorted(outliers_list)
        # return sorted(outliers_list, key=lambda i: i)
        return sorted(outliers_list)

    # Part C - Updates. Allow repeated submissions for the same (task, annotator) pair. Only the last submission
    # from that pair counts for both consensus and accuracy

    def update(self, submission):
        task_id, ann_id, label = submission[0], submission[1], submission[2]
        for i, sub in enumerate(self.submissions):
            if sub[:2] == (task_id, ann_id):
                self.submissions[i] = (task_id, ann_id, label)
                return
        self.submissions.append((task_id, ann_id, label))
