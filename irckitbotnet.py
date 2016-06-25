#!/usr/local/bin/python
'''
DEPENDENCES
pip install irckit
pip install gevent (for botnet)
pip install boto (for botnet's EC2 launcher)
pip install httplib2 (for some of the bots)
'''

from irc import IRCBot, run_bot


class GreeterBot(IRCBot):
    def greet(self, nick, message, channel):
        return 'Hi, %s' % nick

    def command_patterns(self):
        return (
            self.ping('^hello', self.greet),
        )


host = 'irc.freenode.net'
port = 6667
nick = 'greeterbot'

run_bot(GreeterBot, host, port, nick, ['#botwars'])