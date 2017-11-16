from matplotlib import pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage, fcluster


class AgglomerativeClustering:
    """
    Hierarchical Agglomerative Clustering

    Recursively merges the pair of clusters that minimally increases
    a given linkage distance.

    We are not using sklearn.cluster.AgglomerativeClustering because it requires n_clusters parameter

    For more details of parameters, see documentation of scipy.cluster.hierarchy.linkage and scipy.cluster.hierarchy.linkage.fcluster
    """

    def __init__(self, criterion_threshold, linkage_method="ward", distance_metric="euclidean", criterion="distance"):
        self.criterion_threshold = criterion_threshold
        self.criterion = criterion
        self.distance_metric = distance_metric
        self.linkage_method = linkage_method
        self.linkage_matrix_ = None

    def fit_predict(self, X):
        """Performs clustering on X and returns cluster labels.

        :param X: ndarray, shape (n_samples, n_features) Input data.
        :return ndarray, shape (n_samples,) cluster labels
        """
        # generate the linkage matrix
        self.linkage_matrix_ = linkage(X, self.linkage_method, self.distance_metric)
        return fcluster(self.linkage_matrix_, self.criterion_threshold, criterion=self.criterion)

    @property
    def linkage_matrix(self):
        return self.linkage_matrix_

    def dendrogram(self):
        """Showing dendrogram"""
        plt.title('Hierarchical Agglomerative Clustering Dendrogram')
        plt.xlabel('sample index')
        plt.ylabel('distance')
        dendrogram(self.linkage_matrix)
        plt.axhline(y=self.criterion_threshold, c="k")
        plt.show()

    @staticmethod
    def example():
        import numpy as np
        X = np.array([(3, 5), (3, 4), (5, 7), (3, 5), (6, 4)])
        ac = AgglomerativeClustering(3.5)
        print(ac.fit_predict(X))
        print(ac.linkage_matrix)
        ac.dendrogram()


def group_clustering_result(result, index_names=[]):
    """Grouping result of clustering algorithm"""
    groups = [[] for i in range(max(result) + 1)]
    for index, value in enumerate(result):
        groups[value].append(index)
    if index_names:
        return [[index_names[index] for index in group] for group in groups[1:]]
    return groups[1:]


if __name__ == "__main__":
    AgglomerativeClustering.example()