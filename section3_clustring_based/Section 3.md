# Part 3: Clustering-based Collaborative Filters Requirements

### 3.3 Section THREE: Clustering-based Collaborative Filters requirements

#### 3.3.1 Part 1: K-means Clustering based on average number of user ratings

In this part, you will apply K-means clustering to group users based on their average rating behavior. Users with similar rating patterns will be clustered together, reducing the search space for finding similar users during the collaborative filtering process. This approach can significantly improve computational efficiency while maintaining recommendation quality.

**Tasks and questions**

1. Use the calculated average rating given by each user (r̄\_u) from Section ONE.
2. Create a 1-dimensional feature vector for each user where the feature is their average rating value.
3. Calculate the mean of the users’ average ratings, μ = Σr̄\_u / N
4. Compute the Standard deviation of the users’ average ratings, σ = √\[Σ(r̄\_u - μ)² / N]
5. Normalize the feature values for each user using standardization (Z-score normalization) to ensure proper clustering, z\_u = (r̄\_u - μ) / σ
6. Apply K-means clustering with different values of K (e.g., K = 5, 10, 15, 20, 30, 50):  
   6.1. For each K value, calculate and save the cluster centroids and perform K-means clustering on the user feature vectors.  
   6.2. Record the cluster assignments for all users.
7. Analyze the clustering results for each K value:  
   7.1. Calculate the number of users in each cluster.  
   7.2. Compute the within-cluster sum of squares (WCSS) for each K.  
   7.3. Plot the elbow curve (WCSS vs K) to determine the optimal K value.  
   7.4. Calculate the silhouette score for each K value to assess clustering quality.
8. For the optimal K value (based on elbow method and silhouette score):  
   8.1. Display the distribution of users across clusters (create a bar chart).  
   8.2. Show the average rating value for each cluster centroid.  
   8.3. Identify which clusters contain generous raters (high average) and which contain strict raters (low average).
9. Apply user-based collaborative filtering within each cluster:  
   9.1. For each target user from Section ONE (U1, U2, U3), identify which cluster they belong to.  
   9.2. Within the assigned cluster, compute user–user similarity using mean-centered Cosine similarity.  
   9.3. Select the top 20% most similar users from within the same cluster.  
   9.4. Predict ratings for the target items (I1 and I2) using only the similar users from the same cluster.
10. Compare clustering-based predictions with non-clustering predictions from Section TWO:  
    10.1. For each target user, compare the predicted ratings with and without clustering.  
    10.2. Calculate the difference in prediction values.  
    10.3. Discuss whether clustering improved, maintained, or degraded prediction accuracy.
11. Analyze the computational efficiency gains:  
    11.1. Calculate the number of similarity computations needed without clustering (comparing all user pairs).  
    11.2. Calculate the number of similarity computations needed with clustering (only within-cluster pairs).  
    11.3. Compute the speedup factor: (computations without clustering) / (computations with clustering).  
    11.4. Express the efficiency gain as a percentage reduction in computations.
12. Evaluate the impact of cluster imbalance:  
    12.1. Identify if any clusters are significantly larger or smaller than others.  
    12.2. Discuss how cluster imbalance affects computational efficiency.  
    12.3. Propose strategies to handle imbalanced clusters.
13. Test the robustness of the clustering approach:  
    13.1. Re-run K-means with different random initializations (at least 3 times).  
    13.2. Compare the cluster assignments across different runs.  
    13.3. Discuss whether the clustering is stable or varies significantly with initialization.
14. Include the results of all the above points in your report and give your insights and comments in a separate section on:  
    14.1. The effectiveness of clustering based on average user ratings.  
    14.2. The trade-off between prediction accuracy and computational efficiency.  
    14.3. Whether this clustering strategy is suitable for your dataset characteristics.  
    14.4. How the choice of K affects both accuracy and efficiency.

#### 3.3.2 Part 2: K-means Clustering based on average number of common ratings

In this part, you will cluster users based on the number of common items they have rated with other users. This approach aims to group users who have overlapping rating histories, which can lead to more reliable similarity computations since the similarities will be based on a sufficient number of co-rated items. This addresses the significance weighting concept discussed in Section TWO.

**Tasks and questions**

1. Compute the co-rating statistics for each user:  
   1.1. For each user, calculate the average number of common items they have with other users.  
   1.2. For each user, calculate the maximum number of common items they have with any other user.  
   1.3. For each user, calculate the minimum number of common items they have with any other user (excluding zero).  
   1.4. Create a feature vector for each user: \[average\_common, max\_common, min\_common].
