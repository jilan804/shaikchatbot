
import streamlit as st
from main import ask_gemini

# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Gemini Chatbot",
    page_icon="🤖",
    layout="centered"
)

# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown("""
<style>

    .main {
        max-width: 850px;
        margin: auto;
    }

    .header {
        text-align: center;
        padding: 20px 0 10px 0;
    }

    .header h1 {
        font-size: 32px;
        margin-bottom: 5px;
    }

    .header p {
        color: #777;
        font-size: 15px;
    }

    .response-box {
        background-color: #f7f7f8;
        border-radius: 12px;
        padding: 20px;
        margin-top: 20px;
        border: 1px solid #e5e5e5;
        line-height: 1.6;
    }

    .footer {
        text-align: center;
        color: #888;
        font-size: 12px;
        margin-top: 30px;
    }

</style>
""", unsafe_allow_html=True)


# ============================================================
# HEADER
# ============================================================

st.markdown("""
<div class="header">
    <h1>🤖 Shaik Jilan Basha Bot</h1>
    <p>Ask anything and get a response from Shaik Jilan Basha Bot AI</p>
</div>
""", unsafe_allow_html=True)


# ============================================================
# GEMINI MODEL SELECTION
# ============================================================

models = [
    "gemini-3.8-flash",
    "gemini-2.5-pro"
]

selected_model = st.selectbox(
    "Select Gemini Model",
    models
)


# ============================================================
# USER INPUT
# ============================================================

user_input = st.text_area(
    "Enter your question",
    placeholder="Ask something...",
    height=150
)


# ============================================================
# ASK BUTTON
# ============================================================

if st.button("Send 🚀", use_container_width=True):

    if not user_input.strip():

        st.warning("Please enter a question.")

    else:

        with st.spinner("Gemini is thinking..."):

            try:

                response = ask_gemini(
                    selected_model,
                    user_input
                )

                # Display Gemini response
                st.markdown("### 🤖 Gemini Response")

                st.markdown(
                    f"""
                    <div class="response-box">
                        {response}
                    </div>
                    """,
                    unsafe_allow_html=True
                )

            except Exception as e:

                st.error(f"Error: {e}")


# ============================================================
# FOOTER
# ============================================================

st.markdown("""
<div class="footer">
    Powered by Shaik Jilan Basha
</div>
""", unsafe_allow_html=True)
