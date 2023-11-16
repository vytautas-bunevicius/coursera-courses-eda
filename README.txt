Setup Guide:

- Install the required Python packages using the following command:

            pip install -r requirements.txt

- Clone the repository:

            git clone https://github.com/vytautas-bunevicius/CourseraEDA.git

- Navigate to the repository directory:

            cd CourseraEDA

Run the following command to start the Jupyter Notebook:

            jupyter notebook

Open the CourseraEDA.ipynb notebook and start exploring the data.

Overview:

- This exploratory data analysis (EDA) provides insights into the distribution of courses on Coursera, using data from the Coursera API. The analysis encompasses various data preprocessing steps, descriptive statistics, and visualizations to uncover patterns related to course ratings, student enrollments, and certificate types.

Key Steps in the EDA

Data Cleaning:

- Dropped unnecessary "Unnamed: 0" feature for dataset cleanliness.
- Changed feature names to lowercase for consistency.
- Checked for and removed duplicate rows and columns.
- Handled missing values by imputing them with the mean of the corresponding feature.
- Identified and removed duplicate rows and columns by comparing the unique values of each feature.

Data Types and Categorical Features:

- Checked feature types and converted categorical features labeled as 'objects' to the categorical data type for efficiency.
- Transformed object-type features to numeric type, handling abbreviations for thousands ('k') and millions ('m’) using regular expressions.

Descriptive Statistics:

- Examined average course ratings, average number of students enrolled, and other descriptive statistics.
- Investigated the distribution of numerical features such as course ratings and student enrollments using histograms.

Outliers Detection:

- Used the IQR method to identify outliers in course ratings and student enrollments.
- Visualized outliers through box plots, highlighting the natural skewness in the distribution.

Correlation Analysis:

- Checked the correlation between course ratings and students enrolled.
- Identified a weak positive correlation, emphasizing the importance of not inferring causation using a heatmap visualization.

Top and Bottom Courses:

- Identified the course with the most and fewest enrollments, examining their ratings.
- Highlighted popular courses like "Machine Learning" and niche courses like "El Abogado del Futuro" using bar charts.

Certificate Type Analysis:

- Explored the dominance of different certificate types (COURSE, PROFESSIONAL CERTIFICATE, SPECIALIZATION).
- Noted the popularity of COURSE and SPECIALIZATION certificates using a pie chart.

Difficulty Distribution:

- Analyzed the distribution of course difficulties (Beginner, Intermediate, Advanced, Mixed).
- Recognized the prevalence of Beginner and Intermediate levels using a bar chart.

Organization Enrollment Analysis:

- Utilized statistical measures to summarize enrollments for each organization.
- Identified organizations with consistently high enrollments using a table.

Certificate Type and Difficulty Relationship:

- Created a contingency table showing the distribution of course difficulty levels by certificate type.
- Observed patterns in certificate types and difficulty levels using a heatmap visualization.

Conclusion:

- The EDA provides comprehensive insights into Coursera's course distribution, highlighting learner preferences, popular courses, and certificate trends. It emphasizes the importance of data preprocessing, acknowledges skewness in distributions, and explores relationships between key features.
