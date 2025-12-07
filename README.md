# Recommender Systems Assignment

**Course:** AIE425 - Recommender Systems

---

This project implements Neighborhood-Based Collaborative Filtering and Clustering-Based Collaborative Filtering using the Amazon Digital Music dataset.

## Dataset

The Amazon Digital Music dataset contains product reviews and ratings.

Source: [Amazon Product Reviews](https://jmcauley.ucsd.edu/data/amazon/](https://jmcauley.ucsd.edu/data/amazon_v2/categoryFilesSmall/Digital_Music.csv))

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

## How to Run

1. Open the project folder in Visual Studio Code
2. Ensure Python environment is set up with required packages ver 3.13
3. Navigate to each section folder and run the Jupyter notebooks
4. Results are saved in the `/results` directory
