#!/usr/bin/env python

import sys
try:
    from dnslib import *
except ImportError:
    print("Missing dependency dnslib: <https://pypi.python.org/pypi/dnslib>. Please install it with `pip`.")
    sys.exit(2)

d = DNSRecord.parse(sys.stdin.buffer.read())
print(d)
