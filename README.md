# Python Selenium BDD Framework

This project is a Behavior-Driven Development (BDD) framework for web application automation using Python, Selenium, and Behave. It provides a structured approach to writing tests that are easy to understand and maintain.

## Project Structure

```
python-selenium-bdd-framework
├── src
│   ├── environment.py          # Setup and teardown for Behave tests
│   ├── helper_web.py           # Utility functions for browser interactions
│   ├── pages
│   │   └── base_page.py        # Base page class for page object model
│   ├── steps
│   │   └── step_definitions.py  # Step definitions for Behave
│   └── features
│       ├── example.feature      # Feature file in Gherkin syntax
│       └── steps
│           └── example_steps.py # Step implementations for the feature
├── setup.cfg                   # Configuration file for the project
├── requirements.txt            # List of required Python packages
└── README.md                   # Project documentation
```

## Setup Instructions

1. **Clone the repository**:
   ```
   git clone <repository-url>
   cd python-selenium-bdd-framework
   ```

2. **Install dependencies**:
   Make sure you have Python installed, then run:
   ```
   pip install -r requirements.txt
   ```

3. **Configure the environment**:
   Update the `setup.cfg` file to specify your desired browser and other configurations.

## Usage

To run the tests, use the following command:
```
behave
```

This will execute all the scenarios defined in the feature files located in the `src/features` directory.

## Examples

Refer to the `example.feature` file for a sample feature and its corresponding step implementations in `example_steps.py`. You can create additional feature files and step definitions as needed to expand your test coverage.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any enhancements or bug fixes.