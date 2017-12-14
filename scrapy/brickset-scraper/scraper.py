"""Scraper"""
import scrapy



class BricksetSpider(scrapy.Spider):
    """Spider class"""
    name = 'brickset_spider'
    start_urls = ['http://brickset.com/sets/year-2016']

    def parse(self, response):
        """Yields brickset name"""
        set_selector = '.set'
        for brickset in response.css(set_selector):
            name_selector = 'h1 a::attr(href)'
            split_name = brickset.css(name_selector).extract_first().split('/')[3].replace('-', ' ')
            yield {
                'name': split_name,
            }
