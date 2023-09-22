import re
import time
import pandas as pd
import streamlit as st
import datetime as dt
import plotly.express as px
from utils.helpers import get_actual_date

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image(
        "https://www.storymachine.de/assets2/img/storymachine.png",
        width=200,
    )

with col2:
    st.header("Data Team Dashboard")

st.sidebar.success("Choose Category")

st.title("#TeamRWE Keyword Monitoring")

st.image(
    "https://upload.wikimedia.org/wikipedia/commons/thumb/c/ca/LinkedIn_logo_initials.png/640px-LinkedIn_logo_initials.png",
    width=100,
)

my_bar = st.progress(0)

for percent_complete in range(100):
    time.sleep(0.05)
    my_bar.progress(percent_complete + 1)

df = pd.read_csv(
    "https://phantombuster.s3.amazonaws.com/UhrenaxfEnY/hIMTABCvWJ9KLONx3MeTpQ/teamrwe_keyword_search.csv"
)

df.insert(len(df.columns), "Keyword", "#TeamRWE")

df = df.dropna(how="any", subset=["textContent"])


df.drop(["connectionDegree", "timestamp"], axis=1, inplace=True)

df["postDate"] = df.postUrl.apply(get_actual_date)

df = df.dropna(how="any", subset=["postDate"])

df["date"] = pd.to_datetime(df["postDate"])

df.drop_duplicates(subset=["postUrl"], inplace=True)
df = df.reset_index(drop=True)

df["Total Interactions"] = df["likeCount"] + df["commentCount"]

df["likeCount"] = df["likeCount"].fillna(0)
df["commentCount"] = df["commentCount"].fillna(0)
df["Total Interactions"] = df["Total Interactions"].fillna(0)

df["likeCount"] = df["likeCount"].astype(int)
df["commentCount"] = df["commentCount"].astype(int)
df["Total Interactions"] = df["Total Interactions"].astype(int)


####################

col1, col2 = st.columns(2)

with col1:
    st.header("Select Time Range")

    number = st.number_input(
        "Select the days you want to see the posts",
        min_value=1,
        max_value=30,
        value=1,
        step=1,
    )
    if number:
        df = df[df["date"] >= (dt.datetime.now() - dt.timedelta(days=number))]
        st.success(f"Monitor Posts from last {int(number)} Days", icon="✅")

with col2:
    st.write("")


st.header("")
st.header("")

tab1, tab2 = st.tabs(["#TeamRWE", "Search for a Keyowrd Inside Posts"])

df_all = df
df_all["Hour"] = pd.to_datetime(df_all.postDate).dt.strftime("%H")

