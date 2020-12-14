import os
import re
import json

loc = []

os.system("adb shell dumpsys location  | grep 'last location' > %s"%("data/data.txt"))
pattern = re.compile(r"(?<=k)(.*?)(?=h)")

for line in open("data/data.txt"):
    for match in re.findall(pattern, line):
        loc.append(match)
x = loc[0]
print(str(x).split(","))