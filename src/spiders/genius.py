from urllib.parse import urljoin
from ..utils import output
import scrapy

class GeniusSpider(scrapy.Spider):
    name = "genius"

    def start_requests(self):
        seed = 'https://genius.com/artists/Parcels'
        yield scrapy.Request(url=seed, callback=self.parse_artist_page)

    def parse_artist_page(self, response):
        songs_urls = response.css('div.mini_card_grid-song a::attr(href)').getall()
        for song_url in songs_urls:
            yield scrapy.Request(url=song_url, callback=self.parse_lyrics_page)

    def parse_lyrics_page(self, response):
        title = response.css('div.song_body-lyrics h2::text').get()
        song_metadata = response.css('div.rich_text_formatting p::text').getall()
        artists = set(response.css('span.metadata_unit-info a::text').getall())
        lyric = response.css('div.lyrics p::text').getall()
        annotations_ids = response.css('a::attr(annotation-fragment)').getall()

        item = output.make_item(title, artists, lyric, song_metadata)
        if annotations_ids:
            return self.get_annotations(response, annotations_ids, item)
        else:
            return item

    def get_annotations(self, response, annotations_ids, item):
        for annotation_id in annotations_ids:
            url = urljoin(response.url, annotation_id)
            yield scrapy.Request(
                url=url,
                callback=self.parse_annotation_page,
                meta={'item': item}
            )

    def parse_annotation_page(self, response):
        snippet_lyric = response.css("meta[property='og:title']::attr(content)").getall()
        annotations = response.css("meta[property='og:description']::attr(content)").getall()
        item = response.meta['item']
        item['snippet_lyric'] = snippet_lyric
        item['annotations']= annotations

        return item


