import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import seaborn as sn


st.set_page_config(page_title='CS-39AE Project2',
                   page_icon='Movies', layout='wide')


st.markdown(

"""
Netflix 
"""
"""
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
        yaxis_title="Count",
        template="plotly_dark"
    )

    fig.show()


col = st.columns((2,2), gap='medium')

with col[0]:
    season_bargraph()

