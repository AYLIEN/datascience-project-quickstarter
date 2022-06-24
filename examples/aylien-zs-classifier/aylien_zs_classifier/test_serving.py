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

empty_vec_msg = "Vector store is empty, needs to be populated before querying."


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
    assert response["error"] == empty_vec_msg


def test_add(client):
    for req in examples_add:
        response = post_json(client, "/add", req)
        assert response["error"] == 0


def test_add_empty(client):
    response = post_json(client, "/add", {"label": "", "description": "text"})
    assert response["error"] == "At least one label is an empty text."
    response = post_json(client, "/add", {"label": "text", "description": ""})
    assert response["error"] == "At least one description is an empty text."


def test_classify(client):
    for req in examples_add:
        post_json(client, "/add", req)
    response = post_json(client, "/classify", example_classify)
    assert response["labels"][0] == "WIND"


def test_remove(client):
    for req in examples_add:
        post_json(client, "/add", req)
    response = post_json(client, "/remove", example_remove)
    assert response["error"] == 0


def test_reset(client):
    for req in examples_add:
        post_json(client, "/add", req)
    post_json(client, "/reset", {})
    response = post_json(client, "/classify", example_classify)
    assert response["error"] == empty_vec_msg
