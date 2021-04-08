try:
  import usocket as socket
except:
  import socket

from machine import Pin
import network, time

import esp

esp.osdebug(None)

import gc
gc.collect()
