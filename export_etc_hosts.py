#!/usr/bin/python3

# converts all entries in /etc/hosts into exportable bash variables
# so if /etc/hosts contains
# a.b.c.d foo
#
# it becomes
#
# export foo=a.b.c.d

#import pdb
# Read the content of /etc/hosts file
with open('/etc/hosts', 'r') as hosts_file:
    lines = hosts_file.readlines()

# Initialize an empty dictionary to store the hostnames and IP addresses
hosts_dict = {}

# Parse each line in the hosts file
for line in lines:
    #print(f"l:[{line}]")
    #pdb.set_trace()
    if line.startswith("#"):# ignore comments
        continue
    # Remove leading/trailing whitespaces and split by spaces or tabs
    parts = line.strip().split()
    if len(parts) >= 2:
        # The first part is the IP address, and the rest are hostnames
        ip_address = parts[0]
        hostnames = parts[1:]
        for hostname in hostnames:
            # https://stackoverflow.com/questions/2821043/allowed-characters-in-linux-environment-variable-names
            # bash doesnt like variables with - or ., remove them as needed
            hostname = hostname.replace("-", "")
            hostname = hostname.replace(".", "_")

            # Store each hostname as a shell variable with the IP address
            hosts_dict[hostname] = ip_address

# Print the shell variables
for hostname, ip_address in hosts_dict.items():
    print(f"export {hostname}={ip_address}")