2. Normalize the feature vectors:  
   2.1. Apply Z-score standardization to each feature dimension separately:  
   2.1.1. For each feature, calculate its mean (μ) and standard deviation (σ) across all users.  
   2.1.2. Normalize each feature dimension independently using: z\_{u,f} = (x\_{u,f} - μ\_f) / σ\_f  
   • x\_{u,f} = value of feature f for user u  
   • μ\_f = mean of feature f across all users  
   • σ\_f = standard deviation of feature f across all users  
   This normalization ensures all features contribute equally to the clustering by scaling them to comparable ranges (mean = 0, standard deviation = 1), preventing features with larger numerical scales from dominating the distance calculations.
3. Apply K-means clustering with different K values (K = 5, 10, 15, 20, 30, 50):  
   3.1. Perform K-means clustering on the normalized feature vectors.  
   3.2. Record cluster assignments and centroids for each K.  
   3.3. Calculate WCSS and silhouette scores for each K.
4. Determine the optimal K value:  
   4.1. Plot the elbow curve (WCSS vs. K).  
   4.2. Plot silhouette scores vs. K.  
   4.3. Select the optimal K based on both metrics.
5. Analyze the characteristics of each cluster (using optimal K):  
   5.1. Calculate the average co-rating statistics for users in each cluster.  
   5.2. Identify ‘high overlap’ clusters (users who share many common ratings with others).  
   5.3. Identify ‘low overlap’ clusters (users with few common ratings with others).  
   5.4. Visualize the cluster distribution using a 2D or 3D scatter plot.
6. Apply collaborative filtering within clusters:  
   6.1. For each target user (U1, U2, U3), identify their cluster assignment.  
   6.2. Within each cluster, compute user–user similarity using mean-centered Cosine similarity.  
   6.3. Calculate the Discount Factor (DF) based on the number of common ratings (using threshold β from Section ONE) \& Compute Discounted Similarity (DS).  
   6.4. Select the top 20% most similar users based on DS within the cluster.  
   6.5. Predict ratings for target items (I1 and I2) using the selected similar users.
7. Compare this clustering approach with Part 1:  
   7.1. Compare the predicted ratings from Part 2 with those from Part 1.  
   7.2. Which clustering strategy produces more accurate predictions?  
   7.3. Which strategy results in better computational efficiency?  
   7.4. Compare the cluster memberships between the two approaches:  
   7.4.1. Do the same users end up in the same clusters?  
   7.4.2. How do the characteristics of users within each cluster differ between Part 1 and Part 2?  
   7.4.3. Which approach produces more cohesive/meaningful user groups?
8. Evaluate the relationship between common ratings and prediction quality:  
   8.1. For each target user, calculate the average number of common ratings with their top similar users.  
   8.2. Calculate the prediction error for each target user: |actual\_rating – predicted\_rating|.  
   8.3. Is there a correlation between the number of common ratings and prediction accuracy?
9. Analyze the impact on significance weighting:  
   9.1. Compare the distribution of DF values within each cluster.  
   9.2. Do users in the same cluster tend to have similar DF values?  
   9.3. How does clustering affect the effectiveness of significance weighting?
10. Examine extreme cases and challenges:  
    10.1. Identify users who have very few common ratings with anyone in their cluster.  
    10.2. How should these users be handled?  
    10.3. Discuss the cold-start problem within this clustering approach.
11. Include the results of all the above points in your report and give your insights and comments in a separate section on:  
    11.1. The effectiveness of clustering based on common rating patterns.  
    11.2. How this approach addresses the significance weighting problem from Section TWO.  
    11.3. The advantages and disadvantages compared to average-rating-based clustering (Part 1).  
    11.4. Recommendations for when to use this clustering strategy.

#### 3.3.3 Part 3: K-means Clustering based on average number of raters

In this part, you will cluster items (rather than users) based on how many users have rated each item. This item-based clustering approach addresses the long-tail problem identified in Section ONE, where some items have many ratings while others have very few. By clustering items with similar rating frequencies, you can improve the reliability of item-based collaborative filtering.

**Tasks and questions**

1. Compute item statistics:  
   1.1. For each item, use the total number of raters and the average rating it received from Section ONE.  
   1.2. For each item, calculate the standard deviation of its ratings.  
   1.3. Create a feature vector for each item: \[num\_raters, avg\_rating, std\_rating].
