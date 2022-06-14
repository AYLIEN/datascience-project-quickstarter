import pytest
import json

from aylien_model_serving.app_factory import FlaskAppWrapper

from aylien_zs_classifier.serving import run_app
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


@pytest.fixture(scope="session", autouse=True)
def client():
    test_app = run_app()
    test_client = test_app.test_client()
    return test_client


def post_json(client, url, json_dict):
    """Send dictionary json_dict as json to the specified url"""
    response = client.post(
        url, data=json.dumps(json_dict), content_type="application/json"
    )
    return json.loads(response.data)


def test_client_works(client):
    response = client.get("/__ping")
    assert b"Success" in response.data


def test_classify_without_add(client):
    response = post_json(client, "/classify", example_classify)
    assert response["error"] == "EmptyVectorStoreException"


def test_classify(client):
    for req in examples_add:
        post_json(client, "/add", req)
    response = post_json(client, "/classify", example_classify)
    assert response["labels"][0] == "WIND"


def test_remove_label(client):
    for req in examples_add:
        post_json(client, "/add", req)
    response = post_json(client, "/remove", example_remove)
    assert response["error"] == "0"


def test_reset(client):
    for req in examples_add:
        post_json(client, "/add", req)
    post_json(client, "/reset", example_reset)
    response = post_json(client, "/classify", example_classify)
    assert response["error"] == "EmptyVectorStoreException"
