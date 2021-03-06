#!/usr/bin/env python2

from __future__ import print_function
import sys
import subprocess
import keyring
import getpass

#===========================================================
# Folder Name Dictionary
#===========================================================

# This defines the mapping of remote to local folders. On the left are the
# names of the remote folders. You may have to change the name on the left side
# to match your gmail's language. The right side is what the folders will be
# called on the local side. Notice that on the left side I prepend my folders
# that I don't read with a z. That way they end up on the bottom of a mailbox
# list.

mapping = { 'INBOX':              'INBOX'
          , '[Gmail]/All Mail':   'all_mail'
          , '[Gmail]/Drafts':     'drafts'
          , '[Gmail]/Important':  'important'
          , '[Gmail]/Sent Mail':  'sent'
          , '[Gmail]/Spam':       'spam'
          , '[Gmail]/Starred':    'flagged'
          , '[Gmail]/Trash':      'trash'
          , '[Gmail]/Chats':      'chats'
          }

r_mapping = { val: key for key, val in mapping.items() }

def nt_remote(folder):
    try:
        return mapping[folder]
    except:
        #return re.sub(' ', '_', folder).lower()
        return folder;

def nt_local(folder):
    try:
        return r_mapping[folder]
    except:
        return folder
        #return re.sub('_', ' ', folder).capitalize()

def exclude(excludes):
    def inner(folder):
        try:
            excludes.index(folder)
            return False
        except:
            return True

    return inner

#===========================================================
# Password and From and Username retrieval
#===========================================================

SER='mutt'

class Pw():
    def __init__(self,_from='',_user='',_password=''):
        self.frm = _from
        self.usr = _user
        self.pwd = _password
    def __str__(self):
        return '{0},{1},{2}'.format(self.frm,self.usr,self.pwd)
    def get_from(self,account):
        data = keyring.get_password(SER,account)
        self.frm, self.usr, self.pwd = data.split(',')
    def get_from_pass(self,account):
        data = subprocess.check_output(['pass','email/'+str(account)])
        for line in data.split('\n'):
            secret = line.split(':')
            if len(secret) == 1 and secret[0] != '':
                self.pwd = secret[0]
            elif secret[0] == 'user':
                scrt = secret[1].split(',')
                if len(scrt) == 1:
                    self.frm = self.usr = scrt[0]
                elif len(scrt) == 2:
                    self.frm,self.usr = scrt
    def set_to(self,account):
        keyring.set_password(SER,account,str(self))

def get_account_pass(account):
    secret = Pw()
    secret.get_from_pass(account)
    return secret

def get_password_pass(account):
    secret = get_account_pass(account)
    return secret.pwd

def get_user_pass(account):
    secret = get_account_pass(account)
    return secret.usr

def get_from_pass(account):
    secret = get_account_pass(account)
    return secret.frm

def get_account(account):
    secret = Pw()
    secret.get_from(account)
    return secret

def get_password(account):
    secret = get_account(account)
    return secret.pwd

def get_user(account):
    secret = get_account(account)
    return secret.usr

def get_from(account):
    secret = get_account(account)
    return secret.frm

