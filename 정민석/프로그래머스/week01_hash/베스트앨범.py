def solution(genres, plays):
    from collections import defaultdict
    
    genre_play_dict = defaultdict(int)  # 각 장르별 재생 횟수
    genre_songs_dict = defaultdict(list)  # 각 장르별 노래 정보
    
    # 각 노래 정보를 장르에 맞게 정리 and 재생 횟수도 같이 계산
    for index, (genre, play) in enumerate(zip(genres, plays)):
        genre_play_dict[genre] += play
        genre_songs_dict[genre].append((play, index))
    
    # 장르를 재생 횟수 기준으로 desc
    sorted_genres = sorted(genre_play_dict, key=genre_play_dict.get, reverse=True)
    
    result = []
    # 인기 장르 최대 두 곡씩 픽
    for genre in sorted_genres:
        sorted_songs = sorted(genre_songs_dict[genre], key=lambda x: (-x[0], x[1]))
        # 최대 두 곡 추가
        result.extend(song_id for _, song_id in sorted_songs[:2])
    
    return result
