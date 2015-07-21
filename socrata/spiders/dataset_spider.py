import scrapy, datetime

from scrapy.loader import ItemLoader
from scrapy.loader.processors import MapCompose

# from scrapy.spiders import CrawlSpider, Rule
# from scrapy.linkextractors import LinkExtractor


from socrata.items import Dataset

class dataset_spider(scrapy.Spider):
    name = "dataset"
    allowed_domains = ["data.austintexas.gov"]
    start_urls = ['https://data.austintexas.gov/browse?&page=%s' % page for page in xrange(1, 99)]


    def parse(self, response):
        for href in response.xpath('//td/div/a/@href'):
            url = href.extract() + "/about"

            yield scrapy.Request(url, callback=self.parse_datasets)


    def parse_datasets (self, response):
        il = ItemLoader(item=Dataset(), response=response)
        il.default_output_processor = MapCompose(lambda v: v.strip())
        il.add_value('scraped_url', response.url)
        il.add_xpath('desc', '//a[contains(., "Description")]/following-sibling::div/p/text()')
        il.add_value('soc_id', response.url[-15:-6])
        il.add_xpath('name', '//*[@id="datasetName"]/text()')
        il.add_xpath('tags', '//dt[text()="Tags"]/following-sibling::dd/span/text()')
        il.add_xpath('permalink', '//dt[text()="Permalink"]/following-sibling::dd[1]/span/a/text()')
        il.add_xpath('dept', '//dt[text()="Department"]/following-sibling::dd[1]/span/text()')
        il.add_xpath('provided_by', '//dt[text()="Data Provided By"]/following-sibling::dd[1]/text()')
        il.add_xpath('category', '//dt[text()="Category"]/following-sibling::dd[1]/text()')
        # il.add_xpath('contact_name', )
        # il.add_xpath('contact_email', )
        # il.add_xpath('date_created', )
        # il.add_xpath('date_updated', )
        il.add_xpath('num_ratings', '//dd[@class="totalTimesRated"]/text()')
        il.add_xpath('num_visits', '//dt[text()="Visits"]/following-sibling::dd[1]/text()')
        il.add_xpath('num_downloads', '//dt[text()="Downloads"]/following-sibling::dd[1]/text()')
        il.add_xpath('num_comments', '//dd[@class="numberOfComments"]/text()')
        il.add_xpath('num_contributors', '//dt[text()="Downloads"]/following-sibling::dd[1]/text()')
        il.add_xpath('permissions', '//dt[text()="Permissions"]/following-sibling::dd[1]/text()')
        il.add_xpath('row_count',   '//span[contains(@class, "row_count")]/text()')
        il.add_xpath('update_freq', '//dt[text()="Frequency"]/following-sibling::dd[1]/span/text()')
        # il.add_xpath('timestamp', )
        il.add_xpath('set_type', '//span[@class="icon currentViewName"]/text()')

        return il.load_item()

