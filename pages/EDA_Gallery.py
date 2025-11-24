import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import seaborn as sn


#[theme]
#base = 'light'

st.set_page_config(page_title='CS-39AE Project2',
                   page_icon='Movies', layout='wide')


st.markdown(

'''
<style>
    .stApp 
        background-color: #FFFFFF;  


</style>


### **Netflix - Movies and TV Shows** 


Dataset Analysis [Netflix Movies and TV Shows Comprehensive Catalogs](https://www.kaggle.com/datasets/kainatjamil12/niteee)


''', unsafe_allow_html=True
)


df = pd.read_csv('data/netflix_titles.csv', usecols=[0,1,2,3,5,7,8,9,10], low_memory=False)
df = df.dropna(subset=['type', 'country', 'duration'])

# 1st Graph
def season_bargraph():
    shows = df[df['type'] == 'TV Show'].copy()
    shows['seasons'] = shows['duration'].str.extract(r'(\d+)').astype(int)
    showsC = shows['seasons'].value_counts().sort_index().reset_index()

    fig = px.bar(showsC,
        x='seasons',
        y='count',
        color='count',
        color_continuous_scale=[ '#FF5A5A','#E50914'],  
        labels={'seasons': 'Number of Seasons: ', 'count': '# of TV Shows: '},
        title='Distribution of TV Show Seasons'
    )


    fig.update_layout(
        font=dict(color='black', size=14),
        xaxis=dict(title='Number of Seasons'),
        yaxis=dict(title='Number of TV Shows')
    )

    fig.update_traces(textposition='none', showlegend=False)

    return fig
    

#2nd Graph
def dur_movies_bargraph():
    movies = df[df['type'] == 'Movie'].copy()
    movies['durations'] = movies['duration'].str.extract(r'(\d+)').astype(int)

    bins = [0, 60, 90, 120, 150, 200, 300]
    labels = ['0–60', '61–90', '91–120', '121–150', '151–200', '200+']
    movies['duration(mins)'] = pd.cut(movies['durations'], bins=bins, labels=labels, right=False)
    moviesB = movies['duration(mins)'].value_counts().sort_index().reset_index()

    fig = px.bar(moviesB,
        x='duration(mins)',
        y='count',
        color='count',
        color_continuous_scale=['#FF5A5A','#E50914'], 
        labels={'duration(mins)': 'Durations (Minutes)', 'count': 'Number of Movies'},
        title='Distribution of Movie Durations (Minutes)'
    )

    fig.update_layout(
        font=dict(color='black', size=14),
        xaxis=dict(title='Duration (Mins)'),
        yaxis=dict(title='Number of Movies')
    )
    fig.update_traces(textposition='none', showlegend=False)
    return fig

#3rd graph

def rating_pie():
    rating_counts = df['rating'].value_counts().reset_index()
    #print(rating_counts)

    high_contrast_colors = ['#E50914', '#0A84FF',  '#34C759',  '#FF9500','#AF52DE',  '#FFD60A',  '#FF2D55']

    fig = px.pie(rating_counts,
        names='rating',
        values='count',
        title='Distribution of Ratings',
        labels={'rating': 'Rating', 'count': 'Number'},
        color='rating',
        color_discrete_sequence= high_contrast_colors)

    fig.update_layout(
        template='plotly_white',
        font=dict(color='black', size=14),
        title_x=0.5
    )

    return fig



col = st.columns((2,2), gap='medium', border=True)

with col[0]:
    st.markdown('')
    fig1 = season_bargraph()
    fig3 = rating_pie()
    st.plotly_chart(fig1, width='stretch')
    st.plotly_chart(fig3, width='stretch')
    

with col[1]:
    st.markdown('')
    fig2 = dur_movies_bargraph()
    st.plotly_chart(fig2, width='stretch')




