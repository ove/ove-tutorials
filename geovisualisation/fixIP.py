#!/usr/bin/env python

import os, sys

if len(sys.argv) < 2:
    print("usage: python -m %s <IP>" % os.path.basename(sys.argv[0]).split('.')[0])
else:
    ip = sys.argv[1]
    try:
        i = open("crime_map_config_original.json","r")
        o = open("crime_map_config.json","w")
        for line in i:
            o.write(line.replace("localhost", ip))
    finally:
        i.close()
        o.close()

    try:
        i = open("roads_map_config_original.json","r")
        o = open("roads_map_config.json","w")
        for line in i:
            o.write(line.replace("localhost", ip)) 
    finally:
        i.close()
        o.close()
