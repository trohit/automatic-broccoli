# A bunch of nifty utility  functions to use in python
import netifaces
import requests
import datetime
import json
import sys
import pymongo
import pprint
import os
import glob
import logging
import time
import math
import subprocess
import re
import ConfigParser
import socket
import shutil
import random 

import code
#code.interact(local=locals())
import pdb
# pdb.set_trace()

def write_list_to_file(file_name, list_name):
    thefile = open(file_name, 'w')
    for item in list_name:
        thefile.write("%s\n" % item)
    
# sums up all the elements in a list that matches 'field'
# and returns the total     
def sum_list_dict(ll, field):
    mysum = 0
    for i in xrange(len(ll)):
        #print(type(ll[i]['count']))
        #code.interact(local=locals())        
        mysum += ll[i]['count']
    return mysum

# returns rows and cols
def get_screen_size():
    rows, columns = os.popen('stty size', 'r').read().split()
    return (rows, columns)

# draws a line
def drawline(cols=0):
    if cols == 0:
        (_, cols) = get_screen_size()  
    # alternatively
    # print u"\u2501"
    # https://en.wikipedia.org/wiki/Box-drawing_character
    #print unichr(0x2501) * int(cols)
    print '-' * int(cols)
    

# TODO: can go in a seperate file as a module
# print bcolors.WARNING + "Warning: No active frommets remain. Continue?" + bcolors.ENDC
# print bcolors.OKBLUE + 'Test is over' + bcolors.ENDC
# print bcolors.FAIL + 'root perms needed' + bcolors.ENDC
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

# accepts a datetime.timedelta
# time_delta_to_str(8640)
# '2:24:0'
def time_delta_to_str(diff):
    s = diff.seconds
    #s = 13420
    
    hours, remainder = divmod(s, 3600)
    minutes, seconds = divmod(remainder, 60)
    #print '%s:%s:%s' % (hours, minutes, seconds)
    res_str = ''
    if hours:
        res_str += str(hours) + ' hours'
    if minutes:
        res_str += ' ' + str(minutes) + ' mins'
    if seconds:
        res_str += ' ' + str(seconds) + ' secs'
    return res_str    
    #return '%s hours:%s mins:%s seconds' % (hours, minutes, seconds)


# returns date and time in the present
# eg. 2016_09_08_13
def get_date_time_human_readable():
    #return str(datetime.datetime.now().strftime('%Y_%m_%d_%H_%M:%S'))
    return str(datetime.datetime.now().strftime('%Y_%m_%d_%H_%M'))


# expects an array of dicts
# merges array elements with the same key
# Input :
# l = [{u'count': 8, u'user_agent': u'CHROME44'},
#      {u'count': 10, u'user_agent': u'OPERA10'},
#      {u'count': 5, u'user_agent': u'FIREFOX21'},
#      {u'count': 9, u'user_agent': u'DOWNLOAD'},
#      {u'count': 18, u'user_agent': u'UNKNOWN'},
#      {u'count': 6, u'user_agent': u'SAFARI5'}]
#
# merge_list_on_key(l, 'user_agent']) 
# #merges on user_agent UNKNOWN
#
# Output:
# {'SAFARI5': 6, 'CHROME44': 8, 'UNKNOWN': 18, 'OPERA10': 10, 'FIREFOX21': 5, 'DOWNLOAD': 9}
#
def merge_list_on_key(l1, key):
    s1 = set()
    lz = list()
    for i in l1:
        if i[key] not in s1:
            s1.add(i[key])
            lz.append(i)
        else:
            for l in lz:
                if l[key] == i[key]:
                    l['count'] += i['count']
    return lz

# returns True if lists match
# else returns False
def is_list_equal(l1, l2):
    s1 = set(l1)
    s2 = set(l2)
    if s1 == s2:
        #print('sets match')
        return True
    else:
        #print('sets dont match')
        return False
def sleep_sensible():
    print(date_str() + 'Sleeping for ' + str(knob_sleep_sensible) + ' seconds')
    time.sleep(knob_sleep_sensible)
    print(date_str() + 'Resuming...')
    
def sleep_seconds(secs = 10):
    print(date_str() + 'Sleeping for ' + str(secs) + ' seconds')
    time.sleep(secs)
    print(date_str() + 'Resuming...')
    
# creates a directory if it does not exist
def ensure_dir(directory):
    if not os.path.exists(directory):
        print(date_str() + 'creating directory ' + directory)
        os.makedirs(directory)

# rounds a value to the next nearest multiple of 10. 
# roundup_to_nearest_ten(1) = 10
# roundup_to_nearest_ten(10) = 10
# roundup_to_nearest_ten(11) = 20
def roundup_to_nearest_ten(x):
    return int(math.ceil(x / 10.0)) * 10

# rounds a value to the previous nearest multiple of 10. 
# rounddown_to_nearest_ten(1) = 0
# rounddown_to_nearest_ten(9) = 0
# rounddown_to_nearest_ten(10) = 0
def rounddown_to_nearest_ten(x):
    return int(math.floor(x / 10.0)) * 10

# think of it as py_time_round_later
# typically done with the end time
def py_time_round_up(tm):
    upmins = math.ceil(float(tm.minute)/10)*10
    diffmins = upmins - tm.minute
    newtime = tm + datetime.timedelta(minutes=diffmins)
    newtime = newtime.replace(second=0)
    return newtime

