from prime_find import prime_finder


# Test suite for prime_generator


class TestPrimeGenerator:

    def test_for_zero(self):
        """Zero is not a prime and should not be in the prime list"""
        primes = prime_finder(10)
        assert 0 not in primes

    def test_for_one(self):
        """One is not a prime and should not be in the prime list"""
        primes = prime_finder(10)
        assert 1 not in primes

    def test_for_primness_up_to_10(self):
        """Generates primes up to 10 and checks if they are prime"""
        primes = prime_finder(10)
        for prime in primes:
            for i in range(2, prime):
                assert prime % i != 0

    def test_for_primness_up_to_100(self):
        """Generates primes up to 100 and checks if they are prime"""
        primes = prime_finder(100)
        for prime in primes:
            for i in range(2, prime):
                assert prime % i != 0

    def test_for_primness_up_to_1000(self):
        """Generates primes up to 1 thousand and checks if they are prime"""
        primes = prime_finder(1000)
        for prime in primes:
            for i in range(2, prime):
                assert prime % i != 0
