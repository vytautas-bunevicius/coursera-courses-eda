# Coursera EDA: An Exploratory Data Analysis of Coursera Courses

![Python Version](https://img.shields.io/badge/python-3.12%2B-blue)
![GitHub Issues](https://img.shields.io/github/issues/vytautas-bunevicius/coursera-courses-eda)
![GitHub Forks](https://img.shields.io/github/forks/vytautas-bunevicius/coursera-courses-eda)
![GitHub Stars](https://img.shields.io/github/stars/vytautas-bunevicius/coursera-courses-eda)

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation Guide](#installation-guide)
  - [1. Clone the Repository](#1-clone-the-repository)
  - [2. Set Up Virtual Environment](#2-set-up-virtual-environment)
  - [3. Install Dependencies](#3-install-dependencies)
    - [Using Pip](#using-pip)
    - [Using Poetry (Optional)](#using-poetry-optional)
  - [4. Launch Jupyter Notebook](#4-launch-jupyter-notebook)
  - [5. Access the Analysis](#5-access-the-analysis)
- [Analysis Components](#analysis-components)
  - [Data Preprocessing](#data-preprocessing)
  - [Exploratory Analysis](#exploratory-analysis)
- [Visualizations](#visualizations)
- [Results and Findings](#results-and-findings)
- [Usage](#usage)

## Overview

The **Coursera EDA** project conducts an in-depth Exploratory Data Analysis of Coursera courses using data retrieved from the Coursera API. This analysis includes data preprocessing, descriptive statistics, and a variety of visualizations to identify patterns related to course ratings, student enrollments, and certificate types. The insights gained can help educators, learners, and organizations make informed decisions about course offerings and enrollments.

## Features

- **Data Cleaning**: Efficiently cleans and prepares the data for analysis.
- **Descriptive Statistics**: Provides summary statistics to understand data distributions.
- **Correlation Analysis**: Examines relationships between key variables.
- **Comprehensive Visualizations**: Utilizes multiple chart types to illustrate findings.
- **Organizational Insights**: Analyzes enrollment patterns and certificate distributions across organizations.

## Prerequisites

- **Python**: Version 3.12 or higher
- **Git**: For cloning the repository
- **Pip**: Package installer for Python
- **(Optional) Poetry**: For dependency management

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

You have two options to install dependencies: using **pip** or **Poetry**.

#### Using Pip

1. **Generate `requirements.txt` (Optional)**

   If you prefer using `pip`, it's helpful to generate a `requirements.txt` file from your `pyproject.toml`. This ensures that all dependencies are accurately captured.

   ```bash
   # Ensure Poetry is installed
   pip install poetry

   # Export dependencies to requirements.txt
   poetry export -f requirements.txt --output requirements.txt
   ```

2. **Install Dependencies**

   Use `pip` to install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

   Alternatively, you can install the package in editable mode directly:

   ```bash
   pip install -e .
   ```

   > **Note:** Ensure that your `pyproject.toml` includes the necessary metadata for `pip` to recognize the package. Poetry typically handles this, but double-check if you encounter issues.

#### Using Poetry (Optional)

If you prefer to continue using Poetry for dependency management and environment handling, follow these steps:

1. **Install Poetry**

   If you don't have Poetry installed, you can install it using the following command:

   ```bash
   # Using the official installer
   curl -sSL https://install.python-poetry.org | python3 -

   # After installation, ensure Poetry is added to your PATH
   export PATH="$HOME/.local/bin:$PATH"
   ```

   For more installation options and troubleshooting, refer to the [Poetry documentation](https://python-poetry.org/docs/#installation).

2. **Install Dependencies**

   Use Poetry to install the required dependencies and set up the virtual environment:

   ```bash
   poetry install
   ```

   This command will create a virtual environment (if not already created) and install all the dependencies specified in `pyproject.toml`.

### 4. Launch Jupyter Notebook

Start Jupyter Notebook within your activated virtual environment:

```bash
# If installed via Pip
jupyter notebook

# If using Poetry
poetry run jupyter notebook
```

### 5. Access the Analysis

Open the `coursera_courses.ipynb` notebook in your browser to begin exploring the data.

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
