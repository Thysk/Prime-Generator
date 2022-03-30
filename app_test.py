import os

from app import app_menu


class TestMenu:

    def test_read_db_using_menu(self):
        if os.path.isfile('primes.db'):
            os.remove('primes.db')
        read = app_menu('r')
        assert read == [2]

    def test_use_menu_to_find_primes_up_to_10(self):
        if os.path.isfile('primes.db'):
            os.remove('primes.db')
        app_menu('f', 10)
        assert app_menu('r') == [2, 3, 5, 7]
