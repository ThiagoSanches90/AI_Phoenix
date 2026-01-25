def find_jobs_matching_profile(profile):
    """
    First version (prototype):
    Returns a list of example jobs that match the user's profile.
    Later, we will replace this with real web/API search.
    """

    jobs_database = [
        {
            "company": "Solar Tech Brasil",
            "position": "Solar Technician Assistant",
            "location": "Belo Horizonte, MG",
            "job_type": "Junior / Technician",
            "description": "Assist in installation and monitoring of solar panels.",
            "tags": ["solar", "renewable", "technician"],
            "link": "https://example-solar.com/jobs/123"
        },
        {
            "company": "EV Motors Ltd.",
            "position": "Junior Electric Motor Technician",
            "location": "São Paulo, SP",
            "job_type": "Junior",
            "description": "Work with electric motors and testing equipment.",
            "tags": ["electric", "motor", "ev"],
            "link": "https://example-ev.com/jobs/456"
        },
        {
            "company": "Fleet Telematics Solutions",
            "position": "Technical Sales Support",
            "location": "Remote",
            "job_type": "Junior",
            "description": "Support clients using fleet and onboard vehicle technologies.",
            "tags": ["fleet", "telematics", "embedded"],
            "link": "https://example-fleet.com/jobs/789"
        }
    ]

    matching_jobs = []

    for job in jobs_database:
        match_score = 0
        reasons = []

        # Check interests match
        for interest in profile.get("interests", []):
            interest_lower = interest.lower()
            if any(tag in interest_lower for tag in job["tags"]):
                match_score += 30
                reasons.append(f"Matches your interest in {interest}")

        # Check level match
        if profile.get("level") in job["job_type"]:
            match_score += 20
            reasons.append("Matches your career level")

        # Basic skill relevance
        if "Python" in profile.get("skills", []):
            match_score += 10
            reasons.append("Technical/analytical background")

        # Only include reasonably matching jobs
        if match_score >= 30:
            job_entry = job.copy()
            job_entry["match_score"] = match_score
            job_entry["why_match"] = reasons
            matching_jobs.append(job_entry)

    # Sort by best match first
    matching_jobs.sort(key=lambda x: x["match_score"], reverse=True)

    return matching_jobs


if __name__ == "__main__":
    print("Job Finder module ready.")
