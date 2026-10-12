# 💼 AI Job Recommender

### 🤖 AI-Powered Resume Analysis & Job Recommendation System

An AI-powered application that analyzes a candidate's resume, identifies relevant skills, and helps discover suitable job opportunities based on their professional profile.

The project combines **Python, AI/LLMs, resume parsing, and job data extraction** to make the job search process more efficient and personalized.

---

## 🌟 Key Features

- 📄 **Resume Upload:** Upload your resume in PDF format for analysis.
- 🧠 **AI-Powered Resume Analysis:** Use an LLM to understand your resume and professional profile.
- 🛠️ **Skill Identification:** Identify important technical skills and qualifications from your resume.
- 🎯 **Job Recommendations:** Discover job opportunities relevant to your skills and career interests.
- 🔎 **Job Data Extraction:** Retrieve job listings using the configured job data collection integration.
- 📊 **Career Insights:** Generate useful insights about your profile and potential career opportunities.
- ⚡ **Interactive Web Interface:** Access the application's functionality through a user-friendly interface.

## 🛠️ Technology Stack

| Technology | Purpose |
|---|---|
| 🐍 Python | Core application logic |
| 🎈 Streamlit | Interactive web application |
| 🧠 Groq API / LLM | AI-powered resume analysis |
| 📑 PyMuPDF | Extract text from PDF resumes |
| 🔍 Apify | Job data collection through configured actors |
| 📦 uv | Python dependency and environment management |
| 🔐 python-dotenv | Load configuration from environment variables |
| 🐙 Git & GitHub | Version control and project hosting |

*Note: The table lists the technologies associated with the project setup. Retain only the tools and integrations present in your final implementation.*

## ⚙️ How It Works

The application follows a resume-to-recommendation workflow:

1. 📤 **Upload Resume** — The user uploads a PDF resume.
2. 📄 **Extract Text** — PyMuPDF extracts the resume content.
3. 🧠 **Analyze Profile** — The LLM processes the extracted text to understand skills, qualifications, and experience.
4. 🔎 **Collect Job Listings** — The configured job data integration retrieves relevant job postings.
5. 🎯 **Present Recommendations** — The application displays the available job opportunities and AI-generated insights.

```text
       👤 User
          |
          v
    📄 Upload Resume
          |
          v
    📑 Extract PDF Text
          |
          v
    🧠 AI Resume Analysis
          |
          v
    🔎 Retrieve Job Listings
          |
          v
    🎯 Job Recommendations
          |
          v
    💻 Display Results
```

## 🚀 Getting Started

Follow these steps to run the project locally.

### 📋 Prerequisites

Make sure you have installed:

- Python 3.12 or a compatible version required by the project
- Git
- uv
- The required API credentials for the integrations enabled in your application

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/gauravashu/job-recommender.git
cd job-recommender
```

### 2️⃣ Set Up the Environment

If the repository includes `pyproject.toml` and `uv.lock`, install the dependencies with:

```bash
uv sync
```

### 3️⃣ Configure Environment Variables

Create a `.env` file in the project root and add the credentials required by your application.

```env
GROQ_API_KEY=your_groq_api_key
APIFY_API_TOKEN=your_apify_api_token
```

Replace the example values with your actual credentials. Use the exact variable names expected by your code, and never commit your `.env` file or API keys to GitHub.

### 4️⃣ Run the Application

If your main Streamlit file is `app.py`, execute:

```bash
uv run streamlit run app.py
```

If the entry point is located elsewhere, replace `app.py` with the correct path.

### 5️⃣ Open the Application

Streamlit will display a local URL in the terminal, usually:

```text
http://localhost:8501
```

Open the URL in your browser and start exploring the application. 🎉

## 📁 Project Structure

The following is an example structure. Update it to match the actual files in your repository.

```text
job-recommender/
│
├── app.py                  # Main Streamlit application
├── src/
│   ├── helper.py           # Resume parsing and AI utilities
│   └── job_api.py          # Job data integration
│
├── .env                    # Local environment variables
├── .gitignore              # Files excluded from Git
├── pyproject.toml          # Project dependencies
├── uv.lock                 # Locked dependency versions
└── README.md               # Project documentation
```

## 🔒 Security Best Practices

- 🔑 Store API keys in environment variables.
- 🚫 Never push secrets, tokens, or private configuration files to GitHub.
- 📄 Handle uploaded resumes responsibly because they may contain personal information.
- 🛡️ Validate uploaded files and handle API errors gracefully.

## 🔮 Future Improvements

- 🎯 Add resume-to-job matching scores.
- 📍 Enable filtering by location, experience level, and job type.
- 🧩 Identify missing skills and recommend learning resources.
- 📈 Add a dashboard to compare multiple job opportunities.
- 💾 Save favorite jobs and application status.
- 🌐 Deploy the application so users can access it online.
- 🧪 Add automated tests for resume parsing and API integrations.

## 🎓 Learning Outcomes

Through this project, the following practical skills can be developed:

- Python application development
- Integrating LLM APIs into real-world applications
- PDF processing and text extraction
- Working with external APIs and job data
- Building interactive applications with Streamlit
- Managing project dependencies and environment variables
- Version control using Git and GitHub

## 👨‍💻 Author

**Ashish Gaurav**

🔗 GitHub: [gauravashu](https://github.com/gauravashu)

---

⭐ If you find this project useful, consider giving the repository a star!

💡 *Built to make job discovery smarter, more personalized, and more efficient.*







https://job-recommender-5nuww9zmbmcofgvvkj9th7.streamlit.app/
