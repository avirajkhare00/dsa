# Find the contiguous subarray with the largest sum.
# can be solved using Kadane's Algorithm

def max_subarray_sum(arr):
  res = arr[0]
  max_ending = arr[0]
  for i in range(1, len(arr)):
    max_ending = max(max_ending + arr[i], arr[i])
    res = max(res, max_ending)
  return res

print(max_subarray_sum([1,2,-5,-4]))
print(max_subarray_sum([1,2,3,4,5]))
