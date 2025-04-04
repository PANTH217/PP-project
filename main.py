import pandas as pd
import streamlit as st
import random
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neighbors import NearestNeighbors

# 🎬 Set Page Title & Icon
st.set_page_config(page_title="Movies Finder", page_icon="🎥", layout="wide")

# ✅ 50+ Fun Movie Quotes (Auto-Displayed)
movie_quotes = [
   "🎥 \"May the Force be with you.\" – Star Wars",
    "🍿 \"I'll be back.\" – The Terminator",
    "🎬 \"Why so serious?\" – The Dark Knight",
    "🔥 \"Keep your friends close, but your enemies closer.\" – The Godfather II",
    "💥 \"With great power comes great responsibility.\" – Spider-Man",
    "🎭 \"I'm the king of the world!\" – Titanic",
    "🔫 \"Say hello to my little friend!\" – Scarface",
    "🕶 \"I see dead people.\" – The Sixth Sense",
    "🐍 \"Why did it have to be snakes?\" – Indiana Jones",
    "🦇 \"It’s not who I am underneath, but what I do that defines me.\" – Batman Begins",
    "⏳ \"To infinity… and beyond!\" – Toy Story",
    "🚗 \"Roads? Where we’re going, we don’t need roads.\" – Back to the Future",
    "🎤 \"You talking to me?\" – Taxi Driver",
    "💀 \"Hasta la vista, baby.\" – Terminator 2",
    "🎭 \"Houston, we have a problem.\" – Apollo 13",
    "🎶 \"Hakuna Matata!\" – The Lion King",
    "👻 \"Who ya gonna call? Ghostbusters!\" – Ghostbusters",
    "🧙 \"One does not simply walk into Mordor.\" – The Lord of the Rings",
    "🚢 \"You jump, I jump, remember?\" – Titanic",
    "🔮 \"After all this time? Always.\" – Harry Potter",
    "🚀 \"I feel the need... the need for speed!\" – Top Gun",
    "🔪 \"A boy’s best friend is his mother.\" – Psycho",
    "🚬 \"Of all the gin joints in all the towns in all the world, she walks into mine.\" – Casablanca",
    "🍔 \"They call it a Royale with Cheese.\" – Pulp Fiction",
    "🎩 \"My mama always said life was like a box of chocolates.\" – Forrest Gump",
    "🎞️ \"Elementary, my dear Watson.\" – The Adventures of Sherlock Holmes",
    "🎥 \"I'm just a girl, standing in front of a boy, asking him to love her.\" – Notting Hill",
    "⚡ \"It's alive! It's alive!\" – Frankenstein",
    "🎵 \"You can't handle the truth!\" – A Few Good Men",
    "🦁 \"The night is darkest just before the dawn. And I promise you, the dawn is coming.\" – The Dark Knight"
]

# ✅ 100+ Fun Movie Facts (Auto-Displayed)
movie_facts = [
     "🎬 The first movie ever made was 'Roundhay Garden Scene' (1888), lasting just 2.11 seconds.",
    "🍿 'Psycho' (1960) was the first U.S. film to show a toilet being flushed, which was controversial at the time.",
    "🔥 'The Godfather' used real mafia members as consultants, and some even appeared in the movie.",
    "🎞️ 'Gone with the Wind' (1939) is the highest-grossing film of all time (adjusted for inflation).",
    "🎬 'The Lion King' (1994) took three years to animate just the wildebeest stampede scene.",
    "🤯 'The Matrix' (1999) used real code in its green falling text, which was taken from a sushi cookbook!",
    "🔥 'Titanic' (1997) cost more to make ($200 million) than the actual Titanic ship ($7.5 million in 1912, adjusted for inflation).",
    "🍿 'Avengers: Endgame' (2019) was the first film in history to surpass $1 billion in just five days!",
    "🎥 The T-Rex roar in 'Jurassic Park' was created using a mix of elephant, tiger, and alligator sounds.",
    "🎞️ Samuel L. Jackson’s wallet in 'Pulp Fiction' actually belongs to Quentin Tarantino and says 'Bad Mother F***er'.",
    "🎬 The iconic 'I am your father' twist in 'Star Wars: The Empire Strikes Back' was kept a secret from nearly everyone, even the cast.",
    "🐍 Indiana Jones' fear of snakes was inspired by director Steven Spielberg's real-life phobia.",
    "🎭 'The Dark Knight' (2008) was the first major film to use IMAX cameras.",
    "🎥 'The Shining' (1980) used over 900 tons of salt to create the famous snowy hedge maze.",
    "🍿 'Schindler’s List' (1993) was shot almost entirely in black and white to match historical footage.",
    "💥 'Inception' (2010) took 10 years for Christopher Nolan to complete the script.",
    "🔮 'Harry Potter' actors were banned from playing Quidditch on set due to safety concerns.",
    "🎭 'The Lord of the Rings' used over 48,000 handmade pieces of armor.",
    "🐉 The dragon Smaug from 'The Hobbit' was voiced by Benedict Cumberbatch using motion capture.",
    "🚀 'Gravity' (2013) was filmed in a custom-built LED light box to simulate zero gravity.",
    "🎬 'The Joker' in 'The Dark Knight' had all of his makeup applied by Heath Ledger himself to make it look natural.",
    "🔥 'Frozen' (2013) is the most-watched animated movie of all time.",
    "🎞️ 'The Blair Witch Project' (1999) had a marketing campaign that convinced people it was real footage.",
    "🎭 The famous rain scene in 'Singin’ in the Rain' used a mix of milk and water to make the rain visible on camera.",
    "🚢 The 'Titanic' set was built at 90% scale for realism.",
    "🎬 The longest film ever made is 'Logistics' (2012), lasting 857 hours (35 days).",
    "🧙 The 'Harry Potter' franchise has made over $9 billion worldwide.",
    "🔥 'Jaws' (1975) was meant to show the shark frequently, but mechanical failures forced Spielberg to keep it hidden.",
    "🎭 'Rocky' (1976) was filmed in just 28 days with a budget of $1 million.",
]

