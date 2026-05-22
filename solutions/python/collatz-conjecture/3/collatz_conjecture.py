"""Modulo to calculate the number of steps in the Collatz Conjecture."""
def steps(number):
    """Return the number of steps to reach 1 given a positive integer."""
    if number < 1:
        raise ValueError("Only positive integers are allowed")
   
    current = number
    count = 0 

    while current != 1:
        if current % 2 == 0:
            current = current // 2 

        else:
            current = (current * 3) + 1
        count = count + 1

    return count 