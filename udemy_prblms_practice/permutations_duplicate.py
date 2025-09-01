def permuteUnique(nums):
  res = []
  def backtrack(index):
    #base case
    if index == len(nums) - 1:
      res.append(nums[:]) #copy
      return
    seen = set()
    for j in range(index, len(nums)):
      if nums[j] in seen:
        continue
      seen.add(nums[j])
      nums[index], nums[j] = nums[j], nums[index]
      backtrack(index+1)
      nums[index], nums[j] = nums[j], nums[index]

  backtrack(0)
  return res

# example usage
print(permuteUnique([1,1,2]))
