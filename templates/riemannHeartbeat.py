#!/usr/bin/env python
import bernhard
import time
import signal
import sys
import uuid


# Catching gracefully ctrl+c
def signal_handler(signal, frame):
    print "System down"
    sys.exit(0)
signal.signal(signal.SIGINT, signal_handler)

# Set hostname.
my_hostname = '{{ ansible_fqdn }}'

# Creating a default event.
event = {
    'host': str(my_hostname),
    'service': "Heartbeat",
}

# Starting a Riemann client.
client = bernhard.Client(host="{{ riemann_host }}")

while True:
#    print "Sending Heartbeat "
    client.send(event)
    time.sleep({{ interval }})
# print "System down"
