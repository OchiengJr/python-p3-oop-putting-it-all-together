#!/usr/bin/env python3

from book import Book
import io
import sys
import pytest
from contextlib import redirect_stdout

class TestBook:
    '''Test suite for the Book class in book.py'''

    @pytest.fixture
    def book(self):
        """Fixture to create a Book instance."""
        return Book("And Then There Were None", 272)

    def test_has_title_and_page_count(self, book):
        '''has the title and page_count passed into __init__, and values can be set to new instance.'''
        assert book.title == "And Then There Were None"
        assert book.page_count == 272

    def test_requires_int_page_count(self, book):
        '''prints "page_count must be an integer" if page_count is not an integer.'''
        captured_out = io.StringIO()
        with redirect_stdout(captured_out):
            book.page_count = "not an integer"
        assert captured_out.getvalue() == "page_count must be an integer\n"

    def test_can_turn_page(self):
        '''outputs "Flipping the page...wow, you read fast!" when method turn_page() is called'''
        book = Book("The World According to Garp", 69)
        captured_out = io.StringIO()
        with redirect_stdout(captured_out):
            book.turn_page()
        assert captured_out.getvalue() == "Flipping the page...wow, you read fast!\n"
