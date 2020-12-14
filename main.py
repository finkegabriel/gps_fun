import os
import json

os.system("adb shell dumpsys location > %s"%("data/data.txt"))