import os
import requests
from dotenv import load_dotenv

load_dotenv()

ADZUNA_APP_ID = os.getenv("ADZUNA_APP_ID")
ADZUNA_APP_KEY = os.getenv("ADZUNA_APP_KEY")


def fetch_jobs(search_query, location="India", rows=20, page=1):

    if not ADZUNA_APP_ID or not ADZUNA_APP_KEY:
        raise ValueError(
            "ADZUNA_APP_ID or ADZUNA_APP_KEY is missing."
        )

    url = f"https://api.adzuna.com/v1/api/jobs/in/search/{page}"

    params = {
        "app_id": ADZUNA_APP_ID,
        "app_key": ADZUNA_APP_KEY,
        "results_per_page": rows,
        "what": search_query,
        "where": location,
        "content-type": "application/json",
        "sort_by": "date",
    }

    response = requests.get(
        url,
        params=params,
        timeout=20
    )

    response.raise_for_status()

    data = response.json()

    jobs = []

    for job in data.get("results", []):

        location_data = job.get("location", {})
        company_data = job.get("company", {})

        jobs.append({
            "title": job.get("title", "Unknown Job"),
            "companyName": company_data.get(
                "display_name",
                "Unknown Company"
            ),
            "location": location_data.get(
                "display_name",
                location
            ),
            "description": job.get(
                "description",
                ""
            ),
            "url": job.get(
                "redirect_url",
                ""
            ),
            "salary_min": job.get("salary_min"),
            "salary_max": job.get("salary_max"),
            "created": job.get("created", ""),
            "source": "Adzuna"
        })

    return jobs


def fetch_multiple_jobs(search_queries, location="India", rows=20):

    all_jobs = []

    for query in search_queries:

        query = query.strip()

        if not query:
            continue

        try:

            jobs = fetch_jobs(
                search_query=query,
                location=location,
                rows=rows,
                page=1
            )

            all_jobs.extend(jobs)

        except Exception as e:

            print(
                f"Error searching '{query}': {e}"
            )

    # Remove duplicate jobs
    unique_jobs = []
    seen_urls = set()

    for job in all_jobs:

        url = job.get("url")

        if url and url not in seen_urls:

            seen_urls.add(url)
            unique_jobs.append(job)

    return unique_jobs