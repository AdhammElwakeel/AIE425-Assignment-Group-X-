# Recommender Systems Assignment

This project implements Neighborhood-Based Collaborative Filtering and Clustering-Based Collaborative Filtering using the Amazon Electronics dataset.

## Dataset

The Amazon Electronics dataset contains product reviews and ratings from Amazon's Electronics category.

Source: [Amazon Product Reviews](https://jmcauley.ucsd.edu/data/amazon/)

## Project Structure

```
/dataset                                    # Dataset files
/section1_statistical_analysis              # Section 1: Statistical Analysis
/section2_neighborhood_cf                   # Section 2: Neighborhood CF
    /part1_user_based_cf                    # User-based Collaborative Filtering
    /part2_item_based_cf                    # Item-based Collaborative Filtering
/section3_clustering_based_cf               # Section 3: Clustering-based CF
    /part1_user_clustering_avg_ratings      # K-means by avg user ratings
    /part2_user_clustering_common_ratings   # K-means by common ratings
    /part3_item_clustering_avg_raters       # K-means by avg raters
    /part4_cold_start_clustering            # Cold-Start clustering
/utils                                      # Helper functions
/results                                    # Output files and visualizations
```

## Setup

1. Install dependencies:

```bash
pip install -r requirements.txt
```

2. Run notebooks in order:
   - Start with `section1_statistical_analysis/statistical_analysis.ipynb`

## Sections

### Section 1: Statistical Analysis

- Dataset preprocessing and validation
- User and item rating statistics
- Distribution analysis and visualization
- Target user/item selection
- Sparsity and bias analysis

### Section 2: Neighborhood CF

- Part 1: User-based Collaborative Filtering
- Part 2: Item-based Collaborative Filtering

### Section 3: Clustering-based CF

- Part 1: K-means by average user ratings
- Part 2: K-means by common ratings
- Part 3: K-means by average raters
- Part 4: Cold-Start clustering

## Notes

- All values are rounded to 2 decimal places
- Ratings are on a 1-5 scale
- All file paths are relative (no absolute paths)
- Code is compatible with Visual Studio Code
