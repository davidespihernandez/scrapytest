from unittest import mock

from django.test import TestCase
import factory

from news.media_reader import read_all_media
from news.models import Media


class MediaFactory(factory.DjangoModelFactory):
    class Meta:
        model = Media

    name = factory.Sequence(lambda n: "Media %03d" % n)
    title_rule = "h2"
    url = "https://www.elmundo.es/"


class ReadAllMediaTestCase(TestCase):
    @mock.patch('scrapy.crawler.CrawlerProcess.crawl')
    @mock.patch('scrapy.crawler.CrawlerProcess.start')
    def test_read_all_media(self, start_mock, crawl_mock):
        # given 2 media
        MediaFactory()
        MediaFactory()
        # when the read_all_media method is called
        read_all_media()
        # then we add a crawl for each media (it's a dynamic class)
        self.assertEqual(crawl_mock.call_count, 2)
        start_mock.assert_called()
