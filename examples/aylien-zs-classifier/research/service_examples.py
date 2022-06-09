import requests
import json
from aylien_zs_classifier import schema_pb2 as schema
import google.protobuf.json_format as proto_json
from pprint import pprint


def reset():
    headers = {'Content-type': 'application/json'}
    r = requests.post(
        'http://0.0.0.0:8000/reset',
        headers=headers,
        data=json.dumps({})
    )


def remove_label(label):
    data = {
        "label": label,
    }
    headers = {'Content-type': 'application/json'}
    r = requests.post(
        'http://0.0.0.0:8000/remove',
        headers=headers,
        data=json.dumps(data)
    )


def add_label(label, description):
    data = {
        "label": label,
        "description": description
    }
    headers = {'Content-type': 'application/json'}
    r = requests.post(
        'http://0.0.0.0:8000/add',
        headers=headers,
        data=json.dumps(data)
    )


def classify(text):
    data = {
        "text": text,
    }
    headers = {'Content-type': 'application/json'}
    r = requests.post(
        'http://0.0.0.0:8000/classify',
        headers=headers,
        data=json.dumps(data)
    )
    print(r.text)


def main():
    reset()
    add_label("TENNIS", "tennis")
    add_label("BASKETBALL", "basketball")
    add_label("SOCCER", "soccer")
    add_label("WRESTLING", "wrestling")
    remove_label("WRESTLING")
    classify("Lebron James")
    classify("Roger Federer")


if __name__ == '__main__':
    main()
