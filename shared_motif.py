def find_longest_common_substring(sequences):
    """
    Finds the longest common substring among a collection of DNA sequences.

    Args:
        sequences (list): A list of DNA sequences.

    Returns:
        str: The longest common substring.
    """
    if not sequences:
        return ""

    substr = ""
    for i in range(len(sequences[0])):
        for j in range(len(sequences[0]) - i + 1):
            if j > len(substr) and all(sequences[0][i:i + j] in x for x in sequences):
                substr = sequences[0][i:i + j]
    return substr


def parse_fasta(fasta_string):
    """
    Parses a FASTA string and returns a list of DNA sequences.

    Args:
        fasta_string (str): The FASTA string containing DNA sequences.

    Returns:
        list: A list of DNA sequences.
    """
    sequences = []
    current_sequence = ""

    for line in fasta_string.split("\n"):
        if line.startswith(">"):
            if current_sequence:
                sequences.append(current_sequence)
                current_sequence = ""
        else:
            current_sequence += line.strip()

    if current_sequence:
        sequences.append(current_sequence)

    return sequences


def main():
    # Prompt user for input method choice
    choice = input("Enter 'F' to read input from a file or 'M' to enter manually: ")

    if choice.upper() == 'F':
        # Read input from file
        filename = input("Enter the input file name: ")
        try:
            with open(filename, 'r') as file:
                fasta_string = file.read()
        except FileNotFoundError:
            print(f"Error: File '{filename}' not found.")
            return
    elif choice.upper() == 'M':
        # Read input from user
        print("Enter the FASTA sequences (press Enter twice to finish):")
        fasta_string = ""
        while True:
            line = input()
            if line == "":
                break
            fasta_string += line + "\n"
    else:
        print("Error: Invalid choice. Please enter 'F' or 'M'.")
        return

    # Parse FASTA string
    sequences = parse_fasta(fasta_string)

    # Find the longest common substring
    longest_common_substring = find_longest_common_substring(sequences)

    # Print the result
    print("Longest Common Substring:")
    print(longest_common_substring)


if __name__ == "__main__":
    main()