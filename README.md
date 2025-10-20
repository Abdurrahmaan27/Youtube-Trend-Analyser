# 🎬 YouTube Trends Analyzer

**YouTube Trends Analyzer** is an interactive Python web application that fetches and analyzes trending videos on YouTube across different regions. 
It provides insights into video popularity, engagement, categories, and top channels using real-time data from the YouTube Data API v3.

<img width="900" height="700" alt="image" src="https://github.com/user-attachments/assets/80ec22cb-d157-4798-97dc-ac6959936d70" />


## 🔹 Features

- **Regional Analysis:** Fetch trending videos for multiple countries and compare content preferences.  

- **Category Insights:** Map YouTube category IDs to readable names and visualize trending categories.  

- **Engagement Metrics:** Analyze views, likes, and comments for deeper understanding of audience engagement.  

- **Data Export:** Save fetched data to CSV and download directly from the app.  

- **Interactive Visualizations:** View top channels by views, engagement scatter plots, and category distributions using Plotly.

<img width="900" height="700" alt="image" src="https://github.com/user-attachments/assets/69ee5ac8-3064-4567-a540-0d10321c1bef" />


## 🛠️ Technologies Used

- **Python** – Data processing and API integration  

- **Pandas** – Data cleaning and manipulation  

- **Plotly** – Interactive charts and visualizations  

- **Streamlit** – Web application frontend  

- **Google API Python Client** – Access YouTube Data API v3  

- **python-dotenv** – Manage API keys securely

---

## ⚡ Installation & Setup

#### 1. Clone the repository:
```
git clone https://github.com/<yourusername>/youtube-trends-analyzer.git
cd youtube-trends-analyzer
```



#### 2. Create and activate a virtual environment:
```
python3 -m venv env
source env/bin/activate
```



#### 3. Install dependencies:
```
pip install -r requirements.txt
```



#### 4. Create a .env file in the root folder with your YouTube API key:
```
YOUTUBE_API_KEY=your_api_key_here
```



#### 5. Run the Streamlit app:
```
streamlit run src/app.py
```



#### 6. Open the app in your browser at http://localhost:8501

# Responses

<img width="900" height="700" alt="image" src="https://github.com/user-attachments/assets/e38151f2-faf8-40c1-99b2-f22c2318403c" />

<img width="900" height="700" alt="image" src="https://github.com/user-attachments/assets/8fc2f191-c58d-4064-b8d3-0f0b4488341c" />


# Usage
  - Select the country and number of trending videos from the sidebar.
  
  - Fetch trending videos and view the data table and visualizations.
  
  - Save the data as CSV and optionally download it.
  
  - Explore engagement and category trends interactively.
  

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact
For any queries contact - Abraham @ abdurrahamaan27@gmail.com
