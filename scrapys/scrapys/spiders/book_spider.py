import scrapy

class BooksSpider(scrapy.Spider):
    name = "books"
    start_urls = ['http://books.toscrape.com/']
    def parse(self, response):
        for book in response.css('article.product_pod'):
            name = book.xpath('./h3/a/@title').extract_first
            price = book.css('p.price_color::text').extract_first
            yield {
                'name': name,
                'price': price,
            }