import numpy as np

lst = [2,12,30,4,24]
npArr = np.array(lst)
print("Array: ",npArr)
print("Dimension: ",npArr.ndim)

print("Sum of elements: ",np.sum(npArr))
print("Sum : ",npArr.sum())

print("Maximum Element: ",np.max(npArr))
print("Max: ",npArr.max())

print("Minimum Element: ",np.min(npArr))
print("Min: ",npArr.min())

print("Average of elements: ",np.mean(npArr))
print("Average: ",npArr.mean())

print("Indexing the elements: ",npArr[0],npArr[-1])
print("Slicing of Array: ",npArr[0:3])
