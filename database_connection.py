import sqlite3


class DatabaseConnection:
    """ Establishes the self.connection for future use of the database.
        Prodive the host, a string for the database location.
    """

    def __init__(self, host: str):

        self.connection = None
        self.host = host

    def __enter__(self):
        """ Establises and returns the connection \
        to the database to be used by functions.
        """
        self.connection = sqlite3.connect(self.host)
        return self.connection

    def __exit__(self, exc_type, exc_val, exc_tb):
        """ Closes connections to the database when no longer being used.
        """
        self.connection.commit()
        self.connection.close()
