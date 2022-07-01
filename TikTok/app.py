import os
import streamlit as st
# import pandas to load analytics data
import pandas as pd
# from tiktok import get_data
# import subprocess to run tiktok scripy from cmd line
from subprocess import call
# import plotly for viz
import plotly.express as px

# set page to wide
st.set_page_config(layout='wide')

# Create sidebar
st.sidebar.markdown("<div><img src = 'https://www.liblogo.com/img-logo/ti459tfcd-tiktok-logo-the-new-tiktok-logo-png-2022.png' width=100/><h1 style=display:inline>Tiktok Analytics</h1></div>", unsafe_allow_html=True)
st.sidebar.markdown("Use this dashboard to get TikTok data with hashtags📈")
st.sidebar.markdown("To get started: <ol><li>Search for any tiktok Hashtag</li><li>Scroll down to analyze stats</li></ol>", unsafe_allow_html=True)

# Input
hashtag = st.text_input('Search for a TikTok hashtag here', value="")

# Button
if st.button('Get Data'):
    st.subheader('#'+hashtag+' data from Tiktok')
    call(['python', 'tiktok.py', hashtag])

    # load existing data
    path = os.path.dirname(__file__)
    my_file = path+'tiktokdata.csv'
    df = pd.read_csv(my_file)

    # Split page
    left, right = st.columns(2)

    # Left - Video Stats
    scatter1 = px.scatter(df, x='stats_shareCount', y='stats_commentCount', hover_data=['desc'], size='stats_playCount', color='stats_playCount')
    left.plotly_chart(scatter1, use_container_width=True)

    # Right - Author Stats
    scatter2 = px.scatter(df, x='authorStats_videoCount', y='authorStats_heartCount', hover_data=['author_nickname'], size='authorStats_followerCount', color='authorStats_followerCount')
    right.plotly_chart(scatter2, use_container_width=True)

    # Plot viz
    fig = px.histogram(df, x='desc', y='stats_diggCount', hover_data=['desc'], height=300)
    st.plotly_chart(fig, use_container_width=True)

    # show df in streamlit
    df
