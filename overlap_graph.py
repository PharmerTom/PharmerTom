"""
Overlap Graph Creator

This script reads a FASTA file containing DNA sequences and creates an overlap graph
based on the specified suffix/prefix overlap length (k). It generates an adjacency list
representing the overlap graph, where each edge indicates a suffix/prefix overlap
between two sequences.

Usage:
    python overlap_graph.py <fasta_file> <overlap_length>

Args:
    fasta_file (str): The path to the FASTA file containing the DNA sequences.
    overlap_length (int): The length of the suffix/prefix overlap (default: 3).

Output:
    The adjacency list representing the overlap graph, where each line represents an edge
    in the format "sequence_id_1 sequence_id_2".

Example:
    $ python overlap_graph.py sequences.fasta 3
    Rosalind_0498 Rosalind_2391
    Rosalind_0498 Rosalind_0442
    Rosalind_2391 Rosalind_2323
"""

import sys


def read_fasta(file_path):
    """
    Reads a FASTA file and returns a dictionary of sequences.

    Args:
        file_path (str): The path to the FASTA file.

    Returns:
        dict: A dictionary where the keys are sequence IDs and the values are the corresponding sequences.
    """
    sequences = {}
    with open(file_path, 'r') as file:
        current_id = None
        current_sequence = ''
        for line in file:
            if line.startswith('>'):
                if current_id:
                    sequences[current_id] = current_sequence
                current_id = line[1:].strip()
                current_sequence = ''
            else:
                current_sequence += line.strip()
        if current_id:
            sequences[current_id] = current_sequence
    return sequences


def create_overlap_graph(sequences, k):
    """
    Creates an overlap graph from a collection of sequences.

    Args:
        sequences (dict): A dictionary where the keys are sequence IDs and the values are the corresponding sequences.
        k (int): The length of the suffix/prefix overlap.

    Returns:
        list: The adjacency list representing the overlap graph.
    """
    adjacency_list = []
    for seq1_id, seq1 in sequences.items():
        for seq2_id, seq2 in sequences.items():
            if seq1_id != seq2_id and seq1.endswith(seq2[:k]):
                adjacency_list.append((seq1_id, seq2_id))
    return adjacency_list

def main():
    file_path = input("Enter the path to the FASTA file: ")
    k = int(input("Enter the overlap length: "))

    try:
        sequences = read_fasta(file_path)
        adjacency_list = create_overlap_graph(sequences, k)

        for edge in adjacency_list:
            print(f"{edge[0]} {edge[1]}")
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()