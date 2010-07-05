#
# Copyright (c) 2010 rPath, Inc.
#
# This program is distributed under the terms of the MIT License as found 
# in a file called LICENSE. If it is not present, the license
# is always available at http://www.opensource.org/licenses/mit-license.php.
#
# This program is distributed in the hope that it will be useful, but
# without any waranty; without even the implied warranty of merchantability
# or fitness for a particular purpose. See the MIT License for full details.
#

from robj.glue import HTTPClient as _HTTPClient

__ALL__ = ['rObj', 'connect', 'open', ]

def rObj(uri, headers=None, maxClients=None, maxConnections=None):
    client = _HTTPClient(uri, headers=headers, maxClients=maxClients,
        maxConnections=maxConnections)
    robj = client.do_GET('/')
    return robj

connect = open = rObj
