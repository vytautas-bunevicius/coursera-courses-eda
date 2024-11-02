"""Utility module for loading Coursera course data.

This module provides functions to load and manage Coursera course data from CSV
files, ensuring compatibility across different operating systems and project
structures.
"""

import os
from pathlib import Path
from typing import List, Optional, Union

from matplotlib.colors import LinearSegmentedColormap
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

BACKGROUND_COLOR = "#EEECE2"
PRIMARY_COLORS = ["#CC7B5C", "#D4A27F", "#EBDBBC", "#9C8AA5"]
PRIMARY_COLOR = "#CC7B5C"
SECONDARY_COLOR = "#D4A27F"
ACCENT_COLOR = "#9C8AA5"
OUTLIER_COLOR = "#9C8AA5"

FIGURE_SIZE = (10, 6)
TITLE_FONT_SIZE = 12
TICK_FONT_SIZE = 12
AXIS_FONT_SIZE = 14
TITLE_PADDING = 15
AXIS_FONT_SIZE = 10
GRID_ALPHA = 0.7
SPINE_WIDTH = 1
DEFAULT_BINS = 20
SWARM_DOT_SIZE = 1
ANNOTATION_DECIMAL_PLACES = 2
GRID_WIDTH = 0.5
ROTATION_ANGLE = 45
BAR_LABEL_PADDING = 10
TOP_N = 10
BAR_WIDTH = 0.5


def load_coursera_data(
    dataset_file_path: Union[str, Path] = Path("data") / "coursera_data.csv",
    encoding: Optional[str] = None,
) -> pd.DataFrame:
    """Loads Coursera data from a CSV file.

    Reads a CSV file containing Coursera data and returns it as a pandas
    DataFrame. Utilizes `pathlib.Path` for cross-platform compatibility.

    Project structure:
        coursera-courses-eda/
        ├── data/
        │   └── coursera_data.csv
        ├── notebooks/
        └── src/
            └── coursera_courses_eda/
                └── utils.py

    Args:
        dataset_file_path: Path to the CSV file. Defaults to
            'data/coursera_data.csv' in the project root. Accepts both string
            and `Path` inputs with forward or backward slashes.
        encoding: The encoding to use for reading the file. If `None`, the
            system default encoding is used.

    Returns:
        A DataFrame containing the loaded Coursera data.

    Raises:
        FileNotFoundError: If the specified file does not exist.
        Exception: Propagates any exception encountered during file reading,
            augmented with additional system information.

    Examples:
        Load data using default path:

            df = load_coursera_data()

        Load data with a specific path:

            df = load_coursera_data("data/coursera_data.csv")

        Load data using Path object:

            df = load_coursera_data(Path("data") / "coursera_data.csv")
    """
    try:
        path = Path(dataset_file_path)
        current_dir = Path.cwd()

        if current_dir.name == "notebooks":
            project_root = current_dir.parent
        else:
            project_root = current_dir

        if not path.is_absolute():
            path = project_root / path

        path = path.resolve()

        if not path.is_file():
            raise FileNotFoundError(
                f"Dataset file not found at: {path}\n"
                f"Current directory: {current_dir}\n"
                f"Project root: {project_root}\n"
                f"Operating system: {os.name}\n"
                "Ensure you're running from the project root or notebooks "
                "directory."
            )

        return pd.read_csv(path, encoding=encoding)

    except Exception as error:
        raise type(error)(
            f"{error}\n"
            f"Operating system: {os.name}\n"
            f"Current directory: {Path.cwd()}\n"
            f"Attempted path: {path}"
        ) from error


def convert_students_enrolled(value: str) -> int:
    """Converts enrollment numbers from string to integer.

    This function takes a string representing enrollment numbers, which may
    contain suffixes 'k' for thousands or 'm' for millions, and converts it
    into an integer.

    Args:
        value: The enrollment number as a string, possibly containing 'k' or 'm'.

    Returns:
        The enrollment number as an integer.

    Examples:
        >>> convert_students_enrolled('1.5k')
        1500
        >>> convert_students_enrolled('2m')
        2000000
        >>> convert_students_enrolled('500')
        500
    """
    if "k" in value:
        return int(float(value.replace("k", "")) * 1_000)
    elif "m" in value:
        return int(float(value.replace("m", "")) * 1_000_000)
    else:
        return int(value)


