# Clustering and labeling of online product reviews

In this paper, we have presented an unsupervised approach to cluster reviews of products collected from Amazon and then generate labels of each cluster. Instead of using a complete review we split a review into sentences and consider all sentences from the reviews as inputs for clustering. We use Hierarchical Agglomerative Clustering to cluster sentences. \\

Our cluster labeling approaches are also unsupervised. For labeling, we have used three different methods to find out a limited number of important words for each cluster. Extracted important words are used to construct phrases. Constructed phrases are used as labels for each cluster. To evaluate our labeling result, we have compared the result of our labeling method with a baseline labeling. In the evaluation, all of our labeling methods outperform the baseline method.