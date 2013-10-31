#!/usr/bin/env python3

import keyring
import getpass
import argparse

def main():
    parser = argparse.ArgumentParser(description='Store and get addresses information\
                                     into a keyring')
    parser.add_argument('--get-password',\
                        metavar='ACCOUNT', type=str,\
                        help='Get password for given account')
    parser.add_argument('--get-id',\
                        metavar='ACCOUNT', type=str,\
                        help='Get account id for given account (ex. email\
                        address)')
    parser.add_argument('--set-password',\
                        metavar='ACCOUNT', type=str,\
                        help='Set password for given account')
    parser.add_argument('--set-id',\
                        metavar='ACCOUNT', type=str,\
                        help='Set account id for given account (ex. email\
                        address)')
    parser.add_argument('-s','--set-all',\
                        metavar='MSMTPRC',default='~/.msmtprc',type=str,\
                        help='set password and ids for accounts in msmtp\
                        rc-file (default: ~/.msmtprc)')

    args = parser.parse_args()


if __name__ == '__main__':
    main()
