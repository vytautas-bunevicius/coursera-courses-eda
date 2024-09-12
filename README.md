# Coursera EDA: An Exploratory Data Analysis of Coursera Courses

## Overview

This exploratory data analysis (EDA) delves into the distribution of courses on Coursera, utilizing data from the Coursera API. The analysis encompasses various data preprocessing steps, descriptive statistics, and visualizations to uncover patterns related to course ratings, student enrollments, and certificate types.

## Setup Guide

1. **Clone the Repository**
    ```
    git clone https://github.com/vytautas-bunevicius/coursera-courses-eda.git
    ```

2. **Navigate to Repository Directory**
    ```
    cd coursera-courses-eda
    ```
3. **Install the required Python packages using the following command:**
    ```
    pip install -r requirements.txt
    ```
4 **Launch Jupyter Notebook**
    ```
    jupyter notebook
    ```

#### Explore the Data

Open the `coursera_courses.ipynb` notebook and embark on your data exploration journey.

### Key Steps in the EDA

#### Data Cleaning

Removed unnecessary "Unnamed: 0" feature for dataset cleanliness.
Standardized feature names to lowercase for consistency.
Detected and removed duplicate rows and columns.
Imputed missing values with the mean of the corresponding feature.
Identified and eliminated duplicate rows and columns by comparing unique values of each feature.

#### Data Types and Categorical Features

Verified feature types and converted categorical features labeled as 'objects' to the categorical data type for improved efficiency.
Transformed object-type features to numeric type, handling abbreviations for thousands ('k') and millions ('m’) using regular expressions.

#### Descriptive Statistics

Analyzed average course ratings, average number of students enrolled, and other descriptive statistics.
Investigated the distribution of numerical features such as course ratings and student enrollments using histograms.

#### Outliers Detection

Employed the IQR method to identify outliers in course ratings and student enrollments.
Visualized outliers through box plots, highlighting the natural skewness in the distribution.

#### Correlation Analysis

Investigated the correlation between course ratings and students enrolled.
Uncovered a weak positive correlation, emphasizing the importance of avoiding causal inferences using a heatmap visualization.

#### Top and Bottom Courses

Identified the course with the highest and lowest enrollments, examining their ratings.
Highlighted popular courses like "Machine Learning" and niche courses like "El Abogado del Futuro" using bar charts.

#### Certificate Type Analysis

Explored the prevalence of different certificate types (COURSE, PROFESSIONAL CERTIFICATE, SPECIALIZATION).
Noted the popularity of COURSE and SPECIALIZATION certificates using a pie chart.

#### Difficulty Distribution

Analyzed the distribution of course difficulties (Beginner, Intermediate, Advanced, Mixed).
Recognized the dominance of Beginner and Intermediate levels using a bar chart.

#### Organization Enrollment Analysis

Utilized statistical measures to summarize enrollments for each organization.
Identified organizations with consistently high enrollments using a table.

#### Certificate Type and Difficulty Relationship

Created a contingency table showing the distribution of course difficulty levels by certificate type.
Observed patterns in certificate types and difficulty levels using a heatmap visualization.

### Conclusion

This EDA provides comprehensive insights into Coursera's course distribution, shedding light on learner preferences, popular courses, and certificate trends. It emphasizes the importance of data preprocessing, acknowledges skewness in distributions, and explores relationships between key features.
