def hamming_distance(s, t):
    """
    Calculates the Hamming distance between two strings of equal length.

    Args:
        s (str): The first string.
        t (str): The second string.

    Returns:
        int: The Hamming distance between s and t.
    """
    if len(s) != len(t):
        raise ValueError("Strings must be of equal length.")

    return sum(1 for a, b in zip(s, t) if a != b)


def main():
    """
    Main function to read the input strings, calculate the Hamming distance,
    and print the result.
    """
    s = input().strip()
    t = input().strip()

    distance = hamming_distance(s, t)
    print(distance)


if __name__ == '__main__':
    main()