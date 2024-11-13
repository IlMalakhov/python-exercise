def is_power(a, b):
    """
    Checks if a is a power of b.
    """
    # Define when to stop
    if a == 1:
        return True
    # In this case we know that a cannot be a power of b
    if a < b or a % b !=0:
        return False
    
    # Recursively call to this function
    return is_power(a // b, b)

# Test
print(is_power(16, 2))
print(is_power(12,2))