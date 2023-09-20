#!/usr/bin/env python3
"""
Defines function that performs K-means on a dataset
"""


import numpy as np

def kmeans(X, k, iterations=1000):
    """function performs K-means on a dataset"""
    n, d = X.shape
    
    # Initialize cluster centroids using a multivariate uniform distribution
    np.random.seed(0)
    C = np.random.uniform(np.min(X, axis=0), np.max(X, axis=0), size=(k, d))
    
    for _ in range(iterations):
        # Assign each data point to the nearest cluster
        distances = np.linalg.norm(X[:, np.newaxis] - C, axis=2)
        clss = np.argmin(distances, axis=1)
        
        # Update cluster centroids
        new_C = np.empty_like(C)
        for i in range(k):
            if np.sum(clss == i) == 0:
                # Reinitialize the centroid if no data points belong to the cluster
                new_C[i] = np.random.uniform(np.min(X, axis=0), np.max(X, axis=0))
            else:
                new_C[i] = np.mean(X[clss == i], axis=0)
        
        # Check for convergence
        if np.array_equal(C, new_C):
            return C, clss
        
        C = new_C
    
    return None, None
