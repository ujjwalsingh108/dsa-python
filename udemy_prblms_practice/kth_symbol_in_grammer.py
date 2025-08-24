def kthGrammar(n, k):
  if n == 1:
    return 0
  else:
    length = 2 ** (n - 1)
    mid = length // 2
    if k <= mid:
      return kthGrammar(n - 1, k)
    else: 
      return 1 - kthGrammar(n - 1, k - mid)
    
if __name__ == "__main__":
  # Sample input
  n = int(input("Enter value of n: "))
  k = int(input("Enter value of k: "))
  result = kthGrammar(n,k)
  print(f"The {k}th symbol in the {n}th row is: {result}")
