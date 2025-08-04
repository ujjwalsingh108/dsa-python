def sum_of_natural_numbers(n):
  return n * (n + 1) // 2;

if __name__ == "__main__":
  n = int(input("Enter a number(n): "))
  total = sum_of_natural_numbers(n)
  print(f"Sum of first {n} natural numbers is: {total}")
  