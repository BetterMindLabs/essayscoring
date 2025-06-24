import streamlit as st
import google.generativeai as genai

# === Gemini API Setup ===
api_key = st.secrets["api_keys"]["google_api_key"]
genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-1.5-flash")

# === Streamlit UI Setup ===
st.set_page_config(page_title="📝 Automated Essay Scoring")
st.title("📝 Automated Essay Scoring")
st.write("Paste an essay below and get an instant score with feedback based on clarity, grammar, structure, and relevance.")

# === Input Field ===
essay = st.text_area("✍️ Enter Essay Text", height=300, placeholder="Paste your essay here...")

# === Analyze Button ===
if st.button("Score Essay") and essay.strip():
    with st.spinner("Evaluating essay..."):
        prompt = f"""
You are a writing evaluation model trained to assess essays.

Analyze the essay below and respond in this format:
Score: <score out of 10>  
Strengths: <1-2 line summary>  
Areas to Improve: <1-2 line tips for improvement>

Essay:
{essay}
"""
        response = model.generate_content(prompt)
        result = response.text.strip()

        st.subheader("📊 Evaluation Result")
        st.text(result)