# ✅ Display Title, Random Movie Quote & Fact
st.markdown("<h1 style='text-align: center; color: #FFD700;'>🎬 Movie Finder System</h1>", unsafe_allow_html=True)
st.markdown(f"<h3 style='text-align: center;'>{random.choice(movie_quotes)}</h3>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center; color: #FF5733;'>🎭 Fun Movie Fact:</h2>", unsafe_allow_html=True)
st.markdown(f"""
    <h3 style='text-align: center; background-color: #FFD700; color: black; padding: 10px; border-radius: 10px;'>
        {random.choice(movie_facts)}
    </h3>
""", unsafe_allow_html=True)

# ✅ Load Movie Dataset
@st.cache_data
def load_data():
    df = pd.read_csv("movies.csv", nrows=60000)
    df.columns = df.columns.str.strip().str.lower()
    if "title" in df.columns and "genres" in df.columns:
        df["title"] = df["title"].astype(str).str.strip().str.lower()
        df["content"] = df["genres"].str.replace("|", " ", regex=True).fillna("").str.strip()
        if "overview" in df.columns:
            df["overview"] = df["overview"].fillna("")
            df["content"] = df["title"] + " " + df["genres"] + " " + df["overview"]
        else:
            df["content"] = df["title"] + " " + df["genres"] + " A movie in the given genre."
        df = df[df["content"].str.strip() != ""]
        if df.empty:
            st.error("⚠ No valid movie data found! Check dataset.")
            st.stop()
    else:
        st.error("❌ 'title' or 'genres' column not found! Check dataset.")
        st.stop()
    return df

movies = load_data()

# ✅ Movie Finder System
@st.cache_data
def compute_tfidf(data):
    vectorizer = TfidfVectorizer(stop_words="english", max_features=10000)
    return vectorizer.fit_transform(data)

tfidf_matrix = compute_tfidf(movies["content"])

def train_nearest_neighbors(tfidf_matrix):
    nn = NearestNeighbors(metric="cosine", algorithm="brute", n_neighbors=6)
    nn.fit(tfidf_matrix)
    return nn

model_nn = train_nearest_neighbors(tfidf_matrix)

def recommend_movie(movie_title):
    movie_title = movie_title.strip().lower()
    available_titles = movies["title"].tolist()
    exact_match = [t for t in available_titles if t == movie_title]
    similar_matches = [t for t in available_titles if movie_title in t]
    if not exact_match and not similar_matches:
        st.error(f"❌ Movie '{movie_title}' not found! Try another name.")
        return ["Not available."]
    selected_title = exact_match[0] if exact_match else similar_matches[0]
    idx = movies[movies["title"] == selected_title].index[0]
    distances, indices = model_nn.kneighbors(tfidf_matrix[idx])
    return [movies.iloc[i]["title"].title() for i in indices[0][1:]]

# 🎬 Enter Movie Name
st.markdown("<h2 style='text-align: center;'>🎬 Enter a  Name:</h2>", unsafe_allow_html=True)
movie_name = st.text_input("", placeholder="Type a name here...")

# ✅ Display Movies (Auto-Displayed After Input)
if movie_name:
    st.markdown("<h2 style='text-align: center;'>🔥Movies Found:</h2>", unsafe_allow_html=True)
    recommendations = recommend_movie(movie_name)
    for rec in recommendations:
        st.markdown(f"<h4 style='text-align: center; color: #FFD700;'>✅ {rec}</h4>", unsafe_allow_html=True)
