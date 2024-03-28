def population_growth(n, k, f1=1, f2=1):
    """
    Calculate the population size after n generations.

    Args:
        n (int): The number of generations.
        k (float): The average number of offspring per reproductive pair in each generation.
        f1 (int): The initial population size of the first generation (default is 1).
        f2 (int): The initial population size of the second generation (default is 1).

    Returns:
        int: The population size after n generations.
    """
    # Base case: if n is 1 or 2, return the corresponding initial population size
    if n == 1:
        return f1
    elif n == 2:
        return f2

    # Create a list to store the population size for each generation
    population = [0] * (n + 1)

    # Initialize the first two generations with the given initial population sizes
    population[1] = f1
    population[2] = f2

    # Calculate the population size for each subsequent generation
    for i in range(3, n + 1):
        population[i] = population[i - 1] + k * population[i - 2]

    return population[n]

if __name__ == "__main__":
    # Example usage
    generations = 20
    offspring_per_pair = 4
    initial_pop_size1 = 1
    initial_pop_size2 = 1

    total_population = population_growth(generations, offspring_per_pair, initial_pop_size1, initial_pop_size2)
    print(f"Total population after {generations} generations: {total_population}")

