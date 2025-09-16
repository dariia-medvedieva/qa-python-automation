# Basic unit tests for the is_valid_email function
# Positive and negative scenarios covered

import json
import os
import pytest
from src.email_validator import is_valid_email

# Load test data from JSON
def load_test_data():
    with open(os.path.join(os.path.dirname(__file__), '..', 'data', 'test_emails.json'), 'r') as file:
        return json.load(file)

test_data = load_test_data()

@pytest.mark.parametrize("email", test_data["valid_emails"])
def test_valid_emails(email):
    assert is_valid_email(email) is True

@pytest.mark.parametrize("email", test_data["invalid_emails"])
def test_invalid_emails(email):
    assert is_valid_email(email) is False
