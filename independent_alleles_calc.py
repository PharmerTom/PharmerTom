import math

def calculate_probability(k, N):
    """
    Calculates the probability that at least N Aa Bb organisms will belong to the k-th generation of Tom's family tree.

    Args:
        k (int): The generation number (k ≤ 7).
        N (int): The minimum number of Aa Bb organisms in the k-th generation (N ≤ 2^k).

    Returns:
        float: The probability that at least N Aa Bb organisms will belong to the k-th generation.
    """
    total_organisms = 2 ** k
    probability = 0.0

    for i in range(N, total_organisms + 1):
        prob_i = math.comb(total_organisms, i) * (0.25 ** i) * (0.75 ** (total_organisms - i))
        probability += prob_i

    return probability

def validate_input(k, N):
    """
    Validates the input values of k and N.

    Args:
        k (int): The generation number.
        N (int): The minimum number of Aa Bb organisms.

    Returns:
        bool: True if the input is valid, False otherwise.
    """
    if k <= 0 or k > 7:
        print("Invalid input. Please ensure that k is a positive integer and k ≤ 7.")
        return False
    if N <= 0 or N > 2 ** k:
        print(f"Invalid input. Please ensure that N is a positive integer and N ≤ 2^k (N ≤ {2**k} for k = {k}).")
        return False
    return True

def main():
    # Read input from the user
    try:
        k, N = map(int, input("Enter the values of k and N (separated by space): ").split())
    except ValueError:
        print("Invalid input. Please enter integer values for k and N.")
        return

    # Validate input
    if not validate_input(k, N):
        return

    # Calculate the probability
    probability = calculate_probability(k, N)

    # Print the result
    print(f"The probability that at least {N} Aa Bb organisms will belong to the {k}-th generation is: {probability:.3f}")

if __name__ == "__main__":
    main()