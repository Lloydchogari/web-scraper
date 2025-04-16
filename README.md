# Job Scraper

A Python-based web scraper that automatically extracts job listings from VacancyMail Zimbabwe and saves them to a CSV file for easy analysis.

## Overview

This tool scrapes the latest job postings from [VacancyMail Zimbabwe](https://vacancymail.co.zw/jobs/), extracting key information such as:
- Job titles
- Company names
- Locations
- Expiry dates
- Job descriptions

The data is saved in a structured CSV format, making it easy to review job opportunities or perform further analysis.

## Features

- 🔄 Automated daily scraping (configurable)
- 📊 Structured data output in CSV format
- 📝 Comprehensive logging for troubleshooting
- 🛡️ Error handling for robust operation
- ⏱️ Scheduling capabilities for automated runs

## Requirements

- Python 3.6+
- Required packages:
  - beautifulsoup4
  - requests
  - schedule
  - csv (built-in)
  - logging (built-in)
  - os (built-in)
  - time (built-in)

## Installation

1. Clone this repository or download the source code
2. Install the required dependencies:

```bash
pip install beautifulsoup4 requests schedule
```

## Configuration

Before running the script, you may want to modify these variables in the code:

- `URL`: The target website to scrape (default: "https://vacancymail.co.zw/jobs/")
- `OUTPUT_PATH`: Where the CSV file will be saved (default: "C:\\Users\\uncommonStudent\\OneDrive\\Desktop\\test.py\\job_scrape\\scraped_data.csv")

## Usage

### One-time Scraping

To run the scraper once:

```bash
python job_scraper.py
```

### Scheduled Scraping

To enable scheduled daily scraping at 10:00 AM:

1. Uncomment the `schedule_scraping()` line in the main block
2. Comment out the `scrape_jobs()` line
3. Run the script:

```bash
python job_scraper.py
```

The script will continue running in the background, performing the scraping task daily at the scheduled time.

## Output

The script generates:

1. A CSV file with job listings at the specified `OUTPUT_PATH`
2. A log file (`job_scraper.log`) in the same directory as the script

## Troubleshooting

If you encounter issues:

1. Check the `job_scraper.log` file for error messages
2. Ensure you have internet connectivity
3. Verify that the target website structure hasn't changed
4. Make sure you have write permissions for the output directory

## License

[LLOYD DONNEL CHOGARI]

## Disclaimer

This tool is for educational and personal use only. Please respect the target website's terms of service and robots.txt file. Excessive scraping may result in your IP being blocked.
