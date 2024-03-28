# RNA codon table
codon_table = {
    'UUU': 'F', 'CUU': 'L', 'AUU': 'I', 'GUU': 'V',
    'UUC': 'F', 'CUC': 'L', 'AUC': 'I', 'GUC': 'V',
    'UUA': 'L', 'CUA': 'L', 'AUA': 'I', 'GUA': 'V',
    'UUG': 'L', 'CUG': 'L', 'AUG': 'M', 'GUG': 'V',
    'UCU': 'S', 'CCU': 'P', 'ACU': 'T', 'GCU': 'A',
    'UCC': 'S', 'CCC': 'P', 'ACC': 'T', 'GCC': 'A',
    'UCA': 'S', 'CCA': 'P', 'ACA': 'T', 'GCA': 'A',
    'UCG': 'S', 'CCG': 'P', 'ACG': 'T', 'GCG': 'A',
    'UAU': 'Y', 'CAU': 'H', 'AAU': 'N', 'GAU': 'D',
    'UAC': 'Y', 'CAC': 'H', 'AAC': 'N', 'GAC': 'D',
    'UAA': '*', 'CAA': 'Q', 'AAA': 'K', 'GAA': 'E',
    'UAG': '*', 'CAG': 'Q', 'AAG': 'K', 'GAG': 'E',
    'UGU': 'C', 'CGU': 'R', 'AGU': 'S', 'GGU': 'G',
    'UGC': 'C', 'CGC': 'R', 'AGC': 'S', 'GGC': 'G',
    'UGA': '*', 'CGA': 'R', 'AGA': 'R', 'GGA': 'G',
    'UGG': 'W', 'CGG': 'R', 'AGG': 'R', 'GGG': 'G'
}

def translate_rna_to_protein(rna_string):
    """
    Translates an RNA string into a protein string based on the RNA codon table.

    Args:
        rna_string (str): The RNA string to be translated.

    Returns:
        str: The translated protein string.
    """
    protein_string = ''
    for i in range(0, len(rna_string), 3):
        codon = rna_string[i:i+3]
        if len(codon) == 3:
            amino_acid = codon_table[codon]
            if amino_acid == '*':
                break
            protein_string += amino_acid
    return protein_string

def main():
    """
    The main function that reads the RNA string from an input file, translates it,
    and writes the resulting protein string to an output file.
    """
    # Get input file name from the user
    input_file = input("Enter the input file name: ")

    try:
        # Read the RNA string from the input file
        with open(input_file, 'r') as file:
            rna_string = file.read().strip()

        # Translate RNA to protein
        protein_string = translate_rna_to_protein(rna_string)

        # Get output file name from the user
        output_file = input("Enter the output file name: ")

        # Write the protein string to the output file
        with open(output_file, 'w') as file:
            file.write(protein_string)

        print(f"Translation complete. Protein string written to {output_file}.")

    except FileNotFoundError:
        print(f"File '{input_file}' not found.")

if __name__ == '__main__':
    main()