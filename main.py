import datetime
import requests
import webbrowser
import math
import os

hour = int(datetime.datetime.now().hour)
  
if hour>=0 and hour<12:
    print("Good Morning,")

elif hour>=12 and hour<18:
    print("Good Afternoon,")   

else:
    print("Good Evening,") 

print("\nI can do the following:\n\
      1. Search Movie\n\
      2. Weather {city}\n\
      3. Fetch News\n\
      4. Browse Internet\n\
      5. Play Music\n\
      6. Get Images")



def fetch_movie_info(title):
    api_key = "45d9338e"
    url = f"http://www.omdbapi.com/?apikey={api_key}&t={title}"

    response = requests.get(url)
    data = response.json()

    if data["Response"] == "True":
        movie_title = data["Title"]
        movie_year = data["Year"]
        movie_rating = data["imdbRating"]
        movie_plot = data["Plot"]

        print(f"Title: {movie_title}")
        print(f"Year: {movie_year}")
        print(f"IMDb Rating: {movie_rating}")
        print(f"Plot: {movie_plot}")
    else:
        print("Movie not found.")


while(True):
  
  user_query = input("\nHow can I Help you Sir?\n").lower()

  if("movie" in user_query):
    movie_title = input("Enter the movie title: ")
    fetch_movie_info(movie_title)
    
  elif("weather" in user_query):
    city = user_query.replace("weather", "") 
    
    api_key = "37d99f4c8bd8fa96d4509c54c8a262d7"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    response = requests.get(url)
    result = response.json()
    temperature = result["main"]["temp"]
    into_cel = round(temperature - 273.15)
    print(f"The current temperature in {city} is {into_cel} °C")


  elif 'browse' in user_query:
    site = input("Enter the Site: ")
    webbrowser.open(site)

  elif 'play music' in user_query:
            music_dir = 'D:\\'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))

  elif 'news' in user_query:

    api_key = "6b6cda5d67754feb960d2f2c6b5d2f7b"
    url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={api_key}"

    response = requests.get(url)
    data = response.json()

    if data["status"] == "ok":
        articles = data["articles"]
        news_list = []
        for article in articles:
            title = article["title"]
            source = article["source"]["name"]
            published_at = article["publishedAt"]
            url = article["url"]

            news_list.append({
                "title": title,
                "source": source,
                "published_at": published_at,
                "url": url
            })
    print()

    news_articles = news_list
    if news_articles is not None:
        for article in news_articles:
            print("Title:", article["title"])
            print("Source:", article["source"])
            print("Published At:", article["published_at"])
            print("URL:", article["url"])
            print()
    else:
        print("Failed to fetch news articles.")



  
  elif 'image' in user_query:
    api_key = "0TIZw3jNzqKT_DSbKlS8tXGj7Opnzyon4f7diDnJq58"

    query = input("Enter your image search query: ")
    url = f"https://api.unsplash.com/search/photos/?query={query}&client_id={api_key}"

    response = requests.get(url)
    data = response.json()

    if response.status_code == 200:
        results = data["results"]
        image_urls = []
        for result in results:
            image_urls.append(result["urls"]["regular"])

    image_urls = image_urls
    if image_urls is not None:
        for url in image_urls:
            print("Image URL:", url)
    else:
        print("Failed to fetch image search results.")
    
  
  print("\n__________________________________________________________________________________\n")