import requests

# Flask Backend URL
BASE_URL = "https://ai-skill-gap-analyzer-backend-1.onrender.com"


# ==========================================
# AUTHORIZATION HEADER
# ==========================================

def get_headers(token):
    return {
        "Authorization": f"Bearer {token}"
    }


# ==========================================
# REGISTER
# ==========================================

def register_user(data):
    return requests.post(
        f"{BASE_URL}/api/register",
        json=data,
        timeout=10
    )


# ==========================================
# LOGIN
# ==========================================

def login_user(data):
    return requests.post(
        f"{BASE_URL}/api/login",
        json=data,
        timeout=10
    )


# ==========================================
# PROFILE
# ==========================================

def get_profile(user_id, token):
    return requests.get(
        f"{BASE_URL}/api/profile/{user_id}",
        headers=get_headers(token),
        timeout=10
    )


# ==========================================
# ALL SKILLS
# ==========================================

def get_all_skills():
    return requests.get(
        f"{BASE_URL}/api/skills",
        timeout=10
    )


# ==========================================
# USER SKILLS
# ==========================================

def get_user_skills(user_id, token):
    return requests.get(
        f"{BASE_URL}/api/user-skills/{user_id}",
        headers=get_headers(token),
        timeout=10
    )


def add_user_skills(user_id, skill_ids, token):
    return requests.post(
        f"{BASE_URL}/api/user-skills",
        json={
            "user_id": user_id,
            "skill_ids": skill_ids
        },
        headers=get_headers(token),
        timeout=10
    )


# ==========================================
# JOB ROLES
# ==========================================

def get_job_roles():
    return requests.get(
        f"{BASE_URL}/api/job-roles",
        timeout=10
    )


# ==========================================
# ROLE SKILLS
# ==========================================

def get_role_skills(role_id):
    return requests.get(
        f"{BASE_URL}/api/role-skills/{role_id}",
        timeout=10
    )


# ==========================================
# SKILL GAP ANALYSIS
# ==========================================

def get_skill_gap(user_id, role_id, token):
    return requests.get(
        f"{BASE_URL}/api/skill-gap",
        params={
            "user_id": user_id,
            "role_id": role_id
        },
        headers=get_headers(token),
        timeout=10
    )


# ==========================================
# RESUME UPLOAD
# ==========================================

def upload_resume(user_id, uploaded_file, token):

    files = {
        "resume": (
            uploaded_file.name,
            uploaded_file.getvalue(),
            uploaded_file.type
        )
    }

    data = {
        "user_id": str(user_id)
    }

    return requests.post(
        f"{BASE_URL}/api/upload-resume",
        files=files,
        data=data,
        headers=get_headers(token),
        timeout=60
    )


# ==========================================
# PERSONALIZED ROADMAP
# ==========================================

def get_personalized_roadmap(user_id, role_id, token):
    return requests.get(
        f"{BASE_URL}/api/personalized-roadmap",
        params={
            "user_id": user_id,
            "role_id": role_id
        },
        headers=get_headers(token),
        timeout=20
    )


# ==========================================
# LEARNING RESOURCE
# ==========================================

def get_learning_resource(skill_id):
    return requests.get(
        f"{BASE_URL}/api/learning-resources/{skill_id}",
        timeout=10
    )


# ==========================================
# AI RECOMMENDATION
# ==========================================

def get_ai_recommendation(user_id, role_id, token):
    return requests.get(
        f"{BASE_URL}/api/ai-recommendation",
        params={
            "user_id": user_id,
            "role_id": role_id
        },
        headers=get_headers(token),
        timeout=60
    )
