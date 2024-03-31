import requests

def search_movie_budget(movie_title):
    api_key = 'd597ae3f1c2a8cf54d111d498aeeac22'
    base_url = 'https://api.themoviedb.org/3/search/movie'
    params = {
        'api_key': api_key,
        'query': movie_title
    }

    response = requests.get(base_url, params=params)
    data = response.json()

    if 'results' in data and data['results']:
        movie_id = data['results'][0]['id']
        movie_details_url = f'https://api.themoviedb.org/3/movie/{movie_id}'
        details_params = {
            'api_key': api_key,
            'append_to_response': 'budget'
        }
        details_response = requests.get(movie_details_url, params=details_params)
        details_data = details_response.json()
        if 'budget' in details_data:
            return details_data['budget']
        else:
            return "Không có thông tin về ngân sách cho bộ phim này."
    else:
        return "Không tìm thấy bộ phim."

