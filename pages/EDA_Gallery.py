import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import seaborn as sn


st.set_page_config(page_title='CS-39AE Project2',
                   page_icon='Movies', layout='wide')


st.markdown(

"""
### **Netflix - Movies and TV Shows** 


Dataset Analysis [Netflix Movies and TV Shows Comprehensive Catalogs](https://www.kaggle.com/datasets/kainatjamil12/niteee)
"""

)


df = pd.read_csv('data/netflix_titles.csv', usecols=[0,1,2,3,5,7,8,9,10], low_memory=False)


def season_bargraph():
    shows = df[df["type"] == "TV Show"].copy()
    shows["seasons"] = shows["duration"].str.extract(r"(\d+)").astype(int)

    season = shows["seasons"].value_counts().sort_index()

    fig = go.Figure(
        go.Bar(
            x=season.index,
            y=season.values,
            marker_color="#E50914"
    )
    )

    fig.update_layout(
        title="Distribution of TV Show Seasons",
        xaxis_title="Number of Seasons",
        yaxis_title="Number of TV Shows",
        template="plotly_white"
    )

    return fig  


def dur_movies_bargraph():
    movies = df[df["type"] == "Movie"].copy()
    movies["durations"] = movies["duration"].str.extract(r"(\d+)").astype(int)

    bins = [0, 60, 90, 120, 150, 200, 300]
    labels = ["0–60", "61–90", "91–120", "121–150", "151–200", "200+"]
    movies["duration_bin"] = pd.cut(movies["durations"], bins=bins, labels=labels, right=False)

 
    duration_counts = movies["duration_bin"].value_counts().sort_index()

    fig = go.Bar(
            x=duration_counts.index,
            y=duration_counts.values,
            marker_color="#E50914"   # Netflix red
        )
    

    fig.update_layout(
        title="Distribution of Movie Durations (Minutes)",
        xaxis_title="Duration Range (Minutes)",
        yaxis_title="Number of Movies",
        template="plotly_white"
    )

    return fig









col = st.columns((2,2), gap='medium')

with col[0]:
    fig = season_bargraph()
    st.plotly_chart(fig, use_container_width=True)

with col[1]:
    fig = dur_movies_bargraph()
    st.plotly_chart(fig, use_container_width=True)


