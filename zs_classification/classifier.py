import torch
from sentence_transformers import util


class ZeroShotClassifier:
    def __init__(
            self,
            model=None,
            vector_store=None,
            threshold=None,
            null_label="OTHER"
    ):
        self.model = model
        self.v = vector_store
        self.threshold = threshold
        self.null_label = null_label

    def add_labels(self, labels, descriptions):
        label_embeddings = self.model.encode(descriptions)
        self.v.add(labels, label_embeddings)

    def remove_labels(self, labels):
        self.v.remove(labels)

    def predict(
            self,
            input_texts,
            threshold=0.,
            output_scores=False,
            topk=None
        ):
        input_embeddings = self.model.encode(input_texts)
        nn_results = self.v.neighbors(
            input_embeddings,
            thresh=threshold,
            k=topk,
        )
        if output_scores:
            return nn_results
        else:
            labels = [
                (self.null_label if len(nns) == 0 else nns[0][0])
                for nns in nn_results
            ]
            return labels
