import streamlit as st

st.set_page_config(
    page_title="AI Recommendation",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 AI Career Recommendations")
st.write("Get personalized recommendations based on your skill gaps and career goal.")

st.markdown("---")

# Career Goal
st.markdown("### 🎯 Your Career Goal")

target_role = st.selectbox(
    "Select your target role:",
    [
        "AI/ML Engineer",
        "Data Scientist",
        "Data Analyst",
        "Web Developer",
        "Java Developer"
    ]
)

st.markdown("---")

# Skill Analysis
st.markdown("### 📊 Your Skill Analysis")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Current Skills", "8")

with col2:
    st.metric("Missing Skills", "7")

with col3:
    st.metric("Skill Match", "53%")

st.markdown("---")

# AI Recommendations
st.markdown("### 💡 Personalized Recommendations")

recommendations = [
    {
        "title": "1. Learn Machine Learning",
        "text": "Start with supervised and unsupervised learning, regression, classification and model evaluation."
    },
    {
        "title": "2. Learn Deep Learning",
        "text": "After Machine Learning, learn neural networks, CNN, RNN and deep learning fundamentals."
    },
    {
        "title": "3. Practice TensorFlow",
        "text": "Build practical machine learning and deep learning projects using TensorFlow."
    },
    {
        "title": "4. Learn Docker & Kubernetes",
        "text": "Learn containerization and basic Kubernetes concepts to improve deployment skills."
    },
    {
        "title": "5. Learn AWS & CI/CD",
        "text": "Learn cloud fundamentals, AWS services and CI/CD pipelines for real-world deployment."
    }
]

for recommendation in recommendations:
    st.info(
        f"**{recommendation['title']}**\n\n"
        f"{recommendation['text']}"
    )

st.markdown("---")

# Project Recommendations
st.markdown("### 🛠️ Recommended Projects")

projects = [
    "🤖 Machine Learning Prediction System",
    "🧠 Deep Learning Image Classification",
    "📦 Dockerized Python Application",
    "☁️ AWS Cloud Deployment Project",
    "🔄 CI/CD Pipeline using Jenkins"
]

for project in projects:
    st.success(project)

st.markdown("---")

# Career Tips
st.markdown("### 🚀 Career Improvement Tips")

st.write("✅ Build at least 2–3 projects related to your target role.")
st.write("✅ Add your projects and technical skills to your resume.")
st.write("✅ Practice coding and technical interview questions.")
st.write("✅ Keep improving your missing skills step-by-step.")

st.markdown("---")

st.success(
    f"🎯 Based on your current profile, focus on the recommended skills "
    f"to become more prepared for a **{target_role}** role."
)