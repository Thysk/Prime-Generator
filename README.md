# Prime-Generator
## A python coded prime number finder. This is a practice piece of work to work on coding practices and develop my understanding.

The user interface is a simple cli menu that allows users to find new primes, or view the list of primes already found.
The program itself uses the sieve of eratosthenes to find primes.
It then writes all the prime numbers to a sqllite3 database.

### To run the application run the code in app.py to access the CLI.

'f' option is the find_primes workflow that finds primes and saves them to a sqlite databse
  Users will be prompted to fill in an integer to define the upper_bound to find primes up to.
  This upperbound is currently searched for in a single array so large numbers will use a lot of memory (plans to segment the array to improve memory usage)
  
'r' option reads all primes found from the database as a list

'q' quits the program cleanly

### TODO:

   - Segment large arrays to improve memory useage
  
   - Add option to clear database in CLI
  
   - Option to return primes in a defined range
  
  
  
