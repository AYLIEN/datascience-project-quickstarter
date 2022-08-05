import requests
import json


def reverse(text):
    data = {
        "text": text
    }
    headers = {'Content-type': 'application/json'}
    r = requests.post(
        'http://0.0.0.0:8000/reverse',
        headers=headers,
        data=json.dumps(data)
    )
    print("response to reverse request:")
    print(r.text)


def count():
    headers = {'Content-type': 'application/json'}
    r = requests.post(
        'http://0.0.0.0:8000/count',
        headers=headers,
        data=json.dumps({})
    )
    print("response to count request:")
    print(r.text)


def main():
    count()
    count()
    reverse("hello")


if __name__ == '__main__':
    main()
