from os import listdir,rename
from sys import argv

self = argv[0]
prefix = argv[1].strip()

for filename in listdir("."):
    if filename.startswith("."):
        continue
    if filename in self:
        continue
    print(filename)
    rename(filename, prefix+filename)

