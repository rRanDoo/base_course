import sys, os

print(os.getcwd())

os.system("echo hi!")

# os.system("python3 dop_func/14_sys_os.py")
print("Python version is:", sys.version)
print(sys.path)
print(sys.platform)

print(dir(sys))
print(dir(os))