# Job Scraper

## 📌 Overview

This project is a **Python-based web scraper** that extracts job listings from [Vacancy Mail Zimbabwe](https://vacancymail.co.zw/jobs/). It scrapes job details such as **title, company name, location, expiry date, and description**, then **stores the data in a CSV file** for easy analysis.

---

## 🔹 Features

| Feature                 | Description |
|--------------------------|------------|
| **Web Scraping**         | Extracts job postings from Vacancy Mail Zimbabwe |
| **Data Extraction**      | Captures job title, company name, location, expiry date, and description |
| **CSV Storage**          | Saves extracted data to a structured CSV file |
| **Logging Support**      | Tracks errors and processes for easy debugging |
| **Scheduled Execution**  | Automates daily scrapes at **10:00 AM** using `schedule` |

---

## 🔧 Prerequisites

Ensure you have the following installed before running the script:

| Dependency | Installation Command |
|------------|----------------------|
| **Python**  | [Download Python](https://www.python.org/downloads/) |
| requests | pip install requests |
| beautifulsoup4 | pip install beautifulsoup4 |
| schedule | pip install schedule |

---

## 📥 Installation & Setup

1. **Clone** this repository or **download** the script.
2. Ensure the output path (`OUTPUT_PATH`) is correctly set in `job_scraper.py`.
3. Install required dependencies using:

   ```bash
   pip install -r requirements.txt

Done by LLOYD DONNEL CHOGARI
