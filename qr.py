#!/usr/bin/env python
"""Converts first command-line argument to QR code and outputs to stdout."""

import sys
import pyqrcode


def main():
    try:
        input_str = sys.argv[1]
    except IndexError:
        print("requires an input string as first argument")
        exit(1)

    qr = pyqrcode.create(input_str)

    #text = qr.text()
    #print("win:")
    #print(text.replace('1', '  ').replace('0', '$$'))

    #print("unix:")
    print(qr.terminal(module_color='black',
                      background='white',
                      quiet_zone=2))


if __name__ =="__main__":
    main()
