import os
import re
import json
from lib.utm import Convert_LL2UTM as utm

loc = []
stringMe = "fused"
#| grep 'last location'
# os.system("adb shell dumpsys location > %s"%("data/ex.txt"))

def gps_call():
    while True:
        os.system("adb shell dumpsys location | grep %s  > %s"%(stringMe,"data/data.txt"))
        latPat = re.compile(r"(?<=d)(.*?)(?=h)")
        # lonPat = re.compile(r"(?<=LongitudeDegrees:)(.*?)(?=,)")

        for line in open("data/data.txt"):
            for match in re.findall(latPat, line):
                loc.append(match)
        x = loc[1]
        print(x.split(','))
        # for lines in open("data/data.txt"):
        #     for matchs in re.findall(lonPat,lines):
        #         print(match,matchs)
                # loc.append(matchs)
            # x = loc
            # print(loc)
            # print(x)    
            # utms = utm(x)
    # print("easting ",utms[2]," northing ",utms[3])

gps_call()