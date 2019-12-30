#!/usr/bin/env python

import sys
import base64
try:
    from dnslib import *
except ImportError:
    print("Missing dependency dnslib: <https://pypi.python.org/pypi/dnslib>. Please install it with `pip`.")
    sys.exit(2)

d = DNSRecord.question("google.com","AAAA")

print(str(base64.urlsafe_b64encode(d.pack()), "utf-8"))
