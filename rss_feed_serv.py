# !/usr/bin/python3
# -*- coding: utf-8 -*-

import logging
import logging.handlers
import ssl

from tornado import ioloop, web
from tornado.httpserver import HTTPServer
from cfg.cfg import Cfg
from serv.url import app_handlers

__author__ = "Neo"


def init_log_handler():
    try:
        logger = logging.getLogger()
        logger.setLevel(logging.DEBUG)

        stream_handler = logging.StreamHandler()
        file_handler = logging.handlers.TimedRotatingFileHandler("rss_feed_serv.log", "MIDNIGHT", 1, 7)

        log_format = logging.Formatter('[%(asctime)s] [%(levelname)-7s]  %(message)s')
        stream_handler.setFormatter(log_format)
        file_handler.setFormatter(log_format)

        logger.addHandler(stream_handler)
        logger.addHandler(file_handler)

    except Exception as err_info:
        print(err_info)
        exit(-1)


if __name__ == '__main__':
    try:
        # 日志初始化
        init_log_handler()

        # 初始化Server
        app = web.Application(
            handlers=app_handlers,

        )

        ssl_ctx = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
        ssl_ctx.load_cert_chain("2_symmszmszy.club.crt", "3_symmszmszy.club.key")
        ssl_ctx.options &= ~ssl.OP_NO_SSLv2
        ssl_ctx.options &= ~ssl.OP_NO_SSLv3
        server = HTTPServer(app, ssl_options=ssl_ctx)

        # server = HTTPServer(app)
        server.listen(Cfg["ServPort"])
        logging.info("Start server at: %d", Cfg["ServPort"])

        ioloop.IOLoop.instance().start()
    except Exception as err:
        logging.fatal(err)
        print(err)
