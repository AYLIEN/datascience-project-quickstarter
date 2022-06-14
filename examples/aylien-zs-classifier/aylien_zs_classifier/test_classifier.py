import numpy as np
from aylien_zs_classifier.classifier import ZeroShotClassifier
from aylien_zs_classifier.vector_store import NaiveVectorStore
from sentence_transformers import SentenceTransformer


class TestClassifier:
    model = SentenceTransformer(
        "paraphrase-mpnet-base-v2", device="cpu"
    )
    labels = ["FIRE", "WATER", "WIND"]
    descriptions = ["fire", "water", "wind"]

    def test_add_labels(self):
        classifier = ZeroShotClassifier(
            model=self.model, vector_store=NaiveVectorStore()
        )
        classifier.add_labels(self.labels, self.descriptions)
        snippets = ["flame", "ocean", "hurricane"]
        predicted_labels = classifier.predict(snippets)
        assert predicted_labels == self.labels

    def test_add_labels_separate(self):
        classifier = ZeroShotClassifier(
            model=self.model, vector_store=NaiveVectorStore()
        )
        for label, d in zip(self.labels, self.descriptions):
            classifier.add_labels([label], [d])
        snippets = ["flame", "ocean", "hurricane"]
        predicted_labels = classifier.predict(snippets)
        assert predicted_labels == self.labels

    def test_remove_labels(self):
        classifier = ZeroShotClassifier(
            model=self.model,
            vector_store=NaiveVectorStore(),
        )
        classifier.add_labels(self.labels, self.descriptions)
        classifier.remove_labels(["FIRE"])
        assert "FIRE" not in classifier.v.id_to_idx
        predictions = classifier.predict(["flame"], output_scores=True)
        labels = [label for label, score in predictions[0]]
        assert "FIRE" not in labels

    def test_threshold(self):
        classifier = ZeroShotClassifier(
            model=self.model, vector_store=NaiveVectorStore()
        )
        classifier.add_labels(self.labels, self.descriptions)
        snippets = ["flame", "ocean", "hurricane"]
        for t in np.arange(0.0, 1.0, 0.1):
            predictions = classifier.predict(
                snippets, threshold=t, output_scores=True
            )
            scores = [score for pred in predictions for _, score in pred]
            assert len(scores) == 0 or max(scores) >= t
