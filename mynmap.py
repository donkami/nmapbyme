import sys
import time
import socket

if __name__ == "__main__":

    if len( sys.argv ) > 1:
        port = int( sys.argv[ 1 ] )
    else:
        print("Usage python" + sys.argv[0] + "<port>")
        sys.exit( -1 )


    host = "0.0.0.0"

    sock_server = socket.socket()
    sock_server.bind( (host, port) )
    sock_server.listen(3)

    while 1:
        conn, addr = sock_server.accept()

        if conn:
            conn.sendall( str( time.time() ) + "\n")
            conn.close()
            continue
