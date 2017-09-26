#coding=utf8
import itchat
# tuling plugin can be get here:
# https://github.com/littlecodersh/EasierLife/tree/master/Plugins/Tuling
from tuling import get_response
import random

happy = ['蟹蟹蟹蟹我已经快乐得飞起来了呢', '我生日很快乐呀', '我本来就很快乐呀', '我激动得要晕了']

def construct_reply(msg):
    if '生日快乐' in msg.text:
        rep = get_response(msg['Text']) or u'蟹蟹蟹蟹我已经快乐得飞起来了呢'+' '+random.choice(happy)
    else:
        rep = get_response(msg['Text'])
    return(rep)

@itchat.msg_register('Text', isGroupChat = True)
def text_reply(msg, isGroupChat = True):
    if msg.User['NickName'] == '艳霞生日快乐！':
        itchat.send_msg(construct_reply(msg), toUserName=msg.User['UserName'])
        

@itchat.msg_register(['Picture', 'Recording', 'Attachment', 'Video'], isGroupChat = True)
def atta_reply(msg, isGroupChat = True):
    text_reply('生日快乐') # download function is: msg['Text'](msg['FileName'])

#@itchat.msg_register(['Map', 'Card', 'Note', 'Sharing'])
#def mm_reply(msg):
#    if msg['Type'] == 'Map':
#        return u'收到位置分享'
#    elif msg['Type'] == 'Sharing':
#        return u'收到分享' + msg['Text']
#    elif msg['Type'] == 'Note':
#        return u'收到：' + msg['Text']
#    elif msg['Type'] == 'Card':
#        return u'收到好友信息：' + msg['Text']['Alias']

#@itchat.msg_register('Text', isGroupChat = True)
#def group_reply(msg):
#    if msg['isAt']:
#        return u'@%s\u2005%s' % (msg['ActualNickName'],
#            get_response(msg['Text']) or u'收到：' + msg['Text'])


itchat.auto_login()
itchat.run()