

import numpy as np

def k_means_clustering(points, k, initial_centroids, max_iterations):
    points = np.array(points, dtype=float)             
    centroids = np.array(initial_centroids, dtype=float)

    for _ in range(max_iterations):
        distances = np.linalg.norm(points[:, np.newaxis] - centroids, axis=2)
        labels = np.argmin(distances, axis=1)           
        new_centroids = np.array([
            points[labels == j].mean(axis=0) if np.any(labels == j) else centroids[j]
            for j in range(k)                           
        ])

        if np.allclose(new_centroids, centroids):
            break                                       
        centroids = new_centroids

    return [tuple(np.round(c, 4).tolist()) for c in centroids]   