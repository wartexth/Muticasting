#
# mostly copied from
#   http://bioportal.weizmann.ac.il/course/python/PyMOTW/PyMOTW/docs/socket/multicast.html
#

import socket
import struct
import sys
import time
import json

values = {'hostname': 'Morten',
		  'resolutionon': ['1920x480'],
		  'capabibility': ['png']}

message = json.dumps( values, sort_keys=True, indent=4, separators=(',', ': '))

#message = "Hostname: \tCam_of_Cham \nResolution: \t1920x1080 , 640x480 \nCapabibility: \tpng, jpeg , avi , mp4" 	 
multicast_group = ('224.3.29.71', 10000)

# Create the datagram socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Set a timeout so the socket does not block indefinitely when trying
# to receive data.
sock.settimeout(0.2)

counter = 0

try:
    
    while True:
        counter +=1

        # Send data to the multicast group
        print >>sys.stderr, '%d: sending "%s"' % (counter, message )
        sent = sock.sendto(message, multicast_group)
        
        time.sleep( 5 )
    
finally:
    print >>sys.stderr, 'closing socket'
    sock.close()
