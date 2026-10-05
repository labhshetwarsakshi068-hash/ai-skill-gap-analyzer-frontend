import streamlit as st

from api import (
    get_job_roles,
    get_user_skills,
    get_skill_gap
)


st.set_page_config(
    page_title="Skill Gap Analysis",
    page_icon="📊",
    layout="wide"
)


st.title("📊 Skill Gap Analysis")

st.write(
    "Analyze your current skills against the skills required for your target career."
)

st.markdown("---")


# =========================================================
# CHECK LOGIN
# =========================================================

if not st.session_state.get("logged_in"):

    st.warning("Please login first to analyze your skill gap.")

    st.stop()


user = st.session_state.get("user")
token = st.session_state.get("token")

user_id = user.get("id") if user else None


if not user_id or not token:

    st.error("User information is not available.")

    st.stop()


# =========================================================
# GET JOB ROLES
# =========================================================

try:

    roles_response = get_job_roles()

    if roles_response.status_code == 200:

        roles_data = roles_response.json()

        if isinstance(roles_data, dict):

            roles = (
                roles_data.get("job_roles")
                or roles_data.get("roles")
                or roles_data.get("data")
                or []
            )

        else:

            roles = roles_data

    else:

        roles = []

except Exception:

    roles = []


if not roles:

    st.error(
        "Job roles could not be loaded from the backend."
    )

    st.stop()


# =========================================================
# ROLE LIST
# =========================================================

role_names = []
role_map = {}


for role in roles:

    if isinstance(role, dict):

        role_name = (
            role.get("role_name")
            or role.get("name")
            or role.get("title")
        )

        role_id = (
            role.get("id")
            or role.get("role_id")
        )

        if role_name and role_id:

            role_names.append(role_name)

            role_map[role_name] = role_id


if not role_names:

    st.error("No target roles available.")

    st.stop()


# =========================================================
# TARGET ROLE
# =========================================================

st.markdown("### 🎯 Select Target Role")


profile_target_role = None


if user:

    profile_target_role = user.get("target_role")


default_index = 0


if profile_target_role in role_names:

    default_index = role_names.index(
        profile_target_role
    )


target_role = st.selectbox(
    "Choose your desired job role:",
    role_names,
    index=default_index
)


role_id = role_map.get(target_role)


st.markdown("---")


# =========================================================
# CURRENT USER SKILLS
# =========================================================

st.markdown("### ✅ Your Current Skills")


try:

    skills_response = get_user_skills(
        user_id,
        token
    )

    if skills_response.status_code == 200:

        skills_data = skills_response.json()

        if isinstance(skills_data, dict):

            current_skills_data = (
                skills_data.get("skills")
                or skills_data.get("user_skills")
                or skills_data.get("data")
                or []
            )

        else:

            current_skills_data = skills_data

    else:

        current_skills_data = []

except Exception:

    current_skills_data = []


current_skills = []


for skill in current_skills_data:

    if isinstance(skill, dict):

        skill_name = (
            skill.get("skill_name")
            or skill.get("name")
            or skill.get("skill")
        )

        if skill_name:

            current_skills.append(skill_name)

    elif isinstance(skill, str):

        current_skills.append(skill)


if current_skills:

    cols = st.columns(4)

    for i, skill in enumerate(current_skills):

        with cols[i % 4]:

            st.success(
                f"✓ {skill}"
            )

else:

    st.info(
        "No skills found. Please upload your resume first."
    )


st.markdown("---")


# =========================================================
# SKILL GAP ANALYSIS
# =========================================================

gap_data = {}


try:

    gap_response = get_skill_gap(
        user_id,
        role_id,
        token
    )

    if gap_response.status_code == 200:

        gap_data = gap_response.json()

    else:

        st.error(
            "Skill gap analysis could not be loaded."
        )

except Exception as e:

    st.error(
        f"Unable to analyze skill gap: {e}"
    )


# =========================================================
# MATCHED SKILLS
# =========================================================

