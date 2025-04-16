
import logging
from bs4 import BeautifulSoup
import requests
import csv
import os
from datetime import datetime
import schedule
import time

# Setup logging
logging.basicConfig(
    filename="job_scraper.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Constants
URL = "https://vacancymail.co.zw/jobs/"
OUTPUT_PATH = "C:/Users/Quinton Bakasa/Desktop/Job_Scraper/scraped_data.csv"

# Function to fetch and parse the webpage
def fetch_webpage(url):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return BeautifulSoup(response.text, "html.parser")
    except requests.exceptions.RequestException as e:
        logging.error(f"Failed to fetch webpage: {e}")
        return None

# Function to extract job details
def extract_jobs(soup):
    try:
        jobs = []
        job_titles = soup.find_all("h3", class_="job-listing-title")[:10]  # Limit to 10 jobs
        company_names = soup.find_all("h4", class_="job-listing-company")[:10]
        job_listings_footers = soup.find_all("div", class_="job-listing-footer")[:10]
        job_descriptions = soup.find_all("p", class_="job-listing-text")[:10]

        for i, (title, company, footer, description) in enumerate(
            zip(job_titles, company_names, job_listings_footers, job_descriptions), start=1
        ):
            try:
                lis = footer.find_all("li")
                location = None
                expiry_date = None
                for li in lis:
                    if "icon-material-outline-location-on" in li.find("i")["class"]:
                        location = li.text.strip().replace("Location", "").strip()
                    elif "icon-material-outline-access-time" in li.find("i")["class"]:
                        if "Expires" in li.text:
                            expiry_date = li.text.strip().split("Expires")[1].strip()

                jobs.append({
                    "No.": i,
                    "Job Title": title.text.strip(),
                    "Company Name": company.text.strip(),
                    "Location": location if location else "N/A",
                    "Expiry Date": expiry_date if expiry_date else "N/A",
                    "Job Description": description.text.strip().replace("\n", " ").replace("\r", " ")
                })
            except Exception as e:
                logging.error(f"Error processing job listing #{i}: {e}")
        return jobs
    except Exception as e:
        logging.error(f"Error during job extraction: {e}")
        return []

# Function to save jobs to CSV
def save_to_csv(jobs, file_path):
    try:
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, "w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=["No.", "Job Title", "Company Name", "Location", "Expiry Date", "Job Description"])
            writer.writeheader()
            writer.writerows(jobs)
        logging.info(f"✅ Jobs saved successfully to: {file_path}")
        print(f"✅ Jobs saved successfully to: {file_path}")
    except Exception as e:
        logging.error(f"Failed to save jobs to CSV: {e}")
        print("❌ Failed to save data. Check the log for details.")

# Main scraping function
def scrape_jobs():
    logging.info("Starting job scraping process...")
    soup = fetch_webpage(URL)
    if soup:
        jobs = extract_jobs(soup)
        if jobs:
            save_to_csv(jobs, OUTPUT_PATH)
        else:
            logging.warning("No jobs extracted.")
            print("⚠️ No jobs found.")
    else:
        print("❌ Failed to fetch the webpage. Check the log for details.")

# Scheduler setup
def schedule_scraping():
    schedule.every().day.at("10:00").do(scrape_jobs)  # Adjust timing as needed
    logging.info("Scheduling enabled for scraping at 10:00 daily.")

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    # Uncomment the following line if you want to enable scheduling
    #schedule_scraping()

    # Run the scraper immediately
    scrape_jobs()


