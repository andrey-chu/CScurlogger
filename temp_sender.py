#!/usr/bin/env python3

#import sys
import socket
import selectors
import traceback

import message_class_client

sel = selectors.DefaultSelector()


def create_request(action, value, numrecords, maxrecord, minrecord):
    if action == "sendtext":# we will use mostly this typpe of message sending
                            # so we will mostly send the information as text
        return dict(
            type="text/json",
            encoding="utf-8",
            content=dict(action=action, value=value, recordsnum=numrecords,recordsmax=maxrecord, recordsmin=minrecord)

        )
    else:
        return dict(
                # this is something to try just for learning sake, to send 
                # the message as a gzip and check 
            type="binary/custom-client-binary-type",
            encoding="binary",
            content=bytes(action + value, encoding="utf-8"),
        )


def start_connection(host, port, request):
    addr = (host, port)
    print("starting connection to", addr)
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setblocking(False)
    sock.connect_ex(addr)
    events = selectors.EVENT_READ | selectors.EVENT_WRITE
    message = message_class_client.Message(sel, sock, addr, request)
    sel.register(sock, events, data=message)



def client_body(host, port, action, value, numrecords, maxrecord, minrecord):
    request = create_request(action, value, numrecords, maxrecord, minrecord)
    start_connection(host, port, request)
    
    try:
        while True:
            events = sel.select(timeout=1)
            for key, mask in events:
                message = key.data
                try:
                    result = message.process_events(mask)
                except Exception:
                    print(
                        "main: error: exception for",
                        f"{message.addr}:\n{traceback.format_exc()}",
                    )
                    message.close()
            # Check for a socket being monitored to continue.
            if not sel.get_map():
                break
    except KeyboardInterrupt:
        print("caught keyboard interrupt, exiting")
    finally:
        print("we are finished, closing connection")
        sel.close()
        return result
