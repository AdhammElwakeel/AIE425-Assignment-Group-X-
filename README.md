# Recommender Systems Assignment

**Course:** AIE425 - Recommender Systems

---

This project implements Neighborhood-Based Collaborative Filtering and Clustering-Based Collaborative Filtering using the Amazon Digital Music dataset.

## Dataset

The Amazon Digital Music dataset contains product reviews and ratings.

Source: [Amazon Product Reviews](https://jmcauley.ucsd.edu/data/amazon/)

### Dataset Validation Results

**Metric: Number of Users**

- Value: 840,372
- Requirement: ≥ 100,000

**Metric: Number of Items**

- Value: 456,992
- Requirement: ≥ 1,000

**Metric: Number of Ratings**

- Value: 1,584,082
- Requirement: ≥ 1,000,000

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
- User and item rating statistics (calculated manually with loops)
- Distribution analysis and visualization
- Target user/item selection
- Sparsity and bias analysis

### Section 2: Neighborhood CF

- **Part 1:** User-based Collaborative Filtering
- **Part 2:** Item-based Collaborative Filtering
  - Case Study 1: Cosine similarity with mean-centering
  - Case Study 3: Pearson Correlation Coefficient (PCC)

### Section 3: Clustering-based CF

- Part 1: K-means by average user ratings
- Part 2: K-means by common ratings
- Part 3: K-means by average raters
- Part 4: Cold-Start clustering

## How to Run

1. Open the project folder in Visual Studio Code
2. Ensure Python environment is set up with required packages ver 3.13
3. Navigate to each section folder and run the Jupyter notebooks
4. Results are saved in the `/results` directory
