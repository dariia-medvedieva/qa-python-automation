# Basic unit tests for the is_valid_email function
# Positive and negative scenarios covered
import pytest
from src.email_validator import is_valid_email

def test_valid_email():
    assert is_valid_email("test@example.com") == True

def test_invalid_email_no_at():
    assert is_valid_email("testexample.com") == False

def test_invalid_email_no_domain():
    assert is_valid_email("test@") == False

def test_invalid_email_empty():
    assert is_valid_email("") == False

def test_invalid_email_spaces():
    assert is_valid_email("test @example.com") == False
