#!/usr/bin/env python
# coding: utf-8

from jinja2 import Environment, FileSystemLoader
import re
import yaml

regex = re.compile(r'^9GAG ')
with open('feeds.yml', 'r') as f_feeds:
    feeds = yaml.load(f_feeds)
feed_list_unsort = [{
    'categ_name': regex.sub('', f['name']).replace(' - Fresh', '').replace(' - Hot', ''),
    'href': '"rss/{}.atom"'.format(f['name'].replace(' ', '_')),
    'type': 'Hot &raquo;' if 'Hot' in f['name'] else 'Fresh &raquo;',
} for f in feeds['gag9']['feeds'][3:]]

feed_list = []
for i in range(0, len(feed_list_unsort), 2):
    feed_list.append(feed_list_unsort[i+1])
    feed_list.append(feed_list_unsort[i])

env = Environment(loader=FileSystemLoader('templates'), trim_blocks=True, lstrip_blocks=True)
index = env.get_template('index.html')
with open('index.html', 'w') as f_index:
    f_index.write(index.render(feed_list=feed_list))
