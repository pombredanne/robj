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

"""
rObj REST Client Library

This library is primarily intened for use with rPath provied REST APIs, but
should be able to interact with other REST based services that follow similar
best practices.

Example usage:

>>> import robj
>>> api = robj.connect('http://www.rpath.org/api/')
>>> products = api.products
>>> print products[0].name
"""

from robj.glue import HTTPClient as _HTTPClient
from robj.lib.log import setupLogging as _setupLogging

__ALL__ = ['rObj', 'connect', 'open', ]

def rObj(uri, headers=None, maxClients=None, maxConnections=None,
    logging=True):
    """
    @param uri: URI for connectiong to the root of the desired web service. This
                may contain user information and must be http or https.
    @type uri: str
    @param headers: Any headers that should be included in all requets.
    @type headers: dict
    @param maxClients: The maximum number of workers that will be created to
                       handle requets. Works are created as needed, rather than
                       being preallocated. (default: 10)
    @type maxClients: int
    @param maxConnections: The maximum number of connections each client thread
                           should cache. Client threads only cache one
                           connection per host. This should only matter if you
                           are talking to multiple hosts. (default: 2)
    @type maxConnections: int
    @param logging: Set up a logger.
    @type logging: boolean
    """

    # Setup logging if requested.
    if logging:
        # FIXME: Let people specify log files somehow.
        _setupLogging()

    # Instantiate the http client.
    client = _HTTPClient(uri, headers=headers, maxClients=maxClients,
        maxConnections=maxConnections)

    # Get the root rObj
    robj = client.do_GET('/')

    return robj

connect = open = rObj
