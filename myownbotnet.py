import socket
import sys
from random import randint
import re

#----------------------------------- Settings --------------------------------------#
network = 'irc.freenode.net'
port = 6667
homechan = '#botmasterds3za'
irc = socket.socket ( socket.AF_INET, socket.SOCK_STREAM )
irc.connect ( ( network, port ) )
irc.send ( 'NICK botslave\r\n' )
irc.send ( 'USER botslave botslave botslave :Python IRC\r\n' )
irc.send ( 'JOIN' + homechan )
#----------------------------- Reading data received ----------
while 1: # Be careful with these! it might send you to an infinite loop
  ircmsg = irc.recv(2048) # receive data from the server
  ircmsg = ircmsg.strip('\n\r') # removing any unnecessary linebreaks.
  print(ircmsg) # Here we print what's coming from the server
