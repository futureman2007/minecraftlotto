import os
import json
import threading

# you dont need trhead concurrency here... put process concurrency!
# see https://docs.python.org/3/library/multiprocessing.html for more details! Thread is not enough!

def clean_file_content_relative_path(relpath, filename):
    cur_path = os.path.dirname(__file__)
    lock = threading.Lock()
    with lock:
        file = os.path.join(cur_path, relpath + '/' + filename)
        with open(file, 'w') as file:
            file.truncate(0)

def clean_file_content_abs_path(abspath, filename):
    file = os.path.join(abspath, '/' + filename)
    lock = threading.Lock()
    with lock:
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
    lock = threading.Lock()
    with lock:
        file = os.path.join(abspath, '/' + filename)
        with open(file, 'w') as file:
            json.dump(filecontent,file)
    return True

def write_json_file_content_rel_path(relpath, filename, filecontent):
    lock = threading.Lock()
    with lock:
        cur_path = os.path.dirname(__file__)
        file = os.path.join(cur_path, relpath + '/' + filename)
        with open(file, 'w') as file:
            json.dump(filecontent, file)
    return True

def create_new_json_file_content_rel_path(relpath, filename, newContent={}):
    lock = threading.Lock()
    with lock:
        cur_path = os.path.dirname(__file__)
        file = os.path.join(cur_path, relpath + '/' + filename)
        with open(file, 'w') as file:
            file.truncate()
            json.dump(newContent, file)
    return True

def create_new_json_file_content_abs_path(abspath, filename, newContent={}):
    lock = threading.Lock()
    with lock:
        file = os.path.join(abspath, '/' + filename)
        with open(file, 'w') as file:
            file.truncate()
            json.dump(newContent, file)
    return True