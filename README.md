# hotelshift - Book Scraper

A Python web scraping application that extracts book data from [books.toscrape.com](http://books.toscrape.com/), a sandbox website designed for practicing web scraping.

## 📖 Overview

This project scrapes book information from the first 3 pages of books.toscrape.com, filters books by price range, and exports the data to CSV files for analysis.

### Features

- 🔍 Scrapes book title, price, availability, and URL
- 💰 Filters books by price range (£10-£50)
- 📊 Exports data to CSV files (raw and filtered)
- 📈 Calculates and displays statistics
- 🤝 Follows polite scraping practices with delays
- ⚠️ Handles errors gracefully

## 📋 Requirements

- Python 3.7 or higher
- pip (Python package manager)

## 🚀 Local Run SOP (Standard Operating Procedure)
### Step 0: Folder layout

```
PythonProject/
├─ .venv/                ← virtual environment (outside repo)
└─ hotelsheft/          ← your repo
    ├─ main.py
    ├─ requirements.txt
    └─ ...

```

### Step 1: Navigate to Parent Directory

```
cd PythonProject
```

### Step 2: Set Up Virtual Environment(Recommended)
On Windows(PowerShell or CMD):

```
python -m venv .venv
.venv\Scripts\activate
```

On macOS/Linux:

```
python3 -m venv .venv
source .venv/bin/activate
```

### Step 3: Install Dependencies

```
cd hotelshift
pip install -r requirements.txt
```
This will install:
requests==2.31.0 - For HTTP requests
beautifulsoup4==4.12.2 - For HTML parsing
### Step 4: Run the Scraper
```
python main.py
```

### Step 5: View Results
After execution, you'll find two CSV files in the current directory:
books_raw.csv - All scraped books (~60 books)
books_filtered.csv - Books priced between £10-£50

## 📊 Expected Output
```
Starting web scraping...
--------------------------------------------------
Scraping page 1...
Found 20 books on page 1
Scraping page 2...
Found 20 books on page 2
Scraping page 3...
Found 20 books on page 3
--------------------------------------------------
Total books scraped: 60
Saved 60 books to books_raw.csv
Saved XX books to books_filtered.csv
--------------------------------------------------
SUMMARY
--------------------------------------------------
Total books scraped: 60
Total after filtering (£10-£50): XX
Average price of filtered set: £XX.XX
--------------------------------------------------
Done! Check books_raw.csv and books_filtered.csv in the current directory.
```
