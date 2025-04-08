import os
import shutil

os.mkdir("newdir")
shutil.copy("olddir/file.txt", "newdir/file.txt")
