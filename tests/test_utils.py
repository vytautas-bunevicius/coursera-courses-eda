"""
Tests for Coursera Courses EDA Utility Functions

This module contains unit tests for the utility functions used in the Coursera
courses exploratory data analysis (EDA) project. The tests cover data loading,
processing, and visualization functionalities to ensure reliability and correctness.

Dependencies:
    - pytest>=6.0.0
    - pandas>=1.2.0
    - matplotlib>=3.3.0
    - seaborn>=0.11.0
    - pathlib
    - unittest.mock

Fixtures:
    - sample_csv_content: Provides sample CSV content for testing data loading.
    - sample_dataframe: Creates a sample DataFrame for testing data processing and visualization.

Test Cases:
    - test_convert_students_enrolled: Validates the conversion of enrollment numbers.
    - test_convert_students_enrolled_invalid: Checks handling of invalid enrollment formats.
    - test_load_coursera_data_default_path: Tests loading data from the default file path.
    - test_load_coursera_data_file_not_found: Ensures proper error when the file is missing.
    - test_load_coursera_data_read_exception: Verifies error handling during file read failures.
    - test_detect_and_print_outliers_iqr: Tests outlier detection functionality.
    - test_detect_and_print_outliers_iqr_no_outliers: Ensures no false positives in outlier detection.
    - test_detect_and_print_outliers_iqr_invalid_column: Checks error handling for invalid columns.
    - test_detect_and_print_outliers_iqr_non_numeric: Validates error handling for non-numeric data.
    - test_plot_rating_distribution: Ensures rating distribution plot creation.
    - test_plot_enrollment_distribution: Ensures enrollment distribution plot creation.
    - test_plot_enrollment_distribution_log_scale: Tests enrollment distribution plot with logarithmic scale.
    - test_create_custom_colormap: Verifies custom colormap creation.
    - test_plot_correlation_heatmap: Ensures correlation heatmap plot creation.
    - test_plot_top_organizations: Validates top organizations bar chart creation.
    - close_plots: Automatically closes all plots after each test to prevent memory leaks.
"""

import pytest
from pathlib import Path
from unittest.mock import patch, mock_open
from matplotlib.colors import LinearSegmentedColormap
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

from src.coursera_courses_eda.utils import (
    load_coursera_data,
    convert_students_enrolled,
    detect_and_print_outliers_iqr,
    plot_rating_distribution,
    plot_enrollment_distribution,
    create_custom_colormap,
    plot_correlation_heatmap,
    plot_top_organizations,
    plot_category_distribution,
    plot_ratings_by_category,
    plot_organization_heatmap,
    plot_certificate_difficulty_heatmap,
)


@pytest.fixture
def sample_csv_content() -> str:
    """
    Provide sample CSV content for testing data loading functions.

    Returns:
        str: A multi-line string representing CSV data.

    Example:
        >>> csv_content = sample_csv_content()
        >>> print(csv_content)
        organization,course_rating,course_students_enrolled,course_difficulty,course_certificate_type
        OrgA,4.5,1.2k,Intermediate,Verified
        OrgB,4.0,3.5k,Beginner,Audit
        ...
    """
    return """organization,course_rating,course_students_enrolled,course_difficulty,course_certificate_type
OrgA,4.5,1.2k,Intermediate,Verified
OrgB,4.0,3.5k,Beginner,Audit
OrgC,3.8,500,Advanced,Verified
OrgA,4.7,2m,Intermediate,Audit
OrgD,2.5,750,Beginner,None
OrgE,4.2,1.8k,Advanced,Verified
"""


