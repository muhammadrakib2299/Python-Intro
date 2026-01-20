import requests

api_url = "https://api.nasa.gov/planetary/apod?api_key=Hm31gP6cQptCteBowdDv845UPBJlidS2YlTKe8SM"

def get_response(url):
    return requests.get(url)


if __name__ == "main":
    # print(__name__)
    res = get_response(api_url)
   