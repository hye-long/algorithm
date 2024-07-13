def solution(genres, plays):
    from collections import defaultdict

    genre_play_count = defaultdict(int)
    song_list_by_genre = defaultdict(list)

    for i, (genre, play) in enumerate(zip(genres, plays)):
        genre_play_count[genre] += play
        song_list_by_genre[genre].append((play, i))

   
    sorted_genres = sorted(genre_play_count.keys(), key=lambda g: genre_play_count[g], reverse=True)

    
    for genre in song_list_by_genre:
        song_list_by_genre[genre].sort(key=lambda x: (-x[0], x[1]))

    
    best_album = []
    for genre in sorted_genres:
        best_album.extend([song[1] for song in song_list_by_genre[genre][:2]])

    return best_album


