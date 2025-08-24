def findTheWinner(n, k):
  arr = list(range(1, n + 1))

  def helper(arr, startIndex):
    #base case
    if len(arr) == 1:
      return arr[0]
    
    #calculate the index to remove
    indexToRemove = (startIndex + k - 1) % len(arr)
    arr.pop(indexToRemove)

    #recursive call with updated list and new start index

    return helper(arr, indexToRemove)
  
  return helper(arr, 0)


if __name__ == "__main__":
  # Sample input
  n = int(input("Enter the value of n: "))
  k = int(input("Enter the value of k: "))
  result = findTheWinner(n,k)
  print(f"The winner of the game is the person sitting on chair: {result}")

