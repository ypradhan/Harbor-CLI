import os
from functools import wraps

from lib.exceptions.FileNotFound import FileNotFoundException
from lib.exceptions.DirNotFound import DirNotFoundException

def requires_presence_of_file(file_path):
    ''' Decorator to verify if a file exists before doing anything else. '''
    def wrapper(f):
        @wraps(f)
        def with_args(*args, **kwargs):
            if not os.path.isfile(file_path):
                raise FileNotFoundException(file_path)

            return f(*args, **kwargs)
        return with_args
    return wrapper


def requires_presence_of_dir(dir_path):
    ''' Decorator to verify if a file exists before doing anything else. '''
    def wrapper(f):
        @wraps(f)
        def with_args(*args, **kwargs):
            if not os.path.isdir(dir_path):
                raise DirNotFoundException(dir_path)

            return f(*args, **kwargs)
        return with_args
    return wrapper


def with_additional_kwargs(**additional_kwargs):
    '''
    Injects additional kwargs into the kwargs of the original func.
    Useful for injecting credentials/sensitive information into the function.
    '''
    def wrapper(f):
        @wraps(f)
        def inner(*args, **kwargs):
            kwargs.update(additional_kwargs)
            return f(*args, **kwargs)
        return inner
    return wrapper
