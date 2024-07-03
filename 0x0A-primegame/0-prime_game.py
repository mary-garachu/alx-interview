def isWinner(x, nums):
    def sieve_of_eratosthenes(max_n):
        """Generate a list of prime numbers up to max_n"""
        is_prime = [True] * (max_n + 1)
        p = 2
        while p * p <= max_n:
            if is_prime[p]:
                for i in range(p * p, max_n + 1, p):
                    is_prime[i] = False
            p += 1
        prime_numbers = [p for p in range(2, max_n + 1) if is_prime[p]]
        return prime_numbers

    def prime_game(n, primes):
        """Simulate a single round of the prime game for a given n."""
        set_numbers = list(range(1, n + 1))
        prime_set = set(primes)
        turn = 0  # 0 for Maria, 1 for Ben

        while True:
            possible_moves = [p for p in set_numbers if p in prime_set]
            if not possible_moves:
                break
            chosen_prime = possible_moves[0]
            set_numbers = [
                num for num in set_numbers if num % chosen_prime != 0
                ]
            turn = 1 - turn  # Switch turns

        return turn  # 0 if Ben wins, 1 if Maria wins

    max_n = max(nums)
    primes = sieve_of_eratosthenes(max_n)

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        winner = prime_game(n, primes)
        if winner == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
