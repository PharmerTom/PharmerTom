def fibonacci_with_lifespan(n, m):
    """
    Calculates the number of rabbit pairs after n months, given a lifespan of m months.

    Args:
        n (int): The number of months to simulate.
        m (int): The lifespan of each rabbit pair in months.

    Returns:
        int: The total number of rabbit pairs after n months.
    """
    # Initialize the rabbit pairs array with m elements
    pairs = [0] * m

    # Start with one pair of rabbits
    pairs[0] = 1

    # Simulate the rabbit reproduction for n months
    for _ in range(1, n):
        new_pairs = sum(pairs[1:])
        pairs = [new_pairs] + pairs[:-1]

    # Return the total number of rabbit pairs
    return sum(pairs)


def validate_input(n, m):
    """
    Validates the input values of n and m.

    Args:
        n (int): The number of months to simulate.
        m (int): The lifespan of each rabbit pair in months.

    Returns:
        bool: True if the input is valid, False otherwise.
    """
    if n < 1 or n > 100:
        print("Error: n must be between 1 and 100.")
        return False

    if m < 1 or m > 20:
        print("Error: m must be between 1 and 20.")
        return False

    return True


def get_user_input():
    """
    Prompts the user to enter the values of n and m.

    Returns:
        tuple: A tuple containing the values of n and m.
    """
    n = int(input("Enter the number of months (n): "))
    m = int(input("Enter the lifespan of each rabbit pair in months (m): "))
    return n, m


def main():
    # Get user input for n and m
    n, m = get_user_input()

    # Validate the input
    if not validate_input(n, m):
        return

    # Calculate the number of rabbit pairs
    total_pairs = fibonacci_with_lifespan(n, m)

    # Print the result
    print(f"The total number of rabbit pairs after {n} months is: {total_pairs}")


if __name__ == "__main__":
    main()