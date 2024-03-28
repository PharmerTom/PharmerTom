"""
MRNA - Inferring mRNA from Protein

Given a protein string, this program calculates the total number of
different RNA strings from which the protein could have been translated,
modulo 1,000,000. It takes into account the stop codon.

Input:
- A protein string of length at most 1000 aa.

Output:
- The number of possible RNA strings, modulo 1,000,000.

Usage:
- Run the script and enter the protein string when prompted.
"""


def num_rna_strings(protein):
    # Dictionary mapping amino acids to number of codons
    codons = {
        'A': 4, 'C': 2, 'D': 2, 'E': 2, 'F': 2, 'G': 4, 'H': 2, 'I': 3,
        'K': 2, 'L': 6, 'M': 1, 'N': 2, 'P': 4, 'Q': 2, 'R': 6, 'S': 6,
        'T': 4, 'V': 4, 'W': 1, 'Y': 2, '_': 3  # '_' represents stop codon
    }

    # Initialize the number of RNA strings
    num_strings = 1

    # Multiply the number of codons for each amino acid in the protein
    for aa in protein:
        if aa not in codons:
            raise ValueError(f"Invalid amino acid: {aa}")
        num_strings *= codons[aa]

    # Account for the 3 possible stop codons at the end
    num_strings *= 3

    # Return the result modulo 1,000,000
    return num_strings % 1000000


def main():
    # Prompt the user to enter the protein string
    protein = input("Enter the protein string: ")

    try:
        # Calculate and print the number of possible RNA strings
        result = num_rna_strings(protein)
        print(f"Number of possible RNA strings: {result}")
    except ValueError as e:
        print(f"Error: {str(e)}")


if __name__ == '__main__':
    main()