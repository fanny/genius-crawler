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
        song_metadata = response.css("div.rich_text_formatting p::text").getall()
        artists = set(response.css("span.metadata_unit-info a::text").getall())
        lyrics = response.css("div.lyrics p::text").getall()
        annotations = response.css("a::attr(annotation-fragment)").getall()

        item = {'artists': artists, 'lyrics': lyrics, 'metadata': song_metadata}
        for url in annotations:
            link = 'https://genius.com/' + url
            yield scrapy.Request(url=link, callback=self.parse_3, meta={'item': item})



    def parse_3(self, response):
        snippet_lyric = response.css("meta[property='og:title']::attr(content)").getall()
        annotations = response.css("meta[property='og:description']::attr(content)").getall()
        item = response.meta['item']
        item['snippet_lyric'] = snippet_lyric
        item['annotations']= annotations

        return item


