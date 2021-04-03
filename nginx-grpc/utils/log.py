# coding:utf-8
import os
import logging
from logging.handlers import RotatingFileHandler


BASE_DIR = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))


class Logger(object):
    def __init__(self, name, filename, level):
        self.logger = logging.getLogger(name)
        self.log_level = level
        self.logger.setLevel(level)
        self.formatter = logging.Formatter('%(asctime)s %(name)s %(levelname)s %(message)s')
        self.add_console_handler()
        self.add_file_handler(filename)

    def add_console_handler(self):
        console = logging.StreamHandler()
        console.setLevel(self.log_level)
        console.setFormatter(self.formatter)
        self.logger.addHandler(console)

    def add_file_handler(self, filename):
        parent_dir = os.path.join(BASE_DIR, 'log')
        if not os.path.exists(parent_dir):
            os.makedirs(parent_dir)

        fp = os.path.join(parent_dir, filename)
        fh = RotatingFileHandler(filename=fp, maxBytes=10*1024*1024, backupCount=10)
        fh.setLevel(self.log_level)
        fh.setFormatter(self.formatter)
        self.logger.addHandler(fh)


def get_logger(name):
    logger = Logger(name, filename='helloworld.log', level=logging.INFO).logger
    return logger

logger = get_logger(__name__)
logger.info('test')
logger.error('error')
