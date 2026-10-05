import streamlit as st

from api import (
    register_user,
    login_user,
    get_profile,
    get_user_skills,
    get_job_roles,
    get_skill_gap,
    upload_resume,
    get_personalized_roadmap,
    get_ai_recommendation
)


# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="AI Skill Gap Analyzer",
    page_icon="🎯",
    layout="wide"
)


# =========================================================
# SESSION STATE
# =========================================================

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "token" not in st.session_state:
    st.session_state.token = None

if "user" not in st.session_state:
    st.session_state.user = None


# =========================================================
# SIDEBAR
# =========================================================

st.sidebar.title("🎯 Skill Gap Analyzer")

if not st.session_state.logged_in:

    page = st.sidebar.radio(
        "Navigation",
        [
            "Home",
            "Register",
            "Login"
        ]
    )

else:

    page = st.sidebar.radio(
        "Navigation",
        [
            "Dashboard",
            "Resume & Skills",
            "Skill Gap Analysis",
            "Learning Roadmap",
            "AI Recommendation",
            "Logout"
        ]
    )


# =========================================================
# HOME PAGE
# =========================================================

if page == "Home":

    st.title("🎯 AI-Based Skill Gap Analyzer")

    st.subheader(
        "Personalized Career Recommendation System"
    )

    st.write(
        """
        Analyze your current skills, identify skill gaps,
        and get personalized learning recommendations
        based on your target career role.
        """
    )

    st.markdown("---")

    st.markdown("## 🚀 What Our System Provides")

    col1, col2, col3 = st.columns(3)

    with col1:

        st.markdown("### 📄 Resume Analysis")

        st.write(
            "Upload your resume and automatically identify "
            "your existing technical skills."
        )

    with col2:

        st.markdown("### 🎯 Skill Gap Analysis")

        st.write(
            "Compare your current skills with the skills "
            "required for your target job role."
        )

    with col3:

        st.markdown("### 🗺️ Learning Roadmap")

        st.write(
            "Get a personalized roadmap with learning topics, "
            "resources, and project ideas."
        )

    st.markdown("---")

    st.markdown("## 🤖 AI Career Recommendation")

    st.write(
        """
        Our system analyzes your skills and target career role
        to provide personalized career recommendations and
        suggest the skills you should develop.
        """
    )

    st.markdown("---")

    st.subheader("🚀 Start Your Career Skill Analysis")

    st.write(
        "Register or login to analyze your skills and "
        "generate your personalized career roadmap."
    )


# =========================================================
# REGISTER PAGE
# =========================================================

elif page == "Register":

    st.title("📝 Create Your Account")

    st.write(
        "Create your account to start your personalized "
        "skill gap analysis."
    )

    st.markdown("---")

    # Get job roles from backend
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

    with st.form("registration_form"):

        st.markdown("### 👤 Personal Information")

        name = st.text_input(
            "Full Name",
            placeholder="Enter your full name"
        )

        email = st.text_input(
            "Email",
            placeholder="Enter your email address"
        )

        password = st.text_input(
            "Password",
            type="password",
            placeholder="Create a password"
        )

        st.markdown("### 🎓 Academic Information")

        education = st.text_input(
            "Education",
            placeholder="Example: B.Tech"
        )

        branch = st.text_input(
            "Branch",
            placeholder="Example: Computer Science"
        )

        st.markdown("### 🎯 Career Information")

        if roles:

            role_names = []

            for role in roles:

                if isinstance(role, dict):

                    role_name = (
                        role.get("role_name")
                        or role.get("name")
                        or role.get("title")
                    )

                    if role_name:
                        role_names.append(role_name)

            if role_names:

                target_role = st.selectbox(
                    "Target Job Role",
                    role_names
                )

            else:

                target_role = st.text_input(
                    "Target Job Role",
                    placeholder="Example: AI/ML Engineer"
                )

        else:

            target_role = st.text_input(
                "Target Job Role",
                placeholder="Example: AI/ML Engineer"
            )

        register_button = st.form_submit_button(
            "📝 Create Account"
        )

    if register_button:

        if not name.strip():

            st.warning("Please enter your full name.")

        elif not email.strip():

            st.warning("Please enter your email.")

        elif not password:

            st.warning("Please create a password.")

        elif not education.strip():

            st.warning("Please enter your education.")

        elif not branch.strip():

            st.warning("Please enter your branch.")

        elif not target_role:

            st.warning("Please select your target job role.")

        else:

            register_data = {
                "name": name.strip(),
                "email": email.strip(),
                "password": password,
                "education": education.strip(),
                "branch": branch.strip(),
                "target_role": target_role
            }

            try:

                response = register_user(register_data)

                if response.status_code in [200, 201]:

                    st.success(
                        "✅ Registration successful!"
                    )

                    st.info(
                        "You can now go to Login and access your dashboard."
                    )

                else:

                    try:
                        error_data = response.json()

                        error_message = (
                            error_data.get("message")
                            or error_data.get("error")
                            or "Registration failed."
                        )

                    except Exception:

                        error_message = response.text

                    st.error(
                        f"❌ Registration failed: {error_message}"
                    )

            except Exception as e:

                st.error(
                    f"❌ Backend connection error: {e}"
                )


