def extract_profile_from_cv(cv_text):
    """
    Very simple first version:
    Extracts basic skills and interests from the CV text.
    (Later we will replace this with AI/NLP.)
    """

    cv_lower = cv_text.lower()

    profile = {
        "skills": [],
        "interests": [],
        "level": "unknown"
    }

    # --- Detect skills (basic version) ---
    skill_keywords = {
        "python": "Python",
        "linux": "Linux",
        "ai": "Artificial Intelligence",
        "data": "Data Analysis",
        "excel": "Excel"
    }

    for key, label in skill_keywords.items():
        if key in cv_lower:
            profile["skills"].append(label)

    # --- Detect interests ---
    interest_keywords = {
        "solar": "Solar Energy",
        "electric": "Electric Vehicles",
        "ev": "Electric Vehicles",
        "motor": "Electric Motors",
        "battery": "Battery Technology",
        "fleet": "Fleet Technology"
    }

    for key, label in interest_keywords.items():
        if key in cv_lower:
            profile["interests"].append(label)

    # --- Rough level detection ---
    if "intern" in cv_lower or "internship" in cv_lower:
        profile["level"] = "Internship"
    elif "junior" in cv_lower:
        profile["level"] = "Junior"
    elif "senior" in cv_lower:
        profile["level"] = "Senior"
    else:
        profile["level"] = "Entry / Junior"

    return profile

# Simple test
if __name__ == "__main__":
    print("Profile Builder module ready.")
