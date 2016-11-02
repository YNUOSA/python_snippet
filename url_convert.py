#!/usr/bin/env python
# coding=utf8

import base64
import sys

class URL_Convert(object):
    URL_TYPE_PLAIN = 0
    URL_TYPE_THUNDER = 1
    URL_TYPE_QQ = 2
    URL_TYPE_FLASHGET = 3
    URL_TYPE_UNKNOWN = 4

    def __init__(self, url):
        self.url = url
        self.url_type = URL_Convert.URL_TYPE_UNKNOWN
        self.url_plain = self.__convert_to_plain(self.url)
        self.url_thunder = self.__url_thunder_encode(self.url_plain)
        self.url_qq = self.__url_qq_encode(self.url_plain)
        self.url_flashget = self.__url_flashget_encode(self.url_plain)

    def print_result(self):
        print "Plain url is {url_plain}\n" \
              "Thunder url is {url_thunder}\n" \
              "QQ url is {url_qq}\n" \
              "Flashget url is {url_flashget}".format(
            url_plain=self.url_plain,
            url_thunder = self.url_thunder,
            url_qq = self.url_qq,
            url_flashget = self.url_flashget
        )

    def __check_url_type(self, url):
        url_type = URL_Convert.URL_TYPE_UNKNOWN
        if url.startswith("thunder://"):
            url_type = URL_Convert.URL_TYPE_THUNDER
        elif url.startswith("qqdl://"):
            url_type = URL_Convert.URL_TYPE_QQ
        elif url.startswith("Flashget://"):
            url_type = URL_Convert.URL_TYPE_FLASHGET
        else:
            url_type = URL_Convert.URL_TYPE_PLAIN
        return url_type

    def __convert_to_plain(self, url):
        url_plain = ""
        self.url_type = self.__check_url_type(url)
        if self.url_type == URL_Convert.URL_TYPE_PLAIN:
            url_plain = url
        elif self.url_type == URL_Convert.URL_TYPE_THUNDER:
            url_plain = self.__url_thunder_decode(url)
        elif self.url_type == URL_Convert.URL_TYPE_QQ:
            url_plain = self.__url_qq_decode(url)
        elif self.url_type == URL_Convert.URL_TYPE_FLASHGET:
            url_plain = self.__url_flashget_decode(url)
        return url_plain

    def __url_thunder_decode(self, url):
        url = url.replace("thunder://", "")
        url = base64.b64decode(url)
        url = url[2:-2]
        return url

    def __url_qq_decode(self, url):
        url = url.replace("qqdl://", "")
        url = base64.b64decode(url)
        return url

    def __url_flashget_decode(self, url):
        url = url.replace("Flashget://", "")
        url = url[:-5]
        url = base64.b64decode(url)
        url = url.replace("[FLASHGET]", "")
        return url

    def __url_thunder_encode(self, url):
        thunder_prefix = "AA"
        thunder_posix = "ZZ"
        thunder_url_prefix = "thunder://"
        thunder_url = thunder_url_prefix + base64.b64encode(thunder_prefix + url + thunder_posix)
        return thunder_url


    def __url_qq_encode(self, url):
        qq_url_prefix = "qqdl://"
        qq_url = qq_url_prefix + base64.b64encode(url)
        return qq_url

    def __url_flashget_encode(self, url):
        flash_prefix = "[FLASHGET]"
        flash_posix = "[FLASHGET]"
        flash_url_prefix = "Flashget://"
        flash_url_posix = "&1926"
        flash_url = flash_url_prefix + base64.b64encode(flash_prefix + url + flash_posix) + flash_url_posix
        return flash_url

if __name__ == "__main__":
    # http://www.iqshw.com/url/xunlei/urlconvert.js
    url = "http://www.baidu.com"
    # url = "thunder://QUFodHRwOi8vd3d3LmJhaWR1LmNvbVpa"
    # url = "qqdl://aHR0cDovL3d3dy5iYWlkdS5jb20="
    # url = "Flashget://W0ZMQVNIR0VUXWh0dHA6Ly93d3cuYmFpZHUuY29tW0ZMQVNIR0VUXQ==&1926"
    if len(sys.argv) >= 2:
        url = str(sys.argv[1])
    url_convert = URL_Convert(url)
    url_convert.print_result()