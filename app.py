import streamlit as st
import requests
import base64

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Polyvox | AI Translator",
    page_icon="🌍",
    layout="centered"
)

# ---------------- LANGUAGE DATA ----------------
languages = {
    "English": "en",
    "Hindi": "hi",
    "Telugu": "te",
    "Tamil": "ta",
    "Kannada": "kn",
    "Malayalam": "ml",
    "French": "fr",
    "German": "de",
    "Spanish": "es",
    "Japanese": "ja"
}

language_flags = {
    "English": "🇬🇧",
    "Hindi": "🇮🇳",
    "Telugu": "🇮🇳",
    "Tamil": "🇮🇳",
    "Kannada": "🇮🇳",
    "Malayalam": "🇮🇳",
    "French": "🇫🇷",
    "German": "🇩🇪",
    "Spanish": "🇪🇸",
    "Japanese": "🇯🇵"
}

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>

.stApp {
    background:
        radial-gradient(circle at 10% 10%, rgba(120, 70, 255, 0.18), transparent 28%),
        radial-gradient(circle at 90% 20%, rgba(0, 200, 255, 0.12), transparent 25%),
        #080812;
    color: #ffffff;
}

.block-container {
    max-width: 900px;
    padding-top: 3rem;
    padding-bottom: 3rem;
}

