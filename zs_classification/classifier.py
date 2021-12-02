from sentence_transformers import util


class ZeroShotClassifier:
    def __init__(self, model=None, threshold=None, null_label="OTHER"):
        self.model = model
        self.labels = []
        self.label_embeddings = None
        self.threshold = threshold
        self.null_label = null_label

    def train(self, labels, descriptions):
        self.labels = labels
        self.label_embeddings = self.model.encode(descriptions)

    def predict(self, input_texts, output_scores=False):
        input_embeddings = self.model.encode(input_texts)
        S = util.pytorch_cos_sim(input_embeddings, self.label_embeddings)
        output_labels = []
        output_scorings = []
        for i in range(input_embeddings.shape[0]):
            label_scores = S[i].tolist()
            scored = sorted(
                zip(self.labels, label_scores),
                key=lambda x: x[1],
                reverse=True
            )
            pred, score = scored[0]
            if self.threshold is not None and score < self.threshold:
                pred = self.null_label
            output_labels.append(pred)
            output_scorings.append(scored)
        if output_scores:
            return output_labels, output_scorings
        else:
            return output_labels
