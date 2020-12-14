import os
import re
import json
from lib.utm import Convert_LL2UTM as utm

loc = []
stringMe = "Gnss"
#| grep 'last location'
os.system("adb shell dumpsys location | grep %s  > %s"%(stringMe,"data/data.txt"))
latPat = re.compile(r"(?<=LatitudeDegrees:)(.*?)(?=,)")
lonPat = re.compile(r"(?<=LongitudeDegrees:)(.*?)(?=,)")

for line in open("data/data.txt"):
    for match in re.findall(latPat, line):
        loc.append(match)

for lines in open("data/data.txt"):
    for matchs in re.findall(lonPat,lines):
        loc.append(matchs)
x = loc
print(x)
utms = utm(x)
print("easting ",utms[2]," northing ",utms[3])