with tab1:
    if st.button("Show Data"):
        st.write(df_all)
    st.write(f"Total posts found in last Hours: ", df_all.shape[0])
    fig = px.bar(df_all, x="Hour", y="Total Interactions", color="Hour")
    fig.update_layout(showlegend=False, plot_bgcolor="rgba(0,0,0,0)")

    st.header(f"Most Recent Posts")
    st.info("Most recent posts appear first", icon="ℹ️")
    df_all.sort_values(["Total Interactions"], ascending=False, inplace=True)
    df_all = df_all.reset_index(drop=True)
    df_all_100 = df_all.head(10)
    num_posts = df_all_100.shape[0]

    if num_posts > 0:
        splits = df_all_100.groupby(df_all_100.index // 3)
        for _, frames in splits:
            frames = frames.reset_index(drop=True)
            thumbnails = st.columns(frames.shape[0])
            for i, c in frames.iterrows():
                with thumbnails[i]:
                    if not pd.isnull(c["profileImgUrl"]):
                        st.image(c["profileImgUrl"], width=150)
                    if not pd.isnull(c["profileUrl"]):
                        st.subheader(frames.fullName[i])
                        st.write("Personal Account")
                        st.write(c["title"])  # postType
                        st.write("-----------")
                        if not pd.isnull(c["postImgUrl"]):
                            st.image(c["postImgUrl"])
                        st.info(c["textContent"])  # postContent
                        st.write(
                            "Total Interactions 📈:  ", c["Total Interactions"]
                        )  # totInteractions
                        st.write("Likes 👍:  ", c["likeCount"])  # totInteractions
                        st.write("Comments 💬:  ", c["commentCount"])  # totInteractions
                        st.write(
                            "Publish Date & Time 📆:         ", c["postDate"]
                        )  # publishDate
                        with st.expander("Link to this Post 📮"):
                            st.write(c["postUrl"])  # linktoPost
                        with st.expander("Link to  Profile 🔗"):
                            st.write(c["profileUrl"])  # linktoProfile

                    if not pd.isnull(c["logoUrl"]):
                        st.image(c["logoUrl"], width=150)
                        st.subheader(c["companyName"])
                        st.write("Corporate Account")
                        st.write("👥:  ", c["followerCount"])
                        if not pd.isnull(c["postImgUrl"]):
                            st.image(c["postImgUrl"])
                        st.info(c["textContent"])  # postContent
                        st.write(
                            "Total Interactions 📈:  ", c["Total Interactions"]
                        )  # totInteractions
                        st.write("Likes 👍:  ", c["likeCount"])  # totInteractions
                        st.write("Comments 💬:  ", c["commentCount"])  # totInteractions
                        st.write(
                            "Publish Date & Time 📆:         ", c["postDate"]
                        )  # publishDate
                        with st.expander("Link to this Post 📮"):
                            st.write(c["postUrl"])  # linktoPost
                        with st.expander("Link to  Company Profile 🔗"):
                            st.write(c["companyUrl"])  # linktoProfile
    else:
        st.image(
            "https://img.freepik.com/premium-vector/hazard-warning-attention-sign-with-exclamation-mark-symbol-white_231786-5218.jpg?w=2000",
            width=200,
        )
        st.subheader("Oops... No new post found in last Hours.")


with tab2:
    title = st.text_input("Search for a keyword inside posts", "energy")
    title = title.lower()

    df_all.textContent = df_all.textContent.str.lower()

    df_all["client"] = df_all.textContent.str.contains(title)

    df_search = df_all.loc[df_all.client == 1]
    df_search = df_search.reset_index(drop=True)
    st.write(f"Posts found with keyword {title}:", df_search.shape[0])
    # st.write(df_search)

    st.header(f"Posts which mention the keyword {title}")
    num_posts = df_search.shape[0]

    if num_posts > 0:
        splits = df_search.groupby(df_search.index // 3)
        for _, frames in splits:
            frames = frames.reset_index(drop=True)
            thumbnails = st.columns(frames.shape[0])
            for i, c in frames.iterrows():
                with thumbnails[i]:
                    if not pd.isnull(c["profileImgUrl"]):
                        st.image(c["profileImgUrl"], width=150)
                    if not pd.isnull(c["profileUrl"]):
                        st.subheader(frames.fullName[i])
                        st.write("Personal Account")
                        st.write(c["title"])  # postType
                        st.write("-----------")
                        if not pd.isnull(c["postImgUrl"]):
                            st.image(c["postImgUrl"])
                        st.info(c["textContent"])  # postContent
                        st.write(
                            "Total Interactions 📈:  ", c["Total Interactions"]
                        )  # totInteractions
                        st.write("Likes 👍:  ", c["likeCount"])  # totInteractions
                        st.write("Comments 💬:  ", c["commentCount"])  # totInteractions
                        st.write(
                            "Publish Date & Time 📆:         ", c["postDate"]
                        )  # publishDate
                        with st.expander("Link to this Post 📮"):
                            st.write(c["postUrl"])  # linktoPost
                        with st.expander("Link to  Profile 🔗"):
                            st.write(c["profileUrl"])  # linktoProfile

                    if not pd.isnull(c["logoUrl"]):
                        st.image(c["logoUrl"], width=150)

                        st.subheader(c["companyName"])
                        st.write("Corporate Account")
                        st.write("👥:  ", c["followerCount"])
                        if not pd.isnull(c["postImgUrl"]):
                            st.image(c["postImgUrl"])
                        st.info(c["textContent"])  # postContent
                        st.write(
                            "Total Interactions 📈:  ", c["Total Interactions"]
                        )  # totInteractions
                        st.write("Likes 👍:  ", c["likeCount"])  # totInteractions
                        st.write("Comments 💬:  ", c["commentCount"])  # totInteractions
                        # st.write('Action 📌:  ',c['action']) #totInteractions
                        st.write(
                            "Publish Date & Time 📆:         ", c["postDate"]
                        )  # publishDate
                        with st.expander("Link to this Post 📮"):
                            st.write(c["postUrl"])  # linktoPost
                        with st.expander("Link to  Company Profile 🔗"):
                            st.write(c["companyUrl"])  # linktoProfile

    else:
        st.image(
            "https://img.freepik.com/premium-vector/hazard-warning-attention-sign-with-exclamation-mark-symbol-white_231786-5218.jpg?w=2000",
            width=200,
        )
        st.subheader(f"Oops... No new post found with keyword {title}.")