def plot_rating_distribution(
    data: pd.Series,
    title: str = "Distribution of Course Ratings",
    x_label: str = "Course Rating",
    y_label: str = "Frequency",
    bins: int = DEFAULT_BINS,
    show_kde: bool = True,
    fig_size: tuple[int, int] = FIGURE_SIZE,
) -> tuple[plt.Figure, plt.Axes]:
    """Creates a histogram plot showing the distribution of ratings.

    Args:
        data: Pandas Series containing the rating data to plot.
        title: Title of the plot. Defaults to 'Distribution of Course Ratings'.
        x_label: Label for x-axis. Defaults to 'Course Rating'.
        y_label: Label for y-axis. Defaults to 'Frequency'.
        bins: Number of bins for the histogram. Defaults to 20.
        show_kde: Whether to show the KDE line. Defaults to True.
        fig_size: Tuple of (width, height) for the figure. Defaults to (10, 6).

    Returns:
        A tuple containing the matplotlib Figure and Axes objects.

    Example:
        >>> fig, ax = plot_rating_distribution(df['course_rating'])
        >>> plt.show()
    """
    fig = plt.figure(figsize=fig_size, facecolor=BACKGROUND_COLOR)
    ax = sns.histplot(
        data=data,
        kde=show_kde,
        color=PRIMARY_COLOR,
        bins=bins,
        line_kws={"color": ACCENT_COLOR},
    )
    ax.set_title(title, fontsize=TITLE_FONT_SIZE, pad=TITLE_PADDING)
    ax.set_xlabel(x_label, fontsize=AXIS_FONT_SIZE)
    ax.set_ylabel(y_label, fontsize=AXIS_FONT_SIZE)
    ax.set_facecolor(BACKGROUND_COLOR)
    ax.grid(True, linestyle="--", alpha=GRID_ALPHA, color=SECONDARY_COLOR)
    for spine in ax.spines.values():
        spine.set_color(SECONDARY_COLOR)
        spine.set_linewidth(SPINE_WIDTH)
    ax.tick_params(colors=PRIMARY_COLOR)
    plt.tight_layout()
    return fig, ax


def plot_enrollment_distribution(
    data: pd.Series,
    title: Optional[str] = None,
    x_label: Optional[str] = None,
    y_label: str = "Frequency",
    bins: int = DEFAULT_BINS,
    show_kde: bool = True,
    fig_size: tuple[int, int] = FIGURE_SIZE,
    log_scale: bool = False,
) -> tuple[plt.Figure, plt.Axes]:
    """Creates a histogram plot showing the distribution of student enrollment.

    Args:
        data: Pandas Series containing the enrollment data to plot.
        title: Title of the plot. If None, auto-generated based on log_scale.
        x_label: Label for x-axis. If None, auto-generated based on log_scale.
        y_label: Label for y-axis. Defaults to 'Frequency'.
        bins: Number of bins for the histogram. Defaults to 20.
        show_kde: Whether to show the KDE line. Defaults to True.
        fig_size: Tuple of (width, height) for the figure. Defaults to (10, 6).
        log_scale: Whether to use logarithmic scale. Defaults to False.

    Returns:
        A tuple containing the matplotlib Figure and Axes objects.

    Examples:
        Regular scale:

            fig, ax = plot_enrollment_distribution(df['course_students_enrolled'])
            plt.show()

        Log scale:

            fig, ax = plot_enrollment_distribution(
                df['course_students_enrolled'],
                log_scale=True
            )
            plt.show()
    """
    if title is None:
        title = "Distribution of Students Enrolled"
        if log_scale:
            title += " (Log Scale)"

    if x_label is None:
        x_label = "Number of Students Enrolled"
        if log_scale:
            x_label += " (Log Scale)"

    fig = plt.figure(figsize=fig_size, facecolor=BACKGROUND_COLOR)
    ax = sns.histplot(
        data=data,
        kde=show_kde,
        color=PRIMARY_COLOR,
        bins=bins,
        line_kws={"color": ACCENT_COLOR},
        log_scale=log_scale,
    )
    ax.set_title(title, fontsize=TITLE_FONT_SIZE, pad=TITLE_PADDING)
    ax.set_xlabel(x_label, fontsize=AXIS_FONT_SIZE)
    ax.set_ylabel(y_label, fontsize=AXIS_FONT_SIZE)
    ax.set_facecolor(BACKGROUND_COLOR)
    ax.grid(True, linestyle="--", alpha=GRID_ALPHA, color=SECONDARY_COLOR)
    for spine in ax.spines.values():
        spine.set_color(SECONDARY_COLOR)
        spine.set_linewidth(SPINE_WIDTH)
    ax.tick_params(colors=PRIMARY_COLOR)
    plt.tight_layout()
    return fig, ax


