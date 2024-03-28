def count_nucleotides(dna_string):
    """
    Count the occurrences of each nucleotide in a DNA string.

    Args:
        dna_string (str): The DNA string to analyze.

    Returns:
        str: A string containing the counts of each nucleotide (A, C, G, T) separated by spaces.
    """
    count_A = dna_string.count('A')
    count_C = dna_string.count('C')
    count_G = dna_string.count('G')
    count_T = dna_string.count('T')
    return f"{count_A} {count_C} {count_G} {count_T}"


def transcribe(dna_string):
    """
    Transcribe a DNA string into its corresponding RNA string.

    Args:
        dna_string (str): The DNA string to transcribe.

    Returns:
        str: The transcribed RNA string.
    """
    rna_string = dna_string.replace('T', 'U')
    return rna_string


def reverse_complement(dna_string):
    """
    Find the reverse complement of a DNA string.

    Args:
        dna_string (str): The DNA string to find the reverse complement of.

    Returns:
        str: The reverse complement of the DNA string.
    """
    # Create a dictionary to map each nucleotide to its complement
    complement_dict = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}

    # Reverse the DNA string
    reversed_dna = dna_string[::-1]

    # Replace each nucleotide with its complement
    complement_dna = ''.join([complement_dict[nucleotide] for nucleotide in reversed_dna])
    return complement_dna

if __name__ == '__main__':
    # Example usage code
    dna_string1 = "ATGC"
    result = count_nucleotides(dna_string1)
    print("Count of nucleotides:", result)

    dna_string2 = "ATGC"
    rna_string = transcribe(dna_string2)
    print("Transcribed RNA:", rna_string)

    dna_string3 = "ATGA"
    reverse_complement_dna = reverse_complement(dna_string3)
    print("Reverse complement:", reverse_complement_dna)
