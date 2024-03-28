codon_map = {
    "UUU": "F", "UUC": "F", "UUA": "L", "CUU": "L", "CUC": "L", "CUA": "L", "CUG": "L",
    "AUU": "I", "AUC": "I", "AUA": "I", "AUU": "I", "GUU": "V", "GUC": "V", "GUA": "V", "GUG": "V",
    "ACU": "T", "ACC": "T", "ACA": "T", "ACG": "T", "CCU": "P", "CCC": "P", "CCA": "P", "CCG": "P",
    "UCU": "S", "UCC": "S", "UCA": "S", "UCG": "S", "GCU": "A", "GCC": "A", "GCA": "A", "GCG": "A",
    "UAU": "Y", "UAC": "Y", "UAA": "Stop", "UAG": "Stop", "UGU": "C", "UGC": "C", "CGU": "R", "CGC": "R",
    "CGA": "R", "CGG": "R", "AGU": "S", "AGC": "S", "AGA": "R", "AGG": "R", "GGU": "G", "GGC": "G",
    "GGA": "G", "GGG": "G",
    "AUG": "M"
}


def count_rna_strings(protein):
  """
  Counts the number of different RNA strings that could be translated
  into the given protein string (modulo 1,000,000).

  Args:
      protein: A protein string consisting of amino acids.

  Returns:
      The number of different RNA strings modulo 1,000,000.
  """

  # Initialize counter for valid RNA strings
  count = 1

  # Iterate through the protein string
  for i in range(len(protein)):
    # Check if amino acid exists in codon map
    if protein[i] not in codon_map.values():
      return 0  # Invalid protein string

    # Count possibilities for each codon (considering only valid options)
    count = (count * len([codon for codon in codon_map if codon_map[codon] == protein[i]])) % 1000000

  # Enforce stop codon at the end (optional, modify as needed)
  # This ensures a stop codon is present at the end for this scenario
  if codon_map[protein[-1]] != "Stop":
    count = count * 3  # Multiply by 3 for the 3 stop codons (UAA, UAG, UGA)

  return count


def main():
  """
  Reads protein string from user input and prints the number of RNA strings.
  """
  protein = input("Enter protein string: ")
  result = count_rna_strings(protein)
  print(f"Number of RNA strings: {result}")

if __name__ == "__main__":
  main()
