#!/usr/bin/env python2

from __future__ import print_function
import sys
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

def set_all(rcfile):
    with open(expanduser(rcfile),'r') as fin:
        for line in fin:
            line = line.split()
            if len(line)>0 and line[0] == 'account':
                if line[1] != 'default':
                    set_account(line[1])

def set_account(account):
    print ('Storing information about {0} account on a keyring'.format(account))
    _id = input('Id: ')
    _pw = getpass.getpass()

    keyring.set_password('mutt',account+'-pw',_pw)
    keyring.set_password('mutt',account+'-id',_id)
    print ('Password and Id stored')

def get_pw(account):
    _pw = keyring.get_password('mutt',account+'-pw')
    return _pw

def get_id(account):
    _id = keyring.get_password('mutt',account+'-id')
    return _id

