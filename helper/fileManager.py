import os
import json
import threading
import multiprocessing
import shutil
# you dont need trhead concurrency here... put process concurrency!
# see https://docs.python.org/3/library/multiprocessing.html for more details! Thread is not enough!

#TODO: add exception handling for PermissionError: [Errno 13] Permission denied: '/testfile1.txt' (writing to file)


def append_content_to_file(srcpath, srcfilename, content, useRaltivePath=False):
    file = None
    appendReturn = None
    processlock = multiprocessing.Lock()
    threadlock = threading.Lock()

    if(useRaltivePath):
        with processlock:
            with threadlock:
                cur_path = os.path.dirname(__file__)
                file = os.path.join(cur_path, srcpath +  '/' + srcfilename)
                with open(file, 'a') as file:
                    appendReturn = file.write(content)
    else:    
        with processlock:
            with threadlock: 
                file = os.path.normpath(srcpath + '/' + srcfilename)
                with open(file, 'a') as file:
                    appendReturn = file.write(content)

    return appendReturn


def copy_existing_file_and_clean_srcfile(path, filename, destpath, destfilename, useRelativePath=False):
    returnAfterCopy = copy_existing_file(path, filename, destpath, destfilename, useRelativePath)
    print("DEBUG: Copy returned: " + returnAfterCopy)
    
    if (useRelativePath):
        clean_file_content_relative_path(path, filename)
    else:
        clean_file_content_abs_path(path, filename)
    


def copy_existing_file(path, filename, destpath, destfilename, useRelativePath=False):
    cur_path = os.path.dirname(__file__)
    processlock = multiprocessing.Lock()
    threadlock = threading.Lock()
    returnAfterCopy = None
    with processlock:
        with threadlock:
            if (useRelativePath is True):
                returnAfterCopy = shutil.copy(os.path.normpath(cur_path + '/' + path + '/' + filename, cur_path + '/' + destpath + '/' + destfilename))
                
            else:
                returnAfterCopy = shutil.copy(path + '/' + filename, destpath + '/' + destfilename)             
    return returnAfterCopy

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
    file = os.path.normpath(abspath + '/' + filename)
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