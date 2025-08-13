def multiply_numbers(*args):
    """multiply given numbers and return the results"""
    results=1
    for num in args:
        results *=num
    return results
print(multiply_numbers(2,3,4))