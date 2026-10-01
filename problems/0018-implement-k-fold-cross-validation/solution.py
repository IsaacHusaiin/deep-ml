import numpy as np
from typing import List, Tuple

def k_fold_cross_validation(n_samples: int, k: int = 5, shuffle: bool = True) -> List[Tuple[List[int], List[int]]]:
    """
    Generate train/test index splits for k-fold cross-validation.
    
    Args:
        n_samples: Total number of samples in the dataset
        k: Number of folds (default 5)
        shuffle: Whether to shuffle indices before splitting (default True)
    
    Returns:
        List of (train_indices, test_indices) tuples
    """

    import numpy as np
from typing import List, Tuple

def k_fold_cross_validation(n_samples: int, k: int = 5, shuffle: bool = True) -> List[Tuple[List[int], List[int]]]:
    indices = np.arange(n_samples)  
    if shuffle:
        np.random.shuffle(indices)

    fold_size = [n_samples//k + (1 if i < n_samples % k else 0) for i in range(k)]
    folds = []                       
    start = 0
    for size in fold_size:           
        folds.append([int(x) for x in indices[start:start+size]])
        start += size

    result = []
    for i in range(k):               
        test = folds[i]
        train = [x for j, fold in enumerate(folds) if j != i for x in fold]
        result.append((train, test))
    return result


    # Your code here


    pass