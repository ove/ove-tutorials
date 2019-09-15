#!/usr/bin/env python

#copied from https://stackoverflow.com/a/166589

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
try:
  s.connect(("8.8.8.8", 80))
  ip = s.getsockname()[0]
except:
  ip = '127.0.0.1'
finally:
  s.close()
print(ip)

