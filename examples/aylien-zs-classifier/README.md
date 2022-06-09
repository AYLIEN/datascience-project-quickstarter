## Example Project: Zero-shot Event Classification

We included an example data science project that works out of the box.
The project implements a very simple zero-shot classifier that can classify texts only based on short descriptions of classes rather than examples.

#### New environment
To use or work on this project, we first want to create a project-specific Python environment, let's call it `zsc`. <br>

With Anaconda:
```bash
# Create new environment
conda create -n zsc python=3.8
# Activate new environment
conda activate zsc
```

Option 2 with Venv:
```bash
# Create new environment
python3.8 -m venv zsc
# Activate new environment
source zsc/bin/activate
```

#### Install
Run `make dev`

This will install the dependencies in `requirements.txt` and the `zs_classification` library in development mode.

Currently we also need install `model-serving`:

```
git clone git@github.com:AYLIEN/model-serving.git
pip install ./model-serving
```

#### Using the example library

Using the `aylien_zs_classifier` library to create a zero-shot text classifier:
```python
from aylien_zs_classifier.classifier import ZeroShotClassifier
from aylien_zs_classifier.vector_store import NaiveVectorStore
from sentence_transformers import SentenceTransformer
from pprint import pprint


model = SentenceTransformer("paraphrase-mpnet-base-v2", device="cpu")
classifier = ZeroShotClassifier(model=model, vector_store=NaiveVectorStore())

labels = ["fire", "water", "wind"]
descriptions = ["fire", "water", "wind"]
classifier.add_labels(labels, descriptions)

snippets = ["flame", "ocean", "hurricane"]
predictions = classifier.predict(snippets, output_scores=True)
pprint(predictions)
```

#### Using the example service

We also include an example service to demonstrate exposing your library via a REST API.
Use `make run` to get the service running locally. You can now create and interact with a classifier via post requests:

| Endpoint | Request Format | Explanation |
|---|---|---|
| `/add` | `{"label": "<label>", "description": "<description>"}` | Adding a new label |
| `/classify` | At minimum: `{"text": "<text>"}`<br>Optional settings: `{"text": "<text>", "threshold": 0.1, "topk": 10}` | Classify a text snippet |
| `/remove` | `{"label": "<label>"}` | Remove a label |
| `/reset` | (no data) | Delete all labels |

The requests have to follow a Protobuf schema defined in [schema.proto](schema.proto).

We provide request examples in [research/library_usage.py](research/service_usage.py).

## Docker image

Deployment will be easy once you have a working Docker image!
We can containerize our service by creating a Docker image:

```bash
# create Docker image
make build

# run container locally
docker run -p 8000:8000 -e --rm -it zs-classifier:0.1
```
