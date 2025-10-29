
import subprocess
import sys
import importlib
modList = ['requests', 'speedtest-cli', 'time', 'py-cpuinfo']

for each in modList:
    spec = importlib.util.find_spec(each)
    if spec is not None:
        print(f"Module {each} found")
        # importlib.import_module(each)
    else:
        print(f"Module {each} not found")
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', each])
        print(f"Installed module {each}")


import platform
import os
## Good for finding operating system type
## Good for finding files
import psutil

portStat = []
tcp_process = psutil.net_connections(kind='tcp4')
print(type(tcp_process))
# print(tcp_process)
for tcp_process in psutil.net_connections():
    # if tcp_process.status != 'CLOSE_WAIT':
    if tcp_process.status == 'LISTEN' or tcp_process.status == 'ESTABLISHED':
        #print(tcp_process.status,
        #      tcp_process.laddr.ip,
        #      tcp_process.laddr.port)
        portStat.append([tcp_process.status,
              tcp_process.laddr.ip,
              tcp_process.laddr.port])

print(portStat)


## good for network connection
import cpuinfo


def get_cpu_data():
    cpu_data = cpuinfo.get_cpu_info()
    return cpu_data

print("I'm out of the function")

cpu_data = get_cpu_data()  # have to run the function first!!
print(type(cpu_data))
print(cpu_data)
print(cpu_data['brand_raw'])
print(cpu_data['vendor_id_raw'])
print(cpu_data['python_version'])

## Good for finding operating system 
print(platform.processor())

# print("="*40, "System Information", "="*40)
# uname = platform.uname()
# print(f"System: {uname.system}")
# print(f"Node Name: {uname.node}")
# print(f"Release: {uname.release}")
# print(f"Version: {uname.version}")
# print(f"Machine: {uname.machine}")
# print(f"Processor: {uname.processor}")

################
# # Script to ping all IP addresses in a /24 subnet
################
# import os
# import platform
# network = input ("Enter first 3 numbers of IP network, e.g. 1.2.3: ")
# print(network)
# 
# if platform.system() == "Linux":
#     pingflag = 'c'
# elif platform.system() == "Windows":
#     pingflag = 'n'
#     
# 
# # Iterate over all usable IPs in this subnet
# for host in range (1, 2):
#     print("Pinging " + network + "." + str(host))
#     os.system(f"ping -{pingflag} 2 " + network + "." + str(host))


