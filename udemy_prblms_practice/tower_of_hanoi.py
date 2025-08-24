def tower_of_hanoi(n, source, target, auxillary):
  if n == 1:
    print(f"Move disk 1 from {source} to {target}")
    return
  
  #Step 1: Move N-1 disk from source to auxillary
  tower_of_hanoi(n-1, source, auxillary, target)

  #Step 2: Move the Nth disk from source to target
  print(f"Move disk {n} from {source} to {target}")

  #Step 3: Move the N-1 disk from auxillary to target
  tower_of_hanoi(n-1, auxillary, target, source)


#Example usage

n = 3 # Number of disks

tower_of_hanoi(n, 'A', 'B', 'C')


