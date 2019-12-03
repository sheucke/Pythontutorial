import socket


def socket_timeout():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    print("Socket created successfully.")

    print("Default Socket Timeout " + str(s.gettimeout()))

    s.settimeout(100)
    print("Current Socket Timeout " + str(s.gettimeout()))


if __name__ == "__main__":
    socket_timeout()
