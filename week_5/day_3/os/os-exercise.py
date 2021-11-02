# The Os Module
# This module provides functions that wrap operating system functionality, manipulate 
# files, for example (the os module is relatively low level, for high-level operations on file and directory handling, see the shutil module).

# It contains information about your operating system, for example, the name of your 
# OS (os.name), the current working directory (os.getcwd()) 
# and even environment variables (os.environ).



# Manipulating FHiles And Dirs
# The os module provide a lot of functions to manipulate your files and directories,
#  starting by listing them: you can use the os.scandir(directory) to get a 
# list of all the entries in a directory, or the os.walk(directory) to list files
#  recursively (diving into every directory).

# You can also create directories (os.mkdir for a single directory or os.makedirs 
# for multiple folders), rename directories with os.rename or remove them with os.remove and os.removedirs.

import os

print(os.name)
print(os.getcwd())
print(os.environ)

#os.path.join add the os relevant DIRECTORY SEPARATOR between its arguments
#os makedirs create directories with all the intermediate directores
#while os.mkdir will create an error if it gets dir1/dir2 and dir1 doesnt exist already
dir_3_path = os.path.join('dir1','dir2','dir3')
is_dir_3_exists = os.path.exists(dir_3_path)
try:
     os.makedirs(dir_3_path)
except FileExistsError:
    print("Dir already Exists")

dir_5_path = os.path.join('dir1','dir2','dir3','dir4','dir5')
try:
  os.mkdir(dir_5_path) 
except FileExistsError:
    print("File already exists!")
except FileNotFoundError:
    print("An exception occurred - FILE NOT FOUND")


def is_path_or_file(path):
    if os.path.isfile(path):
        print("File")
    elif os.path.isdir(path):
        print("Folder")
    else:
        print("unknown")

is_path_or_file(dir_3_path)
dir_1_dir1file_path = os.path.join('dir1','dir1file.txt')
is_path_or_file(dir_1_dir1file_path)

print(os.path.abspath(dir_1_dir1file_path))
print(os.path.basename(os.path.abspath(dir_1_dir1file_path)))

print(os.path.dirname(os.path.dirname(os.path.dirname(dir_5_path))))

print(os.path.splitext(dir_1_dir1file_path))

# Manipulate Files Names And Paths
# One of the most interesting modules of os is the os.path module,
#  it allow you to manipulates files names and paths. For example given a file name:

# you can check if it exists with os.path.exists(filename)

# and if it’s a file or a directory (os.path.isfile and os.path.isdir),

# you can retrieve his absolute path with os.path.abspath(filename),

# or do the opposite with os.path.basename(abspath),

# or even retrieve the name of its parent directory with os.path.dirname.

# You can also combine two paths with os.path.join(dir, file)

# or get the extension of a file with os.path.splitext(filename).
# For higher-level path functions, see the pathlib module.