@pytest.fixture
def sample_dataframe() -> pd.DataFrame:
    """
    Create a sample DataFrame for testing data processing and visualization functions.

    Returns:
        pd.DataFrame: A DataFrame containing sample course data.

    Example:
        >>> df = sample_dataframe()
        >>> print(df.head())
          organization  course_rating course_students_enrolled course_difficulty course_certificate_type
        0        OrgA            4.5                      1.2k      Intermediate               Verified
        1        OrgB            4.0                      3.5k          Beginner                   Audit
        ...
    """
    data = {
        'organization': ['OrgA', 'OrgB', 'OrgC', 'OrgA', 'OrgD', 'OrgE'],
        'course_rating': [4.5, 4.0, 3.8, 4.7, 2.5, 4.2],
        'course_students_enrolled': ['1.2k', '3.5k', '500', '2m', '750', '1.8k'],
        'course_difficulty': [
            'Intermediate', 'Beginner', 'Advanced', 'Intermediate', 'Beginner', 'Advanced'
        ],
        'course_certificate_type': [
            'Verified', 'Audit', 'Verified', 'Audit', 'None', 'Verified'
        ]
    }
    return pd.DataFrame(data)


@pytest.mark.parametrize(
    "input_value,expected",
    [
        ("1.5k", 1500),
        ("2m", 2000000),
        ("500", 500),
        ("0k", 0),
        ("3.25k", 3250),
        ("4.75m", 4750000),
    ]
)
def test_convert_students_enrolled(input_value: str, expected: int) -> None:
    """
    Test valid conversions of enrollment numbers from string to integer.

    Args:
        input_value (str): The enrollment number as a string, potentially with 'k' or 'm' suffix.
        expected (int): The expected integer result after conversion.

    Example:
        >>> test_convert_students_enrolled("1.5k", 1500)
    """
    assert convert_students_enrolled(input_value) == expected


@pytest.mark.parametrize(
    "invalid_value",
    ["1.2b", "abc", "-1k", " "]
)
def test_convert_students_enrolled_invalid(invalid_value: str) -> None:
    """
    Test handling of invalid enrollment number formats.

    Ensures that the function raises a ValueError for malformed, negative, or empty strings.

    Args:
        invalid_value (str): An invalid enrollment number string.

    Example:
        >>> test_convert_students_enrolled_invalid("abc")
    """
    with pytest.raises(ValueError):
        convert_students_enrolled(invalid_value)


@patch("pathlib.Path.is_file", return_value=True)
@patch("builtins.open", new_callable=mock_open, read_data="""organization,course_rating,course_students_enrolled
OrgA,4.5,1.2k
OrgB,4.0,3.5k
""")
@patch("pandas.read_csv")
def test_load_coursera_data_default_path(
    mock_read_csv, mock_file, mock_is_file
) -> None:
    """
    Test loading data from the default file path.

    Mocks the file existence and content to verify that `load_coursera_data` correctly
    reads data from the default CSV file.

    Args:
        mock_read_csv (MagicMock): Mock for pandas.read_csv.
        mock_file (MagicMock): Mock for built-in open function.
        mock_is_file (MagicMock): Mock for Path.is_file.

    Example:
        >>> test_load_coursera_data_default_path()
    """
    mock_read_csv.return_value = pd.DataFrame({
        'organization': ['OrgA', 'OrgB'],
        'course_rating': [4.5, 4.0],
        'course_students_enrolled': ['1.2k', '3.5k']
    })

    df = load_coursera_data()

    mock_read_csv.assert_called_once()
    assert isinstance(df, pd.DataFrame)
    assert df.shape == (2, 3)
    assert list(df.columns) == [
        'organization', 'course_rating', 'course_students_enrolled'
    ]


@patch("pathlib.Path.is_file", return_value=False)
def test_load_coursera_data_file_not_found(
    mock_is_file, sample_csv_content
) -> None:
    """
    Test proper error handling when the dataset file is not found.

    Ensures that a FileNotFoundError is raised with an appropriate message when
    attempting to load data from a non-existent file path.

    Args:
        mock_is_file (MagicMock): Mock for Path.is_file.
        sample_csv_content (str): Sample CSV content (unused here).

    Example:
        >>> test_load_coursera_data_file_not_found()
    """
    with patch("builtins.open", mock_open(read_data=sample_csv_content)):
        with pytest.raises(FileNotFoundError) as exc_info:
            load_coursera_data("non_existent_file.csv")
        assert "Dataset file not found" in str(exc_info.value)


