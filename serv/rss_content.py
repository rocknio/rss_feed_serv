# !/usr/bin/python3
# -*- coding: utf-8 -*-
import logging
from tornado.gen import engine
from tornado.web import asynchronous
from serv.http_base import BaseHttpHandler

__author__ = "Neo"


class RssContentHandler(BaseHttpHandler):
    @asynchronous
    @engine
    def get(self, title_id):
        try:
            self.write("RssContentHandler: {}".format(title_id))
            self.finish()
        except Exception as ex:
            logging.error("[%s]RssContentHandler handle exception:%s", self.trans_id, ex)
            self.set_status(500)
            self.write("")
            self.finish()