def plot_rating_box_swarm(
    data: Union[pd.Series, pd.DataFrame],
    column: Optional[str] = None,
    title: str = "Distribution of Course Ratings with Outliers Highlighted",
    x_label: str = "Course Rating",
    y_label: str = "",
    fig_size: tuple[int, int] = FIGURE_SIZE,
    box_color: str = SECONDARY_COLOR,
    swarm_color: str = OUTLIER_COLOR,
    show_swarm: bool = True,
) -> tuple[plt.Figure, plt.Axes]:
    """Creates a combined box and swarm plot showing the distribution of course
    ratings.

    Args:
        data: Pandas DataFrame or Series containing the rating data.
        column: Column name if data is DataFrame. Not needed if data is Series.
        title: Title of the plot. Defaults to 'Distribution of Course Ratings
            with Outliers Highlighted'.
        x_label: Label for x-axis. Defaults to 'Course Rating'.
        y_label: Label for y-axis. Defaults to empty string.
        fig_size: Tuple of (width, height) for the figure. Defaults to (12, 6).
        box_color: Color for the box plot. Defaults to SECONDARY_COLOR.
        swarm_color: Color for the swarm plot points. Defaults to OUTLIER_COLOR.
        show_swarm: Whether to show the swarm plot overlay. Defaults to True.

    Returns:
        tuple: (Figure, Axes) containing the matplotlib figure and axes objects.

    Example:
        >>> fig, ax = plot_rating_box_swarm(df, column='course_rating')
        >>> plt.show()

        >>> fig, ax = plot_rating_box_swarm(df['course_rating'])
        >>> plt.show()
    """
    if isinstance(data, pd.Series):
        plot_data = data
    else:
        if column is None:
            raise ValueError("column name must be specified when input is a DataFrame")
        plot_data = data[column]

    fig = plt.figure(figsize=fig_size, facecolor=BACKGROUND_COLOR)

    ax = sns.boxplot(x=plot_data, color=box_color, width=0.5)

    if show_swarm:
        sns.swarmplot(x=plot_data, color=swarm_color, size=SWARM_DOT_SIZE)

    ax.set_title(title, fontsize=TITLE_FONT_SIZE, pad=TITLE_PADDING)
    ax.set_xlabel(x_label, fontsize=AXIS_FONT_SIZE)
    ax.set_ylabel(y_label, fontsize=AXIS_FONT_SIZE)

    ax.set_facecolor(BACKGROUND_COLOR)
    fig.patch.set_facecolor(BACKGROUND_COLOR)

    ax.grid(True, linestyle="--", alpha=GRID_ALPHA, color=SECONDARY_COLOR)

    for spine in ax.spines.values():
        spine.set_color(SECONDARY_COLOR)
        spine.set_linewidth(SPINE_WIDTH)

    ax.tick_params(colors=PRIMARY_COLOR)

    plt.tight_layout()

    return fig, ax


