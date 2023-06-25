import logging
import colorlog
from os import getcwd
from os.path import exists

class Logger:
    '''
    CONSTRUCTOR
    '''
    def __init__(self) -> None:
        # Define the log message format
        self.message_format = "[%(asctime)s] [%(module)s] [%(log_color)s%(levelname)s%(reset)s] - %(message)s "
        # Define the color scheme for different log levels
        self.log_colors = {
            'DEBUG':    'cyan',
            'INFO':     'green',
            'WARNING':  'yellow',
            'ERROR':    'red',
            'CRITICAL': 'red,bg_white'
        }
        # Get the current absolute path
        self.current_path = getcwd()+'/'

    '''
    GETTERS
    '''
    @property
    def message_format(self):
        return self._message_format
    @property
    def log_colors(self):
        return self._log_colors
    @property
    def current_path(self):
        return self._current_path
    
    '''
    SETTERS
    '''
    @message_format.setter
    def message_format(self, value):
        self._message_format = value
    @log_colors.setter
    def log_colors(self, value):
        self._log_colors = value
    @current_path.setter
    def current_path(self, value):
        self._current_path = value

    '''
    METHODS
    '''
    def get_logger(self, filename='logger.log'):
        """
        Retrieves a logger object with color formatting and file logging.

        ### Args:
            filename (str, optional): Name of the log file. Defaults to 'logger.log'.

        ### Returns:
            logging.Logger: The configured logger object.
        """
        absolute_path = self.current_path+filename
        
        # Create a logger object
        logger = logging.getLogger(absolute_path)
        logger.setLevel(logging.DEBUG)

        # Create a handler and set the log level
        handler = logging.StreamHandler()
        handler.setLevel(logging.DEBUG)
        
        # Create a formatter object with the specified format and color scheme
        formatter = colorlog.ColoredFormatter(self.message_format, log_colors=self.log_colors)
        
        # Add the formatter to the handler
        handler.setFormatter(formatter)
        
        # Add the handler to the logger
        logger.addHandler(handler)
        
        # Configuration file
        # Message format file
        format_without_color = "[%(asctime)s] [%(module)s] [%(levelname)s] - %(message)s "
        
        # Create a file handler and set the log level
        fh = logging.FileHandler(absolute_path)
        fh.setLevel(logging.DEBUG)
        
        # Add the formatter to the handler
        fh.setFormatter(logging.Formatter(fmt=format_without_color))
        
        # Add the handler to the logger
        logger.addHandler(fh)
        
        return logger
