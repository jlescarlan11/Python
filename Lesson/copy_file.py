"""
copyfile()  =   copies contents of a file
copy()      =   copyfile() + permission mode + destination can be a directory
copy2()     =   copy() + copies metadata (file's creation and modification times)
"""

import shutil

shutil.copyfile(r'D:\UP Files\Python\Lesson\test.txt', r'D:\UP Files\Python\Lesson\copy.txt')   #   src, dst





