# -*- coding: utf-8 -*-
import scrapy
from spiders.items import SpidersItem
from scrapy.selector import Selector


class MoviesSpider(scrapy.Spider):
    name = 'movies'
    allowed_domains = ['maoyan.com']
    start_urls = ['https://maoyan.com/films?showType=3']

    # def parse(self, response):
    #     pass


    def parse(self, response):

        item = SpidersItem()
        movies = Selector(response=response).xpath('//div[@class="movie-hover-info"]')

        for movie in movies[0:10]:
            movieName = movie.xpath('.//span/text()').extract_first()
            movieType = movie.xpath('.//div[@class="movie-hover-title"]/text()').extract()[0:-1]
            movieShowTime = movie.xpath('.//div[@class="movie-hover-title movie-hover-brief"]/text()').extract()[-1].replace('\n','').replace(' ','')

            # print(movieName)
            # print(movieType)
            # print(movieShowTime)

            item['movieName'] = movieName
            item['movieType'] = movieType
            item['movieShowTime'] = movieShowTime + '\n'

            yield item