import multiprocessing
import time
from tkinter import Tk

PASSWORDS = {'email': 'F7minlBDDuvMJuxESSKHFhTxFtjVB6',
             'blog': 'VmALvQyKAxiVH5G8v01if1MLZF3sdt',
             'luggage': '12345',
             'facebook': 'F8989asd0adbUkJBO90HoadH'}


def get_password (act):

    if act in PASSWORDS:
        r = Tk ()
        r.withdraw ()

        r.clipboard_clear ()
        r.clipboard_append (PASSWORDS[act])
        print('Password for ' + act + ' copied to clipboard.')
        r.mainloop ()
    else:
        print('There is no account named ' + act)


if __name__ == '__main__':

    print("Enter the account name:")
    account = input()

    # Start a process to get password
    p = multiprocessing.Process (target = get_password, name = "Get_Password", args=(account,))
    p.start ()

    # Wait 10 seconds to get password and copy
    time.sleep (10)

    # Terminate foo
    p.terminate ()

    # Cleanup
    p.join ()