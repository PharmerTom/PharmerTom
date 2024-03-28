import requests
import re


def get_sequence(uniprot_id):
    """
    Retrieves the protein sequence from the UniProt database for a given UniProt ID.

    Args:
        uniprot_id (str): UniProt ID of the protein.

    Returns:
        str: Protein sequence in FASTA format.
    """
    uniprot_id = uniprot_id.split("_")[0]  # Extract the accession number part
    url = f"http://www.uniprot.org/uniprot/{uniprot_id}.fasta"
    response = requests.get(url)
    if response.status_code == 200:
        return ''.join(response.text.splitlines()[1:])
    else:
        raise requests.exceptions.RequestException(f"Error retrieving data for {uniprot_id}")


def find_motifs(sequence):
    """
    Finds the locations of the N-glycosylation motif in a given protein sequence.

    Args:
        sequence (str): Protein sequence.

    Returns:
        list: Locations of the N-glycosylation motif in the protein sequence.
    """
    motif = re.compile('(?=N[^P][ST][^P])')
    locations = [str(m.start() + 1) for m in motif.finditer(sequence)]
    return locations


def main():
    # Read UniProt IDs from file
    file_path = input("Enter the file path: ")
    with open(file_path, 'r') as file:
        uniprot_ids = [line.strip().lstrip('>') for line in file]  # Remove leading '>' character

    # Process each UniProt ID
    output = []
    for uniprot_id in uniprot_ids:
        print(f"Processing UniProt ID: {uniprot_id}")
        try:
            sequence = get_sequence(uniprot_id)
            motif_locations = find_motifs(sequence)
            output.append(uniprot_id.split("_")[0])
            if motif_locations:
                output.append(' '.join(motif_locations))
            else:
                output.append('')  # Add an empty string if no motif matches found
        except requests.exceptions.RequestException as e:
            print(f"Error retrieving data for {uniprot_id}: {e}")

    # Display output
    print("\nOutput:")
    print('\n'.join(output))


if __name__ == '__main__':
    main()