2. Normalize the feature vectors:  
   2.1. Apply Z-score standardization independently to each feature dimension:  
   2.1.1. For each feature, calculate its mean (μ) and standard deviation (σ) across all items.  
   2.1.2. Normalize each feature dimension independently using: z\_{i,f} = (x\_{i,f} - μ\_f) / σ\_f  
   2.2. Verify that all features are now on the same scale (mean = 0, standard deviation = 1), ensuring equal contribution to the clustering process.
3. Apply K-means clustering on item feature vectors (K = 5, 10, 15, 20, 30, 50):  
   3.1. Perform K-means clustering on the normalized item feature vectors.  
   3.2. Record cluster assignments for all items.  
   3.3. Calculate WCSS and silhouette scores for each K.
4. Determine the optimal K value:  
   4.1. Plot the elbow curve and silhouette scores.  
   4.2. Select the optimal K value.
5. Analyze the characteristics of each item cluster (using optimal K):  
   5.1. Calculate the average number of raters for items in each cluster.  
   5.2. Identify ‘popular item’ clusters (high number of raters).  
   5.3. Identify ‘niche item’ clusters (low number of raters).  
   5.4. Identify ‘long-tail item’ clusters (very few raters).  
   5.5. Visualize the distribution of items across clusters.
6. Analyze the relationship between cluster membership and item popularity:  
   6.1. Plot the distribution of number of raters within each cluster.  
   6.2. Are items with similar popularity levels grouped together?  
   6.3. Analyze how items from different parts of the popularity distribution (head vs. tail from Section ONE) are distributed across the clusters. Are popular and unpopular items separated into different clusters, or mixed within clusters?
7. Apply item-based collaborative filtering within clusters:  
   7.1. For each target item (I1 and I2 from Section ONE), identify their cluster assignment.  
   7.2. Within each cluster, compute item–item similarity using Adjusted Cosine similarity.  
   7.3. Select the top 20% most similar items from within the same cluster.  
   7.4. For each target user (U1, U2, U3), predict their rating for the target items using only similar items from the same cluster.
8. Compare clustering-based item CF with non-clustering item CF from Section TWO:  
   8.1. Compare the predicted ratings with and without clustering.  
   8.2. Calculate the prediction error for each approach: |actual\_rating – predicted\_rating|.  
   8.3. Which approach produces more reliable predictions?
9. Evaluate the impact on the long-tail problem:  
   9.1. How does clustering affect predictions for items with very few ratings (long-tail items)?  
   9.2. Are predictions for long-tail items more or less reliable within their clusters?  
   9.3. Compare the number of similar items found for long-tail items with and without clustering.
10. Analyze computational efficiency:  
    10.1. Calculate the reduction in item–item similarity computations due to clustering.  
    10.2. Compute the speedup factor compared to non-clustering item-based CF.  
    10.3. Is the speedup greater for item-based or user-based clustering?
11. Examine the effect of cluster size on prediction quality:  
    11.1. For clusters of different sizes, calculate the average prediction error.  
    11.2. Do larger clusters produce better or worse predictions?  
    11.3. Is there an optimal cluster size for balancing accuracy and efficiency?
12. Compare user-based clustering (Parts 1 \& 2) with item-based clustering (Part 3):  
    12.1. Which clustering approach (user or item) is more effective for your dataset?  
    12.2. When would you recommend user-based clustering vs. item-based clustering?  
    12.3. Can both clustering strategies be combined? Discuss the feasibility and benefits.
13. Include the results of all the above points in your report and give your insights and comments in a separate section on:  
    13.1. The effectiveness of item-based clustering for addressing the long-tail problem.  
    13.2. The relationship between item popularity and clustering quality.  
    13.3. Comparison between user-based and item-based clustering strategies.  
    13.4. Recommendations for practical deployment of item-based clustering.

#### 3.3.4 Part 4: K-means Clustering for Cold-Start

In this part, you will develop a clustering-based approach to handle the cold-start problem: the challenge of making recommendations for new users who have provided only a few ratings, or recommending new items with limited data.

**Tasks and questions**

1. Simulate cold-start scenarios:  
   1.1. From your dataset, randomly select 100 users with more than 50 ratings each.  
   1.2. For each selected user, hide 90% of their ratings to simulate a cold-start user with only 10–20 ratings.  
   1.3. Store the hidden ratings as ground truth for evaluation.  
   1.4. Similarly, select 50 items with many ratings and hide most ratings to simulate cold-start items.
