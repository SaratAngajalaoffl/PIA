import sys as system
import os

Directory = system.argv[1]
ProjectName = system.argv[2]

if Directory == '-l':
    print("Changed directory to learning")
    os.system('cd d:/Academics/Learning/test_runs/')
elif Directory == '-p':
    print("Changed directory to Projects")
    os.system('cd D:/Academics/Projects/')
    os.system('dir')

os.system('mkdir ' + ProjectName)
os.system('cd ' + ProjectName)
# os.system('code .')

