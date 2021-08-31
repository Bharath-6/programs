
import numpy as np

# Creating array object
arr = np.array( [[ 1, 2, 3],
				[ 4, 2, 5]] )

# Printing type of arr object
print("Array is of type: ", type(arr))

# Printing array dimensions (axes)
print("No. of dimensions: ", arr.ndim)

# Printing shape of array
print("Shape of array: ", arr.shape)

# Printing size (total number of elements) of array
print("Size of array: ", arr.size)

# Printing type of elements in array
print("Array stores elements of type: ", arr.dtype)

#pandas
import pandas as pd
df = pd.DataFrame({'X':[78,85,96,80,86], 'Y':[84,94,89,83,86],'Z':[86,97,96,72,83]});
print(df)

#scipy
import numpy as np
 from scipy import io as sio
 array = np.ones((4, 4))
 sio.savemat('example.mat', {'ar': array}) 
 data = sio.loadmat(‘example.mat', struct_as_record=True)
 data['ar']
 
