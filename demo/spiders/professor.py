import scrapy

from demo.items import ProfItem


class ProfessorSpider(scrapy.Spider):
    name = 'professor'
    allowed_domains = ['scholars.cityu.edu.hk']
    start_urls = [
        'https://scholars.cityu.edu.hk/en/persons/search.html?filter=&lastName=&search=computer%20science&search=computer%20science&publicationYearsFrom=&affiliationStatus=&pageSize=100&publicationYearsTo=&page=0&type=&expertise=']
    next_urls = [
        "https://scholars.cityu.edu.hk/en/persons/search.html?filter=&lastName=&search=data%20science&search=deep%20learning&publicationYearsFrom=&affiliationStatus=&pageSize=200&publicationYearsTo=&page=0&type=&expertise=",
        "https://scholars.cityu.edu.hk/en/persons/search.html?filter=&lastName=&search=information%20system&search=informationsystem&publicationYearsFrom=&affiliationStatus=&pageSize=200&publicationYearsTo=&page=0&type=&expertise="]
    num_url = 0

    def parse(self, response):
        professors = response.css('.portal_list_item')
        for professor in professors:
            item = ProfItem()
            item["title"] = professor.css('.title a span::text').extract_first()
            item["email"] = professor.css('.email a::attr("href")').extract_first()
            item['org'] = professor.xpath('div/ul[2]/li/a/span').xpath('string(.)').extract_first()
            # if professor.xpath('div/ul[2]/li/a/span/text()') is not None:
            #     item['org'] = item['org'] + professor.xpath('div/ul[2]/li/a/span/span/text()').extract()[0] \
            #               + professor.xpath('div/ul[2]/li/a/span/span/text()').extract()[1]
            item["type"] = professor.css('.type::text').extract()
            item['url'] = professor.css('.title a::attr("href")').extract_first()
            # if str(item["type"] and str(item["type"]).find("student") == -1):
            yield item
        base = response.css('.portal_navigator_prev_next')[1]
        url = base.css('a::attr("href")').extract_first()
        # print(self.logger.debug(response.text))
        if url is not None:
            yield scrapy.Request(url=url, callback=self.parse)
        if url is None:
            if self.num_url < len(self.next_urls):
                url = self.next_urls[self.num_url]
                self.num_url += 1
                yield scrapy.Request(url=url, callback=self.parse)