def plot_enrollment_box_swarm(
    data: Union[pd.Series, pd.DataFrame],
    column: Optional[str] = None,
    title: str = "Distribution of Students Enrolled with Outliers Highlighted",
    x_label: str = "Students Enrolled",
    y_label: str = "",
    fig_size: tuple[int, int] = FIGURE_SIZE,
    box_color: str = SECONDARY_COLOR,
    swarm_color: str = OUTLIER_COLOR,
    show_swarm: bool = True,
    log_scale: bool = False,
) -> tuple[plt.Figure, plt.Axes]:
    """Creates a combined box and swarm plot showing the distribution of student
    enrollment.

    Args:
        data: Pandas DataFrame or Series containing the enrollment data.
        column: Column name if data is DataFrame. Not needed if data is Series.
        title: Title of the plot. Defaults to 'Distribution of Students Enrolled
            with Outliers Highlighted'.
        x_label: Label for x-axis. Defaults to 'Students Enrolled'.
        y_label: Label for y-axis. Defaults to empty string.
        fig_size: Tuple of (width, height) for the figure. Defaults to (12, 6).
        box_color: Color for the box plot. Defaults to SECONDARY_COLOR.
        swarm_color: Color for the swarm plot points. Defaults to OUTLIER_COLOR.
        show_swarm: Whether to show the swarm plot overlay. Defaults to True.
        log_scale: Whether to use logarithmic scale for x-axis. Defaults to
            False.

    Returns:
        tuple: (Figure, Axes) containing the matplotlib figure and axes objects.

    Example:
        >>> fig, ax = plot_enrollment_box_swarm(df, column='course_students_enrolled')
        >>> plt.show()

        >>> fig, ax = plot_enrollment_box_swarm(df['course_students_enrolled'],
        ...     log_scale=True)
        >>> plt.show()
    """
    if isinstance(data, pd.Series):
        plot_data = data
    else:
        if column is None:
            raise ValueError("column name must be specified when input is a DataFrame")
        plot_data = data[column]

    fig = plt.figure(figsize=fig_size, facecolor=BACKGROUND_COLOR)

    ax = sns.boxplot(x=plot_data, color=box_color, width=0.5)

    if show_swarm:
        sns.swarmplot(x=plot_data, color=swarm_color, size=SWARM_DOT_SIZE)

    if log_scale:
        ax.set_xscale("log")
        if x_label == "Students Enrolled":
            x_label += " (Log Scale)"
        if not title.endswith("(Log Scale)"):
            title += " (Log Scale)"

    ax.set_title(title, fontsize=TITLE_FONT_SIZE, pad=TITLE_PADDING)
    ax.set_xlabel(x_label, fontsize=AXIS_FONT_SIZE)
    ax.set_ylabel(y_label, fontsize=AXIS_FONT_SIZE)

    ax.set_facecolor(BACKGROUND_COLOR)
    fig.patch.set_facecolor(BACKGROUND_COLOR)

    ax.grid(True, linestyle="--", alpha=GRID_ALPHA, color=SECONDARY_COLOR)

    for spine in ax.spines.values():
        spine.set_color(SECONDARY_COLOR)
        spine.set_linewidth(SPINE_WIDTH)

    ax.tick_params(colors=PRIMARY_COLOR)

    plt.tight_layout()

    return fig, ax


def create_custom_colormap():
    """Creates a custom colormap from PRIMARY_COLORS."""
    return LinearSegmentedColormap.from_list("custom", PRIMARY_COLORS)


def plot_correlation_heatmap(
    data: pd.DataFrame,
    columns: Optional[List[str]] = None,
    title: str = "Correlation Matrix: Course Ratings vs. Students Enrolled",
    x_label: str = "Features",
    y_label: str = "Features",
    fig_size: tuple[int, int] = FIGURE_SIZE,
    show_annotations: bool = True,
) -> tuple[plt.Figure, plt.Axes]:
    """Creates a heatmap visualization of correlation matrix.

    Args:
        data: Pandas DataFrame containing the data.
        columns: List of column names to include in correlation. If None, uses
            all numeric columns.
        title: Title of the plot. Defaults to 'Correlation Matrix: Course
            Ratings vs. Students Enrolled'.
        x_label: Label for x-axis. Defaults to 'Features'.
        y_label: Label for y-axis. Defaults to 'Features'.
        fig_size: Tuple of (width, height) for the figure. Defaults to (12, 6).
        show_annotations: Whether to show correlation values in cells. Defaults
            to True.

    Returns:
        tuple: (Figure, Axes) containing the matplotlib figure and axes objects.

    Example:
        >>> fig, ax = plot_correlation_heatmap(
        ...     df,
        ...     columns=['course_rating', 'course_students_enrolled']
        ... )
        >>> plt.show()
    """
    if columns is not None:
        correlation_matrix = data[columns].corr()
    else:
        correlation_matrix = data.select_dtypes(include=["float64", "int64"]).corr()

    fig = plt.figure(figsize=fig_size, facecolor=BACKGROUND_COLOR)

    custom_cmap = create_custom_colormap()

    ax = sns.heatmap(
        correlation_matrix,
        annot=show_annotations,
        cmap=custom_cmap,
        fmt=f".{ANNOTATION_DECIMAL_PLACES}f",
        linewidths=GRID_WIDTH,
        cbar=True,
    )

    ax.set_title(title, fontsize=TITLE_FONT_SIZE, pad=TITLE_PADDING)
    ax.set_xlabel(x_label, fontsize=AXIS_FONT_SIZE)
    ax.set_ylabel(y_label, fontsize=AXIS_FONT_SIZE)

    ax.tick_params(labelsize=TICK_FONT_SIZE)

    plt.tight_layout()

    return fig, ax


