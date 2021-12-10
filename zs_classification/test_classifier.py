import unittest
import numpy as np
from zs_classification.classifier import ZeroShotClassifier
from zs_classification.vector_store import NaiveVectorStore
from sentence_transformers import SentenceTransformer


class TestClassifier(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.model = SentenceTransformer(
            "paraphrase-mpnet-base-v2",
            device="cpu"
        )
        cls.labels = ["FIRE", "WATER", "WIND"]
        cls.descriptions = ["fire", "water", "wind"]

    def test_add_labels(self):
        classifier = ZeroShotClassifier(
            model=self.model,
            vector_store=NaiveVectorStore()
        )
        classifier.add_labels(self.labels, self.descriptions)
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
        labels = [l for l, score in predictions[0]]
        assert "FIRE" not in labels

    def test_threshold(self):
        classifier = ZeroShotClassifier(
            model=self.model,
            vector_store=NaiveVectorStore()
        )
        classifier.add_labels(self.labels, self.descriptions)
        snippets = ["flame", "ocean", "hurricane"]
        for t in np.arange(0., 1., 0.1):
            predictions = classifier.predict(
                snippets, threshold=t, output_scores=True
            )
            scores = [score for pred in predictions for l, score in pred]
            assert len(scores) == 0 or max(scores) >= t



if __name__ == '__main__':
    unittest.main()
