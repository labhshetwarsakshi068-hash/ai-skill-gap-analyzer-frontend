import streamlit as st

st.set_page_config(
    page_title="Resume & Skills",
    page_icon="📄",
    layout="wide"
)

st.title("📄 Resume Upload & Skills")
st.write("Upload your resume to identify your current skills.")

st.markdown("---")

st.markdown("### 📤 Upload Your Resume")

uploaded_file = st.file_uploader(
    "Choose your resume",
    type=["pdf", "docx"],
    help="Upload your resume in PDF or DOCX format."
)

if uploaded_file is not None:
    st.success(f"Resume uploaded successfully: {uploaded_file.name}")

    col1, col2 = st.columns(2)

    with col1:
        st.info(f"📄 File Name\n\n{uploaded_file.name}")

    with col2:
        file_size = uploaded_file.size / 1024
        st.info(f"📦 File Size\n\n{file_size:.2f} KB")

    st.markdown("---")

    st.markdown("### 🧠 Extracted Skills")
    st.write("Skills detected from your resume:")

    skills = [
        "Python",
        "SQL",
        "Git",
        "HTML",
        "CSS",
        "Java",
        "Flask",
        "MySQL"
    ]

    cols = st.columns(4)

    for i, skill in enumerate(skills):
        with cols[i % 4]:
            st.success(f"✓ {skill}")

    st.markdown("---")

    st.markdown("### ⚠️ Skills Not Detected")

    missing_skills = [
        "Machine Learning",
        "Deep Learning",
        "TensorFlow",
        "Docker",
        "Kubernetes",
        "AWS",
        "CI/CD"
    ]

    cols = st.columns(4)

    for i, skill in enumerate(missing_skills):
        with cols[i % 4]:
            st.warning(f"○ {skill}")

    st.markdown("---")

    if st.button("🔍 Analyze Resume", use_container_width=True):
        st.success("Resume analysis completed!")

else:
    st.info(
        "👆 Please upload your resume in PDF or DOCX format to begin."
    )