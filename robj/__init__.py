#
# Copyright (c) SAS Institute Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#


"""
rObj REST Client Library

This library is primarily intended for use with rPath provided REST APIs, but
should be able to interact with other REST based services that follow similar
best practices.

Example usage:

>>> import robj
>>> api = robj.connect('http://www.rpath.org/api/')
>>> products = api.products
>>> print products[0].name
"""

from robj.lib.httputil import HTTPData  # pyflakes=ignore
from robj.glue import HTTPClient as _HTTPClient
from robj.lib.log import setupLogging as _setupLogging

__all__ = ['rObj', 'connect', 'open', 'HTTPData', ]


def rObj(uri, headers=None, maxClients=None, maxConnections=None,
        logging=False, maxRedirects=None):
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
    @param maxRedirects: The maximum number of redirects that will be followed
                         before an exception is raised. (default: 10)
    @type maxRedirects: int
    @param logging: Set up a logger.
    @type logging: boolean
    """

    # Setup logging if requested.
    if logging:
        # FIXME: Let people specify log files somehow.
        _setupLogging()

    # Instantiate the http client.
    client = _HTTPClient(uri, headers=headers, maxClients=maxClients,
        maxConnections=maxConnections, maxRedirects=maxRedirects)

    # Get the root rObj
    if client.querystring:
        robj = client.do_GET(client.querystring)
    else:
        robj = client.do_GET('/')

    return robj

connect = open = rObj