matched_skills = gap_data.get(
    "matched_skills",
    []
)


if not isinstance(matched_skills, list):

    matched_skills = []


# =========================================================
# MISSING SKILLS
# =========================================================

missing_skills = gap_data.get(
    "missing_skills",
    []
)


if not isinstance(missing_skills, list):

    missing_skills = []


# =========================================================
# REQUIRED SKILLS
# =========================================================

# Required skills are derived from the actual
# skill-gap analysis so that all sections
# use the same backend data.

required_skills = []


for skill in matched_skills:

    if isinstance(skill, dict):

        skill_name = (
            skill.get("skill_name")
            or skill.get("name")
            or skill.get("skill")
        )

        if skill_name:
            required_skills.append(skill_name)

    elif isinstance(skill, str):

        required_skills.append(skill)


for skill in missing_skills:

    if isinstance(skill, dict):

        skill_name = (
            skill.get("skill_name")
            or skill.get("name")
            or skill.get("skill")
        )

        if skill_name:
            required_skills.append(skill_name)

    elif isinstance(skill, str):

        required_skills.append(skill)


# Remove duplicate skills while preserving order

required_skills = list(
    dict.fromkeys(required_skills)
)


# =========================================================
# REQUIRED SKILLS DISPLAY
# =========================================================

st.markdown(
    "### 🎯 Skills Required for Your Target Role"
)


if required_skills:

    cols = st.columns(4)

    for i, skill in enumerate(required_skills):

        with cols[i % 4]:

            st.info(
                f"• {skill}"
            )

else:

    st.info(
        "Required skills could not be loaded."
    )


st.markdown("---")


# =========================================================
# IDENTIFIED SKILL GAPS
# =========================================================

st.markdown(
    "### ⚠️ Identified Skill Gaps"
)


if missing_skills:

    for skill in missing_skills:

        if isinstance(skill, dict):

            skill_name = (
                skill.get("skill_name")
                or skill.get("name")
                or skill.get("skill")
            )

        else:

            skill_name = skill


        if skill_name:

            st.warning(
                f"⚠️ {skill_name}"
            )

else:

    st.success(
        "🎉 No skill gaps identified for this role."
    )


st.markdown("---")


# =========================================================
# MATCH SCORE
# =========================================================

st.markdown(
    "### 📈 Skill Match Score"
)


match_score = gap_data.get(
    "match_percentage",
    0
)


try:

    match_score = float(match_score)

except Exception:

    match_score = 0


st.metric(
    label="Overall Skill Match",
    value=f"{match_score:.0f}%"
)


st.progress(
    min(
        max(
            match_score / 100,
            0
        ),
        1
    )
)


st.write(
    f"You currently match approximately "
    f"{match_score:.0f}% of the required skills "
    f"for your selected role."
)


st.markdown("---")


# =========================================================
# ANALYSIS SUMMARY
# =========================================================

st.markdown(
    "### 📝 Analysis Summary"
)


# Use backend values wherever available

total_required = gap_data.get(
    "total_required_skills"
)

total_matched = gap_data.get(
    "total_matched_skills"
)

total_missing = gap_data.get(
    "total_missing_skills"
)


# Fallback values

if total_required is None:

    total_required = len(required_skills)


if total_matched is None:

    total_matched = len(matched_skills)


if total_missing is None:

    total_missing = len(missing_skills)


col1, col2, col3 = st.columns(3)


with col1:

    st.metric(
        "Required Skills",
        total_required
    )


with col2:

    st.metric(
        "Skills Present",
        total_matched
    )


with col3:

    st.metric(
        "Skills Missing",
        total_missing
    )


st.markdown("---")


# =========================================================
# RECOMMENDATION
# =========================================================

if missing_skills:

    st.info(
        "💡 Recommendation: Focus on the missing skills "
        "step-by-step to improve your career readiness."
    )

else:

    st.success(
        "🎉 Great! You currently have all the required "
        "skills for your selected target role."
    )