#!/usr/bin/env python2

from __future__ import print_function,division
from utils import *
import argparse
from os.path import expanduser

def set_account(account):
    print ('\nStoring information about {0} account on a keyring'.format(account))
    usr = raw_input('User:                         ')
    frm = raw_input('From (default: same as User): ')
    frm = frm if frm != '' else usr
    while True:
        pwd = getpass.getpass(prompt='Password:                     ')
        pwd1 = getpass.getpass(prompt='Retype it:                    ')
        if pwd == pwd1:
            break
        else:
            print ('\nPassword are different. Retry.\n')

    secret = Pw(_from=frm, _user=usr, _password=pwd)
    secret.set_to(account)
    print ('Password and Username and From stored')

def print_mutt(account):
    secret = get_account(account)
    return 'msmtp -a {0} -f {1} --user {2}'.format(account,\
                                                   secret.frm,\
                                                   secret.usr)

def main():
    parser = argparse.ArgumentParser(description='Store and get addresses information\
                                     into a keyring')
    group_get = parser.add_mutually_exclusive_group()
    group_get.add_argument('-p', '--get-password',\
                           action='store_true',\
                        help='Get password for given account')
    group_get.add_argument('-u', '--get-user',\
                           action='store_true',\
                        help='Get account id for given account (ex. email\
                        address)')
    group_get.add_argument('-f', '--get-from',\
                           action='store_true',\
                        help='Get account id for given account (ex. email\
                        address)')
    group_get.add_argument('-m', '--mutt-string',\
                           action='store_true',\
                           help='Get a mutt compatible string like:\
                           msmtp -a ACCOUNT -f FROM --user USERID'\
                         )
    parser.add_argument('-s','--set-account',\
                        action='store_true',\
                        help='Set password and id for given account')
    parser.add_argument('-F','--rc-file',\
                        metavar='MSMTPRC', type=str,\
                        default='~/.msmtprc',\
                        help='set msmtp rc-file (default: ~/.msmtprc)')
    parser.add_argument("account",\
                        metavar='ACCOUNT', type=str,\
                        default='default',\
                        help="account in the keyring (default = 'default')")
    

    args = parser.parse_args()

    # set account information
    if args.set_account:
        set_account(args.account)

    # get account information
    if args.get_password:
        print(get_password(args.account))
    elif args.get_user:
        print(get_user(args.account))
    elif args.get_from:
        print(get_from(args.account))
    elif args.mutt_string:
        print('"{0}"'.format(print_mutt(args.account)))

if __name__ == '__main__':
    main()

