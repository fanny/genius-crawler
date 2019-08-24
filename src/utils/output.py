def make_item(title, artists, lyric, song_metadata):
    return {
        'title': title,
        'artists': artists,
        'lyric': lyric,
        'metadata': song_metadata,
        'annotations': []
    }