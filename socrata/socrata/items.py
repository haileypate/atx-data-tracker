# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader import ItemLoader

def check_null_value(value):
	if len(value) < 1:
		return 'no_value_found'
	else:
		return value

class Dataset(scrapy.Item):
    scraped_url = scrapy.Field()
    desc = scrapy.Field()
    soc_id = scrapy.Field()
    tags = scrapy.Field()
    permalink = scrapy.Field()
    dept = scrapy.Field()
    contact_name = scrapy.Field()
    contact_email = scrapy.Field()
    date_created = scrapy.Field()
    date_updated = scrapy.Field()
    num_ratings = scrapy.Field()
    num_visits = scrapy.Field()
    num_downloads = scrapy.Field()
    num_comments = scrapy.Field()
    num_contributors = scrapy.Field()
    permissions = scrapy.Field()
    row_count = scrapy.Field()
    update_freq = scrapy.Field()
    timestamp = scrapy.Field()
