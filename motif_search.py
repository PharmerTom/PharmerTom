def find_substring_locations(s, t):
    """
    Finds all locations of substring t in string s.

    Args:
        s (str): The input string to search within.
        t (str): The substring to search for.

    Returns:
        list: A list of starting positions of t in s (1-based numbering).
    """
    locations = []
    i = s.find(t)
    while i != -1:
        locations.append(i + 1)  # 1-based numbering
        i = s.find(t, i + 1)
    return locations


def process_input(s, t):
    """
    Processes the input string and substring and prints the locations of t in s.

    Args:
        s (str): The input string to search within.
        t (str): The substring to search for.
    """
    if not s or not t:
        print("Error: Input string and substring cannot be empty.")
        return

    locations = find_substring_locations(s, t)

    if locations:
        print("Locations of substring t in s:")
        print(" ".join(map(str, locations)))
    else:
        print("Substring t not found in s.")


def main():
    input_choice = input("Enter 'F' to input from a file or 'M' for manual input: ").strip().upper()

    if input_choice == 'F':
        file_path = input("Enter the file path: ").strip()
        try:
            with open(file_path, 'r') as file:
                s = file.readline().strip()
                t = file.readline().strip()
            process_input(s, t)
        except FileNotFoundError:
            print("Error: File not found.")
        except IOError:
            print("Error: An error occurred while reading the file.")
    elif input_choice == 'M':
        s = input("Enter the input string (s): ").strip()
        t = input("Enter the substring to search for (t): ").strip()
        process_input(s, t)
    else:
        print("Error: Invalid input choice.")


if __name__ == "__main__":
    main()