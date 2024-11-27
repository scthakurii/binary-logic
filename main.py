def generate_sequence(n):
    """
    Generate the sequence where letters repeat in the specific pattern, 
    with compact notation for large numbers.
    """
    if n <= 0:
        return ""
    
    # Full sequence generator
    sequence = []
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    
    # Build the sequence iteratively
    for i in range(n):
        sequence.append(alphabet[i % len(alphabet)])
        sequence.extend(sequence[:-1])  # Append the pattern
    
    # Convert to string
    full_sequence = ''.join(sequence[:n])

    # Compact representation for large n
    if n > 64:
        compact_form = f"{full_sequence[:8]}...{full_sequence[-8:]} ({n})"
        return compact_form
    else:
        return full_sequence


# Example Usage
num = int(input("Enter the position (n): "))
result = generate_sequence(num)
print(result)
