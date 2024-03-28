def calculate_gc_content(sequence):
    """
    Calculates the GC-content percentage of a given DNA sequence.

    Args:
        sequence (str): The DNA sequence.

    Returns:
        float: The GC-content percentage.
    """
    gc_count = sequence.count('G') + sequence.count('C')
    return (gc_count / len(sequence)) * 100

def main():
    """
    Main function to read the FASTA format input, find the string with the highest GC-content,
    and output the result.
    """
    fasta_strings = []
    current_id = ''
    current_sequence = ''

    # Prompt the user to enter FASTA data
    print("Enter FASTA data (press Enter twice to finish):")

    # Read the input
    while True:
        line = input().strip()
        if line == '':
            if current_id != '':
                fasta_strings.append((current_id, current_sequence))
            break
        elif line.startswith('>'):
            if current_id != '':
                fasta_strings.append((current_id, current_sequence))
            current_id = line[1:]
            current_sequence = ''
        else:
            current_sequence += line

    # Find the string with the highest GC-content
    highest_gc_id = ''
    highest_gc_content = 0

    for fasta_id, sequence in fasta_strings:
        gc_content = calculate_gc_content(sequence)
        if gc_content > highest_gc_content:
            highest_gc_id = fasta_id
            highest_gc_content = gc_content

    # Output the result
    print("\nResult:")
    print(highest_gc_id)
    print(f'{highest_gc_content:.6f}')

if __name__ == '__main__':
    main()
