def solution(genres, plays):
    answer = []
    dicts = {}
    n = len(genres)
    
    for i in range(n):
        genre = genres[i]
        
        if genre not in dicts:
            dicts[genre] = [[plays[i], -1]]
        else:
            dicts[genre][0][0] += plays[i]
        dicts[genre].append([plays[i], i])
    
    # 속한 노래가 많이 재생된 장르 순서대로 정렬
    sorted_dicts = dict(sorted(dicts.items(), key=lambda x: x[1][0][0], reverse=True))
    
    for genre_type in sorted_dicts.values():
        sorted_genre_type = sorted(genre_type, key= lambda x : (x[0], -x[1]))
        
        answer.append(sorted_genre_type[-2][1])
        if(len(sorted_genre_type) >= 3):
            answer.append(sorted_genre_type[-3][1])
        
        
    return answer