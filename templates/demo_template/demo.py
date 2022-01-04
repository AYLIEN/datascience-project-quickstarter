import streamlit as st
import streamlit.components.v1 as components
import streamlit.report_thread as ReportThread
from streamlit.server.server import Server


page_config = st.set_page_config(
    page_title="Page Title",
)


def get_session_state():
    session_id = ReportThread.get_report_ctx().session_id
    session_info = Server.get_current()._get_session_info(session_id)

    if session_info is None:
        raise RuntimeError("Could not get Streamlit session object.")

    # this session object
    this_session = session_info.session

    # Initialize user state if session doesn't exist
    if not hasattr(this_session, "_custom_session_state"):
        user_state = {
            "button_click_count": 0,
        }
        this_session._custom_session_state = user_state

    return this_session._custom_session_state


def main():
    session_state = get_session_state()

    st.write("# Simple Streamlit Demo")

    if st.button("Click Me"):
        session_state["button_click_count"] += 1
        clicks = session_state["button_click_count"]
        st.write(
            f"This button has been clicked {clicks} times in this session."
        )



if __name__ == '__main__':
    main()
