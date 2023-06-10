import requests
import json

url = "https://api.themoviedb.org/3/movie/now_playing?language=ko-KR&page=1"

headers = {
    "accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJiNjY5ZDdlOGM3YjljZDNlNmQ2OWQyMmM2NTQzYmU2ZCIsInN1YiI6IjYzZDMxN2I5ZTcyZmU4MDA4NDkxNmNmZCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.8DnMZoPyVRhKNXbZJpqls78v7McdxjsUkYNrrmcXR1g"
}

response = requests.get(url, headers=headers)

print(response)
if response.status_code == 200:
    data = response.json()

    with open("nowplaying.json", "w", encoding='utf-8') as json_file:
        json.dump(data,json_file,ensure_ascii=False, indent='\t' )

    with open('nowplaying.json', 'r', encoding='utf-8') as file:
        json_data = json.load(file)['results']
    
    print(json_data)

    for i in range(0, len(json_data)):
        fields = {}
        pk = json_data[i]['id']
        fields['title'] = json_data[i]['title']
        fields['release_date'] = json_data[i]['release_date']
        fields['popularity'] = json_data[i]['popularity']
        fields['vote_count'] = json_data[i]['vote_count']
        fields['vote_average'] = json_data[i]['vote_average']
        fields['overview'] = json_data[i]['overview']
        fields['poster_path'] = json_data[i]['poster_path']
        fields['genre_ids'] = json_data[i]['genre_ids']
        fields['like_users'] = []

        json_data[i] = {}
        json_data[i]['model'] = "movies.movie"
        json_data[i]['pk'] = pk
        json_data[i]['fields'] = fields
    
    with open('nowplaying.json', 'w', encoding='utf-8') as file:
        json.dump(json_data, file, ensure_ascii=False, indent='\t')

    print("JSON 파일이 성공적으로 저장되었습니다.")
else:
    print("API 요청이 실패했습니다.")