def plot_top_organizations(
    data: Union[pd.Series, pd.DataFrame],
    column: Optional[str] = None,
    title: str = "Top 10 Organizations with the Most Courses",
    x_label: str = "Organizations",
    y_label: str = "Number of Courses",
    fig_size: tuple[int, int] = FIGURE_SIZE,
    bar_color: str = PRIMARY_COLOR,
    top_n: int = TOP_N,
    show_values: bool = True,
) -> tuple[plt.Figure, plt.Axes]:
    """Creates a bar chart showing organizations with the most courses.

    Args:
        data: Pandas Series with organization counts or DataFrame containing the data.
        column: Column name if data is DataFrame. Not needed if data is Series.
        title: Title of the plot. Defaults to 'Top 10 Organizations with the Most Courses'.
        x_label: Label for x-axis. Defaults to 'Organizations'.
        y_label: Label for y-axis. Defaults to 'Number of Courses'.
        fig_size: Tuple of (width, height) for the figure. Defaults to (10, 8).
        bar_color: Color for the bars. Defaults to PRIMARY_COLOR.
        top_n: Number of top organizations to display. Defaults to 10.
        show_values: Whether to show value labels on bars. Defaults to True.

    Returns:
        tuple: (Figure, Axes) containing the matplotlib figure and axes objects.

    Example:
        >>> organization_counts = df['organization'].value_counts()
        >>> fig, ax = plot_top_organizations(organization_counts)
        >>> plt.show()
    """
    if isinstance(data, pd.Series):
        plot_data = data
    else:
        if column is None:
            raise ValueError("column name must be specified when input is a DataFrame")
        plot_data = data[column].value_counts()

    most_courses = plot_data.sort_values(ascending=True).tail(top_n)

    fig = plt.figure(figsize=fig_size, facecolor=BACKGROUND_COLOR)
    ax = most_courses.plot(kind="bar", color=bar_color)

    ax.set_title(title, fontsize=TITLE_FONT_SIZE, pad=TITLE_PADDING)
    ax.set_xlabel(x_label, fontsize=AXIS_FONT_SIZE)
    ax.set_ylabel(y_label, fontsize=AXIS_FONT_SIZE)

    ax.set_facecolor(BACKGROUND_COLOR)
    fig.patch.set_facecolor(BACKGROUND_COLOR)

    plt.xticks(rotation=ROTATION_ANGLE, ha="right")

    if show_values:
        for patch in ax.patches:
            ax.annotate(
                f"{int(patch.get_height())}",
                (patch.get_x() + patch.get_width() / 2.0, patch.get_height()),
                ha="center",
                va="center",
                xytext=(0, BAR_LABEL_PADDING),
                textcoords="offset points",
            )

    for spine in ax.spines.values():
        spine.set_color(SECONDARY_COLOR)

    ax.tick_params(colors=PRIMARY_COLOR)
    ax.grid(True, linestyle="--", alpha=0.7, color=SECONDARY_COLOR)

    plt.tight_layout()

    return fig, ax


