#!/bin/python3

import os
import sys

if len(sys.argv) != 2:
    print(f"Usage: {sys.argv[0]} ip_responder")
    exit(1)

for file in os.listdir("./template"):
    open("out/"+file,"w").write(open("./template/"+file,"r").read().replace("CHEVALOPKTPARTIE",sys.argv[1]))