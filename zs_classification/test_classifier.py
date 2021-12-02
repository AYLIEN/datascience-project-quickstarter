import unittest
from zs_classification.classifier import ZeroShotClassifier
from sentence_transformers import SentenceTransformer


class TestClassifier(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.model = SentenceTransformer(
            "paraphrase-mpnet-base-v2",
            device="cpu"
        )

    def test_example(self):
        labels = ["fire", "water", "wind"]
        descriptions = ["fire", "water", "wind"]
        classifier = ZeroShotClassifier(model=self.model)
        classifier.train(labels, descriptions)
        snippets = ["flame", "ocean", "hurricane"]
        predicted_labels = classifier.predict(snippets)
        assert predicted_labels == labels


if __name__ == '__main__':
    unittest.main()
