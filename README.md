# QA Python Automation  

Repository for Python-based QA automation practice.  
Includes exercises, test scripts, and examples focused on:  
- UI and API testing  
- Test automation best practices  
- CI/CD integration  
- Exploring AI-powered testing approaches  

## Status
Work in progress — evolving with each commit.  

## Tech Stack
- Python 3
- `pytest` — test framework
- `requests` — API testing (planned)
- GitHub Actions (planned CI)
- Logging (planned)

## Project Structure

```text
qa-python-automation/
├── src/                  # Core logic (validators, utilities, etc.)
│   └── email_validator.py
│
├── tests/                # Unit and integration tests
│   └── test_email_validator.py
│
├── data/                 # Test data (JSON, CSV)
│   └── test_emails.json
│
├── docs/                 # Docs and checklists
│
├── 01_python_basics/     # Python CLI and warmups
│   └── hello_cli.py
│
├── requirements.txt      # Dependencies
└── README.md
```

## How to Run CLI script

Clone the repository (or download ZIP) and run scripts from your terminal:

```bash
# basic run
python3 01_python_basics/hello_cli.py

# with custom name
python3 01_python_basics/hello_cli.py --name Dariia

# repeat multiple times
python3 01_python_basics/hello_cli.py --name Tester --repeat 3

# see help
python3 01_python_basics/hello_cli.py --help
```

##  How to Run Tests

Make sure pytest is installed:

```bash
pip install -r requirements.txt
```

Then run:
```bash
pytest tests/
```

## Planned Features

- Add API testing module with `requests`
- Create GitHub Actions workflow for CI
- Add logging and structured reports
- Expand test coverage with parametrized edge cases
- Integrate with JSON/CSV test data
- Build exploratory AI-assisted test PoC
