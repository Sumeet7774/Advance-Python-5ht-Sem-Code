# import os

# for i in range(0,100):
#     # os.mkdir(f"/Advance Python/Lecture Codes/Empty/advance_python{i}")
#     os.mkdir(f"advance_python{i}")
    

# cwd = os.getcwd()
# print("Current working directory: ", cwd)


# os.chdir("/Advance Python/Lecture Codes/Empty")
# print("Changed directory to: ", os.getcwd())


# files_and_dirs = os.listdir()
# print("FIles and directories: ", files_and_dirs)


# cwd = os.getcwd()
# files=[]
# directories=[]

# for item in os.listdir(cwd):
#     if os.path.isfile(item):
#         files.append(item)
#     elif os.path.isdir(item):
#         directories.append(item)
        
# print("files:", files)
# print("Directories:", directories)

# import shutil

# shutil.move("temp.txt","destination")


# from pathlib import Path

# path = Path("/Advance Python/Lecture Codes/Empty/abc.txt")

# path.mkdir(parents=True,exist_ok=True)
# print(f"Directory{path} created")


# import logging

# logging.basicConfig(level=logging.DEBUG)
# logging.debug("This is a debug msg")
# logging.info("Module 1 completed and module start")
# logging.warning("This is a warning msg")
# logging.error("This is a error msg")
# logging.critical("This is a crictical msg")