# Genius crawler

Crawler for extract genius metadata and annotations of [**Parcels**](https://genius.com/artists/Parcels) top songs.

![](https://ksassets.timeincuk.net/wp/uploads/sites/55/2018/10/PARCELS_MAY2018_3_image_AntoineHenault-920x584.jpg)

## Prerequisites

You need to have `Python 3`, or create a [virtualenv](https://towardsdatascience.com/all-you-need-to-know-about-python-virtual-environments-9b4aae690f97), so you can run:

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

