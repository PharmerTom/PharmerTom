from collections import Counter


def read_fasta(file_path):
    """
    Reads a FASTA file and returns a list of DNA strings.

    Args:
        file_path (str): The path to the FASTA file.

    Returns:
        list: A list of DNA strings.
    """
    dna_strings = []
    with open(file_path, 'r') as file:
        current_dna = ""
        for line in file:
            if line.startswith('>'):
                if current_dna:
                    dna_strings.append(current_dna)
                    current_dna = ""
            else:
                current_dna += line.strip()
        if current_dna:
            dna_strings.append(current_dna)
    return dna_strings


def get_consensus_and_profile(dna_strings):
    """
    Given a list of DNA strings, returns the consensus string and profile matrix.

    Args:
        dna_strings (list): A list of DNA strings.

    Returns:
        tuple: A tuple containing the consensus string and profile matrix.
    """
    n = len(dna_strings[0])
    profile = {'A': [0] * n, 'C': [0] * n, 'G': [0] * n, 'T': [0] * n}

    for dna in dna_strings:
        for i, base in enumerate(dna):
            profile[base][i] += 1

    consensus = "".join(max(profile, key=lambda x: profile[x][i]) for i in range(n))

    return consensus, profile


def format_profile(profile):
    """
    Formats the profile matrix as a string.

    Args:
        profile (dict): The profile matrix.

    Returns:
        str: The formatted profile matrix string.
    """
    formatted_profile = ""
    for base in 'ACGT':
        formatted_profile += f"{base}: {' '.join(map(str, profile[base]))}\n"
    return formatted_profile.strip()


def main():
    input_file = input("Enter the path to the input FASTA file: ")
    output_file = input("Enter the path to the output text file: ")

    try:
        dna_strings = read_fasta(input_file)
        if not dna_strings:
            print("Error: No DNA strings found in the FASTA file.")
            return

        consensus, profile = get_consensus_and_profile(dna_strings)
        formatted_profile = format_profile(profile)

        with open(output_file, 'w') as file:
            file.write(consensus + "\n")
            file.write(formatted_profile)

        print("Results exported to", output_file)
    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")
    except Exception as e:
        print(f"Error: {str(e)}")


if __name__ == "__main__":
    main()