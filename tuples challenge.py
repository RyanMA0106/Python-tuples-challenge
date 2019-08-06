imelda = 'More Mayhem', 'Imelda May', 2011, (
    (1, 'Pulling the Rug '), (2, 'Psycho'), (3, 'Mayhem'), (4, 'Kentish Town Waltz'))
title, artist, year, tracks = imelda
print(title, artist, year)
for songs in tracks:
    track, title = songs
    print('\tTrack number {}, Title: {}'.format(track, title))  # '\t' is tab

