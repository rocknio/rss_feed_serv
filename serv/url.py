# !/usr/bin/python3
# -*- coding: utf-8 -*-
from serv.rss_title import RssTitleHandler
from serv.rss_content import RssContentHandler


__author__ = "Johnny"

app_handlers = [
    (r'/rss_title/(.*)/(.*)/(.*)', RssTitleHandler),
    (r'/rss_title/(.*)', RssTitleHandler),
    (r'/rss_content/(.*)', RssContentHandler),
]
