import unittest
import json
import aylien_model_serving.service as svc
from aylien_zs_classifier.serving import ServingHandler
from aylien_zs_classifier.classifier import ZeroShotClassifier
from aylien_zs_classifier.vector_store import NaiveVectorStore
from sentence_transformers import SentenceTransformer

examples_add = [
    {"label": "WIND", "description": "wind"},
    {"label": "FIRE", "description": "fire"},
    {"label": "WATER", "description": "water"},
]

example_classify = {"text": "It's windy today."}

example_remove = {"label": "WIND"}

example_reset = {}


class TestServingHandler(ServingHandler):
    """
    Simplified handler class that is easier to initialise for testing.
    """

    def __init__(self, model):
        self.classifier = ZeroShotClassifier(
            model=model, vector_store=NaiveVectorStore()
        )
        self.label_to_description = {}


class TestServing(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.model = SentenceTransformer(
            "paraphrase-mpnet-base-v2", device="cpu"
        )

    def test_add_label(self):
        handler = TestServingHandler(self.model)
        for r in examples_add:
            request = handler.json_in(json.dumps(r))
            response = handler.handle_add_label(request)
            assert len(response.error) == 0
        assert len(handler.classifier.v.ids) == len(examples_add)

    def test_classify(self):
        handler = TestServingHandler(self.model)
        for r in examples_add:
            request = handler.json_in(json.dumps(r))
            response = handler.handle_add_label(request)
        request = handler.json_in(json.dumps(example_classify))
        response = handler.handle_classify(request)
        assert len(response.error) == 0

    def test_classify_without_add(self):
        handler = TestServingHandler(self.model)
        request = handler.json_in(json.dumps(example_classify))
        with self.assertRaises(svc.RequestFailed):
            handler.handle_classify(request)

    def test_remove_label(self):
        handler = TestServingHandler(self.model)
        for r in examples_add:
            request = handler.json_in(json.dumps(r))
            response = handler.handle_add_label(request)
        request = handler.json_in(json.dumps(example_remove))
        response = handler.handle_remove_label(request)
        assert len(handler.classifier.v.ids) == len(examples_add) - 1
        assert len(response.error) == 0

    def test_reset(self):
        handler = TestServingHandler(self.model)
        for r in examples_add:
            request = handler.json_in(json.dumps(r))
            response = handler.handle_add_label(request)
        request = handler.json_in(json.dumps(example_reset))
        response = handler.handle_reset(request)
        assert len(response.error) == 0
        with self.assertRaises(svc.RequestFailed):
            handler.handle_classify(request)


if __name__ == "__main__":
    unittest.main()
