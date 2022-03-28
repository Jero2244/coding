#! /usr/bin/python3

import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('youtube.com', 80))