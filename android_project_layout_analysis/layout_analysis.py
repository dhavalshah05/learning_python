import os
from layout_parser import LayoutParser


# cwd = os.getcwd()
cwd = "../../../hl_android_workspace/sugarfree"
os.chdir(f"{cwd}/app/src/main/res/layout")
dirs = os.listdir()

dic = {}
for file_name in dirs:
    LayoutParser(file_path=file_name, counter=dic)

print(sorted(dic.items(), key=lambda item: item[1], reverse=True))







