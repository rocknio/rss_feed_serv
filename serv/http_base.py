# -*- coding: utf-8 -*-
import logging
import uuid

from tornado.web import RequestHandler

__author__ = 'Neo'


class BaseHttpHandler(RequestHandler):
    def __init__(self, application, request, **kwargs):
        super(BaseHttpHandler, self).__init__(application, request, **kwargs)
        self.trans_id = str(uuid.uuid1()).replace("-", "")

    def set_default_headers(self):
        # 后面的*可以换成ip地址，意为允许访问的地址
        self.set_header('Access-Control-Allow-Origin', '*')
        self.set_header('Access-Control-Allow-Headers', 'x-requested-with,Content-Type')
        self.set_header('Access-Control-Allow-Methods', 'POST, GET, PUT, DELETE, OPTIONS')

    def options(self):
        self.set_status(204)
        self.finish()

    def data_received(self, chunk):
        pass

    def debug(self, msg, *args, **kwargs):
        """
        子类日志代理，传入额外参数trans_identity

        :param msg:
        :param args:
        :param kwargs:
        :return:
        """
        msg = "[%s] [%s] %s" % (self.__class__.__name__, self.trans_id, msg)
        logging.debug(msg, *args, **kwargs)

    def info(self, msg, *args, **kwargs):
        """
        子类日志代理，传入额外参数trans_identity

        :param msg:
        :param args:
        :param kwargs:
        :return:
        """
        msg = "[%s] [%s] %s" % (self.__class__.__name__, self.trans_id, msg)
        logging.info(msg, *args, **kwargs)

    def warning(self, msg, *args, **kwargs):
        """
        子类日志代理，传入额外参数trans_identity

        :param msg:
        :param args:
        :param kwargs:
        :return:
        """
        msg = "[%s] [%s] %s" % (self.__class__.__name__, self.trans_id, msg)
        logging.warning(msg, *args, **kwargs)

    def error(self, msg, *args, **kwargs):
        """
        子类日志代理，传入额外参数trans_identity

        :param msg:
        :param args:
        :param kwargs:
        :return:
        """
        msg = "[%s] [%s] %s" % (self.__class__.__name__, self.trans_id, msg)
        logging.error(msg, *args, **kwargs)

    def critical(self, msg, *args, **kwargs):
        """
        子类日志代理，传入额外参数trans_identity

        :param msg:
        :param args:
        :param kwargs:
        :return:
        """
        msg = "[%s] [%s] %s" % (self.__class__.__name__, self.trans_id, msg)
        logging.critical(msg, *args, **kwargs)

    def log(self, lvl, msg, *args, **kwargs):
        """
        子类日志代理，传入额外参数trans_identity

        :param msg:
        :param lvl:
        :param args:
        :param kwargs:
        :return:
        """
        msg = "[%s] [%s] %s" % (self.__class__.__name__, self.trans_id, msg)
        logging.log(lvl, msg, *args, **kwargs)
