## please see https://fangpenlin.com/posts/2012/08/26/good-logging-practice-in-python/
import logging
import logging.config
import yaml
import os


class infoFilter(logging.Filter):
    def filter(self, log_record):
        return log_record.levelno == logging.INFO


class warningErrorCriticalFilter(logging.Filter):
    def filter(self, log_record):

        if log_record.levelno in {logging.WARNING, logging.ERROR, logging.CRITICAL}:
            return True
        else:
            return False


class Log:
    class __Log:
        def __init__(self, dir_name: str = "log", file_name: str = "logging.yaml", name=__name__, default_level: int = logging.INFO):
            if not os.path.exists(dir_name):
                os.makedirs(dir_name)
            if os.path.exists(file_name):
                with open(file_name, 'rt') as f:
                    config = yaml.safe_load(f.read())
                logging.config.dictConfig(config)
            else:
                logging.basicConfig(level=default_level)

            self.logger = logging.getLogger(name)
            self.logger.info("Configured the logger!")

        def get(self):
            return self.logger

    log = __Log()

    @staticmethod
    def get():
        return Log.log.get()
