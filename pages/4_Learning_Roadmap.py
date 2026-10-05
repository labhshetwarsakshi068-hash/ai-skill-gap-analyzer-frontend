import streamlit as st

st.set_page_config(
    page_title="Learning Roadmap",
    page_icon="🛣️",
    layout="wide"
)

st.title("🛣️ Personalized Learning Roadmap")
st.write("Follow a step-by-step learning path to improve your missing skills.")

st.markdown("---")

st.markdown("### 🎯 Target Role")

target_role = st.selectbox(
    "Your selected career goal:",
    [
        "AI/ML Engineer",
        "Data Scientist",
        "Data Analyst",
        "Web Developer",
        "Java Developer"
    ]
)

st.markdown("---")

st.markdown("### 📚 Recommended Learning Path")

roadmap = [
    {
        "step": "Step 1",
        "skill": "Machine Learning",
        "description": "Learn supervised learning, unsupervised learning, regression, classification and model evaluation.",
        "duration": "4 Weeks"
    },
    {
        "step": "Step 2",
        "skill": "Deep Learning",
        "description": "Learn neural networks, CNN, RNN and deep learning fundamentals.",
        "duration": "4 Weeks"
    },
    {
        "step": "Step 3",
        "skill": "TensorFlow",
        "description": "Build and train machine learning and deep learning models using TensorFlow.",
        "duration": "3 Weeks"
    },
    {
        "step": "Step 4",
        "skill": "Docker & Kubernetes",
        "description": "Learn containerization, Docker images, containers and basic Kubernetes concepts.",
        "duration": "3 Weeks"
    },
    {
        "step": "Step 5",
        "skill": "AWS & CI/CD",
        "description": "Learn cloud deployment, AWS fundamentals and continuous integration and deployment.",
        "duration": "4 Weeks"
    }
]

for item in roadmap:
    st.markdown(f"### {item['step']} — {item['skill']}")

    col1, col2 = st.columns([3, 1])

    with col1:
        st.write(item["description"])

    with col2:
        st.info(f"⏱️ {item['duration']}")

    st.markdown("---")

st.markdown("### 📈 Overall Roadmap Progress")

progress = 0.20

st.progress(progress)

st.write("1 of 5 learning stages completed — 20% progress")

st.markdown("---")

st.markdown("### 💡 Learning Tips")

st.success("✅ Practice every topic with a small project.")
st.info("📖 Revise concepts regularly and solve practical problems.")
st.warning("🎯 Complete each stage before moving to the next one.")