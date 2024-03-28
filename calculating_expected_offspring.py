def calculate_expected_offspring(genotypes):
    """
    Calculates the expected number of offspring displaying the dominant phenotype.

    Args:
        genotypes (list): A list of six integers representing the number of couples
                          with each genotype pairing (AA-AA, AA-Aa, AA-aa, Aa-Aa, Aa-aa, aa-aa).

    Returns:
        float: The expected number of offspring displaying the dominant phenotype.
    """
    probabilities = [1, 1, 1, 0.75, 0.5, 0]
    expected_dominant_offspring = sum(count * prob * 2 for count, prob in zip(genotypes, probabilities))

    return expected_dominant_offspring


def validate_input(genotypes):
    """
    Validates the input genotype counts.

    Args:
        genotypes (list): A list of genotype counts.

    Returns:
        bool: True if the input is valid, False otherwise.
    """
    if len(genotypes) != 6:
        print("Error: Please provide exactly six genotype counts.")
        return False

    for count in genotypes:
        if count < 0 or count > 20000:
            print("Error: Genotype counts must be non-negative integers not exceeding 20,000.")
            return False

    return True


def main():
    # Prompt user for input method choice
    choice = input("Enter 'F' to read input from a file or 'M' to enter manually: ")

    if choice.upper() == 'F':
        # Read input from file
        filename = input("Enter the input file name: ")
        try:
            with open(filename, 'r') as file:
                genotypes = list(map(int, file.read().split()))
        except FileNotFoundError:
            print(f"Error: File '{filename}' not found.")
            return
    elif choice.upper() == 'M':
        # Read input from user
        genotypes = list(map(int, input("Enter the genotype counts (space-separated): ").split()))
    else:
        print("Error: Invalid choice. Please enter 'F' or 'M'.")
        return

    # Validate input
    if not validate_input(genotypes):
        return

    # Calculate and print the expected number of offspring with dominant phenotype
    expected_offspring = calculate_expected_offspring(genotypes)
    print(f"Expected number of offspring displaying the dominant phenotype: {expected_offspring:.1f}")


if __name__ == "__main__":
    main()