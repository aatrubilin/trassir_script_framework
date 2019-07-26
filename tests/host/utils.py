import os
import random
import string
import sys


def try_to_find_t1script_event():
    if "AB_HOME" in os.environ:
        utils_location = os.environ["AB_HOME"]  # /some/path/to/trassir/tech1utils/ab
        sources_dir = cd_to_parent(utils_location, 2)  # /some/path/to/trassir
        t1script_dir = os.path.join(sources_dir, "tech1script")
        if os.path.exists(t1script_dir):
            if 'LD_LIBRARY_PATH' in os.environ and os.environ['LD_LIBRARY_PATH']:
                os.environ['LD_LIBRARY_PATH'] = t1script_dir + ":" + os.environ['LD_LIBRARY_PATH']
            else:
                os.environ['LD_LIBRARY_PATH'] = t1script_dir
            sys.path.append(t1script_dir)
        else:
            print "Can not find path to tech1script (tried: {})".format(t1script_dir)
    else:
        print "No AB_HOME in environ"


def secs_to_usecs(seconds):
    return seconds*1000000


def cd_to_parent(path, level):
    for _ in range(level):
        path = os.path.dirname(path)
    return path


def compare_text_files(file_path_1, file_path_2):
    try:
        with open(file_path_1, 'r') as f_in:
            text_data_1 = f_in.readlines()
        with open(file_path_2, 'r') as f_in:
            text_data_2 = f_in.readlines()
        return text_data_1 == text_data_2
    except IOError as e:
        print 'Unable to compare text files. %s' % str(e)
        return False

 # Some dirtiness for checking only one arg in mock
def any(cls):
    class Any(cls):
        def __eq__(self, other):
            return True
    return Any()


def generate_random_guid():
    return "".join([random.choice(string.letters + string.digits) for _ in range(8)])
