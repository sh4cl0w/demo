def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def generate_primes(limit):

    primes = []
    for num in range(2, limit + 1):
        if is_prime(num):
            primes.append(num)
    return primes

def find_sum_of_primes(primes, target, count, start, current_combination, result):
    """Use backtracking to find combinations of prime numbers that sum to the target."""
    if count == 0 and target == 0:
        result.append(list(current_combination))
        return
    if count == 0 or target <= 0:
        return

    for i in range(start, len(primes)):
        current_combination.append(primes[i])
        find_sum_of_primes(primes, target - primes[i], count - 1, i + 1, current_combination, result)
        current_combination.pop()

def main(N, M):
    """Main function to determine and print the combination of M prime numbers that sum to N."""
    if not (1 <= N <= 10000) or not (2 < M <= 100):
        return "Invalid input"

    primes = generate_primes(N)
    result = []
    find_sum_of_primes(primes, N, M, 0, [], result)

    if result:
        for combination in result:
            print(combination)
    else:
        print("No combination found")

# Example usage:
N = int(input("Enter N: "))
M = int(input("Enter M: "))
main(N, M)
