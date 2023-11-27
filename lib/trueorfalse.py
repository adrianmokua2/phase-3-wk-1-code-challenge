def false_true(a, b, c):
    # Check if each of the input integers is greater than 0 (positive)
    if a > 0:
        result += 1
    if b > 0:
        result += 1
    if c > 0:
        result += 1
        
    # Print whether exactly two of the input numbers are positive
    print(f"Positive numbers count: {result == 2}")
    
    # Return whether exactly two of the input numbers are positive
    return result == 2

# Prompt the user to input values for a, b, and c
a = int(input("Enter the value for a: "))
b = int(input("Enter the value for b: "))
c = int(input("Enter the value for c: "))

# Call the false_true function with the input values and print the result
result = false_true(a, b, c)
print(f"Result: {result}")