def power_set_duplicate(nums):
  res = []
  nums.sort()
  def helper(i, subset):
    if i == len(nums):
      res.append(subset[:])
      return
    subset.append(nums[i])
    helper(i+1, subset)
    subset.pop()
    while i < len(nums) - 1 and nums[i] == nums[i+1]:
      i += 1
    helper(i+1, subset)
  helper(0, [])
  return res

print(power_set_duplicate([1,3,3,3,7]))