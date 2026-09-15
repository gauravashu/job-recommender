import streamlit as st

from src.helper import (
    extract_text_from_pdf,
    ask_openai
)

from src.job_api import fetch_jobs


# --------------------------------------------------
# PAGE CONFIGURATION
# --------------------------------------------------

st.set_page_config(
    page_title="AI Job Recommender",
    page_icon="💼",
    layout="wide"
)


# --------------------------------------------------
# HEADER
# --------------------------------------------------

st.title("📄 AI Job Recommender")

st.markdown(
    """
    Upload your resume and get:

    - 📑 Resume Summary
    - 🛠️ Skill Gap Analysis
    - 🚀 Career Roadmap
    - 💼 Real Job Recommendations
    """
)


# --------------------------------------------------
# RESUME UPLOAD
# --------------------------------------------------

uploaded_file = st.file_uploader(
    "Upload your resume (PDF)",
    type=["pdf"]
)


# --------------------------------------------------
# RESUME PROCESSING
# --------------------------------------------------

if uploaded_file:

    # Extract resume text
    with st.spinner("📖 Extracting text from your resume..."):

        resume_text = extract_text_from_pdf(
            uploaded_file
        )

    if not resume_text.strip():

        st.error(
            "❌ Could not extract text from this PDF."
        )

        st.stop()


    # --------------------------------------------------
    # RESUME SUMMARY
    # --------------------------------------------------

    with st.spinner("🧠 Analyzing your resume..."):

        summary = ask_openai(
            f"""
            Analyze this resume and provide a concise professional summary.

            Highlight:
            - Education
            - Technical skills
            - Projects
            - Experience
            - Strengths

            Resume:

            {resume_text}
            """,
            max_tokens=500
        )


    # --------------------------------------------------
    # SKILL GAP ANALYSIS
    # --------------------------------------------------

    with st.spinner("🔍 Finding skill gaps..."):

        gaps = ask_openai(
            f"""
            Analyze this resume and identify:

            1. Missing technical skills
            2. Missing certifications
            3. Missing experience
            4. Skills required for better job opportunities

            Give practical suggestions.

            Resume:

            {resume_text}
            """,
            max_tokens=400
        )


    # --------------------------------------------------
    # CAREER ROADMAP
    # --------------------------------------------------

    with st.spinner("🚀 Creating your career roadmap..."):

        roadmap = ask_openai(
            f"""
            Based on this resume, create a practical career roadmap.

            Include:

            - Skills to learn
            - Technologies to learn
            - Certifications
            - Projects to build
            - Industry exposure
            - Interview preparation

            Keep the roadmap suitable for a fresher / early-career
            software developer.

            Resume:

            {resume_text}
            """,
            max_tokens=500
        )


    # --------------------------------------------------
    # DISPLAY RESUME SUMMARY
    # --------------------------------------------------

    st.markdown("---")

    st.header("📑 Resume Summary")

    st.markdown(summary)


    # --------------------------------------------------
    # DISPLAY SKILL GAPS
    # --------------------------------------------------

    st.markdown("---")

    st.header("🛠️ Skill Gaps & Missing Areas")

    st.markdown(gaps)


    # --------------------------------------------------
    # DISPLAY ROADMAP
    # --------------------------------------------------

    st.markdown("---")

    st.header("🚀 Future Roadmap & Preparation Strategy")

    st.markdown(roadmap)


    st.success(
        "✅ Resume analysis completed successfully!"
    )


    # --------------------------------------------------
    # JOB RECOMMENDATION BUTTON
    # --------------------------------------------------

    st.markdown("---")

    if st.button(
        "🔎 Get Real Job Recommendations",
        type="primary"
    ):

        # --------------------------------------------------
        # GENERATE JOB SEARCH KEYWORDS
        # --------------------------------------------------

        with st.spinner(
            "🤖 Finding the best job titles for your resume..."
        ):

            keywords = ask_openai(
                f"""
                Based on this resume summary, suggest the best
                job titles for searching real jobs.

                Give ONLY a comma-separated list.

                Example:

                Python Developer, Backend Developer,
                Software Developer, Junior Software Engineer

                Do not provide explanations.

                Resume Summary:

                {summary}
                """,
                max_tokens=150
            )


        # Clean keywords
        search_keywords = keywords.replace(
            "\n",
            " "
        ).strip()


        st.success(
            f"🔑 Job Search Keywords: {search_keywords}"
        )


        # --------------------------------------------------
        # FETCH REAL JOBS FROM ADZUNA
        # --------------------------------------------------

        with st.spinner(
            "🌐 Searching real job listings..."
        ):

            try:

                jobs = fetch_jobs(
                    search_query=search_keywords,
                    location="India",
                    rows=20,
                    page=1
                )

            except Exception as e:

                st.error(
                    f"❌ Could not fetch jobs: {str(e)}"
                )

                st.stop()


        # --------------------------------------------------
        # DISPLAY JOBS
        # --------------------------------------------------

        st.markdown("---")

        st.header(
            f"💼 Real Job Recommendations ({len(jobs)})"
        )


        if not jobs:

            st.warning(
                "No jobs found. Try uploading a different resume "
                "or use broader job keywords."
            )

        else:

            for index, job in enumerate(jobs, start=1):

                st.subheader(
                    f"{index}. {job['title']}"
                )

                st.write(
                    f"🏢 **Company:** {job['companyName']}"
                )

                st.write(
                    f"📍 **Location:** {job['location']}"
                )


                # Salary
                salary_min = job.get("salary_min")
                salary_max = job.get("salary_max")


                if salary_min or salary_max:

                    if salary_min and salary_max:

                        st.write(
                            f"💰 **Salary:** "
                            f"{salary_min:,.0f} - "
                            f"{salary_max:,.0f}"
                        )

                    elif salary_min:

                        st.write(
                            f"💰 **Minimum Salary:** "
                            f"{salary_min:,.0f}"
                        )

                    elif salary_max:

                        st.write(
                            f"💰 **Maximum Salary:** "
                            f"{salary_max:,.0f}"
                        )


                # Description
                description = job.get(
                    "description",
                    ""
                )

                if description:

                    st.write(
                        f"📝 **Description:** "
                        f"{description[:500]}..."
                    )


                # Job link
                job_url = job.get(
                    "url",
                    ""
                )


                if job_url:

                    st.link_button(
                        "🔗 View Job",
                        job_url
                    )


                st.caption(
                    f"Source: {job.get('source', 'Adzuna')}"
                )

                st.markdown("---")