# =========================================================
# LOGIN PAGE
# =========================================================

elif page == "Login":

    st.title("🔐 Login")

    st.write(
        "Login to access your Skill Gap Analyzer dashboard."
    )

    st.markdown("---")

    with st.form("login_form"):

        st.markdown("### 🔐 Account Login")

        email = st.text_input(
            "Email",
            placeholder="Enter your email address"
        )

        password = st.text_input(
            "Password",
            type="password",
            placeholder="Enter your password"
        )

        login_button = st.form_submit_button(
            "🔐 Login"
        )

    if login_button:

        if not email.strip():

            st.warning("Please enter your email.")

        elif not password:

            st.warning("Please enter your password.")

        else:

            login_data = {
                "email": email.strip(),
                "password": password
            }

            try:

                response = login_user(login_data)

                if response.status_code == 200:

                    data = response.json()

                    st.session_state.token = data.get(
                        "access_token"
                    )

                    st.session_state.user = data.get(
                        "user"
                    )

                    st.session_state.logged_in = True

                    st.success(
                        "✅ Login successful!"
                    )

                    st.rerun()

                else:

                    try:
                        error_data = response.json()

                        error_message = (
                            error_data.get("message")
                            or error_data.get("error")
                            or "Invalid email or password."
                        )

                    except Exception:

                        error_message = response.text

                    st.error(
                        f"❌ Login failed: {error_message}"
                    )

            except Exception as e:

                st.error(
                    f"❌ Backend connection error: {e}"
                )


# =========================================================
# DASHBOARD
# =========================================================

# =========================================================
# DASHBOARD
# =========================================================

