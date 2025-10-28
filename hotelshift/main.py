"""
Main entry point for the book scraping application.
"""

from scraper import BookScraper
from utils import save_to_csv, calculate_average_price


def main():
    """
    Main function to orchestrate the scraping process.
    """
    scraper = BookScraper(base_url="http://books.toscrape.com")

    print("Starting web scraping...")
    print("-" * 50)

    # Scrape first 3 pages
    all_books = scraper.scrape_multiple_pages(num_pages=3)

    print("-" * 50)
    print(f"Total books scraped: {len(all_books)}")

    # Save raw data
    save_to_csv(all_books, 'books_raw.csv')

    # Filter books by price (£10 - £50 inclusive)
    filtered_books = scraper.filter_books_by_price(all_books, min_price=10.0, max_price=50.0)

    # Save filtered data
    save_to_csv(filtered_books, 'books_filtered.csv')

    # Calculate statistics
    avg_price = calculate_average_price(filtered_books)

    # Print summary
    print("-" * 50)
    print("SUMMARY")
    print("-" * 50)
    print(f"Total books scraped: {len(all_books)}")
    print(f"Total after filtering (£10-£50): {len(filtered_books)}")
    print(f"Average price of filtered set: £{avg_price}")
    print("-" * 50)
    print("Done! Check books_raw.csv and books_filtered.csv in the current directory.")


if __name__ == "__main__":
    main()