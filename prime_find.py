import time

from math import isqrt
from database_connection import DatabaseConnection

# TODO: Segment array when large to improve performance


def create_primes_table():
    """ Creates the 'primes.db' database \
        it then  populates the database with the value of 2 \
        the first prime number, which helps prevent crashes \
        from later functions
    """
    with DatabaseConnection('primes.db') as connection:
        cursor = connection.cursor()
        cursor.execute(
            '''CREATE TABLE IF NOT EXISTS primes
            (prime_number INTEGER PRIMARY KEY)''')
        val = 2
        cursor.execute(
            f"INSERT OR REPLACE INTO primes (prime_number) VALUES ({val})")


def prime_finder(upper_bound: int) -> list:
    """ Searches for the primes between 2 and the defined upper_bound.
        It does this by initialising an array, and using the \
        Sieve of Eratosthenes method quickly finds more primes.

    Args:
        upper_bound (int): An integer defining the upper bounds of the array \
            in which primes are searched for within

    Returns:
        list: A List of prime numbers found between the lower_bound=2 \
        and your upper_bound
    """
    prime_array = [True] * upper_bound
    prime_array[0] = False
    prime_array[1] = False

    for i in range(2, 1+isqrt(upper_bound)):
        if prime_array[i]:
            for x in range(i*i, upper_bound, i):
                prime_array[x] = False
    return [i for i in range(upper_bound) if prime_array[i]]


def write_primes_to_db(n: list) -> None:
    """ Writes the input list to the DB
        In this case takes a list and writes each item to the \
        column prime_number in the table primes, \
        in the database primes.db.

    Args:
        n (list): A list of inputs to be written to a database
    """
    with DatabaseConnection('primes.db') as connection:
        cursor = connection.cursor()
        for val in n:
            cursor.execute(
                f"INSERT OR REPLACE INTO primes (prime_number) VALUES ({val})")


def return_primes() -> list:
    """ Reads from the DB and returns all the primes

    Returns:
        list: Returns a list of all the columns \
        found within the table primes, within the database primes.db
    """
    create_primes_table()
    with DatabaseConnection('primes.db') as connection:
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM primes')
        primes = [row[0] for row in cursor.fetchall()]
        return(primes)


# Initialising menu for finding the primes
def find_primes_workflow(upper_bound: int = None,) -> None:
    """ The main workflow function for the prime number searching functionality.
        This can function can be called directly for automated workflows,
        or this function will be called from the App Menu found in app.py.

        This function works in several stage:
            1. Established an upper_bound for the array, \
            either through user input or passed argumennts
            2. Creates the database if required
            3. Finds all the primes up to the upper_bound, \
            while timing the function
            4. writes the found primes to the database

    Args:
        upper_bound (int, optional): This intiger can be provided by calling \
        this function directly, or from inputs. Defaults to None.
    """

    if not upper_bound:
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
    write_primes_to_db(write)
    end = time.perf_counter()
    print(f"To write it took {end - start} Seconds")
