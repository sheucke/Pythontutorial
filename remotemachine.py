import socket


def main():
    remote_host = "www.codeloop.org"

    try:
        print("IP Address Of " + remote_host + " Is " +
              socket.gethostbyname(remote_host))

    except socket.error as e:
        print("Error: {}".format(e))


if __name__ == "__main__":
    main()
