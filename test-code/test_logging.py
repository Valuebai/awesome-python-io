import logging
import logging.config
from os import path


def main():
    # Configure the logging system
    log_file_path = path.join(path.dirname(path.abspath(__file__)), '../config/logging.ini')
    logging.config.fileConfig(log_file_path)

    # Variables (to make the calls that follow work)
    hostname = 'www.python.org'
    item = 'spam'
    filename = 'data.csv'
    mode = 'r'

    # Example logging calls (insert into your program)
    logging.critical('Host %s unknown', hostname)
    logging.error("Couldn't find %r", item)
    logging.warning('Feature is deprecated')
    logging.info('Opening file %r, mode=%r', filename, mode)
    logging.debug('Got here')


if __name__ == '__main__':
    main()
