from scapy.all import*

iface = 'eth0'

valid_ips =['192.168.1.1','192.168.1.2','192.168.1.3']

def valid(ip):
	return ip in valid_ips
	
def handler(packet):
	src_ip=packet[IP].src
	
if not valid(src_ip):
	print("WARNING:Unauthorised access from",src_ip)
	
sniff(iface=iface, filter ='ip',prn=packet)

