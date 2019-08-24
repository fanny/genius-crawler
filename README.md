# Genius crawler

Crawler for extract genius metadata and annotations of [**Parcels**](https://genius.com/artists/Parcels) top songs.

![](https://images.sk-static.com/images/media/profile_images/artists/8653309/huge_avatar)

## Prerequisites

You need to have `Python 3` in your local machine, so you can run:

`pip install -r requirements.txt`

## Running

`scrapy crawl genius -o output/parcels-lyrics.json`

## Data

The current behaviour of this crawler is get top songs of an artist, in this case, parcels,
then if you go in `output/parcels-lyrics.json` folder,  
you should encounter this lyrics(not necessarily in this order):

1. Tieduprightnow
2. Gamesoffluck
3. Lightenup
4. Allaround
5. Herefore
6. Overnight
7. Hideout
8. Withorwithoutyou
9. Bemyself
10. Older

