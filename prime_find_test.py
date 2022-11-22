import os
# Test suite for prime_finder
from prime_find import create_primes_table, return_primes
from prime_find import prime_finder
from prime_find import write_primes_to_db


class TestDataBaseReadAndWrite:

    def test_returns_list(self):
        """ Removes any db before testing,
        then in reading db creates a new DB with default
        checks default creation is a list"""
        if os.path.isfile('primes.db'):
            os.remove('primes.db')
        returned_value = return_primes()
        assert isinstance(returned_value, list)

    def test_returns_default_values(self):
        """ Removes any db before testing,
        then in reading db creates a new DB with default
        checks default creation is initialised with value [2]"""
        if os.path.isfile('primes.db'):
            os.remove('primes.db')
        returned_value = return_primes()
        assert returned_value == [2]

    def test_returns_correct_values_upto_10(self):
        """ Removes any db before testing,
        creates a new DB
        finds primes up to 10
        writes the primes
        reads the primes and checks against known list"""
        if os.path.isfile('primes.db'):
            os.remove('primes.db')
        create_primes_table()
        primes = prime_finder(10)
        print(f"primes is {primes}")
        write_primes_to_db(primes)
        returned_value = return_primes()
        assert returned_value == [2, 3, 5, 7]

    def test_returns_correct_values_upto_100(self):
        """ Removes any db before testing,
        creates a new DB
        finds primes up to 100
        writes the primes
        reads the primes and checks against known list"""
        if os.path.isfile('primes.db'):
            os.remove('primes.db')
        create_primes_table()
        primes = prime_finder(100)
        print(f"primes is {primes}")
        write_primes_to_db(primes)
        returned_value = return_primes()
        assert returned_value == [2, 3, 5, 7, 11, 13, 17, 19, 23,
                                  29, 31, 37, 41, 43, 47, 53, 59,
                                  61, 67, 71, 73, 79, 83, 89, 97]


class TestPrimeFinder:

    """ Tests for the prime_finder function"""

    def test_for_zero(self):
        """ Zero is not a prime and should not be in the prime list"""
        primes = prime_finder(10)
        assert 0 not in primes

    def test_for_one(self):
        """ One is not a prime and should not be in the prime list"""
        primes = prime_finder(10)
        assert 1 not in primes

    def test_for_primness_up_to_10(self):
        """ Generates primes up to 10 and checks if they are prime"""
        primes = prime_finder(10)
        for prime in primes:
            for i in range(2, prime):
                assert prime % i != 0

    def test_for_primness_up_to_100(self):
        """ Generates primes up to 100 and checks if they are prime"""
        primes = prime_finder(100)
        for prime in primes:
            for i in range(2, prime):
                assert prime % i != 0

    def test_for_primness_up_to_1000(self):
        """ Generates primes up to 1 thousand and checks if they are prime"""
        primes = prime_finder(1000)
        for prime in primes:
            for i in range(2, prime):
                assert prime % i != 0
