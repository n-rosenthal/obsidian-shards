import logging, logging.handlers, logging.config
import os, sys, time, traceback
import json
import gzip

from pathlib import Path
from datetime import datetime
from colorama import Fore, Back, Style, init, Cursor, deinit

from settings import __all__ as settings
version, author, description = settings["__version__"], settings["__author__"], settings["__description__"];

class ContextFilter(logging.Filter):
    """
        Contextual information for logs.
    """
    def __init__(self, app_name: str, environment: str, version: str, author: str):
        super().__init__();
        self.app_name, self.environment, self.version, self.author = app_name, environment, version, author;
        
    def filter(self, record):
        """
            Contextual information for logs.
        """
        record.app_name = self.app_name;
        record.env = self.environment;
        record.version = self.version;
        return True;