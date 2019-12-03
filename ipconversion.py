import socket
from binascii import hexlify


def ipConversion():
    for ip_addr in ['127.0.0.1', '192.160.0.1']:
        packed_ip_addr = socket.inet_aton(ip_addr)
        unpacked_ip_addr = socket.inet_ntoa(packed_ip_addr)

        print("IP Address : {} => Packed: {} , Unpacked: {}".format(
            ip_addr, hexlify(packed_ip_addr), unpacked_ip_addr))


ipConversion()