elif page == "Dashboard":

    st.markdown(
        """
        <style>
        .dashboard-title {
            font-size: 34px;
            font-weight: 700;
            margin-bottom: 0px;
        }
        .dashboard-subtitle {
            font-size: 16px;
            color: #6b7280;
            margin-bottom: 25px;
        }
        .section-title {
            font-size: 22px;
            font-weight: 700;
            margin-top: 18px;
            margin-bottom: 12px;
        }
        .profile-card {
            padding: 18px;
            border-radius: 12px;
            border: 1px solid #e5e7eb;
            background: #ffffff;
            min-height: 105px;
        }
        .profile-card-green {
            padding: 18px;
            border-radius: 12px;
            border: 1px solid #bbf7d0;
            background: #f0fdf4;
            min-height: 105px;
        }
        .card-label {
            color: #6b7280;
            font-size: 12px;
            font-weight: 600;
            margin-bottom: 8px;
        }
        .card-value {
            font-size: 15px;
            font-weight: 600;
        }
        .summary-value {
            font-size: 28px;
            font-weight: 700;
        }
        .skill-current {
            display: inline-block;
            padding: 7px 12px;
            margin: 4px;
            border-radius: 20px;
            background: #ecfdf5;
            color: #047857;
            font-size: 13px;
            font-weight: 600;
        }
        .skill-missing {
            display: inline-block;
            padding: 7px 12px;
            margin: 4px;
            border-radius: 20px;
            background: #fff7ed;
            color: #c2410c;
            font-size: 13px;
            font-weight: 600;
        }
        .learning-step {
            padding: 10px 14px;
            margin: 7px 0;
            border-left: 4px solid #6366f1;
            background: #f8fafc;
            border-radius: 6px;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    user = st.session_state.user

    if not user:

        st.error("User information not available.")

    else:

        user_id = user.get("id")
        token = st.session_state.token

        # =================================================
        # PROFILE
        # =================================================

        try:
            profile_response = get_profile(user_id, token)

            if profile_response.status_code == 200:
                profile_data = profile_response.json()
                profile = profile_data.get("user") or profile_data
            else:
                profile = user
        except Exception:
            profile = user

        st.markdown(
            '<div class="dashboard-title">🎯 Skill Gap Analyzer</div>',
            unsafe_allow_html=True
        )
        st.markdown(
            '<div class="dashboard-subtitle">Student Dashboard</div>',
            unsafe_allow_html=True
        )

        st.markdown(
            f"## 👋 Welcome, {profile.get('name', 'User')}!"
        )

        st.markdown("### 👤 Profile")

        education = profile.get("education", "Not Available")
        branch = profile.get("branch", "Not Available")
        target_role_name = profile.get("target_role", "Not Available")

        col1, col2, col3, col4 = st.columns(4)

        with col1:
            st.markdown(
                f"""
                <div class="profile-card">
                    <div class="card-label">🎓 Education</div>
                    <div class="card-value">{education}</div>
                </div>
                """,
                unsafe_allow_html=True
            )

        with col2:
            st.markdown(
                f"""
                <div class="profile-card">
                    <div class="card-label">💻 Branch</div>
                    <div class="card-value">{branch}</div>
                </div>
                """,
                unsafe_allow_html=True
            )

        with col3:
            st.markdown(
                f"""
                <div class="profile-card">
                    <div class="card-label">🎯 Target Role</div>
                    <div class="card-value">{target_role_name}</div>
                </div>
                """,
                unsafe_allow_html=True
            )

        with col4:
            st.markdown(
                """
                <div class="profile-card-green">
                    <div style="color:#22c55e;font-size:12px;font-weight:600;margin-bottom:8px;">
                        🟢 Status
                    </div>
                    <div style="font-size:14px;font-weight:600;">
                        Active
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )

        st.markdown("---")

        # =================================================
        # GET JOB ROLES
        # =================================================

        try:
            roles_response = get_job_roles()
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
        except Exception:
            roles = []

        role_id = None

        for role in roles:
            if isinstance(role, dict):
                role_name = (
                    role.get("role_name")
                    or role.get("name")
                    or role.get("title")
                )

                if role_name == target_role_name:
                    role_id = role.get("id") or role.get("role_id")
                    break

        # =================================================
        # GET USER SKILLS
        # =================================================

        try:
            skills_response = get_user_skills(user_id, token)

            if skills_response.status_code == 200:
                skills_data = skills_response.json()

                if isinstance(skills_data, dict):
                    user_skills = (
                        skills_data.get("skills")
                        or skills_data.get("user_skills")
                        or skills_data.get("data")
                        or []
                    )
                else:
                    user_skills = skills_data
            else:
                user_skills = []
        except Exception:
            user_skills = []

        # =================================================
        # GET SKILL GAP
        # =================================================

        match_percentage = 0
        matched_skills = []
        missing_skills = []
        total_matched = 0
        total_required = 0
        total_missing = 0

        if role_id:
            try:
                gap_response = get_skill_gap(
                    user_id,
                    role_id,
                    token
                )

                if gap_response.status_code == 200:
                    gap_data = gap_response.json()

                    match_percentage = gap_data.get(
                        "match_percentage", 0
                    )

                    matched_skills = gap_data.get(
                        "matched_skills", []
                    ) or []

                    missing_skills = gap_data.get(
                        "missing_skills", []
                    ) or []

                    total_matched = gap_data.get(
                        "total_matched_skills",
                        len(matched_skills)
                    )

                    total_required = gap_data.get(
                        "total_required_skills",
                        total_matched + len(missing_skills)
                    )

                    total_missing = len(missing_skills)

            except Exception:
                pass

        # =================================================
        # SKILL SUMMARY
        # =================================================

        st.markdown("### 📊 Skill Summary")

        col1, col2, col3, col4 = st.columns(4)

        with col1:
            st.metric("Total Skills", total_required)

        with col2:
            st.metric("Skills Present", total_matched)

        with col3:
            st.metric("Skills Missing", total_missing)

        with col4:
            st.metric("Skill Match", f"{match_percentage}%")

        # =================================================
        # OVERALL LEARNING PROGRESS
        # =================================================

        st.markdown("### 📈 Overall Learning Progress")
        st.progress(int(match_percentage))
        st.write(f"Current progress: **{match_percentage}%**")

        # =================================================
        # SKILLS OVERVIEW
        # =================================================

        st.markdown("### 📊 Skills Overview")

        st.write(f"✅ Skills Present: {total_matched}")
        st.progress(
            int((total_matched / total_required) * 100)
            if total_required else 0
        )

        st.write(f"⚠️ Skills Missing: {total_missing}")

        missing_percentage = (
            (total_missing / total_required) * 100
            if total_required
            else 0
        )

        st.progress(int(missing_percentage))

        # =================================================
        # CURRENT SKILLS
        # =================================================

        st.markdown("### 🛠️ Current Skills")

        current_skill_names = []

        for skill in user_skills:
            if isinstance(skill, dict):
                skill_name = (
                    skill.get("skill_name")
                    or skill.get("name")
                    or skill.get("skill")
                )

                if skill_name:
                    current_skill_names.append(skill_name)

            elif isinstance(skill, str):
                current_skill_names.append(skill)

        if current_skill_names:
            skills_html = "".join(
                f'<span class="skill-current">{skill}</span>'
                for skill in current_skill_names
            )

            st.markdown(
                skills_html,
                unsafe_allow_html=True
            )
        else:
            st.info(
                "No skills found. Upload your resume to detect skills."
            )

        # =================================================
        # SKILLS TO LEARN
        # =================================================

        st.markdown("### 📚 Skills to Learn")

        if missing_skills:
            missing_html = "".join(
                f'<span class="skill-missing">{skill}</span>'
                for skill in missing_skills
            )

            st.markdown(
                missing_html,
                unsafe_allow_html=True
            )
        else:
            st.success("No missing skills for the selected target role.")

        # =================================================
        # RECOMMENDED LEARNING PATH
        # =================================================

        st.markdown("### 🧭 Recommended Learning Path")

        if missing_skills:
            for index, skill in enumerate(
                missing_skills,
                start=1
            ):
                st.markdown(
                    f"""
                    <div class="learning-step">
                        <strong>{index}. {skill}</strong>
                    </div>
                    """,
                    unsafe_allow_html=True
                )
        else:
            st.success(
                "Your current skills match the selected target role."
            )
