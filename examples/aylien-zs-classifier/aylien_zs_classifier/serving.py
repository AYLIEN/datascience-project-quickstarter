import argparse
from aylien_model_serving.app_factory import FlaskAppWrapper
from aylien_zs_classifier.classifier import ZeroShotClassifier
from aylien_zs_classifier.vector_store import NaiveVectorStore
from aylien_zs_classifier.vector_store import EmptyVectorStoreException
from sentence_transformers import SentenceTransformer


def run_app():

    model = SentenceTransformer("paraphrase-mpnet-base-v2", device="cpu")
    classifier = ZeroShotClassifier(
        model=model, vector_store=NaiveVectorStore()
    )

    def reset():
        classifier.reset()
        return {}

    def add_label(label, description):
        classifier.add_labels([label], [description])
        return {}

    def remove_label(label):
        classifier.remove_labels([label])
        return {}

    def classify(text, threshold=0.0, topk=1):
        texts = [text]
        try:
            scored_labels = classifier.predict(
                texts, threshold=threshold, topk=topk, output_scores=True
            )[0]
            labels, scores = zip(*scored_labels)
            response = {
                "labels": list(labels),
                "scores": list(scores)
            }
        except EmptyVectorStoreException as e:
            response = {
                "error": "EmptyVectorStoreException"
            }
        return response

    def process_reset_request():
        return FlaskAppWrapper.process_json(reset)

    def process_add_label_request():
        return FlaskAppWrapper.process_json(add_label)

    def process_remove_label_request():
        return FlaskAppWrapper.process_json(remove_label)

    def process_classify_request():
        return FlaskAppWrapper.process_json(classify)

    routes = [
        {
            "endpoint": "/reset",
            "callable": process_reset_request,
            "methods": ["POST"]
        },
        {
            "endpoint": "/add",
            "callable": process_add_label_request,
            "methods": ["POST"]
        },
        {
            "endpoint": "/remove",
            "callable": process_remove_label_request,
            "methods": ["POST"]
        },
        {
            "endpoint": "/classify",
            "callable": process_classify_request,
            "methods": ["POST"]
        }
    ]
    return FlaskAppWrapper.create_app(routes)
