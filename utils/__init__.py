"""
Utils Package for Recommender Systems Assignment.

This package provides utility functions for:
- Data loading and path management
- Statistical calculations (manual implementations)
- Result saving and file operations
- Percentile grouping

All functions use relative paths for portability.
"""

from .helpers import (
    # Path management
    get_project_root,
    
    # Data loading
    load_ratings,
    
    # Result saving
    save_results,
    
    # Utility functions
    round_values,
    compute_sparsity,
    get_percentile_group,
    
    # Manual statistical functions (no built-in functions used)
    manual_mean,
    manual_median,
    manual_std,
    manual_min,
    manual_max,
    manual_count_unique,
    manual_value_counts
)

__all__ = [
    'get_project_root',
    'load_ratings',
    'save_results',
    'round_values',
    'compute_sparsity',
    'get_percentile_group',
    'manual_mean',
    'manual_median',
    'manual_std',
    'manual_min',
    'manual_max',
    'manual_count_unique',
    'manual_value_counts'
]