# think of it as py_time_round_earlier
# typically done with the start time
def py_time_round_down(tm):
    upmins = math.floor(float(tm.minute)/10)*10
    diffmins = upmins - tm.minute
    newtime = tm + datetime.timedelta(minutes=diffmins)
    newtime = newtime.replace(second=0)
    return newtime

# checks if the program has root permissions
def is_sudo():
    if os.getuid() == 0:
        #print("root perms acquired")
        return True
    else:
        #print("I cannot run as a mortal. Sorry.")
        return False


# class that adds a fake section to c ofnig file
class FakeSecHead(object):
    def __init__(self, fp):
        self.fp = fp
        self.sechead = '[asection]\n'

    def readline(self):
        if self.sechead:
            try: 
                return self.sechead
            finally: 
                self.sechead = None
        else: 
            return self.fp.readline()

# reads all the important config into a dict 
def read_config_file_without_sections(file_path):
    cp = ConfigParser.SafeConfigParser()
    #cp.readfp(FakeSecHead(open('/home/rohit/Downloads/somefile.json')))
    cp.readfp(FakeSecHead(open(file_path)))

    #print cp.items('asection')
    #print(type(cp.items('asection')))
    
    # convert from a two tuple list into a dict
    dd = dict( cp.items('asection'))
    #print(dd)
    return dd

###############################################################################
# Networking utils
###############################################################################


def is_port_open_local(port):
    popen = subprocess.Popen(['netstat', '-lpn'],
                             shell=False,
                             stdout=subprocess.PIPE)
    #(data, err) = popen.communicate()
    (data, _) = popen.communicate()
    patt = '^tcp.*((?:' + str(port) + ')).* (?P<pid>[0-9]*)/.*'
    p = re.compile(patt)

    for line in data.split('\n'):
        match = re.match(p, line)
        if match:
            #pid = match.group('pid')
            #print('found pid ' + str(pid))
            return True
    return False

def find_pid_by_port(port):
    popen = subprocess.Popen(['netstat', '-lpn'],
                             shell=False,
                             stdout=subprocess.PIPE)
    #(data, err) = popen.communicate()
    (data, _) = popen.communicate()


    patt = '^tcp.*((?:' + str(port) + ')).* (?P<pid>[0-9]*)/.*'
    print(patt)
    p = re.compile(patt)

    for line in data.split('\n'):
        match = re.match(p, line)
        if match:
            pid = match.group('pid')
            #print('found pid ' + str(pid))
            return pid
    return 0


def are_all_ports_open(host, port_dict):
    # convert dict of ports into a list and string it
    str_port_list = [str(i) for i in port_dict.values()]
    
    for check_port in str_port_list:
#         print('converting portstr ' + check_port + ' to int')
        check_port = int(check_port)
        if is_port_open(host, check_port) == False:
            return False
    return True
     
# checks if a port is open on a host
#     host is string
#     port is a number
# returns true if port is open, else returns false 
# ex.
#     result = is_port_open('127.0.0.1', 80)
def is_port_open(host, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = sock.connect_ex((host, port))
    if result == 0:
#         print host + ':' + str(port) + ' is open'
        return True
    else:
        print host + ':' + str(port) + ' is not open'
        popen = subprocess.Popen(['netstat', '-tlpn'],
                    shell=False,
                    stdout=subprocess.PIPE)
        #(data, err) = popen.communicate()
        (data, _) = popen.communicate()
        print(data)

        return False    

# sends n requests
# returns the total number of requests sent 
def send_request_n_times(method, url, user_agent_str, repetitions = 10):
    #url = "http://localhost/atm/zipcode"
    header_dict = dict()
    header_dict['User-Agent'] = user_agent_str
    
    iterations = int(repetitions)
    #print("Sending " + iterations + " requests")
    for _ in range(iterations):
        # response is returned and is unused  
        _ = requests.request(method, url, headers=header_dict)
        #print(response.text)
    # housekeeping
    add_to_total_requests_sent(repetitions)    
    return repetitions 

def get_active_interface():
    # returns a tuple like
    # ('192.168.5.1', 'wlp3s0')
    (gw_ip, gw_if) = netifaces.gateways()['default'][netifaces.AF_INET]
    return gw_if

# dumps a list of secondary ip addresses to a file

# returns list of interfaces
def get_interfaces():
    if_list = netifaces.interfaces()
    return if_list
     
# takes an interface name like 'wlp3s0'
# and returns a list of secondary ip addresses     
def get_ip_addresses(iface):
    #if_list = get_interfaces()
    ip_list = []
    if_count = len(netifaces.ifaddresses(iface)[netifaces.AF_INET])
    for i in xrange(1,if_count - 1):
        tmp_addr = netifaces.ifaddresses(iface)[netifaces.AF_INET][i]['addr']
        ip_list.append(tmp_addr)
    return ip_list    


    
# accepts a list of port numbers
# and kills the processes that are attached to them
def kill_ports(port_list):
    popen = subprocess.Popen(['netstat', '-tlpn'],
                             shell=False,
                             stdout=subprocess.PIPE)
    #(data, err) = popen.communicate()
    (data, _) = popen.communicate()
    
    pattern = "^tcp.*((?:{0})).* (?P<pid>[0-9]*)/.*$"
    pattern = pattern.format(')|(?:'.join(port_list))
    prog = re.compile(pattern)
    for line in data.split('\n'):
        match = re.match(prog, line)
        if match:
            pid = match.group('pid')
#             print(date_str() + 'killing PID ' + pid)
            subprocess.Popen(['kill', '-9', pid])
            #os.kill(pid)
    
