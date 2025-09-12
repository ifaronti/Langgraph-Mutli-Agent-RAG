import os


def file_path(path:str)->str:

    if not os.path.isdir(path):
        return "The path does not exist"
    
    return path