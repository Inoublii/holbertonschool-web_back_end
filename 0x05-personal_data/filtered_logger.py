#!/usr/bin/env python3
"""
Logging module.

"""
import os
import mysql.connector
import re
from typing import List
import logging
PII_FIELDS = ('name', 'email', 'phone', 'ssn', 'password')


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = list(fields)

    def format(self, record: logging.LogRecord) -> str:
        '''Returns a log'''
        msg = logging.Formatter(self.FORMAT).format(record)
        return filter_datum(self.fields, self.REDACTION,
                            msg, self.SEPARATOR)


def filter_datum(fields: List[str],
                 redaction: str,
                 message: str,
                 separator: str) -> str:
    """ Logging module. """
    lst = message.split(separator)

    for f in fields:
        for i in range(len(lst)):
            if lst[i].startswith(f):
                subst = f + '=' + redaction
                lst[i] = re.sub(lst[i], subst, lst[i])

    return separator.join(lst)


def get_logger() -> logging.Logger:
    """Returns a Logger object."""
    logger = logging.getLogger('user_data')
    logger.setLevel(logging.INFO)
    logger.propagate = False

    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.INFO)

    formatter = logging.Formatter(RedactingFormatter(PII_FIELDS))
    stream_handler.setFormatter(formatter)

    logger.addHandler(stream_handler)

    return logger


def get_db() -> mysql.connector.connection.MySQLConnection:
    """ A function that returns a connector to a database """
    c = mysql.connector.connection.MySQLConnection(
      user=os.getenv('PERSONAL_DATA_DB_USERNAME', 'root'),
      password=os.getenv('PERSONAL_DATA_DB_PASSWORD', ''),
      host=os.getenv('PERSONAL_DATA_DB_HOST', 'localhost'),
      database=os.getenv('PERSONAL_DATA_DB_NAME')
    )
    return c


def main() -> None:
    """Obtains a database connection using get_db and retrieve all rows
    in the users table and display each row under a filtered format.
    """
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM users")
    records = cursor.fetchall()
    logger = get_logger()

    fields = [x[0] for x in cursor.description]

    for row in records:
        msg = ''
        for i in range(len(fields)):
            msg += fields[i] + '=' + str(row[i]) + ';'
        logger.info(msg)

    cursor.close()
    db.close()


if __name__ == "__main__":
    main()