elif page == "Resume & Skills":

    st.title("📄 Resume Analysis")

    st.write(
        "Upload your resume to automatically detect your skills."
    )

    st.markdown("---")

    user = st.session_state.user

    uploaded_file = st.file_uploader(
        "Upload Resume",
        type=["pdf", "docx"]
    )

    if uploaded_file:

        st.write(
            f"Selected file: **{uploaded_file.name}**"
        )

        if st.button("📤 Analyze Resume"):

            try:

                response = upload_resume(
                    user.get("id"),
                    uploaded_file,
                    st.session_state.token
                )

                if response.status_code == 200:

                    data = response.json()

                    st.success(
                        data.get(
                            "message",
                            "Resume uploaded successfully."
                        )
                    )

                    st.markdown("### 🔍 Detected Skills")

                    detected_skills = data.get(
                        "detected_skills",
                        []
                    )

                    if detected_skills:

                        st.write(
                            ", ".join(
                                map(
                                    str,
                                    detected_skills
                                )
                            )
                        )

                    else:

                        st.info(
                            "No skills detected."
                        )

                    st.markdown("### 💾 Saved Skills")

                    saved_skills = data.get(
                        "saved_skills",
                        []
                    )

                    if saved_skills:

                        st.write(
                            ", ".join(
                                map(
                                    str,
                                    saved_skills
                                )
                            )
                        )

                    else:

                        st.info(
                            "No new skills were saved."
                        )

                    not_found_skills = data.get(
                        "not_found_skills",
                        []
                    )

                    if not_found_skills:

                        st.markdown(
                            "### ℹ️ Skills Not Found in Database"
                        )

                        st.write(
                            ", ".join(
                                map(
                                    str,
                                    not_found_skills
                                )
                            )
                        )

                else:

                    st.error(
                        f"Resume upload failed: {response.text}"
                    )

            except Exception as e:

                st.error(
                    f"❌ Backend connection error: {e}"
                )


