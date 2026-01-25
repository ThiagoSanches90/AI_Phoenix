def format_jobs_for_display(jobs):
    if not jobs:
        return "No jobs found."

    output = ""
    for i, job in enumerate(jobs, start=1):
        text = f"""
{i}️⃣ Company: {job.get('company', 'Unknown')}
📌 Role: {job.get('title', 'N/A')}
📍 Location: {job.get('location', 'N/A')}
🔗 Link: {job.get('link', 'N/A')}
----------------------------
"""
        output += text

    return output
