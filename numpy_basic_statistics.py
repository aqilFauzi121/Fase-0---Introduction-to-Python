# Data Analysis: 
# - Get to know your data
# Little data -> simply look at it
# Big data -> use Python to analyze it

# Generate Data

# Arguments for np.random.normal()
# - distribution mean
# - distribution standard deviation
# - number of samples

import numpy as np

height = np.round(np.random.normal(1.75, 0.20, 5000), 2)
weight = np.round(np.random.normal(60.32, 15, 5000), 2)
np_city = np.column_stack((height, weight))
print(np_city)