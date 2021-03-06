#!/usr/bin/env python
"""Converts first command-line argument to QR code and outputs to stdout."""

import sys
import pyqrcode


def main():
    input_str = None
    try:
        input_str = sys.argv[1]
    except IndexError:
        print("reading from stdin", file=sys.stderr)
        input_str = "\n".join([line.rstrip('\n') for line in sys.stdin.readlines()])

    qr = pyqrcode.create(input_str)

    #text = qr.text()
    #print("win:")
    #print(text.replace('1', '  ').replace('0', '$$'))

    #print("unix:")
    text_only = True
    if text_only:
        print(qr.text().replace("0", "  ").replace("1", "##"))
    else:
        print(qr.terminal(module_color='black',
                          background='white',
                          quiet_zone=2))


if __name__ =="__main__":
    main()
