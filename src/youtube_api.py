import os
import pandas as pd
from googleapiclient.discovery import build
from dotenv import load_dotenv


# Mapping YouTube category IDs to readable names
CATEGORY_MAPPING = {
    "1": "Film & Animation",
    "2": "Autos & Vehicles",
    "10": "Music",
    "15": "Pets & Animals",
    "17": "Sports",
    "18": "Short Movies",
    "19": "Travel & Events",
    "20": "Gaming",
    "21": "Videoblogging",
    "22": "People & Blogs",
    "23": "Comedy",
    "24": "Entertainment",
    "25": "News & Politics",
    "26": "Howto & Style",
    "27": "Education",
    "28": "Science & Technology",
    "29": "Nonprofits & Activism",
    "30": "Movies",
    "31": "Anime/Animation",
    "32": "Action/Adventure",
    "33": "Classics",
    "34": "Comedy",
    "35": "Documentary",
    "36": "Drama",
    "37": "Family",
    "38": "Foreign",
    "39": "Horror",
    "40": "Sci-Fi/Fantasy",
    "41": "Thriller",
    "42": "Shorts",
    "43": "Shows",
    "44": "Trailers"
}

# Load API key from .env
load_dotenv()
API_KEY = os.getenv("YOUTUBE_API_KEY")

def fetch_trending_videos(region_code='US', max_results=25):
    youtube = build('youtube', 'v3', developerKey=API_KEY)
    
    # Fetch trending videos
    request = youtube.videos().list(
        part='snippet,statistics',
        chart='mostPopular',
        regionCode=region_code,
        maxResults=max_results
    )
    response = request.execute()
    
    videos = []
    for item in response['items']:
        videos.append({
            'Title': item['snippet']['title'],
            'Channel': item['snippet']['channelTitle'],
            'CategoryID': item['snippet']['categoryId'],
            'Views': int(item['statistics'].get('viewCount', 0)),
            'Likes': int(item['statistics'].get('likeCount', 0)),
            'Comments': int(item['statistics'].get('commentCount', 0)),
            'PublishedAt': item['snippet']['publishedAt']
        })
    
    df = pd.DataFrame(videos)
    df['Category'] = df['CategoryID'].astype(str).map(CATEGORY_MAPPING)
    df.drop(columns=['CategoryID'], inplace=True)
    return df


if __name__ == "__main__":
    # Try India (IN) or US
    df = fetch_trending_videos('IN', 10)
    print(df.head())
