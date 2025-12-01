"""
Utility functions for the Recommender Systems Assignment.
Contains helper functions for data loading, processing, and saving.
"""

import pandas as pd
import numpy as np
import os
from typing import Tuple, Dict, Any


def get_project_root() -> str:
    """
    Get the project root directory.
    
    Returns:
        str: Path to the project root directory.
    """
    current_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.dirname(current_dir)


def load_ratings(dataset_path: str = None) -> pd.DataFrame:
    """
    Load the ratings dataset.
    
    Args:
        dataset_path: Path to the dataset directory. If None, uses default.
    
    Returns:
        pd.DataFrame: Ratings dataframe with columns [user_id, book_id, rating].
    """
    if dataset_path is None:
        dataset_path = os.path.join(get_project_root(), 'dataset')
    
    ratings_path = os.path.join(dataset_path, 'ratings.csv')
    return pd.read_csv(ratings_path)


def load_books(dataset_path: str = None) -> pd.DataFrame:
    """
    Load the books dataset.
    
    Args:
        dataset_path: Path to the dataset directory. If None, uses default.
    
    Returns:
        pd.DataFrame: Books dataframe.
    """
    if dataset_path is None:
        dataset_path = os.path.join(get_project_root(), 'dataset')
    
    books_path = os.path.join(dataset_path, 'books.csv')
    return pd.read_csv(books_path)


def save_results(data: Any, filename: str, results_path: str = None) -> str:
    """
    Save results to the results directory.
    
    Args:
        data: Data to save (DataFrame, dict, or array).
        filename: Name of the file (with extension).
        results_path: Path to results directory. If None, uses default.
    
    Returns:
        str: Path to the saved file.
    """
    if results_path is None:
        results_path = os.path.join(get_project_root(), 'results')
    
    os.makedirs(results_path, exist_ok=True)
    filepath = os.path.join(results_path, filename)
    
    if isinstance(data, pd.DataFrame):
        data.to_csv(filepath, index=False)
    elif isinstance(data, dict):
        pd.DataFrame([data]).to_csv(filepath, index=False)
    elif isinstance(data, np.ndarray):
        np.save(filepath.replace('.csv', '.npy'), data)
    else:
        pd.DataFrame(data).to_csv(filepath, index=False)
    
    return filepath


def round_values(value: float, decimals: int = 2) -> float:
    """
    Round value to specified decimal places.
    
    Args:
        value: Value to round.
        decimals: Number of decimal places (default: 2).
    
    Returns:
        float: Rounded value.
    """
    return round(value, decimals)


def compute_sparsity(n_users: int, n_items: int, n_ratings: int) -> float:
    """
    Compute the sparsity of the user-item rating matrix.
    
    Args:
        n_users: Number of users.
        n_items: Number of items.
        n_ratings: Number of ratings.
    
    Returns:
        float: Sparsity percentage (0-100).
    """
    total_possible = n_users * n_items
    sparsity = (1 - (n_ratings / total_possible)) * 100
    return round_values(sparsity)


def get_percentile_group(value: float, max_value: float) -> str:
    """
    Assign a value to a percentile group (G1-G10).
    
    Groups are defined as:
    - G1: ≤1%
    - G2: 1% < x ≤ 5%
    - G3: 5% < x ≤ 10%
    - G4: 10% < x ≤ 20%
    - G5: 20% < x ≤ 30%
    - G6: 30% < x ≤ 40%
    - G7: 40% < x ≤ 50%
    - G8: 50% < x ≤ 60%
    - G9: 60% < x ≤ 70%
    - G10: 70% < x ≤ 100%
    
    Args:
        value: The value to classify.
        max_value: The maximum possible value.
    
    Returns:
        str: Group label (G1-G10).
    """
    percentage = (value / max_value) * 100
    
    if percentage <= 1:
        return 'G1'
    elif percentage <= 5:
        return 'G2'
    elif percentage <= 10:
        return 'G3'
    elif percentage <= 20:
        return 'G4'
    elif percentage <= 30:
        return 'G5'
    elif percentage <= 40:
        return 'G6'
    elif percentage <= 50:
        return 'G7'
    elif percentage <= 60:
        return 'G8'
    elif percentage <= 70:
        return 'G9'
    else:
        return 'G10'