# =========================================================
# SKILL GAP ANALYSIS
# =========================================================

elif page == "Skill Gap Analysis":

    st.title("🎯 Skill Gap Analysis")

    user = st.session_state.user

    if not user:

        st.error("User session not found.")

    else:

        user_id = user.get("id")

        token = st.session_state.token

        try:

            profile_response = get_profile(
                user_id,
                token
            )

            profile_data = profile_response.json()

            profile = (
                profile_data.get("user")
                or profile_data
            )

            target_role_name = profile.get(
                "target_role"
            )

        except Exception:

            target_role_name = user.get(
                "target_role"
            )

        # Get roles

        try:

            roles_response = get_job_roles()

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

        except Exception:

            roles = []

        role_id = None

        for role in roles:

            if isinstance(role, dict):

                role_name = (
                    role.get("role_name")
                    or role.get("name")
                    or role.get("title")
                )

                if role_name == target_role_name:

                    role_id = (
                        role.get("id")
                        or role.get("role_id")
                    )

                    break

        if role_id:

            try:

                response = get_skill_gap(
                    user_id,
                    role_id,
                    token
                )

                if response.status_code == 200:

                    data = response.json()

                    match_percentage = data.get(
                        "match_percentage",
                        0
                    )

                    st.metric(
                        "🎯 Skill Match Percentage",
                        f"{match_percentage}%"
                    )

                    st.markdown("---")

                    col1, col2 = st.columns(2)

                    with col1:

                        st.markdown(
                            "### ✅ Matched Skills"
                        )

                        matched = data.get(
                            "matched_skills",
                            []
                        )

                        if matched:

                            for skill in matched:
                                st.success(
                                    str(skill)
                                )

                        else:

                            st.info(
                                "No matched skills found."
                            )

                    with col2:

                        st.markdown(
                            "### ❌ Missing Skills"
                        )

                        missing = data.get(
                            "missing_skills",
                            []
                        )

                        if missing:

                            for skill in missing:
                                st.warning(
                                    str(skill)
                                )

                        else:

                            st.success(
                                "No missing skills!"
                            )

                else:

                    st.error(
                        f"Unable to load skill gap: {response.text}"
                    )

            except Exception as e:

                st.error(
                    f"❌ Backend connection error: {e}"
                )

        else:

            st.warning(
                "Target role could not be mapped to a job role in the backend."
            )


# =========================================================
# LEARNING ROADMAP
# =========================================================

elif page == "Learning Roadmap":

    st.title("🗺️ Personalized Learning Roadmap")

    user = st.session_state.user

    user_id = user.get("id")

    token = st.session_state.token

    # Get profile

    try:

        profile_response = get_profile(
            user_id,
            token
        )

        profile_data = profile_response.json()

        profile = (
            profile_data.get("user")
            or profile_data
        )

        target_role_name = profile.get(
            "target_role"
        )

    except Exception:

        target_role_name = user.get(
            "target_role"
        )

    # Get roles

    try:

        roles_response = get_job_roles()

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

    except Exception:

        roles = []

    role_id = None

    for role in roles:

        if isinstance(role, dict):

            role_name = (
                role.get("role_name")
                or role.get("name")
                or role.get("title")
            )

            if role_name == target_role_name:

                role_id = (
                    role.get("id")
                    or role.get("role_id")
                )

                break

    if role_id:

        try:

            response = get_personalized_roadmap(
                user_id,
                role_id,
                token
            )

            if response.status_code == 200:

                data = response.json()

                st.metric(
                    "🎯 Current Match",
                    f"{data.get('match_percentage', 0)}%"
                )

                missing_skills = data.get(
                    "missing_skills",
                    []
                )

                if missing_skills:

                    st.markdown(
                        "### ❌ Skills To Develop"
                    )

                    st.write(
                        ", ".join(
                            map(
                                str,
                                missing_skills
                            )
                        )
                    )

                st.markdown("---")

                roadmap = data.get(
                    "personalized_roadmap",
                    []
                )

                if roadmap:

                    for index, item in enumerate(
                        roadmap,
                        start=1
                    ):

                        skill_name = item.get(
                            "skill_name",
                            "Skill"
                        )

                        with st.expander(
                            f"📚 Step {index}: {skill_name}"
                        ):

                            difficulty = item.get(
                                "difficulty"
                            )

                            if difficulty:
                                st.write(
                                    f"**Difficulty:** {difficulty}"
                                )

                            topics = item.get(
                                "learning_topics"
                            )

                            if topics:

                                st.markdown(
                                    "#### 📖 Learning Topics"
                                )

                                st.write(topics)

                            resources = item.get(
                                "resources"
                            )

                            if resources:

                                st.markdown(
                                    "#### 🔗 Resources"
                                )

                                st.write(resources)

                            projects = item.get(
                                "project_ideas"
                            )

                            if projects:

                                st.markdown(
                                    "#### 💡 Project Ideas"
                                )

                                st.write(projects)

                else:

                    st.info(
                        "No personalized roadmap available."
                    )

            else:

                st.error(
                    f"Unable to load roadmap: {response.text}"
                )

        except Exception as e:

            st.error(
                f"❌ Backend connection error: {e}"
            )

    else:

        st.warning(
            "Target role could not be mapped to backend job role."
        )


