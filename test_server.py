#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 17 16:08:24 2019
This is a simple test server that will be used solely for debugging the client
all it is able to do is to listen to incoming connections, log them and send 
confirm message
@author: andrey

"""
import logging
import auxserver
logger_server = logging.getLogger('Server.'+__name__)
    
def test_server1(HOST = "127.0.0.1", PORT = 65432):
    import socket
    import io
    import json
    saved_data =b""


#HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
#PORT = 65432  # Port to listen on (non-privileged ports are > 1023)

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        logger_server.info('TCP Socket Initialized')
        s.bind((HOST, PORT))
        s.listen()
        logger_server.info('Object binded to the socket. Listening at %s:%s', HOST, PORT)
        conn, addr = s.accept()
        with conn:
            logger_server.info("Got connected from %s", addr)
            while True:
                data = conn.recv(1024)
                saved_data +=data
                logger_server.info("Received data from %s", addr)    
                if not data:
                    logger_server.info("No more data from %s", addr)
                    break
            tiow = io.TextIOWrapper(io.BytesIO(saved_data), encoding="utf8", newline="")
            obj = json.load(tiow)
            tiow.close()
            if auxserver.data_is_complete(obj):
                
                conn.sendall('Data Received successfully'.encode())
                logger_server.info('Data from %s received successfully', addr)
            else:
                conn.sendall('Data is corrupted'.encode())
                logger_server.info('Data from %s is corrupted', addr)
    