/* Header */
.logo {
    text-align: center;
    font-size: 3.2rem;
    font-weight: 800;
    letter-spacing: 5px;
    background: linear-gradient(90deg, #9b6cff, #42d9ff);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin-bottom: 0;
}

.tagline {
    text-align: center;
    color: #a9a9c2;
    font-size: 1.05rem;
    margin-top: 5px;
}

.description {
    text-align: center;
    color: #77778f;
    font-size: 0.9rem;
    margin-bottom: 2.5rem;
}

/* Cards */
.card {
    background: rgba(22, 22, 38, 0.78);
    border: 1px solid rgba(155, 108, 255, 0.22);
    border-radius: 22px;
    padding: 24px;
    box-shadow: 0 15px 45px rgba(0, 0, 0, 0.35);
    backdrop-filter: blur(12px);
    margin-bottom: 20px;
}

.card-title {
    color: #bcb9d6;
    font-size: 0.78rem;
    font-weight: 700;
    letter-spacing: 1.5px;
    text-transform: uppercase;
    margin-bottom: 10px;
}

/* Text area */
textarea {
    background: rgba(10, 10, 20, 0.8) !important;
    color: white !important;
    border: 1px solid rgba(155, 108, 255, 0.25) !important;
    border-radius: 16px !important;
}

/* Select boxes */
div[data-baseweb="select"] > div {
    background: rgba(10, 10, 20, 0.85) !important;
    border: 1px solid rgba(155, 108, 255, 0.25) !important;
    border-radius: 14px !important;
}

/* Translate button */
.stButton > button {
    width: 100%;
    height: 52px;
    border: none;
    border-radius: 16px;
    color: white;
    font-size: 1rem;
    font-weight: 700;
    letter-spacing: 1px;
    background: linear-gradient(90deg, #7c4dff, #00b8ff);
    box-shadow: 0 8px 25px rgba(124, 77, 255, 0.28);
    transition: all 0.25s ease;
}

.stButton > button:hover {
    transform: translateY(-2px);
    box-shadow: 0 12px 32px rgba(0, 184, 255, 0.25);
}

/* Translation result */
.result {
    background: rgba(15, 15, 28, 0.9);
    border: 1px solid rgba(66, 217, 255, 0.25);
    border-radius: 18px;
    padding: 22px;
    font-size: 1.15rem;
    line-height: 1.7;
    min-height: 80px;
    box-shadow: 0 0 30px rgba(66, 217, 255, 0.06);
}

.result-title {
    color: #42d9ff;
    font-size: 0.78rem;
    font-weight: 700;
    letter-spacing: 1.5px;
    margin-bottom: 10px;
}

/* Footer */
.footer {
    text-align: center;
    color: #66667c;
    font-size: 0.78rem;
    margin-top: 40px;
}

.divider {
    height: 1px;
    background: linear-gradient(
        90deg,
        transparent,
        rgba(155, 108, 255, 0.35),
        transparent
    );
    margin: 30px 0;
}

</style>
""", unsafe_allow_html=True)


# ---------------- HEADER ----------------
st.markdown('<div class="logo">✦ POLYVOX</div>', unsafe_allow_html=True)

st.markdown(
    '<div class="tagline">AI-Powered Language Translation</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="description">Translate ideas. Connect the world. 🌍</div>',
    unsafe_allow_html=True
)


# ---------------- LANGUAGE SELECTION ----------------

# ---------------- LANGUAGE SELECTION ----------------

# ---------------- LANGUAGE SELECTION ----------------

language_list = list(languages.keys())

if "source_language" not in st.session_state:
    st.session_state.source_language = "English"

if "target_language" not in st.session_state:
    st.session_state.target_language = "Hindi"


def swap_languages():
    source = st.session_state.source_language
    target = st.session_state.target_language

    st.session_state.source_language = target
    st.session_state.target_language = source


st.markdown('<div class="card">', unsafe_allow_html=True)

col1, col2, col3 = st.columns([5, 1, 5])

with col1:
    st.markdown(
        '<div class="card-title">FROM</div>',
        unsafe_allow_html=True
    )

    st.selectbox(
        "Source Language",
        language_list,
        format_func=lambda x: f"{language_flags[x]}  {x}",
        label_visibility="collapsed",
        key="source_language"
    )

with col2:
    st.markdown("<br>", unsafe_allow_html=True)

    st.button(
        "⇄",
        help="Swap languages",
        on_click=swap_languages
    )

with col3:
    st.markdown(
        '<div class="card-title">TO</div>',
        unsafe_allow_html=True
    )

    st.selectbox(
        "Target Language",
        language_list,
        format_func=lambda x: f"{language_flags[x]}  {x}",
        label_visibility="collapsed",
        key="target_language"
    )

st.markdown('</div>', unsafe_allow_html=True)

source_language = st.session_state.source_language
target_language = st.session_state.target_language


# ---------------- TEXT INPUT ----------------
st.markdown('<div class="card">', unsafe_allow_html=True)

st.markdown(
    '<div class="card-title">YOUR TEXT</div>',
    unsafe_allow_html=True
)

text = st.text_area(
    "Text",
    placeholder="Type or paste the text you want to translate...",
    height=170,
    label_visibility="collapsed"
)

if text:
    st.caption(f"{len(text)} characters")

st.markdown('</div>', unsafe_allow_html=True)


# ---------------- TRANSLATE ----------------
if st.button("✨  TRANSLATE"):

    if not text.strip():

        st.warning("Please enter some text to translate.")

    elif source_language == target_language:

        st.info("Source and target languages are the same.")
        
        st.markdown(
            f"""
            <div class="card">
                <div class="result-title">✨ TRANSLATION</div>
                <div class="result">{text}</div>
            </div>
            """,
            unsafe_allow_html=True
        )

    else:

        try:

            with st.spinner("Translating..."):

                response = requests.post(
                    "http://127.0.0.1:5000/translate",
                    json={
                        "q": text,
                        "source": languages[source_language],
                        "target": languages[target_language],
                        "format": "text"
                    },
                    timeout=30
                )

            if response.status_code == 200:

                result = response.json()
                translated_text = result["translatedText"]

                st.markdown(
                    f"""
                    <div class="card">
                        <div class="result-title">
                            ✨ TRANSLATION
                        </div>
                    </div>
                    """,
                    unsafe_allow_html=True
                )
                st.markdown(
                    f'<div class="result">{translated_text}</div>',
                    unsafe_allow_html=True      
                )
                copy_text = base64.b64encode(
                    translated_text.encode("utf-8")
                ).decode("utf-8")

                st.markdown(
                    f"""
                    <div style="text-align: right; margin-top: 8px;">
                        <a
                            href="data:text/plain;base64,{copy_text}"
                            download="polyvox_translation.txt"
                            style="
                                display: inline-block;
                                padding: 8px 14px;
                                border-radius: 10px;
                                background: rgba(124, 77, 255, 0.15);
                                border: 1px solid rgba(155, 108, 255, 0.35);
                                color: white;
                                text-decoration: none;
                                font-size: 0.85rem;
                            "
                        >
                            📋 Copy Translation
                        </a>
                    </div>
                    """,
                    unsafe_allow_html=True
                )
                
                    
                

                st.success("Translation completed successfully!")

            else:

                st.error("Translation failed. Please try again.")

        except requests.exceptions.RequestException:

            st.error(
                "Could not connect to the translation server. "
                "Please make sure LibreTranslate is running."
            )


# ---------------- FOOTER ----------------
st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

st.markdown(
    """
    <div class="footer">
        ⚡ Powered by LibreTranslate &nbsp; • &nbsp;
        Built with Python & Streamlit<br><br>
        CodeAlpha AI Internship • Project 1
    </div>
    """,
    unsafe_allow_html=True
)