import requests

# Fetch all jobs
url = "https://www.arbeitnow.com/api/job-board-api"
response = requests.get(url)
data = response.json().get("data", [])

# Filter for Brazilian fleet-related jobs
fleet_keywords = ["fleet", "frota", "gestão de frotas", "telemática", "consultor técnico de vendas"]
brazil_jobs = []

for job in data:
    title = job.get("title","").lower()
    location = job.get("location","").lower()
    if any(k.lower() in title for k in fleet_keywords) and "brasil" in location:
        brazil_jobs.append({
            "company": job.get("company_name"),
            "title": job.get("title"),
            "location": job.get("location"),
            "link": job.get("url"),
            "salary": job.get("salary", "Not informed")
        })

# Print results
print(f"Found {len(brazil_jobs)} Brazilian fleet jobs:\n")
for j in brazil_jobs[:10]:
    print(j["company"], "-", j["title"], "-", j["location"])
    print("Link:", j["link"])
    print("Salary:", j["salary"])
    print("-------------------")
