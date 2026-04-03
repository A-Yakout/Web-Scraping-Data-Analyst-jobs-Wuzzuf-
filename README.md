# 📊 Wuzzuf Data Analyst Job Market Analysis (Egypt 2026)

An end-to-end Data Engineering and Analysis project that scrapes, cleans, and analyzes Data Analyst job postings on **Wuzzuf** (Egypt's leading job portal). This project aims to uncover the most in-demand skills, top-hiring sectors, and geographic distribution of data roles in the Egyptian market.

---

## 🚀 Project Overview
The project follows a complete **ETL (Extract, Transform, Load)** pipeline:
1.  **Extraction:** Scraped dynamic job data using `Python` and `Playwright`.
2.  **Transformation:** Cleaned and structured the raw data using `Pandas` (Python) and `Power Query` (Excel).
3.  **Analysis:** Performed statistical analysis to identify skill trends and market hotspots.

---

## 🛠️ Tech Stack
* **Language:** Python 3.x
* **Scraping:** [Playwright](https://playwright.dev/python/) (To handle dynamic content and async loading).
* **Data Manipulation:** [Pandas](https://pandas.pydata.org/) (For data unnesting/exploding skills).
* **Data Cleaning:** Power Query (For geographic mapping and data imputation).
* **Visualization:** Excel

---

## 🔍 Key Features & Challenges
* **Dynamic Scraping:** Implemented advanced Playwright selectors to handle asynchronous page loads.
* **Error Handling:** Managed `TimeoutErrors` and `Strict Mode Violations` to ensure a robust scraping process.
* **Skill Unnesting:** Used Pandas `.explode()` to transform comma-separated skills into individual rows for accurate frequency counting.
* **Data Imputation:** Applied conditional logic in Power Query to map "Egypt" entries to their specific "City" counterparts for better geographic granularity.

---

## 📈 Top Insights (Egypt 2026)
Based on the analyzed data, here are the core findings:

1.  **The Dominant Tools:** **Microsoft Excel** remains the #1 requested tool, followed closely by **SQL**.
2.  **The Communication Gap:** Surprisingly, **English Language** appeared as a top-tier "skill" tag, often prioritized alongside technical tools.
3.  **Industry Hotspots:** The **Finance/Accounting** and **IT/Software Development** sectors are the biggest employers for Data Analysts.
4.  **Geographic Focus:** **Cairo** holds the vast majority of job opportunities, followed by Giza and Alexandria.

---
## Author
Abdelrhman Yakout

---

## 📁 Repository Structure
```text
├── data/                   # Raw and Cleaned CSV files
├── src/                    # Scraper source code (Playwright)
├── notebooks/              # Analysis and Visualization (Pandas)
├── README.md               # Project documentation
└── requirements.txt        # Python dependencies
