import scrapy
from django.utils import timezone
from scrapy.crawler import CrawlerProcess

from news.models import Media, Article


def ensure_proper_link(link, web):
    if not link.startswith('http'):
        return web[:-1] + link
    return link


def parse(self, response):
    for link in response.css(self.media.title_rule):
        text = str(link.css('a::text').extract_first())
        link = str(link.css('a::attr(href)').extract_first())
        link = ensure_proper_link(link, self.media.url)
        if link and text:
            Article.objects.update_or_create(
                url=link,
                defaults={
                    'date': timezone.now(),
                    'media': self.media,
                    'title': text,
                }
            )
        yield {'title': text, 'url': link}


def read_all_media():
    print("Reading all media")
    process = CrawlerProcess({
        'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
    })
    types = {}
    for media in Media.objects.all():
        # create dynamic types
        types[media.name] = type("Spider" + str(media.pk),
                                 (scrapy.Spider,),
                                 {
                                     'name': media.name,
                                     'media': media,
                                     'start_urls': [media.url, ],
                                     'parse': parse,
                                 })
        process.crawl(types[media.name])
    process.start()