def plot_category_distribution(
    data: pd.DataFrame,
    category_column: str,
    title: str,
    x_label: Optional[str] = None,
    y_label: str = "Count",
    fig_size: tuple[int, int] = FIGURE_SIZE,
    bar_color: str = PRIMARY_COLOR,
    bar_width: float = BAR_WIDTH,
    show_values: bool = True,
    rotate_labels: bool = False,
    order: Optional[list] = None,
) -> tuple[plt.Figure, plt.Axes]:
    """Creates a count plot showing the distribution of categories.

    Args:
        data: Pandas DataFrame containing the data.
        category_column: Name of the column containing categories.
        title: Title of the plot.
        x_label: Label for x-axis. If None, uses category_column name.
        y_label: Label for y-axis. Defaults to 'Count'.
        fig_size: Tuple of (width, height) for the figure. Defaults to (12, 6).
        bar_color: Color for the bars. Defaults to PRIMARY_COLOR.
        bar_width: Width of the bars. Defaults to 0.5.
        show_values: Whether to show value labels on bars. Defaults to True.
        rotate_labels: Whether to rotate x-axis labels. Defaults to False.
        order: Specific order for categories. If None, uses default order.

    Returns:
        tuple: (Figure, Axes) containing the matplotlib figure and axes objects.

    Example:
        >>> fig, ax = plot_category_distribution(
        ...     df,
        ...     'course_difficulty',
        ...     'Course Difficulty Level Distribution'
        ... )
        >>> plt.show()
    """
    fig = plt.figure(figsize=fig_size, facecolor=BACKGROUND_COLOR)

    ax = sns.countplot(
        x=category_column, data=data, color=bar_color, width=bar_width, order=order
    )

    ax.set_title(title, fontsize=TITLE_FONT_SIZE, pad=TITLE_PADDING)
    ax.set_xlabel(x_label if x_label else category_column, fontsize=AXIS_FONT_SIZE)
    ax.set_ylabel(y_label, fontsize=AXIS_FONT_SIZE)

    ax.set_facecolor(BACKGROUND_COLOR)
    fig.patch.set_facecolor(BACKGROUND_COLOR)

    if rotate_labels:
        plt.xticks(rotation=ROTATION_ANGLE, ha="right")

    if show_values:
        for patch in ax.patches:
            ax.annotate(
                f"{int(patch.get_height())}",
                (patch.get_x() + patch.get_width() / 2.0, patch.get_height()),
                ha="center",
                va="center",
                xytext=(0, BAR_LABEL_PADDING),
                textcoords="offset points",
            )

    for spine in ax.spines.values():
        spine.set_color(SECONDARY_COLOR)

    ax.tick_params(colors=PRIMARY_COLOR)
    ax.grid(True, linestyle="--", alpha=0.7, color=SECONDARY_COLOR)

    plt.tight_layout()

    return fig, ax


def plot_ratings_by_category(
    data: pd.DataFrame,
    category_column: str,
    rating_column: str = "course_rating",
    title: str = "Course Ratings Across Different Difficulty Levels",
    x_label: Optional[str] = None,
    y_label: str = "Course Rating",
    fig_size: tuple[int, int] = FIGURE_SIZE,
    box_color: str = PRIMARY_COLOR,
    order: Optional[list] = None,
) -> tuple[plt.Figure, plt.Axes]:
    """Creates a box plot showing course ratings distribution across categories.

    Args:
        data: Pandas DataFrame containing the data.
        category_column: Name of the column containing categories (e.g., difficulty levels).
        rating_column: Name of the column containing ratings. Defaults to 'course_rating'.
        title: Title of the plot. Defaults to 'Course Ratings Across Different Difficulty Levels'.
        x_label: Label for x-axis. If None, uses category_column name.
        y_label: Label for y-axis. Defaults to 'Course Rating'.
        fig_size: Tuple of (width, height) for the figure. Defaults to (12, 6).
        box_color: Color for the boxes. Defaults to PRIMARY_COLOR.
        order: Specific order for categories. If None, uses default order.

    Returns:
        tuple: (Figure, Axes) containing the matplotlib figure and axes objects.

    Example:
        >>> difficulty_distribution = df['course_difficulty'].value_counts()
        >>> fig, ax = plot_ratings_by_category(
        ...     df,
        ...     'course_difficulty',
        ...     order=difficulty_distribution.index
        ... )
        >>> plt.show()
    """
    fig = plt.figure(figsize=fig_size, facecolor=BACKGROUND_COLOR)

    ax = sns.boxplot(
        x=category_column, y=rating_column, data=data, color=box_color, order=order
    )

    ax.set_title(title, fontsize=TITLE_FONT_SIZE, pad=TITLE_PADDING)
    ax.set_xlabel(x_label if x_label else category_column, fontsize=AXIS_FONT_SIZE)
    ax.set_ylabel(y_label, fontsize=AXIS_FONT_SIZE)

    ax.set_facecolor(BACKGROUND_COLOR)
    fig.patch.set_facecolor(BACKGROUND_COLOR)

    ax.grid(True, linestyle="--", alpha=GRID_ALPHA, color=SECONDARY_COLOR)

    for spine in ax.spines.values():
        spine.set_color(SECONDARY_COLOR)
        spine.set_linewidth(SPINE_WIDTH)

    ax.tick_params(colors=PRIMARY_COLOR)

    plt.tight_layout()

    return fig, ax


