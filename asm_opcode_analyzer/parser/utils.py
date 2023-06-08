import os


def get_absolute_path():
    """Get the absolute path of the current directory"""
    abs_path = str(os.getcwd())
    if 'Parser' not in abs_path:
        abs_path += '/Parser'
    return abs_path
