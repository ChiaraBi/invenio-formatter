# -*- coding: utf-8 -*-
##
## $Id$
##
## This file is part of CDS Invenio.
## Copyright (C) 2002, 2003, 2004, 2005, 2006 CERN.
##
## CDS Invenio is free software; you can redistribute it and/or
## modify it under the terms of the GNU General Public License as
## published by the Free Software Foundation; either version 2 of the
## License, or (at your option) any later version.
##
## CDS Invenio is distributed in the hope that it will be useful, but
## WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
## General Public License for more details.  
##
## You should have received a copy of the GNU General Public License
## along with CDS Invenio; if not, write to the Free Software Foundation, Inc.,
## 59 Temple Place, Suite 330, Boston, MA 02111-1307, USA.
"""BibFormat element - Prints contact information
"""
__revision__ = "$Id$"

def format(bfo, separator='; ', link="yes"):
    """
    Prints contact information for the record
    
    @param separator the separator between addresses.
    @param link Link the addresses to search engine (HTML links) if 'yes'
    """
    from urllib import quote
    from invenio.config import weburl

    addresses = bfo.fields('270__p')

    if link == "yes":
        addresses = ['<a href="'+weburl+'/search?f=author&p='+ \
                     quote(address) +'&amp;ln=' + bfo.lang + '">' + \
                     address +'</a>' for address in addresses]
        
    return separator.join(addresses)