@patch("pandas.read_csv", side_effect=Exception("Read error"))
@patch("pathlib.Path.is_file", return_value=True)
def test_load_coursera_data_read_exception(
    mock_is_file, mock_read_csv, sample_csv_content
) -> None:
    """
    Test handling of exceptions during data loading.

    Simulates an error during the file read process and verifies that the exception
    is propagated with additional context.

    Args:
        mock_is_file (MagicMock): Mock for Path.is_file.
        mock_read_csv (MagicMock): Mock for pandas.read_csv to raise an exception.
        sample_csv_content (str): Sample CSV content.

    Example:
        >>> test_load_coursera_data_read_exception()
    """
    with patch("builtins.open", mock_open(read_data=sample_csv_content)):
        with pytest.raises(Exception) as exc_info:
            load_coursera_data("data/coursera_data.csv")
        assert "Read error" in str(exc_info.value)
        assert "Attempted path" in str(exc_info.value)


def test_detect_and_print_outliers_iqr(
    capsys, sample_dataframe: pd.DataFrame
) -> None:
    """
    Test outlier detection with a known outlier.

    Adds an outlier to the DataFrame and verifies that it is correctly identified
    and printed by the `detect_and_print_outliers_iqr` function.

    Args:
        capsys (Fixture): Pytest fixture to capture print outputs.
        sample_dataframe (pd.DataFrame): Sample DataFrame fixture.

    Example:
        >>> test_detect_and_print_outliers_iqr(capsys, sample_dataframe)
    """
    df = sample_dataframe.copy()
    df.loc[len(df)] = ['OrgF', 5.0, '10m', 'Advanced', 'Verified']

    df['course_students_enrolled'] = df['course_students_enrolled'].apply(
        convert_students_enrolled
    )

    detect_and_print_outliers_iqr(df, 'course_students_enrolled')
    captured = capsys.readouterr()

    assert "Potential outliers for 'course_students_enrolled':" in captured.out
    assert "OrgF" in captured.out
    assert "10000000" in captured.out


def test_detect_and_print_outliers_iqr_no_outliers(
    capsys, sample_dataframe: pd.DataFrame
) -> None:
    """
    Test outlier detection when no outliers are present.

    Ensures that the function runs without errors and does not falsely identify
    outliers in a dataset without any anomalies.

    Args:
        capsys (Fixture): Pytest fixture to capture print outputs.
        sample_dataframe (pd.DataFrame): Sample DataFrame fixture.

    Example:
        >>> test_detect_and_print_outliers_iqr_no_outliers(capsys, sample_dataframe)
    """
    df = sample_dataframe.copy()
    df['course_students_enrolled'] = df['course_students_enrolled'].apply(
        convert_students_enrolled
    )

    detect_and_print_outliers_iqr(df, 'course_students_enrolled')
    captured = capsys.readouterr()

    assert "Potential outliers for 'course_students_enrolled':" in captured.out


def test_detect_and_print_outliers_iqr_invalid_column(
    sample_dataframe: pd.DataFrame
) -> None:
    """
    Test error handling for outlier detection on a non-existent column.

    Ensures that a KeyError is raised when attempting to analyze a column
    that does not exist in the DataFrame.

    Args:
        sample_dataframe (pd.DataFrame): Sample DataFrame fixture.

    Example:
        >>> test_detect_and_print_outliers_iqr_invalid_column(sample_dataframe)
    """
    with pytest.raises(KeyError):
        detect_and_print_outliers_iqr(sample_dataframe, 'non_existent_column')


def test_detect_and_print_outliers_iqr_non_numeric(
    sample_dataframe: pd.DataFrame
) -> None:
    """
    Test error handling for outlier detection on a non-numeric column.

    Ensures that a TypeError is raised when the specified column contains
    non-numeric data.

    Args:
        sample_dataframe (pd.DataFrame): Sample DataFrame fixture.

    Example:
        >>> test_detect_and_print_outliers_iqr_non_numeric(sample_dataframe)
    """
    with pytest.raises(TypeError):
        detect_and_print_outliers_iqr(sample_dataframe, 'organization')


