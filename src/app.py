import streamlit as st
import plotly.express as px
from youtube_api import fetch_trending_videos

# Streamlit page settings
st.set_page_config(page_title="YouTube Trends Analyzer", layout="wide")
st.title("🎬 YouTube Trends Analyzer")

# Sidebar filters
st.sidebar.header("Filter Options")
region = st.sidebar.selectbox("Select Country", ["US", "IN", "GB", "DE", "BR", "JP"])
max_results = st.sidebar.slider("Number of Videos", 10, 50, 25)

# Fetch data button
if st.sidebar.button("Fetch Trending Videos"):
    with st.spinner("Fetching trending videos..."):
        df = fetch_trending_videos(region, max_results)

# Save fetched data to CSV
    csv_path = f"data/trending_{region}.csv"
    df.to_csv(csv_path, index=False)
    st.success(f"✅ Data saved to {csv_path}")

# Download CSV button
    st.download_button(
    label="📥 Download CSV",
    data=df.to_csv(index=False).encode('utf-8'),
    file_name=f"trending_{region}.csv",
    mime='text/csv'
)


    st.subheader(f"Top {max_results} Trending Videos in {region}")
    st.dataframe(df)
    category_counts = df['Category'].value_counts().reset_index()
    category_counts.columns = ['Category', 'Count']
    fig_cat = px.bar(category_counts, x='Category', y='Count',
                     title="Trending Videos by Category", color='Count')
    st.plotly_chart(fig_cat, use_container_width=True)

    
    # Plot 1 — Top Channels by Views
    top_channels = df.groupby("Channel", as_index=False)["Views"].sum().sort_values(by="Views", ascending=False).head(10)
    fig1 = px.bar(top_channels, x="Channel", y="Views", title="Top Channels by Total Views", color="Views")
    st.plotly_chart(fig1, use_container_width=True)

    # Plot 2 — Engagement scatter
    fig2 = px.scatter(df, x="Likes", y="Views", size="Comments", color="Channel",
                      hover_name="Title", title="Engagement Overview (Likes vs Views)",
                      size_max=30)
    st.plotly_chart(fig2, use_container_width=True)

    # Plot 3 — Likes-to-Views ratio
    df["Like_View_Ratio"] = df["Likes"] / df["Views"]
    fig3 = px.histogram(df, x="Like_View_Ratio", nbins=20, title="Like-to-View Ratio Distribution")
    st.plotly_chart(fig3, use_container_width=True)

else:
    st.info("👈 Use the sidebar to select region and number of videos, then click *Fetch Trending Videos*.")
