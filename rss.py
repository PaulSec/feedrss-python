import feedparser
import time

feeds = ['http://malware.dontneedcoffee.com/feeds/posts/default?alt=rss',
    'http://maldr0id.blogspot.com/feeds/posts/default?alt=rss',
    'http://www.virqdroid.com/feeds/posts/default?alt=rss',
    'https://blog.lookout.com/feed/',
    'http://news.drweb.com/rss/get/?c=5&lng=en',
    'http://research.zscaler.com/feeds/posts/default?alt=rss']

entries = []
for feed in feeds:
    d = feedparser.parse(feed)
    entries.extend(d.entries)

for entry in entries:
    date = time.strftime("%Y-%m-%d %H:%M:%S", entry.published_parsed)
    entry.published = date
    
    entries = sorted(entries, key=lambda k: k.published)

for entry in entries:
    print "%s (%s) - %s " % (entry.title, entry.link, entry.published)
