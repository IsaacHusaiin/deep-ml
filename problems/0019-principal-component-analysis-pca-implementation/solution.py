import numpy as np

def pca(data: np.ndarray, k: int) -> np.ndarray:
    """
    Perform PCA and return the top k principal components.
    
    Args:
        data: Input array of shape (n_samples, n_features)
        k: Number of principal components to return
    
    Returns:
        Principal components of shape (n_features, k), rounded to 4 decimals.
        Each eigenvector's sign is fixed so its first non-zero element is positive.
    """
    # Your code here
    std_data = (data - data.mean(axis =0))/ data.std (axis=0)
    cov = np.cov(std_data, rowvar=False)
    eigenvalues, eigenvectors = np.linalg.eigh(cov)
    eigenvalues = eigenvalues[::-1]
    eigenvectors = eigenvectors[:, ::-1]
    components = eigenvectors[:, :k].copy()  

    for j in range(components.shape[1]):                       
        col = components[:, j]
        nonzero = np.nonzero(np.abs(col) > 1e-10)[0]          
        if nonzero.size > 0 and col[nonzero[0]] < 0:           
            components[:, j] = -col                            
    return np.round(components, 4)


    
