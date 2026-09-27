import numpy as np

def feature_scaling(data: np.ndarray) -> (np.ndarray, np.ndarray):
	# Your code here
	mean = np.mean(data,axis=0)
	std= np.std(data,axis=0)
	dmin=np.min(data,axis=0)
	dmax= np.max(data, axis=0)

	standardized_data = np.round((data-mean)/std,4)
	normalized_data = np.round((data-dmin)/(dmax-dmin),4)

	return standardized_data, normalized_data