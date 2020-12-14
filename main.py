import os
import re
import json
from lib.utm import Convert_LL2UTM

loc = []

os.system("adb shell dumpsys location  | grep 'last location' > %s"%("data/data.txt"))
pattern = re.compile(r"(?<=k)(.*?)(?=h)")

for line in open("data/data.txt"):
    for match in re.findall(pattern, line):
        loc.append(match)
x = loc[0]
# print(str(x).split(","))
utms = Convert_LL2UTM(str(x).split(","))
print(utms)