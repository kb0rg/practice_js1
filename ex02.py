"""
example python code to translate into JS
"""

def fibonacci_set(max):
    """Return list of fibonacci numbers going up to but not beyond max."""
    if max > 1:
        fib_list = [1]
        current_fib = 1
        while current_fib < max:
            fib_list.append(current_fib)
            current_fib = fib_list[-1] + fib_list[-2]
        return fib_list
    else:
        return [1, 1]

def is_even(n):
    """Is number even?"""
    return n % 2 == 0

print sum(filter(is_even, fibonacci_set(4000000)))