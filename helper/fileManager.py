from asyncio.windows_events import NULL
from concurrent.futures import process
import os
import json
import threading
import multiprocessing
import shutil
# you dont need trhead concurrency here... put process concurrency!
# see https://docs.python.org/3/library/multiprocessing.html for more details! Thread is not enough!

def copy_existing_file(path, filename, destpath, destfilename, useRelativePath=False):
    cur_path = os.path.dirname(__file__)
    processlock = multiprocessing.Lock()
    threadlock = threading.Lock()

    with processlock:
        with threadlock:
            if (useRelativePath is True):
                shutil.copy(cur_path + '/' + path + '/' + filename, cur_path + '/' + destpath + '/' + destfilename)
            else:
                shutil.copy(path + '/' + filename, destpath + '/' + destfilename)


def clean_file_content_relative_path(relpath, filename):
    cur_path = os.path.dirname(__file__)
    
    processlock = multiprocessing.Lock()
    threadlock = threading.Lock()
    with processlock:
        with threadlock:
            file = os.path.join(cur_path, relpath + '/' + filename)
            with open(file, 'w') as file:
                file.truncate(0)

def clean_file_content_abs_path(abspath, filename):
    file = os.path.join(abspath, '/' + filename)
    processlock = multiprocessing.Lock()
    threadlock = threading.Lock()
    with processlock:
        with threadlock:
            with open(file, 'w') as file:
                file.truncate(0)

def load_file_content_relative_path(relpath, filename):
    cur_path = os.path.dirname(__file__)
    file = os.path.join(cur_path, relpath + '/' + filename)

    with open(file, 'r') as file:
        file_content = file.read()
    return file_content

def load_file_content_abs_path(abspath, filename):
    file = os.path.join(abspath, '/' + filename)
    with open(file, 'r') as file:
        file_content = file.read()
    return file_content

def load_file_content_relative_path_json(relpath, filename):
    cur_path = os.path.dirname(__file__)
    file = os.path.join(cur_path, relpath + '/' + filename)
    with open(file, 'r') as file:
        file_content = json.load(file)
    return file_content

def load_file_content_abs_path_json(abspath, filename):
    file = os.path.join(abspath, '/' + filename)
    with open(file, 'r') as file:
        file_content = json.load(file)
    return file_content

def write_json_file_content_abs_path(abspath, filename, filecontent):
    processlock = multiprocessing.Lock()
    threadlock = threading.Lock()
    with processlock:        
        with threadlock:
            file = os.path.join(abspath, '/' + filename)
            with open(file, 'w') as file:
                json.dump(filecontent,file)
    return True

def write_json_file_content_rel_path(relpath, filename, filecontent):
    threadlock = threading.Lock()
    processlock = multiprocessing.Lock()
    with processlock:
        with threadlock:
            cur_path = os.path.dirname(__file__)
            file = os.path.join(cur_path, relpath + '/' + filename)
            with open(file, 'w') as file:
                json.dump(filecontent, file)
    return True

def create_new_json_file_content_rel_path(relpath, filename, newContent={}):
    threadlock = threading.Lock()
    processlock = multiprocessing.Lock()
    with processlock:
        with threadlock:
            cur_path = os.path.dirname(__file__)
            file = os.path.join(cur_path, relpath + '/' + filename)
            with open(file, 'w') as file:
                file.truncate()
                json.dump(newContent, file)
    return True

def create_new_json_file_content_abs_path(abspath, filename, newContent={}):
    threadlock = threading.Lock()
    processlock = multiprocessing.Lock()
    with processlock:
        with threadlock:
            file = os.path.join(abspath, '/' + filename)
            with open(file, 'w') as file:
                file.truncate()
                json.dump(newContent, file)
    return True