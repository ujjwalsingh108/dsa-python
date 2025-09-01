def permute(nums):
  res = []
  n = len(nums)

  def helper(i):
    # base case
    if i == n-1:
      res.append(nums[:]) # append a copy
      return
    # recursive case
    for j in range(i, n):
      nums[i], nums[j] = nums[j], nums[i] # swap
      helper(i+1)
      nums[i], nums[j] = nums[j], nums[i] #backtrack

  helper(0)
  return res

# Example usage
print(permute([1, 2, 3]))