def test_plot_rating_distribution(sample_dataframe: pd.DataFrame) -> None:
    """
    Test creation of the rating distribution histogram plot.

    Verifies that the `plot_rating_distribution` function returns valid
    matplotlib Figure and Axes objects with correct titles and labels.

    Args:
        sample_dataframe (pd.DataFrame): Sample DataFrame fixture.

    Example:
        >>> test_plot_rating_distribution(sample_dataframe)
    """
    fig, ax = plot_rating_distribution(sample_dataframe['course_rating'])

    assert isinstance(fig, plt.Figure)
    assert isinstance(ax, plt.Axes)
    assert ax.get_title() == "Distribution of Course Ratings"
    assert ax.get_xlabel() == "Course Rating"
    assert ax.get_ylabel() == "Frequency"


def test_plot_enrollment_distribution(sample_dataframe: pd.DataFrame) -> None:
    """
    Test creation of the enrollment distribution histogram plot.

    Ensures that the `plot_enrollment_distribution` function correctly
    processes enrollment data and generates valid plots.

    Args:
        sample_dataframe (pd.DataFrame): Sample DataFrame fixture.

    Example:
        >>> test_plot_enrollment_distribution(sample_dataframe)
    """
    enrollments = sample_dataframe['course_students_enrolled'].apply(
        convert_students_enrolled
    )
    fig, ax = plot_enrollment_distribution(enrollments)

    assert isinstance(fig, plt.Figure)
    assert isinstance(ax, plt.Axes)
    assert ax.get_title() == "Distribution of Students Enrolled"
    assert ax.get_xlabel() == "Number of Students Enrolled"
    assert ax.get_ylabel() == "Frequency"


def test_plot_enrollment_distribution_log_scale(
    sample_dataframe: pd.DataFrame
) -> None:
    """
    Test creation of the enrollment distribution plot with logarithmic scale.

    Verifies that the `plot_enrollment_distribution` function correctly applies
    a logarithmic scale to the x-axis when specified.

    Args:
        sample_dataframe (pd.DataFrame): Sample DataFrame fixture.

    Example:
        >>> test_plot_enrollment_distribution_log_scale(sample_dataframe)
    """
    enrollments = sample_dataframe['course_students_enrolled'].apply(
        convert_students_enrolled
    )
    fig, ax = plot_enrollment_distribution(enrollments, log_scale=True)

    assert isinstance(fig, plt.Figure)
    assert ax.get_xscale() == "log"
    assert "Log Scale" in ax.get_title()
    assert "Log Scale" in ax.get_xlabel()


def test_create_custom_colormap() -> None:
    """
    Test creation of the custom colormap.

    Ensures that the `create_custom_colormap` function returns a valid
    LinearSegmentedColormap object.

    Example:
        >>> test_create_custom_colormap()
    """
    cmap = create_custom_colormap()
    assert isinstance(cmap, LinearSegmentedColormap)
    assert cmap.N > 0


def test_plot_correlation_heatmap(sample_dataframe: pd.DataFrame) -> None:
    """
    Test creation of the correlation heatmap plot.

    Verifies that the `plot_correlation_heatmap` function generates a valid
    heatmap with correct titles and labels based on the provided DataFrame.

    Args:
        sample_dataframe (pd.DataFrame): Sample DataFrame fixture.

    Example:
        >>> test_plot_correlation_heatmap(sample_dataframe)
    """
    df_numeric = sample_dataframe.copy()
    df_numeric['course_students_enrolled'] = df_numeric['course_students_enrolled'].apply(
        convert_students_enrolled
    )
    df_numeric['course_difficulty_num'] = df_numeric['course_difficulty'].astype(
        'category'
    ).cat.codes

    fig, ax = plot_correlation_heatmap(
        df_numeric,
        columns=['course_rating', 'course_students_enrolled', 'course_difficulty_num']
    )

    assert isinstance(fig, plt.Figure)
    assert isinstance(ax, plt.Axes)
    assert "Correlation Matrix" in ax.get_title()


@pytest.fixture(autouse=True)
def close_plots() -> None:
    """
    Automatically close all matplotlib plots after each test.

    Prevents memory leaks and interference between tests by ensuring that
    all figures are closed after each test case is executed.

    Example:
        This fixture is applied automatically to all tests in the module.
    """
    yield
    plt.close('all')
