#!/usr/bin/env python

__author__ = "bt3"

import socket
import os
import struct
import ctypes
from ICMPHeader import ICMP
import coord_fetch
import app
from geopy.distance import great_circle
from requests import get

# host to listen on
HOST = '172.28.39.38'
coordarr = []
malarr = []

def main():
    # type: () -> object
    socket_protocol = socket.IPPROTO_ICMP
    sniffer = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket_protocol)
    sniffer.bind((HOST, 0))
    sniffer.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)

    myIP = get('https://api.ipify.org').text

    print myIP
    myCoord = coord_fetch.ipinfo(myIP)
    print myCoord

        # continually read in packets and parse their information
    while 1:
        # read in a packet and pass the first 20 bytes to initialize the IP structure
        raw_buffer = sniffer.recvfrom(55056)[0] #original: 65565

        # take first 20 characters for the ip header
        ip_header = raw_buffer[0:20]

        # unpack them
        iph = struct.unpack('!BBHHHBBH4s4s', ip_header)

        # print
        version_ihl = iph[0]
        version = version_ihl >> 4
        ihl = version_ihl & 0xF
        iph_length   = ihl * 4
        ttl = iph[5]
        protocol = iph[6]
        s_addr = socket.inet_ntoa(iph[8]);
        d_addr = socket.inet_ntoa(iph[9]);
        ip = str(s_addr)

        # print 'IP -> Version:' + str(version) + ', Header Length:' + str(ihl) + \
        #       ', TTL:' + str(ttl) + ', Protocol:' + str(protocol) + ', Source:' \
        #       + str(s_addr) + ', Destination:' + str(d_addr)

        # create our ICMP structure
        buf = raw_buffer[iph_length:iph_length + ctypes.sizeof(ICMP)]
        icmp_header = ICMP(buf)

        #print "ICMP -> Type:%d, Code:%d" % (icmp_header.type, icmp_header.code) + '\n'

        #return str(s_addr)
        thisCoord = coord_fetch.ipinfo(ip)
        print thisCoord

        if 'undefined' not in thisCoord:
            if thisCoord not in coordarr:
                coordarr.append(thisCoord)
                #app.showMap(coordarr)
                myDistance = great_circle(myCoord, thisCoord).miles
                print 'Distance: %s' % myDistance

                if myDistance > 25:
                    malarr.append(thisCoord)
                    print "malarr: %s" % malarr
                    print "coordarr: %s" % coordarr
                    #app.showmap(coordarr, malarr)
                print coordarr

        if len(coordarr) > 5:
            return coordarr, malarr

if __name__ == '__main__':
     main()
