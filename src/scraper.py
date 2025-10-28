"""
Web scraper module for extracting book data from books.toscrape.com
"""

import requests
from bs4 import BeautifulSoup
import time
import re
from typing import List, Dict, Optional


class BookScraper:
    """
    A web scraper for books.toscrape.com that extracts book information.
    """

    def __init__(self, base_url: str):
        """
        Initialize the scraper with a base URL.

        Args:
            base_url: The base URL of the website to scrape
        """
        self.base_url = base_url.rstrip('/')
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Educational Purpose Book Scraper)'
        })

    def scrape_page(self, page_num: int) -> List[Dict[str, str]]:
        """
        Scrape book data from a single page.

        Args:
            page_num: The page number to scrape

        Returns:
            List of dictionaries containing book data
        """
        url = f"{self.base_url}/catalogue/page-{page_num}.html"

        try:
            response = self.session.get(url, timeout=10)
            response.raise_for_status()

            soup = BeautifulSoup(response.content, 'html.parser')
            books = []

            # Find all book articles
            book_articles = soup.find_all('article', class_='product_pod')

            for article in book_articles:
                book_data = self._extract_book_data(article, url)
                if book_data:
                    books.append(book_data)

            return books

        except requests.RequestException as e:
            print(f"Error fetching page {page_num}: {e}")
            return []
        except Exception as e:
            print(f"Error parsing page {page_num}: {e}")
            return []

    def _extract_book_data(self, article, base_url: str) -> Optional[Dict[str, str]]:
        """
        Extract book data from an article element.

        Args:
            article: BeautifulSoup article element
            base_url: Base URL for constructing absolute URLs

        Returns:
            Dictionary containing book data or None if extraction fails
        """
        try:
            # Extract title
            title_tag = article.find('h3').find('a')
            title = title_tag.get('title', '')

            # Extract relative URL and convert to absolute
            relative_url = title_tag.get('href', '')
            book_url = requests.compat.urljoin(base_url, relative_url)

            # Extract price
            price_tag = article.find('p', class_='price_color')
            price_text = price_tag.text if price_tag else '£0.00'

            # Extract availability
            availability_tag = article.find('p', class_='instock availability')
            availability = availability_tag.text.strip() if availability_tag else 'Unknown'

            return {
                'title': title,
                'price': price_text,
                'availability': availability,
                'url': book_url
            }
        except Exception as e:
            print(f"Error extracting book data: {e}")
            return None

    def scrape_multiple_pages(self, num_pages: int, delay: float = 1.0) -> List[Dict[str, str]]:
        """
        Scrape multiple pages with polite delays between requests.

        Args:
            num_pages: Number of pages to scrape
            delay: Delay in seconds between requests (default: 1.0)

        Returns:
            List of all books scraped from all pages
        """
        all_books = []

        for page_num in range(1, num_pages + 1):
            print(f"Scraping page {page_num}...")

            books = self.scrape_page(page_num)
            all_books.extend(books)

            print(f"Found {len(books)} books on page {page_num}")

            # Be polite: wait between requests
            if page_num < num_pages:
                time.sleep(delay)

        return all_books

    @staticmethod
    def clean_price(price_str: str) -> float:
        """
        Clean price string and convert to float.

        Args:
            price_str: Price string like "£53.74"

        Returns:
            Float value of the price
        """
        # Remove currency symbols and spaces
        cleaned = re.sub(r'[£$€\s]', '', price_str)
        try:
            return float(cleaned)
        except ValueError:
            return 0.0

    def filter_books_by_price(self, books: List[Dict[str, str]],
                              min_price: float = 10.0,
                              max_price: float = 50.0) -> List[Dict[str, str]]:
        """
        Filter books based on price range.

        Args:
            books: List of book dictionaries
            min_price: Minimum price (inclusive)
            max_price: Maximum price (inclusive)

        Returns:
            Filtered list of books
        """
        filtered = []
        for book in books:
            price = self.clean_price(book['price'])
            if min_price <= price <= max_price:
                filtered.append(book)
        return filtered