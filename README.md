# Coursera EDA: An Exploratory Data Analysis of Coursera Courses

![Python Version](https://img.shields.io/badge/python-3.12%2B-blue)
![GitHub Issues](https://img.shields.io/github/issues/vytautas-bunevicius/coursera-courses-eda)
![GitHub Forks](https://img.shields.io/github/forks/vytautas-bunevicius/coursera-courses-eda)
![GitHub Stars](https://img.shields.io/github/stars/vytautas-bunevicius/coursera-courses-eda)
![Pytest](https://img.shields.io/badge/tests-passing-brightgreen) <!-- Update this badge based on your CI setup -->

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation Guide](#installation-guide)
  - [1. Clone the Repository](#1-clone-the-repository)
  - [2. Set Up Virtual Environment](#2-set-up-virtual-environment)
  - [3. Install Dependencies](#3-install-dependencies)
  - [4. Launch Jupyter Notebook](#4-launch-jupyter-notebook)
  - [5. Access the Analysis](#5-access-the-analysis)
- [Testing](#testing)
  - [Running Unit Tests](#running-unit-tests)
- [Analysis Components](#analysis-components)
  - [Data Preprocessing](#data-preprocessing)
  - [Exploratory Analysis](#exploratory-analysis)
- [Visualizations](#visualizations)
- [Results and Findings](#results-and-findings)
- [Usage](#usage)
- [License](#license)

## Overview

The **Coursera EDA** project conducts an in-depth Exploratory Data Analysis of Coursera courses using data retrieved from the Coursera API. This analysis includes data preprocessing, descriptive statistics, and a variety of visualizations to identify patterns related to course ratings, student enrollments, and certificate types. The insights gained can help educators, learners, and organizations make informed decisions about course offerings and enrollments.

## Features

- **Data Cleaning**: Efficiently cleans and prepares the data for analysis.
- **Descriptive Statistics**: Provides summary statistics to understand data distributions.
- **Correlation Analysis**: Examines relationships between key variables.
- **Comprehensive Visualizations**: Utilizes multiple chart types to illustrate findings.
- **Organizational Insights**: Analyzes enrollment patterns and certificate distributions across organizations.
- **Unit Testing**: Ensures reliability and correctness of utility functions through comprehensive tests.

## Prerequisites

- **Python**: Version 3.12 or higher
- **Git**: For cloning the repository
- **Pip**: Package installer for Python

## Installation Guide

### 1. Clone the Repository

Clone the repository to your local machine using Git:

```bash
git clone https://github.com/vytautas-bunevicius/coursera-courses-eda.git
cd coursera-courses-eda
```

### 2. Set Up Virtual Environment

Create and activate a virtual environment to manage dependencies:

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate

# On macOS/Linux:
source venv/bin/activate
```

### 3. Install Dependencies

Use `pip` to install the required packages, including testing frameworks:

```bash
pip install -e .
```

*This command installs all necessary dependencies listed in your project's configuration files (e.g., `setup.py` or `pyproject.toml`), including `pytest` for running unit tests.*

### 4. Launch Jupyter Notebook

Start Jupyter Notebook within your activated virtual environment:

```bash
jupyter notebook
```

### 5. Access the Analysis

Open the `coursera_courses.ipynb` notebook in your browser to begin exploring the data.

## Testing

Comprehensive unit tests ensure the reliability and correctness of the utility functions used in this project.

### Running Unit Tests

To run the unit tests, follow these steps:

1. **Ensure that `pytest` is installed** (installed via `pip install -e .` as part of dependencies).

2. **Execute the tests** by running the following command in the project's root directory:

    ```bash
    pytest tests/
    ```

    This command will discover and run all tests located in the `tests/` directory.

3. **Review Test Results**:

    - **Passed Tests**: Indicated by dots (`.`) in the output.
    - **Failed Tests**: Indicated by `F`, along with detailed failure messages.

    Example output:

    ```bash
    ============================================================================== test session starts ==============================================================================
    platform darwin -- Python 3.12.5, pytest-8.3.3, pluggy-1.5.0
    rootdir: /Users/vytautasbunevicius/coursera-courses-eda
    configfile: pyproject.toml
    collected 22 items

    tests/test_utils.py .............FF.......                                                                                                                                [100%]

    =================================================================================== FAILURES ====================================================================================
    ...
    ============================================================================ short test summary info ============================================================================
    FAILED tests/test_utils.py::test_detect_and_print_outliers_iqr - assert "Potential outliers for 'course_students_enrolled':" in ...
    FAILED tests/test_utils.py::test_detect_and_print_outliers_iqr_no_outliers - assert "Potential outliers for 'course_students_enrolled':" in ...
    ========================================================================= 2 failed, 20 passed in 0.98s ==========================================================================
    ```

4. **Addressing Failures**:

    - Review the failure messages to identify and fix issues in the code.
    - Re-run the tests to ensure all tests pass after making corrections.

## Analysis Components

### Data Preprocessing

- **Data Cleaning**
  - Removal of unnecessary features
  - Standardization of feature names
  - Duplicate detection and removal
  - Missing value imputation
- **Data Type Management**
  - Conversion of categorical features
  - Numeric type transformation
  - Handling of abbreviated values (e.g., k for thousands, m for millions)

### Exploratory Analysis

#### 1. Descriptive Statistics

- Calculation of average course ratings
- Analysis of enrollment statistics
- Distribution analysis of key metrics
- Outlier detection using the IQR method

#### 2. Correlation Studies

- Examination of the relationship between course ratings and enrollments
- Visualization of the correlation matrix
- In-depth relationship analysis between variables

#### 3. Course Analysis

- Identification of top-performing courses
- Analysis of enrollment patterns
- Distribution of certificate types
- Assessment of course difficulty levels

#### 4. Organizational Insights

- Analysis of enrollments across different organizations
- Examination of relationships between certificate types and organizations
- Distribution analysis of course difficulty levels within organizations

## Visualizations

- **Histograms**: Display numerical distributions
- **Box Plots**: Identify outliers and distribution spread
- **Heat Maps**: Visualize correlations between variables
- **Pie Charts**: Show categorical distributions
- **Bar Charts**: Compare different categories and metrics

## Results and Findings

- **Course Ecosystem Insights**: Comprehensive understanding of Coursera's course offerings
- **Learner Preferences**: Patterns in what learners prefer based on ratings and enrollments
- **Popular Course Characteristics**: Identifying features of high-performing courses
- **Certificate Trends**: Analysis of the types and popularity of certificates offered
- **Difficulty Distribution**: Insights into the distribution of course difficulty levels

## Usage

To utilize this project for your own analysis:

1. **Data Retrieval**: Update the `coursera_courses.csv` with the latest data from the Coursera API.
2. **Customization**: Modify the Jupyter Notebook (`coursera_courses.ipynb`) to include additional analyses or visualizations as needed.
3. **Visualization**: Use the existing visualization templates to create new charts or graphs relevant to your interests.

## License

This project is licensed under the [Unlicense](LICENSE).
