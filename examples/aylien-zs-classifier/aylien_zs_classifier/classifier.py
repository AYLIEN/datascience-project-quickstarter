class EmptyTextException(Exception):
    pass


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

    def reset(self):
        self.v.reset()

    def add_labels(self, labels, descriptions):
        if any([t.strip() == "" for t in labels]):
            raise EmptyTextException("At least one label is an empty text.")
        if any([t.strip() == "" for t in descriptions]):
            raise EmptyTextException(
                "At least one description is an empty text."
            )
        label_embeddings = self.model.encode(
            descriptions, convert_to_tensor=True
        )
        self.v.add(labels, label_embeddings)

    def remove_labels(self, labels):
        self.v.remove(labels)

    def predict(
            self,
            input_texts,
            threshold=0.0,
            output_scores=False,
            topk=None
    ):
        if any([t.strip() == "" for t in input_texts]):
            raise EmptyTextException(
                "At least one input text is empty."
            )

        input_embeddings = self.model.encode(
            input_texts, convert_to_tensor=True
        )
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
