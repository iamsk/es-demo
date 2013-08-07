# -*- coding: utf-8 -*-

import re
import json
from pyquery import PyQuery as pq


class Data(object):

    def __init__(self):
        with open('rss.xml', 'r') as f:
            xml = f.read()
            d = pq(xml)
        self.list = []
        for item in d('item').items():
            model = {}
            model['title'] = item('title').text()
            model['link'] = item('link').text().split('?')[0]
            model['id'] = int(re.search(r'(\d+)$', model['link']).group(1))
            self.list.append(model)

    def getData(self):
        return self.list


if __name__ == '__main__':
    data = Data()
    item = data.getData()[0]
    print json.dumps(item, ensure_ascii=False, indent=4)
