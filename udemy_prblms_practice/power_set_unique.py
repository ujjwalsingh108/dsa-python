def power_set(nums):
  res = []
  def helper(i, subset):
    if i == len(nums):
      res.append(subset[:]) # copy current subset
      return

    # choice 1: don't include nums[i]
    helper(i+1, subset)
    # choice 2: include nums[i]
    subset.append(nums[i])
    helper(i+1, subset)
    subset.pop()  # backtrack
  
  helper(0, [])
  return res

print(power_set([1,2,3]))