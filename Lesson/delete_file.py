import os
import shutil
path = 'test.txt'

path = r'D:\UP Files\Python\Lesson\test.txt'

try:
    os.remove(path) #   To remove file
    # os.rmdir(path)    #   To remove folder
    shutil.rmtree(path) #   To remove folder with files on it
except FileNotFoundError:
    print("That file was not found")
except PermissionError:
    print("You do not have permission to delete that")
except OSError:
    print("You cannot delete that using that function")
else:
    print(f"{path} has been deleted successfully")