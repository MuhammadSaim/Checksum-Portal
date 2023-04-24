import hashlib, os
from werkzeug.utils import secure_filename
from datetime import datetime


def hash_file(filename):
    """"This function returns the SHA-1 hash
   of the file passed into it"""

    # make a hash object
    h = hashlib.sha1()

    # open file for reading in binary mode
    with open(filename, 'rb') as file:
        # loop till the end of the file
        chunk = 0
        while chunk != b'':
            # read only 1024 bytes at a time
            chunk = file.read(1024)
            h.update(chunk)

    # return the hex representation of digest
    return h.hexdigest()


def get_filename(filename):
    filename = secure_filename(filename)
    name, extension = os.path.splitext(filename)
    new_file_name = name+'_'+str(int(datetime.now().timestamp()))+extension
    return new_file_name, extension
