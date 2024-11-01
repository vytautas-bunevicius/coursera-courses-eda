# Coursera EDA: An Exploratory Data Analysis of Coursera Courses

## Overview

This exploratory data analysis (EDA) delves into the distribution of courses on Coursera, utilizing data from the Coursera API. The analysis encompasses various data preprocessing steps, descriptive statistics, and visualizations to uncover patterns related to course ratings, student enrollments, and certificate types.

## Prerequisites

- Python 3.8 or higher
- Git

## Installation Guide

### 1. Clone the Repository

```bash
git clone https://github.com/vytautas-bunevicius/coursera-courses-eda.git
cd coursera-courses-eda
```

### 2. Set Up Virtual Environment

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

```bash
# Upgrade pip
python -m pip install --upgrade pip

# Install required packages
pip install -r requirements.txt
```

### 4. Launch Jupyter Notebook

```bash
jupyter notebook
```

### 5. Access the Analysis

Open `coursera_courses.ipynb` in your browser to start exploring the data.

## Project Structure

```
coursera-courses-eda/
├── README.md
├── requirements.txt
├── data/
│   └── coursera_courses.csv
├── notebooks/
│   └── coursera_courses.ipynb
└── venv/                      # Virtual environment directory
```

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
  - Handling of abbreviated values (k, m)

### Exploratory Analysis

#### 1. Descriptive Statistics

- Average course ratings
- Enrollment statistics
- Distribution analysis
- Outlier detection using IQR method

#### 2. Correlation Studies

- Course ratings vs. enrollments
- Correlation matrix visualization
- Relationship analysis

#### 3. Course Analysis

- Top performing courses
- Enrollment patterns
- Certificate type distribution
- Difficulty level assessment

#### 4. Organizational Insights

- Organization-wise enrollment analysis
- Certificate type relationships
- Difficulty level distribution

## Visualizations

- Histograms for numerical distributions
- Box plots for outlier analysis
- Heat maps for correlations
- Pie charts for categorical distributions
- Bar charts for comparative analysis

## Results and Findings

- Comprehensive insights into Coursera's course ecosystem
- Learner preference patterns
- Popular course characteristics
- Certificate type trends
- Difficulty level distribution patterns
