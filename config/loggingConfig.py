import logging
from config.const import logFileName


class Formatter(logging.Formatter):

    default_format = "%(asctime)s\t[%(levelname)-5.5s]:\t%(message)s"
    error_format = '\t--> Occured in "%(pathname)s":%(lineno)s'

    def __init__(self, fmt=None):
        if fmt is None:
            fmt = self.default_format
        super().__init__(fmt, style="%")

    def format(self, record):
        # Save the original format when instantiated
        format_original = self._style._fmt

        if record.levelno >= logging.ERROR:
            self._style._fmt += self.error_format

        # Calls the original formatter class to format
        result = logging.Formatter.format(self, record)

        # Restore the original format
        self._style._fmt = format_original
        return result


logFormatter = Formatter()
rootLogger = logging.getLogger()

fileHandler = logging.FileHandler("{0}/{1}.log".format(".", logFileName))
fileHandler.setFormatter(logFormatter)
rootLogger.addHandler(fileHandler)
rootLogger.setLevel(logging.DEBUG)
