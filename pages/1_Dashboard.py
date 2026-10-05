import streamlit as st

st.set_page_config(
    page_title="Skill Gap Analyzer - Dashboard",
    page_icon="🎯",
    layout="wide"
)

st.title("🎯 Skill Gap Analyzer")
st.subheader("Student Dashboard")

st.write("Welcome to your personalized skill gap dashboard.")

st.markdown("---")

# Profile
st.markdown("### 👤 Profile")

col1, col2, col3 = st.columns(3)

with col1:
    st.info("🎓 **Education**\n\nB.Tech Computer Science")

with col2:
    st.info("🎯 **Target Role**\n\nAI/ML Engineer")

with col3:
    st.success("🟢 **Status**\n\nActive")

st.markdown("---")

# Skill Summary
st.markdown("### 📊 Skill Summary")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Total Skills", 15)

with col2:
    st.metric("Skills Present", 8)

with col3:
    st.metric("Skills Missing", 7)

with col4:
    st.metric("Skill Match", "53%")

st.markdown("---")

# Progress
st.markdown("### 📈 Overall Learning Progress")

st.progress(53)
st.write("53% of the recommended skills are currently covered.")

st.markdown("---")

# Chart
st.markdown("### 📊 Skills Overview")

chart_data = {
    "Category": ["Skills Present", "Skills Missing"],
    "Count": [8, 7]
}

st.bar_chart(
    chart_data,
    x="Category",
    y="Count"
)

st.markdown("---")

# Current Skills
st.markdown("### ✅ Current Skills")

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

# Skills to Learn
st.markdown("### ⚠️ Skills to Learn")

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

# Learning Path
st.markdown("### 🛣️ Recommended Learning Path")

path = [
    "1. Machine Learning",
    "2. Deep Learning",
    "3. TensorFlow",
    "4. Docker & Kubernetes",
    "5. AWS & CI/CD"
]

for item in path:
    st.write(f"➡️ {item}")

st.markdown("---")

st.success(
    "💡 Follow the recommended learning path to improve your skill match."
)