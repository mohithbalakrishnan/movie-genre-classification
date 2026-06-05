import streamlit as st
import pickle
import numpy as np

# ----------------------------
# PAGE CONFIG
# ----------------------------
st.set_page_config(
    page_title="Movie Genre Classifier",
    page_icon="🎬",
    layout="centered"
)

# ----------------------------
# LOAD MODEL
# ----------------------------
@st.cache_resource
def load_model():
    model = pickle.load(open("model.pkl", "rb"))
    vectorizer = pickle.load(open("tfidf.pkl", "rb"))
    return model, vectorizer

model, vectorizer = load_model()

# ----------------------------
# HEADER UI
# ----------------------------
st.title("🎬 Movie Genre Classification AI")
st.markdown("### Predict movie genre using Machine Learning (TF-IDF + ML Model)")
st.markdown("---")

# ----------------------------
# SIDEBAR INFO
# ----------------------------
st.sidebar.title("📊 About Project")
st.sidebar.info(
    """
    This AI model classifies movie descriptions into genres like:
    - Action
    - Romance
    - Drama
    - Horror
    - Comedy
    
    Built using:
    ✔ TF-IDF Vectorizer  
    ✔ Machine Learning Model  
    ✔ Streamlit UI  
    """
)

st.sidebar.markdown("---")
st.sidebar.write("👨‍💻 Developed by Mohith")

# ----------------------------
# USER INPUT
# ----------------------------
st.subheader("✍ Enter Movie Description")

user_input = st.text_area(
    "Type here...",
    placeholder="Example: A young couple falls in love but faces emotional struggles..."
)

# ----------------------------
# PREDICTION FUNCTION
# ----------------------------
GENRES = [
    "action", "adult", "adventure", "animation", "biography", "comedy",
    "crime", "documentary", "drama", "family", "fantasy", "game-show",
    "history", "horror", "music", "musical", "mystery", "news",
    "reality-tv", "romance", "sci-fi", "short", "sport", "talk-show",
    "thriller", "war", "western"
]

def predict_genre(text):
    vect = vectorizer.transform([text])
    pred_idx = model.predict(vect)[0]
    if 0 <= pred_idx < len(GENRES):
        return GENRES[pred_idx].capitalize()
    return str(pred_idx)

# ----------------------------
# BUTTON
# ----------------------------
if st.button("🔍 Predict Genre"):

    if user_input.strip() == "":
        st.warning("⚠ Please enter a movie description")
    else:
        result = predict_genre(user_input)

        st.success(f"🎯 Predicted Genre: **{result}**")

        # ----------------------------
        # SIMPLE INSIGHT SECTION
        # ----------------------------
        st.markdown("### 📌 Insight")

        if result.lower() == "romance":
            st.info("💖 Romantic themes detected: love, emotions, relationships")
        elif result.lower() == "horror":
            st.info("👻 Horror elements detected: fear, suspense, dark tone")
        elif result.lower() == "action":
            st.info("💥 Action-packed storyline detected")
        elif result.lower() == "drama":
            st.info("🎭 Emotional storytelling detected")
        else:
            st.info("🎬 General entertainment content detected")

# ----------------------------
# FOOTER
# ----------------------------
st.markdown("---")
st.markdown("⭐ Built using Machine Learning + Streamlit | Movie Genre AI")