import time
from math import isqrt
from database_connection import DatabaseConnection


def create_primes_table():
    with DatabaseConnection('primes.db') as connection:
        cursor = connection.cursor()

        cursor.execute(
            'CREATE TABLE IF NOT EXISTS primes (prime_number INTEGER PRIMARY KEY)')
        val = 2
        cursor.execute(
            f"INSERT OR REPLACE INTO primes (prime_number) VALUES ({val})")


def prime_generator(upper_bound, my_highest_prime):
    start = time.perf_counter()
    primes_list = []
    with DatabaseConnection('primes.db') as connection:
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM primes')
        primes = [row[0] for row in cursor.fetchall()]
        for p in primes:

            primes_list.append(p)
    if int(my_highest_prime) < 2:
        low = 2
    else:
        low = my_highest_prime

    start = time.perf_counter()

    prime_array = [True] * upper_bound
    prime_array[0] = False
    prime_array[1] = False

    for i in range(2, isqrt(upper_bound)):
        if prime_array[i]:
            for x in range(i*i, upper_bound, i):
                prime_array[x] = False
    end = time.perf_counter()
    print(f"To find primes up to {upper_bound} it took {end - start} Seconds")
    return [i for i in range(upper_bound) if prime_array[i]]


def write_primes_to_db(n):
    with DatabaseConnection('primes.db') as connection:
        cursor = connection.cursor()
        val = n
        cursor.execute(
            f"INSERT OR REPLACE INTO primes (prime_number) VALUES ({val})")


def return_primes():
    create_primes_table()
    with DatabaseConnection('primes.db') as connection:
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM primes')
        primes = [row[0] for row in cursor.fetchall()]
        print(primes)


def find_primes():
    upper_bound = int(input("Input an integer for upper bound: "))
    create_primes_table()
    with DatabaseConnection('primes.db') as connection:
        cursor = connection.cursor()

        cursor.execute(
            'SELECT prime_number FROM primes ORDER BY prime_number DESC')
        my_highest_prime = cursor.fetchone() or 2
        if my_highest_prime != 2:
            my_highest_prime = (my_highest_prime[0]) + 1
        else:
            pass
    write = prime_generator(upper_bound, my_highest_prime)
    for n in write:
        write_primes_to_db(n)


user_options = {
    'r': return_primes,
    'f': find_primes
}
USER_CHOICE = "What would you like to do? 'r' to return all primes found or 'f' to find more: "


def menu():
    user_input = input(USER_CHOICE)
    while True:
        if user_input in user_options:
            selected_function = user_options[user_input]
            selected_function()
        else:
            print("Input not recognised, please try again.")
        user_input = input(USER_CHOICE)


menu()
