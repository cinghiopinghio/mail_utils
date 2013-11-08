#!/usr/bin/env python2

from __future__ import print_function,division
import keyring
import getpass
import argparse
from os.path import expanduser


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

def print_mutt(account):
    _id = keyring.get_password('mutt',account+'-id')
    return 'msmtp -a {0} -f {1} --user {2}'.format(account,_id,_id)

def main():
    parser = argparse.ArgumentParser(description='Store and get addresses information\
                                     into a keyring')
    group_get = parser.add_mutually_exclusive_group()
    group_get.add_argument('-p', '--get-password',\
                        metavar='ACCOUNT', type=str,\
                        default="",\
                        help='Get password for given account')
    group_get.add_argument('-i', '--get-id',\
                        metavar='ACCOUNT', type=str,\
                        default="",\
                        help='Get account id for given account (ex. email\
                        address)')
    group_get.add_argument('-m', '--mutt-string',\
                        metavar='ACCOUNT', type=str,\
                        default="",\
                           help='Get a mutt compatible string like:\
                           msmtp -a ACCOUNT -f FROM --user USERID'\
                         )
    parser.add_argument('-s','--set-account',\
                        metavar='ACCOUNT', type=str,\
                        default="",\
                        help='Set password and id for given account')
    parser.add_argument('-S','--set-all',\
                        action='store_true',\
                        help='set password and ids for accounts in msmtp\
                        rc-file')
    parser.add_argument('-f','--rc-file',\
                        metavar='MSMTPRC', type=str,\
                        default='~/.msmtprc',\
                        help='set msmtp rc-file (default: ~/.msmtprc)')
    

    args = parser.parse_args()

    if args.set_all:
        # set all accounts in msmtprc
        set_all(args.rc_file)
    else:
        # set account information
        if args.set_account != '':
            set_account(args.set_account)

    # get account information
    if args.get_password != '':
        print(get_pw(args.get_password))
    elif args.get_id != '':
        print(get_id(args.get_id))
    elif args.mutt_string != '':
        print('"{0}"'.format(print_mutt(args.mutt_string)))

if __name__ == '__main__':
    main()
