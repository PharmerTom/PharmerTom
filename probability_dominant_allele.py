def calculate_dominant_probability(k, m, n):
    """
    Calculates the probability of producing an offspring with a dominant allele.

    Args:
        k (int): Number of homozygous dominant individuals.
        m (int): Number of heterozygous individuals.
        n (int): Number of homozygous recessive individuals.

    Returns:
        float: Probability of producing an offspring with a dominant allele.
    """
    total_population = k + m + n
    total_combinations = total_population * (total_population - 1)

    # Probability of selecting a homozygous dominant and any other individual
    prob_dom_dom = (k / total_population) * ((k - 1) / (total_population - 1))
    prob_dom_het = (k / total_population) * (m / (total_population - 1))
    prob_dom_rec = (k / total_population) * (n / (total_population - 1))

    # Probability of selecting a heterozygous and a homozygous dominant or heterozygous
    prob_het_dom = (m / total_population) * (k / (total_population - 1))
    prob_het_het = (m / total_population) * ((m - 1) / (total_population - 1)) * 0.75
    prob_het_rec = (m / total_population) * (n / (total_population - 1)) * 0.5

    # Probability of selecting a homozygous recessive and a homozygous dominant or heterozygous
    prob_rec_dom = (n / total_population) * (k / (total_population - 1))
    prob_rec_het = (n / total_population) * (m / (total_population - 1)) * 0.5

    # Sum up all probabilities to get the total probability of producing an offspring with a dominant allele
    total_probability = (prob_dom_dom + prob_dom_het + prob_dom_rec +
                         prob_het_dom + prob_het_het + prob_het_rec +
                         prob_rec_dom + prob_rec_het)

    return total_probability

if __name__ == "__main__":
    # Prompt the user for inputs
    k = int(input("Enter the number of homozygous dominant individuals: "))
    m = int(input("Enter the number of heterozygous individuals: "))
    n = int(input("Enter the number of homozygous recessive individuals: "))

    # Calculate the probability
    probability = calculate_dominant_probability(k, m, n)

    # Print the result
    print(f"The probability of producing an offspring with a dominant allele is: {probability:.5f}")