## Example Project: Zero-shot Event Classification

We included an example data science project that works out of the box.
The project implements a very simple zero-shot classifier that can classify texts only based on short descriptions of classes rather than examples.

#### New environment
To use or work on this project, we first want to create a project-specific Python environment, let's call it `zsc`. <br>

We like to use Anaconda/Miniconda but feel free to use other options:
```bash
# Create new environment
conda create -n zsc python=3.8
# Activate new environment
conda activate zsc
```

#### Install
Run `make dev`

This will install the dependencies in `requirements.txt` and the `aylien_zs_classifier` library in development mode.

Currently we also need install `model-serving`:

```
git clone git@github.com:AYLIEN/model-serving.git
pip install ./model-serving
```

#### Using the library

Using the `aylien_zs_classifier` library, you can create and use a zero-shot text classifier:
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

""" output looks like this:
[[('fire', 0.7852495908737183),
  ('wind', 0.31472715735435486),
  ('water', 0.25439903140068054)],
 [('water', 0.5859522819519043),
  ('wind', 0.3676087260246277),
  ('fire', 0.22406277060508728)],
 [('wind', 0.48003238439559937),
  ('water', 0.2777974009513855),
  ('fire', 0.2622990310192108)]]
"""
```

#### Using the service

We also include a service to expose this library via a REST API.
Use `make run` to get the service running locally. You can now create and interact with a classifier via post requests:

| Endpoint | Request Format | Explanation |
|---|---|---|
| `/add` | `{"label": "<label>", "description": "<description>"}` | Adding a new label |
| `/classify` | At minimum: `{"text": "<text>"}`<br>Optional settings: `{"text": "<text>", "threshold": 0.1, "topk": 10}` | Classify a text snippet |
| `/remove` | `{"label": "<label>"}` | Remove a label |
| `/reset` | (no data) | Delete all labels |

You can check if the service is working by running `make example-request-add` and `make-request-classify`.

We also put together some more examples for interacting with the service: [examples/service_examples.py](examples/service_examples.py).

## Docker image

Deployment will be easy once you have a working Docker image!
We can containerize our service by creating a Docker image:

```bash
# create Docker image
make build

# run container locally
docker run -p 8000:8000 -e --rm -it zs-classifier:0.1
```

## Demo

Check out the demo for this project [here](demos/zs-classifier-demo) where you can create and interact with a classifier on a UI.
