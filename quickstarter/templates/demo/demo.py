import streamlit as st
# importing tools from your library into the demo:
from {{PKG_NAME}}.example_module import Counter, TextReverser


page_config = st.set_page_config(
    page_title="Demo",
)


def get_session_state():
    # Initialize session state
    if not st.session_state.get('INIT', False):
        st.session_state['counter'] = Counter()

    st.session_state['INIT'] = True
    return st.session_state


def main():
    session_state = get_session_state()
    text_reverser = TextReverser()
    counter = session_state["counter"]

    st.write("# Simple Streamlit Demo")

    if st.button("Click Me"):
        counter()
    clicks = counter.count
    st.write(
        f"This button has been clicked {clicks} times in this session."
    )

    text = st.text_input("Enter text")
    if st.button("Click to reverse text"):
        new_text = text_reverser(text)
        st.write(new_text)


if __name__ == '__main__':
    main()
