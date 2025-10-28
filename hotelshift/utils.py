"""
Utility functions for data processing and file operations.
"""

import csv
from typing import List, Dict
import re


def save_to_csv(books: List[Dict[str, str]], filename: str):
    """
    Save books data to CSV file.

    Args:
        books: List of book dictionaries
        filename: Output CSV filename
    """
    if not books:
        print(f"No data to save to {filename}")
        return

    fieldnames = ['title', 'price', 'availability', 'url']

    try:
        with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(books)
        print(f"Saved {len(books)} books to {filename}")
    except IOError as e:
        print(f"Error writing to {filename}: {e}")


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


def calculate_average_price(books: List[Dict[str, str]]) -> float:
    """
    Calculate average price of books.

    Args:
        books: List of book dictionaries

    Returns:
        Average price rounded to 2 decimals
    """
    if not books:
        return 0.0

    total = sum(clean_price(book['price']) for book in books)
    return round(total / len(books), 2)