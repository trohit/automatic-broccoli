# A bunch of nifty networking functions to use in python
import netifaces

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


def write_list_to_file(file_name, list_name):
    thefile = open(file_name, 'w')
    for item in list_name:
        thefile.write("%s\n" % item)
    
