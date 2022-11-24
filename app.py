import pickle       #transforms a complex object into a byte stream and vice versa
import streamlit as st      #app framework
import requests     #The requests module allows you to send HTTP requests using Python.
import base64   #used to embed raw image data into a CSS property such as background-image.

from PIL import Image   #used for image processing


def add_css(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
        background-size: cover
    }}
    #movie-recommendation-system {{
      color: #fff;
       text-align: center;
       font-size: 47px;
    }}
    .stSelectbox label {{
          color: #fff;
       text-align: center;
    }} 
    .row-widget.stButton {{
        text-align:center;
    }}
    .stAlert {{
       display:none;
    }}
    .css-1b0udgb {{
        color:#fff;
    }}
    .css-1en3hua .css-1b0udgb {{
        color:#000;
    }}
    .css-1en3hua .css-1v0mbdj {{
    width: 100%;
    height: auto;
    }}
    </style>
    """,
    unsafe_allow_html=True
    )
add_css('C:/Users/DIKSHA/Downloads/background.jpg') 

#opening the image
#image = Image.open('C:/Users/DIKSHA/Downloads/background.jpg')

#displaying the image on streamlit app
#st.image(image)


def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    recommended_movie_posters = []
    for i in distances[1:6]:
        # fetch the movie poster
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movie_posters.append(fetch_poster(movie_id))
        recommended_movie_names.append(movies.iloc[i[0]].title)

    return recommended_movie_names,recommended_movie_posters


st.header('MOVIE RECOMMENDATION SYSTEM')
movies = pickle.load(open('movie_list.pkl','rb'))
similarity = pickle.load(open('similarity.pkl','rb'))

movie_list = movies['title'].values

selected_movie = st.selectbox(
    "Type or select a movie from the dropdown: ",
    movie_list
)

if st.button('Show Recommendation'):
    recommended_movie_names,recommended_movie_posters = recommend(selected_movie)
    col1, col2, col3, col4, col5 = st.beta_columns(5)
    with col1:
        #st.text(recommended_movie_names[0])
        st.image(recommended_movie_posters[0], 
        caption= recommended_movie_names[0])
    with col2:
        #st.text(recommended_movie_names[1])
        st.image(recommended_movie_posters[1], 
        caption= recommended_movie_names[1])

    with col3:
       # st.text(recommended_movie_names[2])
        st.image(recommended_movie_posters[2], 
        caption= recommended_movie_names[2])
    with col4:
       # st.text(recommended_movie_names[3])
        st.image(recommended_movie_posters[3], 
        caption= recommended_movie_names[3])
    with col5:
       # st.text(recommended_movie_names[4])
        st.image(recommended_movie_posters[4], 
        caption= recommended_movie_names[4]
        )





