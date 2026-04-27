import streamlit as st
import requests
from PyPDF2 import PdfReader
import docx

st.title("🧠 AI Skill Assessment Agent")

def extract_text(file):
    if file.name.endswith(".pdf"):
        reader = PdfReader(file)
        return "".join([p.extract_text() for p in reader.pages])
    else:
        doc = docx.Document(file)
        return "\n".join([p.text for p in doc.paragraphs])

uploaded = st.file_uploader("Upload Resume", type=["pdf", "docx"])
jd = st.text_area("Paste Job Description")

if st.button("Analyze"):

    if uploaded is None:
        st.warning("Please upload a resume")
    elif not jd:
        st.warning("Please paste job description")
    else:
        resume_text = extract_text(uploaded)

        response = requests.post(
            "http://127.0.0.1:8000/analyze",
            json={"resume": resume_text, "jd": jd}
        )

        st.write("Raw response:", response.text)

        try:
            data = response.json()
        except:
            st.error("❌ Backend not returning valid JSON")
            st.stop()

        # 🔥 SHOW RESULTS
        st.success("✅ Analysis Complete")

        st.subheader("📊 Score")
        st.write(data["score"])

        col1, col2 = st.columns(2)

        with col1:
            st.subheader("✅ Matched Skills")
            st.write(data["matched_skills"])

        with col2:
            st.subheader("❌ Missing Skills")
            st.write(data["missing_skills"])

        st.subheader("📚 Learning Plan")
        st.write(data["plan"])