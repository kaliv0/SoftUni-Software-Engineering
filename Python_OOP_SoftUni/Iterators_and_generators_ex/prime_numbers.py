def get_primes(nums):
    def is_prime(n):
        if n > 1:
            for i in range(2, n):
                if n % i == 0:
                    return False
            return True

    for num in nums:
        if is_prime(num):
            yield num


if __name__ == "__main__":
    print(list(get_primes([2, 4, 3, 5, 6, 9, 1, 0])))
