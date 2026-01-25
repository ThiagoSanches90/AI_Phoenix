import requests

# RapidAPI credentials
RAPIDAPI_HOST = "jsearch.p.rapidapi.com"
RAPIDAPI_KEY = "f4398ed7d3msh79ca18af194bd1ep150c8cjsnc267f4bac122"

def search_jobs_brazil(keywords=None, location="Brazil", page=1):
    if keywords is None:
        keywords = ["frota", "fleet", "gestão de frotas", "telemática", "consultor técnico de vendas"]

    url = "https://jsearch.p.rapidapi.com/search"
    headers = {
        "x-rapidapi-host": RAPIDAPI_HOST,
        "x-rapidapi-key": RAPIDAPI_KEY
    }

    all_jobs = []

    for kw in keywords:
        params = {
            "query": kw,
            "location": location,
            "page": page
        }
        response = requests.get(url, headers=headers, params=params)
        if response.status_code != 200:
            print(f"Error fetching jobs for '{kw}':", response.status_code)
            continue

        data = response.json().get("data", [])
        for job in data:
            loc = f"{job.get('job_country','')} {job.get('job_city','')}".lower()
            title = job.get("job_title","").lower()
            if "brazil" in loc:
                all_jobs.append({
                    "company": job.get("job_company","Unknown"),
                    "role": job.get("job_title","Unknown"),
                    "location": f"{job.get('job_city','')} , {job.get('job_country','')}",
                    "salary": job.get("salary","Not informed"),
                    "link": job.get("job_google_link","No link")
                })

    # Remove duplicates based on title + company
    seen = set()
    unique_jobs = []
    for j in all_jobs:
        key = (j["company"], j["role"])
        if key not in seen:
            seen.add(key)
            unique_jobs.append(j)

    return unique_jobs

# Example usage
if __name__ == "__main__":
    jobs = search_jobs_brazil()
    print(f"Found {len(jobs)} Brazilian fleet jobs:\n")
    for j in jobs[:10]:
        print(j["company"], "-", j["role"], "-", j["location"])
        print("Salary:", j["salary"])
        print("Link:", j["link"])
        print("--------------------------")
