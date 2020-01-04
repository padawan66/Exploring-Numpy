import numpy as np

#Addition, substraction, Multiplication and Broadcasting
broadcast_array = np.array([1,2])
print("Original ",broadcast_array)
print("Sum ",broadcast_array + broadcast_array)
broadcast_array = np.array([1,2])
print("Substraction  ",broadcast_array - broadcast_array)
broadcast_array = np.array([1,2])
print("Multiplication  ",broadcast_array * broadcast_array)
broadcast_array = np.array([1,2])
print("Broadcasting  ",broadcast_array * 1.5) # Here each cell in the array is multiplied by the constant value


#Aggregation functions
broadcast_array = np.array([1,2])
print("Sum using aggregation function " ,broadcast_array.sum())
print("Min using aggregation function " ,broadcast_array.min())
print("Max using aggregation function " ,broadcast_array.max())
print("Mean using aggregation function " ,broadcast_array.mean())
print("Prod using aggregation function " ,broadcast_array.prod()) # Prod gives the value after multiplying all the elements in the array
print("Standard deviation using aggregation function " ,broadcast_array.std()) # Std gives the standard deviation of the elements in the array
