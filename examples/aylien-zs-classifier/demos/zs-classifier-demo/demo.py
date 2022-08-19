import streamlit as st
from aylien_zs_classifier.classifier import ZeroShotClassifier
from aylien_zs_classifier.vector_store import NaiveVectorStore
from sentence_transformers import SentenceTransformer

page_config = st.set_page_config(
    page_title='Zero-Shot Classification',
)


def get_session_state():
    state = st.session_state

    # Initialize user state if session doesn't exist
    if not state.get('INIT', False):
        state["classifier"] = None
        state["label_to_description"] = {}

    state['INIT'] = True
    return state


@st.cache(allow_output_mutation=True)
def load_model():
    model = SentenceTransformer("paraphrase-mpnet-base-v2", device="cpu")
    return model


def build_classifier(label_to_desc):
    labels = sorted(label_to_desc)
    descriptions = [label_to_desc[lb] for lb in labels]
    model = load_model()
    classifier = ZeroShotClassifier(
        model=model,
        vector_store=NaiveVectorStore()
    )
    classifier.add_labels(labels, descriptions)
    return classifier


def main():

    session_state = get_session_state()
    st.write("# Simple Zero-Shot Text Classification")

    label_to_desc = session_state["label_to_description"]

    st.write("### Build Classifier")
    default_input = (
        "\n".join([f"{lb}: {d}" for lb, d in label_to_desc.items()])
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
        scored = classifier.predict([input], output_scores=True)
        scored = scored[0]
        top_label = scored[0][0]
        st.write(f"This text is classified as `{top_label}`.")
        st.write("Score breakdown:")
        st.write(dict(scored))


if __name__ == '__main__':
    main()