def plot_organization_heatmap(
    data: pd.Series,
    top_n: int = 10,
    title: str = "Top 10 Organizations by Average Enrollments (Heatmap)",
    x_label: str = "Average Enrollment",
    y_label: str = "Organization",
    fig_size: tuple[int, int] = FIGURE_SIZE,
) -> tuple[plt.Figure, plt.Axes]:
    """Creates a heatmap visualization of top organizations by average enrollments.

    Args:
        data: Pandas Series containing organization mean enrollments.
        top_n: Number of top organizations to display. Defaults to 10.
        title: Title of the plot. Defaults to
            'Top 10 Organizations by Average Enrollments (Heatmap)'.
        x_label: Label for x-axis. Defaults to 'Average Enrollment'.
        y_label: Label for y-axis. Defaults to 'Organization'.
        fig_size: Tuple of (width, height) for the figure. Defaults to (12, 6).

    Returns:
        tuple: (Figure, Axes) containing the matplotlib figure and axes objects.

    Example:
        >>> organization_mean_enrollments = df.groupby('organization')['enrollments'].mean()
        >>> fig, ax = plot_organization_heatmap(organization_mean_enrollments)
        >>> plt.show()
    """
    filtered_data = data.nlargest(top_n).to_frame()

    fig = plt.figure(figsize=fig_size, facecolor=BACKGROUND_COLOR)

    custom_cmap = LinearSegmentedColormap.from_list("custom", PRIMARY_COLORS)

    ax = sns.heatmap(filtered_data, cmap=custom_cmap, linewidths=GRID_WIDTH, cbar=True)

    ax.set_title(title, fontsize=TITLE_FONT_SIZE, pad=TITLE_PADDING)
    ax.set_xlabel(x_label, fontsize=AXIS_FONT_SIZE)
    ax.set_ylabel(y_label, fontsize=AXIS_FONT_SIZE)

    plt.tight_layout()

    return fig, ax


def plot_certificate_difficulty_heatmap(
    data: pd.DataFrame,
    certificate_col: str,
    difficulty_col: str,
    title: str = "Relationship between Certificate Types and Difficulty Levels",
    x_label: str = "Course Difficulty",
    y_label: str = "Certificate Type",
    fig_size: tuple[int, int] = FIGURE_SIZE,
    show_annotations: bool = True,
) -> tuple[plt.Figure, plt.Axes]:
    """Creates a heatmap visualization of the relationship between
    certificate types and difficulty levels.

    Args:
        data: Pandas DataFrame containing the course data.
        certificate_col: Name of the column containing certificate types.
        difficulty_col: Name of the column containing difficulty levels.
        title: Title of the plot. Defaults to (
            'Relationship between Certificate Types and Difficulty Levels'
        ).
        x_label: Label for x-axis. Defaults to 'Course Difficulty'.
        y_label: Label for y-axis. Defaults to 'Certificate Type'.
        fig_size: Tuple of (width, height) for the figure. Defaults to (10, 6).
        show_annotations: Whether to show count values in cells. Defaults to True.

    Returns:
        tuple: (Figure, Axes) containing the matplotlib figure and axes objects.

    Example:
        >>> fig, ax = plot_certificate_difficulty_heatmap(
        ...     df,
        ...     'course_certificate_type',
        ...     'course_difficulty'
        ... )
        >>> plt.show()
    """
    cross_table = pd.crosstab(data[certificate_col], data[difficulty_col])

    fig = plt.figure(figsize=fig_size, facecolor=BACKGROUND_COLOR)

    custom_cmap = LinearSegmentedColormap.from_list("custom", PRIMARY_COLORS)

    ax = sns.heatmap(
        cross_table,
        annot=show_annotations,
        fmt="d",
        cmap=custom_cmap,
        linewidths=GRID_WIDTH,
        cbar=True,
    )

    ax.set_title(title, fontsize=TITLE_FONT_SIZE, pad=TITLE_PADDING)
    ax.set_xlabel(x_label, fontsize=AXIS_FONT_SIZE)
    ax.set_ylabel(y_label, fontsize=AXIS_FONT_SIZE)

    plt.tight_layout()

    return fig, ax
