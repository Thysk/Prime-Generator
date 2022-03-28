import time

from math import isqrt
from database_connection import DatabaseConnection


# Create the 'primes' database and populates it with 2 to prevent crashes
def create_primes_table():
    with DatabaseConnection('primes.db') as connection:
        cursor = connection.cursor()
        cursor.execute(
            '''CREATE TABLE IF NOT EXISTS primes
            (prime_number INTEGER PRIMARY KEY)''')
        val = 2
        cursor.execute(
            f"INSERT OR REPLACE INTO primes (prime_number) VALUES ({val})")


# Searches for the primes.
# Loads in previously found primes.
# Uses Sieve of Eratosthenes to search for primes
def prime_finder(upper_bound: int) -> list:
    prime_array = [True] * upper_bound
    prime_array[0] = False
    prime_array[1] = False

    for i in range(2, 1+isqrt(upper_bound)):
        if prime_array[i]:
            for x in range(i*i, upper_bound, i):
                prime_array[x] = False
    return [i for i in range(upper_bound) if prime_array[i]]


# Writes the found primes to the DB
def write_primes_to_db(n: list) -> None:
    with DatabaseConnection('primes.db') as connection:
        cursor = connection.cursor()
        for val in n:
            cursor.execute(
                f"INSERT OR REPLACE INTO primes (prime_number) VALUES ({val})")


# Reads from the DB and returns all the primes
def return_primes() -> list:
    create_primes_table()
    with DatabaseConnection('primes.db') as connection:
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM primes')
        primes = [row[0] for row in cursor.fetchall()]
        return(primes)


# Initialising menu for finding the primes
def find_primes_workflow() -> None:
    # gets an integer from user, if invalid input loops input
    while True:
        try:
            upper_bound = int(
                input("Input an integer for upper bound 3 or above: "))
            if upper_bound <= 2:
                print("Please make the value above 2")
                continue
            break
        except ValueError:
            print("That is not a valid intiger.")
            continue

    # Creates db if needed
    create_primes_table()

    # Find the primes with a timer wrapper
    start = time.perf_counter()
    write = prime_finder(upper_bound)
    end = time.perf_counter()

    print(f"To find primes up to {upper_bound} it took {end - start} Seconds")

    # write the primes to a database with a timer wrapper
    start = time.perf_counter()
    with DatabaseConnection('primes.db') as connection:
        cursor = connection.cursor()
    write_primes_to_db(write)
    end = time.perf_counter()
    print(f"To write it took {end - start} Seconds")
