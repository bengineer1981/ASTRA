#!/usr/bin/env python
# -*- coding: utf-8 -*-
import socket
port = int(raw_input('port number = '))
ip_addr = raw_input('ip address = ')
clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientsocket.connect((ip_addr, port))
clientsocket.send('1464267974.1745632858,188.478595133,1')
