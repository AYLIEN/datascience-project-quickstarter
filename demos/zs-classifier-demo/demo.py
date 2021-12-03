import argparse
import numpy as np
import json
from pathlib import Path
from pprint import pprint
from copy import deepcopy
from collections import defaultdict
import streamlit as st
import streamlit.components.v1 as components
import streamlit.report_thread as ReportThread
from streamlit.server.server import Server

from zs_classification.classifier import ZeroShotClassifier
from sentence_transformers import SentenceTransformer

page_config = st.set_page_config(
    page_title='Zero-Shot Classification',
)
#
# MODEL = SentenceTransformer("paraphrase-mpnet-base-v2", device="cpu")

def get_session_state():
    session_id = ReportThread.get_report_ctx().session_id
    session_info = Server.get_current()._get_session_info(session_id)

    if session_info is None:
        raise RuntimeError('Could not get Streamlit session object.')

    # this session object
    this_session = session_info.session

    # Initialize user state if session doesn't exist
    if not hasattr(this_session, '_custom_session_state'):
        user_state = {
            "classifier": None,
            "label_to_description": {},
        }
        this_session._custom_session_state = user_state

    return this_session._custom_session_state


@st.cache(allow_output_mutation=True)
def load_model():
    model = SentenceTransformer("paraphrase-mpnet-base-v2", device="cpu")
    return model


def build_classifier(label_to_desc):
    labels = sorted(label_to_desc)
    descriptions = [label_to_desc[l] for l in labels]
    model = load_model()
    classifier = ZeroShotClassifier(model)
    classifier.train(labels, descriptions)
    return classifier


def main():

    session_state = get_session_state()
    st.write("# Simple Zero-Shot Text Classification")

    label_to_desc = session_state["label_to_description"]

    st.write("### Build Classifier")
    default_input = (
        "\n".join([f"{l}: {d}" for l, d in label_to_desc.items()])
        if len(label_to_desc) > 0
        else "good news: happy great nice\nbad news: sad angry horrible bad"
    )
    input = st.text_area(
        "In each line, enter a label and description (separated with ':')",
        value=default_input
    ).strip()

    if st.button("build classifier"):

        lines = input.split("\n")
        label_to_desc = {}
        for line in lines:
            label, desc = line.split(":")
            label, desc = label.strip(), desc.strip()
            label_to_desc[label] = desc
        session_state["label_to_description"] = label_to_desc
        classifier = build_classifier(label_to_desc)
        session_state["classifier"] = classifier


    label_to_desc = session_state["label_to_description"]
    if len(label_to_desc) > 0:
        st.write("Your labels:")
        st.write(label_to_desc)

    st.write("### Use Classifier")
    input = st.text_area("Enter text to classify", "it's a sunny day")
    if st.button("Classify"):
        classifier = session_state["classifier"]
        _, scored = classifier.predict([input], output_scores=True)
        scored = scored[0]
        top_label = scored[0][0]
        st.write(f"This text is classified as `{top_label}`.")
        st.write("Score breakdown:")
        st.write(dict(scored))
        # for l, score in scored:
        #     st.write(f"{l}: `{score:.3f}`")





if __name__ == '__main__':
    main()
