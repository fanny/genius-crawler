import scrapy


class GeniusSpider(scrapy.Spider):
    name = "genius"

    def start_requests(self):
        urls = ['https://genius.com/artists/Parcels']
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        p_res = response.css("div.mini_card_grid-song a::attr(href)").getall()
        for url in p_res:
            yield scrapy.Request(url=url, callback=self.parse_2)

    def parse_2(self, response):
        page = response.url.split("/")[-1]
        song_metadata = response.css("div.rich_text_formatting p::text").getall()
        annotations = response.css("a::attr(annotation-fragment)").getall()
        print(annotations)
        filename = 'quotes-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)
