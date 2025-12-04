"""
Utility functions for the Recommender Systems Assignment.
Contains helper functions for data loading, processing, and saving.
"""

import pandas as pd
import numpy as np
import os
from typing import Tuple, Dict, Any, List


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
    Load the Digital Music ratings dataset.
    
    Args:
        dataset_path: Path to the dataset directory. If None, uses default.
    
    Returns:
        pd.DataFrame: Ratings dataframe with columns [item_id, user_id, rating, timestamp].
    """
    if dataset_path is None:
        dataset_path = os.path.join(get_project_root(), 'dataset')
    
    ratings_path = os.path.join(dataset_path, 'Digital_Music.csv')
    return pd.read_csv(
        ratings_path,
        header=None,
        names=['item_id', 'user_id', 'rating', 'timestamp']
    )


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


# ============================================================================
# Manual Calculation Functions (No Built-in Statistical Functions)
# ============================================================================

def manual_mean(values: List[float]) -> float:
    """
    Calculate mean manually using a loop.
    
    Args:
        values: List of numeric values.
    
    Returns:
        float: The mean value.
    """
    total = 0
    count = 0
    for val in values:
        total += val
        count += 1
    return total / count if count > 0 else 0


def manual_median(values: List[float]) -> float:
    """
    Calculate median manually using sorting.
    
    Args:
        values: List of numeric values.
    
    Returns:
        float: The median value.
    """
    sorted_vals = sorted(values)
    n = len(sorted_vals)
    if n == 0:
        return 0
    if n % 2 == 0:
        return (sorted_vals[n//2 - 1] + sorted_vals[n//2]) / 2
    else:
        return sorted_vals[n//2]


def manual_std(values: List[float], mean: float = None) -> float:
    """
    Calculate standard deviation manually.
    
    Args:
        values: List of numeric values.
        mean: Pre-calculated mean (optional).
    
    Returns:
        float: The standard deviation.
    """
    if mean is None:
        mean = manual_mean(values)
    
    variance_sum = 0
    count = 0
    for val in values:
        variance_sum += (val - mean) ** 2
        count += 1
    
    if count == 0:
        return 0
    variance = variance_sum / count
    return variance ** 0.5


def manual_min(values: List[float]) -> float:
    """
    Find minimum value manually using a loop.
    
    Args:
        values: List of numeric values.
    
    Returns:
        float: The minimum value.
    """
    min_val = None
    for val in values:
        if min_val is None or val < min_val:
            min_val = val
    return min_val


def manual_max(values: List[float]) -> float:
    """
    Find maximum value manually using a loop.
    
    Args:
        values: List of numeric values.
    
    Returns:
        float: The maximum value.
    """
    max_val = None
    for val in values:
        if max_val is None or val > max_val:
            max_val = val
    return max_val


def manual_count_unique(values: List) -> int:
    """
    Count unique values manually using a set.
    
    Args:
        values: List of values.
    
    Returns:
        int: Number of unique values.
    """
    unique = set()
    for val in values:
        unique.add(val)
    return len(unique)


def manual_value_counts(values: List) -> Dict:
    """
    Count occurrences of each value manually.
    
    Args:
        values: List of values.
    
    Returns:
        Dict: Dictionary with value counts.
    """
    counts = {}
    for val in values:
        if val in counts:
            counts[val] += 1
        else:
            counts[val] = 1
    return counts
