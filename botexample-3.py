import socket
import sys
from random import randint
import re

#----------------------------------- Settings --------------------------------------#
network = 'irc.onlinegamesnet.net'
port = 6667
homechan = '#berend'
irc = socket.socket ( socket.AF_INET, socket.SOCK_STREAM )
irc.connect ( ( network, port ) )
print irc.recv ( 4096 )
irc.send ( 'PASS *********\r\n')
irc.send ( 'NICK bython\r\n' )
irc.send ( 'USER bython bython bython :Python IRC\r\n' )
#----------------------------------------------------------------------------------#

#---------------------------------- Functions -------------------------------------#
def readAdmin(host):                        # Return status 0/1
    bestand = open('admins.txt', 'r')
    for line in bestand:
        if host in line:
            status = 1
            return status
        else:
            status = 0
            return status

def GetHost(host):                            # Return Host
    host = host.split('@')[1]
    host = host.split(' ')[0]
    return host

def GetChannel(data):                        # Return Channel
    channel = data.split('#')[1]
    channel = channel.split(':')[0]
    channel = '#' + channel
    channel = channel.strip(' \t\n\r')
    return channel

def GetNick(data):                            # Return Nickname
    nick = data.split('!')[0]
    nick = nick.replace(':', ' ')
    nick = nick.replace(' ', '')
    nick = nick.strip(' \t\n\r')
    return nick

def Send(msg):
    irc.send('PRIVMSG ' + homechan + ' : ' + msg +  '\r\n')

def Join(chan):
    irc.send ( 'JOIN ' + chan + '\r\n' )

def Part(chan):
    irc.send ( 'PART ' + chan + '\r\n' )

def Op(to_op, chan):
    irc.send( 'MODE ' + chan + ' +o: ' + to_op + '\r\n')

def DeOp(to_deop, chan):
    irc.send( 'MODE ' + chan + ' -o: ' + to_deop + '\r\n')

def Voice(to_v, chan):
    irc.send( 'MODE ' + chan + ' +v: ' + to_v + '\r\n')

def DeVoice(to_dv, chan):
    irc.send( 'MODE ' + chan + ' -v: ' + to_dv + '\r\n')
#------------------------------------------------------------------------------#

while True:
    action = 'none'
    data = irc.recv ( 4096 ) 
    print data

    if data.find ( 'Welcome to the OnlineGamesNet IRC Network' ) != -1:
            Join(homechan)

    if data.find ( 'PING' ) != -1:
            irc.send ( 'PONG ' + data.split() [ 1 ] + '\r\n' )

    #--------------------------- Action check --------------------------------#
    if data.find('#') != -1:
        action = data.split('#')[0]
        action = action.split(' ')[1]

    if data.find('NICK') != -1:
        if data.find('#') == -1:
            action = 'NICK'

    #----------------------------- Actions -----------------------------------#
    if action != 'none':

        if action == 'PRIVMSG':
            if data.find('$') != -1:
                x = data.split('#')[1]
                x = x.split('$')[1]
                info = x.split(' ')
                info[0] = info[0].strip(' \t\n\r')

                if info[0] == 'op':
                    host = GetHost(data)
                    status = readAdmin(host)
                    if status == 1:
                        chan = GetChannel(data)
                        Op(info[1], chan) 
                if info[0] == 'deop':
                    host = GetHost(data)
                    status = readAdmin(host)
                    if status == 1:
                        chan = GetChannel(data)
                        DeOp(info[1], chan)
                if info[0] == 'voice':
                    host = GetHost(data)
                    status = readAdmin(host)
                    if status == 1:
                        chan = GetChannel(data)
                        Voice(info[1], chan) 
                if info[0] == 'devoice':
                    host = GetHost(data)
                    status = readAdmin(host)
                    if status == 1:
                        chan = GetChannel(data)
                        DeVoice(info[1], chan) 
                if info[0] == 'join':
                    Join('#' + info[1])
                if info[0] == 'part':
                    Part('#' + info[1])
                if info[0] == 'version':
                    Send('Im a Python IRC bot coded by berend')

        if action == 'MODE':
            Host = GetHost(data)
            status = readAdmin(Host)
            if status == 0:
                if data.find('-o') != -1:
                    to_op = data.split('-o')[1]
                    chan = GetChannel(data)
                    chan = chan.split('-o')[0]
                    Op(to_op, chan)

                if data.find('+o') != -1:
                    to_deop = data.split('+o')[1]
                    chan = GetChannel(data)
                    chan = chan.split('+o')[0]
                    DeOp(to_deop, chan)

        if action == 'JOIN':
            Host = GetHost(data)
            status = readAdmin(Host)
            if status == 1:
                chan = GetChannel(data)
                nick = GetNick(data)
                Op(nick, chan)