#
# mostly from
#   http://bioportal.weizmann.ac.il/course/python/PyMOTW/PyMOTW/docs/socket/multicast.html
#

import socket
import struct
import sys
import json
import datetime

multicast_group = '224.3.29.71'
server_address = ('', 10000)

# Create the socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind to the server address
sock.bind(server_address)

# Tell the operating system to add the socket to the multicast group
# on all interfaces.
group = socket.inet_aton(multicast_group)
mreq = struct.pack('4sL', group, socket.INADDR_ANY)
sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)

devices = {}

# Receive/respond loop
while True:
	#print >>sys.stderr, '\nwaiting to receive message'
    data, address = sock.recvfrom(1024)
    
    try:
    	date = datetime.datetime.now() 
    	parsedDate = json.loads( data )
    	print >> sys.stderr, date, parsedDate
    except:
		print >> sys.stderr, "failed to decode from " %(address, )


    #	print >> sys.stderr
    #print >>sys.stderr, 'received %s bytes from %s' % (len(data), address)
    print >>sys.stderr, ""