# =========================================================
# AI RECOMMENDATION
# =========================================================

elif page == "AI Recommendation":

    st.title("🤖 AI Career Recommendation")

    st.write(
        "Get an AI-generated recommendation based on your actual skills and target role."
    )

    user = st.session_state.user

    user_id = user.get("id")

    token = st.session_state.token

    # Get profile

    try:

        profile_response = get_profile(
            user_id,
            token
        )

        profile_data = profile_response.json()

        profile = (
            profile_data.get("user")
            or profile_data
        )

        target_role_name = profile.get(
            "target_role"
        )

    except Exception:

        target_role_name = user.get(
            "target_role"
        )

    # Get roles

    try:

        roles_response = get_job_roles()

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

    except Exception:

        roles = []

    role_id = None

    for role in roles:

        if isinstance(role, dict):

            role_name = (
                role.get("role_name")
                or role.get("name")
                or role.get("title")
            )

            if role_name == target_role_name:

                role_id = (
                    role.get("id")
                    or role.get("role_id")
                )

                break

    if role_id:

        if st.button("🤖 Generate AI Recommendation"):

            try:

                response = get_ai_recommendation(
                    user_id,
                    role_id,
                    token
                )

                if response.status_code == 200:

                    data = response.json()

                    st.success(
                        "AI recommendation generated successfully."
                    )

                    st.markdown("### 🎯 Skill Match")

                    st.metric(
                        "Match Percentage",
                        f"{data.get('match_percentage', 0)}%"
                    )

                    st.markdown("---")

                    recommendation = (
                        data.get("recommendation")
                        or data.get("ai_recommendation")
                        or data.get("message")
                    )

                    if recommendation:

                        st.markdown(
                            "### 💡 AI Recommendation"
                        )

                        st.write(
                            recommendation
                        )

                    matched = data.get(
                        "matched_skills",
                        []
                    )

                    missing = data.get(
                        "missing_skills",
                        []
                    )

                    if matched:

                        st.markdown(
                            "### ✅ Matched Skills"
                        )

                        st.write(
                            ", ".join(
                                map(
                                    str,
                                    matched
                                )
                            )
                        )

                    if missing:

                        st.markdown(
                            "### 📚 Skills To Develop"
                        )

                        st.write(
                            ", ".join(
                                map(
                                    str,
                                    missing
                                )
                            )
                        )

                else:

                    st.error(
                        f"AI recommendation failed: {response.text}"
                    )

            except Exception as e:

                st.error(
                    f"❌ Backend connection error: {e}"
                )

    else:

        st.warning(
            "Target role could not be mapped to backend job role."
        )


# =========================================================
# LOGOUT
# =========================================================

elif page == "Logout":

    st.session_state.logged_in = False

    st.session_state.token = None

    st.session_state.user = None

    st.success(
        "You have been logged out successfully."
    )

    st.rerun()