2. Develop a cold-start user assignment strategy:  
   2.1. For each cold-start user, calculate their limited profile features (e.g., average rating from their few ratings).  
   2.2. Compute the distance between the cold-start user’s feature vector and each cluster centroid from Part 1.  
   2.3. Assign the cold-start user to the nearest cluster.  
   2.4. Record the confidence of the assignment (e.g., distance to nearest centroid vs. distance to second-nearest centroid).
3. Generate recommendations for cold-start users:  
   3.1. Within the assigned cluster, find the most similar users based on the limited ratings.  
   3.2. Use these similar users to predict ratings for items the cold-start user hasn’t rated.  
   3.3. Generate top-10 item recommendations for each cold-start user.
4. Evaluate cold-start user recommendations:  
   4.1. Compare the predicted ratings with the hidden ground truth ratings.  
   4.2. Calculate the Mean Absolute Error (MAE) and Root Mean Squared Error (RMSE).  
   4.3. Compute precision@10 and recall@10 for the top-10 recommendations.  
   Precision@10 = number of relevant items in top 10 / 10  
   Recall@10 = number of relevant items in top 10 / total number of relevant items  
   4.4. Compare the accuracy with and without clustering for cold-start users.
5. Develop a cold-start item assignment strategy:  
   5.1. For each cold-start item, calculate its limited profile (e.g., average rating, number of raters).  
   5.2. Assign the item to the nearest item cluster from Part 3.  
   5.3. Calculate the confidence of each cold-start item assignment using the following steps:  
   5.3.1. Compute the Euclidean distance from the cold-start item to its assigned (nearest) cluster centroid: d\_nearest  
   5.3.2. Compute the Euclidean distance from the cold-start item to the second-nearest cluster centroid: d\_second  
   5.3.3. For each cold-start item, calculate the assignment confidence using:  
   Confidence = (d\_second − d\_nearest) / d\_second  
   Where:  
   • Values close to 1.0 indicate high confidence (the item clearly belongs to the assigned cluster)  
   • Values close to 0.0 indicate low confidence (the item is nearly equidistant between clusters)  
   5.3.4. Present your results in a table showing: cold-start item ID, assigned cluster, d\_nearest, d\_second, and confidence score.
6. Generate recommendations involving cold-start items:  
   6.1. For users who might be interested in the cold-start item, predict their ratings.  
   6.2. Use similar items within the same cluster to make predictions.  
   6.3. Identify which users would most likely rate the cold-start item highly.
7. Evaluate cold-start item predictions:  
   7.1. Compare predicted ratings with hidden ground truth.  
   7.2. Calculate MAE and RMSE for cold-start item predictions.  
   7.3. Compare accuracy with and without clustering.
8. Analyze the relationship between the number of ratings and prediction accuracy:  
   8.1. For cold-start users with 5, 10, 15, and 20 ratings, measure prediction accuracy.  
   8.2. Plot accuracy vs. number of available ratings.  
   8.3. At what point does a user transition from ‘cold-start’ to having sufficient data?
9. Develop a hybrid cold-start strategy:  
   9.1. Combine clustering-based CF with content-based features (if available).  
   9.2. Use demographic information or item attributes to improve cold-start cluster assignment.  
   9.3. Evaluate whether the hybrid approach improves prediction accuracy.
10. Test the robustness of cold-start handling:  
    10.1. Vary the amount of information available for cold-start users (e.g., 3, 5, 10, 20 ratings).  
    10.2. Measure how prediction quality degrades as less information is available.  
    10.3. Identify the minimum number of ratings needed for acceptable prediction quality.
11. Analyze cluster assignment confidence:  
    11.1. For cold-start users/items, calculate the confidence of cluster assignments:  
    Confidence = (d\_second − d\_nearest) / d\_second  
    Where d\_nearest is the distance to the assigned cluster and d\_second is distance to the second-nearest cluster.  
    Lower ratios (<0.5) indicate confident assignments; higher ratios (>0.7) indicate ambiguous assignments.  
    11.2. Identify cases where cluster assignment is ambiguous (similar distances to multiple clusters).  
    11.3. Propose strategies for handling ambiguous cases (e.g., multi-cluster membership, weighted recommendations).

Include the results of all the above points in your report and give your insights and comments in a separate section on cold-start clustering strategies and their effectiveness.

