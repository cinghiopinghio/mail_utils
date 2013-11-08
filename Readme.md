#PYASTORE and MAIL_UTILS

Python code to help offlineimap + mutt + msmtp day-by-day
use.

Mainly it is usefull to store password and email addresses in a keyring
(such as gnome-keyring) in order to have them protected and secrets-free 
config files.

##PYASTORE

Use this to store your secrets in the keyring.
Secrets are composed of : Username, From, Password.
Usage:
`pyastore -h`
it's self explanatory.

make sure `.local/bin` is in your `$PATH` (or modify the Makefile
accordingly, it's really simple).

##MAIL_UTILS

To be loaded into offlineimap.
Add to `.offlineimaprc`
the following:
`pythonfile = path/to/utils.py`

# Licence

WTFPD
But if you find some bugs, please let me know.
