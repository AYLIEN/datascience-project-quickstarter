import requests
import json


def reset():
    headers = {'Content-type': 'application/json'}
    r = requests.post(
        'http://0.0.0.0:8000/reset',
        headers=headers,
        data=json.dumps({})
    )
    print("response to reset request:")
    print(r.text)


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
    print("response to remove request:")
    print(r.text)


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
    print("response to add request:")
    print(r.text)


def classify(text, topk=1):
    data = {
        "text": text,
        "topk": topk
    }
    headers = {'Content-type': 'application/json'}
    r = requests.post(
        'http://0.0.0.0:8000/classify',
        headers=headers,
        data=json.dumps(data)
    )
    print("response to classify request:")
    print(r.text)


def main():
    reset()
    add_label("TENNIS", "tennis")
    add_label("BASKETBALL", "basketball")
    add_label("SOCCER", "soccer")
    add_label("WRESTLING", "wrestling")
    add_label("", "running")
    remove_label("WRESTLING")
    remove_label("UNKNOWN-LABEL")
    classify("Serena Williams", topk=2)
    classify("Lebron James", topk=2)


if __name__ == '__main__':
    main()
