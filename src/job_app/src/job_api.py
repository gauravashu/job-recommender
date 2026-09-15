from apify_client import ApifyClient
from apify_client.errors import ApifyApiError
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get Apify API token
APIFY_API_TOKEN = os.getenv("APIFY_API_TOKEN")

# Create Apify client
apify_client = ApifyClient(APIFY_API_TOKEN)


# =========================================================
# SAMPLE LINKEDIN JOBS
# =========================================================

def get_sample_linkedin_jobs(search_query):

    companies = [
        "TCS",
        "Infosys",
        "Wipro",
        "Accenture",
        "Cognizant",
        "Capgemini",
        "Deloitte",
        "Tech Mahindra",
        "HCLTech",
        "IBM"
    ]

    locations = [
        "Bangalore, India",
        "Hyderabad, India",
        "Pune, India",
        "Noida, India",
        "Gurgaon, India",
        "Mumbai, India",
        "Chennai, India",
        "Indore, India",
        "Remote, India",
        "Delhi, India"
    ]

    job_titles = [
        f"{search_query} Developer",
        f"Junior {search_query} Developer",
        f"{search_query} Engineer",
        f"Associate {search_query} Developer",
        f"{search_query} Software Engineer",
        f"{search_query} Intern",
        f"Graduate {search_query} Engineer",
        f"{search_query} Trainee",
        f"Software Developer - {search_query}",
        f"Entry Level {search_query} Developer"
    ]

    jobs = []

    for i in range(10):
        jobs.append({
            "title": job_titles[i],
            "companyName": companies[i],
            "location": locations[i],
            "link": "https://www.linkedin.com/jobs/"
        })

    return jobs


# =========================================================
# SAMPLE NAUKRI JOBS
# =========================================================

def get_sample_naukri_jobs(search_query):

    companies = [
        "Accenture",
        "Infosys",
        "Wipro",
        "Cognizant",
        "TCS",
        "HCLTech",
        "Capgemini",
        "Tech Mahindra",
        "Deloitte",
        "IBM"
    ]

    locations = [
        "Bangalore, India",
        "Pune, India",
        "Hyderabad, India",
        "Chennai, India",
        "Noida, India",
        "Gurgaon, India",
        "Mumbai, India",
        "Indore, India",
        "Kolkata, India",
        "Delhi, India"
    ]

    job_titles = [
        f"{search_query} Engineer",
        f"Junior {search_query} Developer",
        f"{search_query} Software Engineer",
        f"Associate {search_query} Engineer",
        f"{search_query} Developer",
        f"{search_query} Intern",
        f"Graduate {search_query} Engineer",
        f"{search_query} Trainee",
        f"Software Developer - {search_query}",
        f"Entry Level {search_query} Engineer"
    ]

    jobs = []

    for i in range(10):
        jobs.append({
            "title": job_titles[i],
            "companyName": companies[i],
            "location": locations[i],
            "url": "https://www.naukri.com/"
        })

    return jobs


# =========================================================
# FETCH LINKEDIN JOBS
# =========================================================

def fetch_linkedin_jobs(
    search_query,
    location="India",
    rows=10
):

    run_input = {
        "title": search_query,
        "location": location,
        "rows": rows,
        "proxy": {
            "useApifyProxy": True,
            "apifyProxyGroups": ["RESIDENTIAL"]
        }
    }

    try:

        print("🔎 Fetching LinkedIn jobs from Apify...")

        run = apify_client.actor(
            "hKByXkMQaC5Qt9UMN"
        ).call(
            run_input=run_input
        )

        jobs = list(
            apify_client.dataset(
                run.default_dataset_id
            ).iterate_items()
        )

        print(f"✅ Found {len(jobs)} LinkedIn jobs")

        return jobs

    except ApifyApiError as e:

        error_message = str(e)

        if "Monthly usage hard limit exceeded" in error_message:

            print(
                "⚠️ Apify monthly limit exceeded."
            )

            print(
                "📦 Using 10 sample LinkedIn jobs."
            )

            return get_sample_linkedin_jobs(
                search_query
            )

        print(
            f"❌ LinkedIn Apify error: {error_message}"
        )

        return get_sample_linkedin_jobs(
            search_query
        )

    except Exception as e:

        print(
            f"❌ LinkedIn error: {e}"
        )

        print(
            "📦 Using sample LinkedIn jobs."
        )

        return get_sample_linkedin_jobs(
            search_query
        )


# =========================================================
# FETCH NAUKRI JOBS
# =========================================================

def fetch_naukri_jobs(
    search_query,
    location="India",
    rows=10
):

    run_input = {
        "keyword": search_query,
        "maxJobs": rows,
        "freshness": "all",
        "sortBy": "relevance",
        "experience": "all"
    }

    try:

        print("🔎 Fetching Naukri jobs from Apify...")

        run = apify_client.actor(
            "alpcnRV9YI9lYVPWk"
        ).call(
            run_input=run_input
        )

        jobs = list(
            apify_client.dataset(
                run.default_dataset_id
            ).iterate_items()
        )

        print(f"✅ Found {len(jobs)} Naukri jobs")

        return jobs

    except ApifyApiError as e:

        error_message = str(e)

        if "Monthly usage hard limit exceeded" in error_message:

            print(
                "⚠️ Apify monthly limit exceeded."
            )

            print(
                "📦 Using 10 sample Naukri jobs."
            )

            return get_sample_naukri_jobs(
                search_query
            )

        print(
            f"❌ Naukri Apify error: {error_message}"
        )

        return get_sample_naukri_jobs(
            search_query
        )

    except Exception as e:

        print(
            f"❌ Naukri error: {e}"
        )

        print(
            "📦 Using sample Naukri jobs."
        )

        return get_sample_naukri_jobs(
            search_query
        )