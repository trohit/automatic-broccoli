#!/usr/bin/env python
# Client side Utility to create script to generate ip aliases
# creates IPs from 1.1.1.[1-100]
#
# On the server side, need to add a return route like
# route add -net 1.1.1.0 netmask 255.255.255.0 gw 172.17.0.57
# where 172.17.0.57 is the primary ip address of the server

fgood = open('iplist.txt','w')
fbad = open('badiplist.txt','w')
ifconfig = open('ifconfig.sh', 'w')
i = 1 
while i < 101:
    cmd = 'ifconfig eth0:' + str(i) + ' 1.1.1.' + str(i) + '/8 up'
    syn_ip = '1.1.1.' + str(i)
    ifconfig.write(cmd + '\n')
    #print(cmd)
    if i < 10: 
        fgood.write(syn_ip + '\n')
    else:
        fbad.write(syn_ip + '\n')

    i = i + 1 
