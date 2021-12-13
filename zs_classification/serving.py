import argparse
import json
import cherrypy
import aylien_model_serving.service as svc
from zs_classification.classifier import ZeroShotClassifier
from zs_classification.vector_store import NaiveVectorStore
from zs_classification.vector_store import EmptyVectorStoreException
import zs_classification.schema_pb2 as schema
import google.protobuf.json_format as proto_json
from sentence_transformers import SentenceTransformer
from pprint import pprint


class ServingHandler:
    def __init__(self, args):
        self.logger = svc.create_logger(__name__)
        self.version = self._parse_args(args)
        model = SentenceTransformer(
            "paraphrase-mpnet-base-v2",
            device="cpu"
        )
        self.classifier = ZeroShotClassifier(
            model=model,
            vector_store=NaiveVectorStore()
        )
        self.label_to_description = {}

    def _parse_args(self, args):
        parser = argparse.ArgumentParser()
        parser.add_argument(
            '--version',
            type=str,
            default='0.1',
            help='an example argument to the handler'
        )
        parsed = parser.parse_args(args)
        return parsed.version

    def handlers(self):
        return {"/reset": self.handle_reset,
                "/add": self.handle_add_label,
                "/remove": self.handle_remove_label,
                "/classify": self.handle_classify}

    def handle_reset(self, request):
        request = proto_json.Parse(request, schema.ResetRequest())
        self.classifier.reset()
        return schema.ResetResponse()

    def handle_add_label(self, request):
        request = proto_json.Parse(request, schema.AddLabelRequest())
        self.classifier.add_labels(
            [request.label], [request.description]
        )
        return schema.AddLabelResponse()

    def handle_remove_label(self, request):
        request = proto_json.Parse(request, schema.RemoveLabelRequest())
        self.classifier.remove_labels([request.label])
        return schema.RemoveLabelResponse()

    def handle_classify(self, request):
        request = proto_json.Parse(request, schema.ClassifyRequest())
        texts = [request.text]
        threshold = request.threshold or None
        topk = request.topk or None

        try:
            scored_labels = self.classifier.predict(
                texts,
                threshold=threshold,
                topk=topk,
                output_scores=True
            )[0]
            scored_labels = [
                schema.ScoredLabel(label=l, score=s) for l, s in scored_labels
            ]
            response = schema.ClassifyResponse()
            response.scored_labels.extend(scored_labels)
        except EmptyVectorStoreException as e:
            raise svc.RequestFailed(e)
        return response

    def json_in(self, request):
        return request

    def json_out(self, response):
        return proto_json.MessageToJson(response).encode('utf-8')
