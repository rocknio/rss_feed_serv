# !/usr/bin/python3
# -*- coding: utf-8 -*-
import datetime
import json
import logging
from tornado.gen import engine
from tornado.web import asynchronous
from serv.http_base import BaseHttpHandler
from cfg.cfg import Cfg
import feedparser

__author__ = "Neo"


class RssTitleHandler(BaseHttpHandler):
    rss_title_list = {
        "CNBETA": {
            "timestamp": None,
            "title_list": []
        },
        "知乎": {
            "timestamp": None,
            "title_list": []
        }
    }

    @asynchronous
    @engine
    def get(self, feed_name, start_idx=0, end_idx=20):
        try:
            if self.rss_title_list[feed_name.upper()]["timestamp"] is None or (datetime.datetime.now() - self.rss_title_list[feed_name.upper()]["timestamp"]).seconds > (10 * 60):
                feed_url = Cfg.get(feed_name.upper(), None)
                if feed_url:
                    rss_info = feedparser.parse(feed_url)
                    for one_content in rss_info["entries"]:
                        if feed_name.upper() == 'CNBETA':
                            link = "https://m.cnbeta.com/view/" + str(one_content.link)[str(one_content.link).rfind('/') + 1:]
                        else:
                            link = one_content.link
                        self.rss_title_list[feed_name.upper()]["title_list"].append({
                            "title": one_content.title,
                            "link": link,
                            "icon": feed_name,
                            "pub_time": "{}-{}-{} {}:{}".format(one_content.published_parsed[0], one_content.published_parsed[1], one_content.published_parsed[2], one_content.published_parsed[3], one_content.published_parsed[4])
                        })

                    self.rss_title_list[feed_name.upper()]['timestamp'] = datetime.datetime.now()

            if int(start_idx) < 0 or int(end_idx) > self.rss_title_list[feed_name.upper()]["title_list"].__len__():
                self.write(json.dumps([]))
                self.finish()
                return

            resp = self.rss_title_list[feed_name.upper()]["title_list"][int(start_idx):int(end_idx)]
            self.write(json.dumps(resp))
            self.finish()
        except Exception as ex:
            logging.error("[%s]RssTitleHandler handle exception:%s", self.trans_id, ex)
            self.set_status(500)
            self.write("")