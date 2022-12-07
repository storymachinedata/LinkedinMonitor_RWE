import numpy as np
import altair as alt
import pandas as pd
import streamlit as st

#from st_aggrid import AgGrid

#import pandas_profiling
#from streamlit_pandas_profiling import st_profile_report

from datetime import datetime,timedelta
import pytz
import re

#from germansentiment import SentimentModel

st.set_page_config(layout="wide")


with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

import time

col1,col2= st.columns(2)

with col1:
   #st.header("A cat")
   st.image("https://storymachine.mocoapp.com/objects/accounts/a201d12e-6005-447a-b7d4-a647e88e2a4a/logo/b562c681943219ea.png", width=200)
   
with col2:
   
   st.header("Data Team Dashboard")

st.sidebar.success("Choose Category")

st.title('LinkedIn Live Monitoring')

st.image(
    "https://upload.wikimedia.org/wikipedia/commons/thumb/c/ca/LinkedIn_logo_initials.png/640px-LinkedIn_logo_initials.png",
    width=100,
)


with st.expander('Monitoring Posts of Given Companies from LinkedIn everyday'):
     st.write('')

my_bar = st.progress(0)

for percent_complete in range(100):
     time.sleep(0.05)
     my_bar.progress(percent_complete + 1)





#st.balloons()

#st.header('`streamlit_pandas_profiling`')

st.header('Companies Posts last 12 Months')



df =pd.read_csv('https://phantombuster.s3.amazonaws.com/UhrenaxfEnY/oxZonAvAoy7dQrL90UuZqA/ruben_company_posts.csv')
#df2 =pd.read_csv('https://phantombuster.s3.amazonaws.com/UhrenaxfEnY/Vx2c6OJZ59781jp9zKPViw/Andere_CEOs_2.csv')
#df3 =pd.read_csv('https://phantombuster.s3.amazonaws.com/UhrenaxfEnY/JUeq71McCykmR5ZrlZTJdQ/Andere_CEOs_3.csv')

##frames = [df1, df2, df3]

#df = pd.concat(frames)

df = df.dropna(how='any', subset=['postContent'])


df.drop(['viewCount'], axis=1, inplace=True)


#st.write(df.profileUrl.value_counts())



df['Company']  = df['action']

df.loc[df.profileUrl == "https://www.linkedin.com/company/orsted/", "Company"] = "Ørsted"
df.loc[df.profileUrl == "https://www.linkedin.com/company/rwe-", "Company"] = "RWE"
df.loc[df.profileUrl == "https://www.linkedin.com/company/engie/", "Company"] = "ENGIE"
df.loc[df.profileUrl == "https://www.linkedin.com/company/e-on/", "Company"] = "E.ON"
df.loc[df.profileUrl == "https://www.linkedin.com/company/iberdrola/", "Company"] = "Iberdrola"
df.loc[df.profileUrl == "https://www.linkedin.com/company/uniper-se/", "Company"] = "Uniper"
df.loc[df.profileUrl == "https://www.linkedin.com/company/enbw/", "Company"] = "EnBW Energie Baden"
df.loc[df.profileUrl == "https://www.linkedin.com/company/edf/", "Company"] = "EDF"
df.loc[df.profileUrl == "https://www.linkedin.com/company/vattenfall/", "Company"] = "Vattenfall"
df.loc[df.profileUrl == "https://www.linkedin.com/company/nextera-energy-inc/", "Company"] = "NextEra Energy, Inc."




def getActualDate(url):

    a= re.findall(r"\d{19}", url)

    a = int(''.join(a))

    a = format(a, 'b')

    first41chars = a[:41]

    ts = int(first41chars,2)

    #tz = pytz.timezone('Europe/Paris')

    actualtime = datetime.fromtimestamp(ts/1000).strftime("%Y-%m-%d %H:%M:%S %Z")

    return actualtime

df['postDate'] = df.postUrl.apply(getActualDate)


df = df.dropna(how='any', subset=['postDate'])


import datetime as dt

#def datenow(date):
     #a = re.(datetime.now() - df.postDate.days >1:)

#df5= df
#df5['date'] =  pd.to_datetime(df5['postDate'])
df['date'] =  pd.to_datetime(df['postDate'])

df['Total_Interactions'] = df['likeCount'] + df['commentCount']


df['profileImg']  = df['action']

df.loc[df.profileUrl == "https://www.linkedin.com/company/orsted/", "profileImg"] = "https://media-exp1.licdn.com/dms/image/C4D0BAQFdfN5NpZ_MaQ/company-logo_200_200/0/1556536677355?e=1677715200&v=beta&t=DptUnIdy5Rj8V2osg2Rr-2LzF_6jc5ihneWCcjWj2so"
df.loc[df.profileUrl == "https://www.linkedin.com/company/rwe-", "profileImg"] = "https://media-exp1.licdn.com/dms/image/C4D0BAQHcUAokOSCKEg/company-logo_200_200/0/1569830150461?e=1677715200&v=beta&t=oadmmk3lkKcr50qtA2SqPqA1O_SdizkfrQl2hlwsWKo"
df.loc[df.profileUrl == "https://www.linkedin.com/company/engie/", "profileImg"] = "https://media-exp1.licdn.com/dms/image/C4D0BAQHQn5EB4SKDyg/company-logo_200_200/0/1579011791766?e=1677715200&v=beta&t=1YdQUvOkPxZ5YDkgilyBj-s3RPu1pSX4wen8qSLwr_g"
df.loc[df.profileUrl == "https://www.linkedin.com/company/e-on/", "profileImg"] = "https://media-exp1.licdn.com/dms/image/C4D0BAQF7fed0Gm-rYg/company-logo_200_200/0/1539172087292?e=1677715200&v=beta&t=rUaxzD5r96vkDbIwP1aFMXGbqA00glHZl1ACBolg44w"
df.loc[df.profileUrl == "https://www.linkedin.com/company/iberdrola/", "profileImg"] = "https://media-exp1.licdn.com/dms/image/D4D0BAQHOakeSm8V2Yg/company-logo_200_200/0/1666261647681?e=1677715200&v=beta&t=zerWiX43RWRqDfPrA4M0wAY1bsiXdCsttaLW5ZPMd4M"
df.loc[df.profileUrl == "https://www.linkedin.com/company/uniper-se/", "profileImg"] = "https://media-exp1.licdn.com/dms/image/C4E0BAQE8g5waUJEVow/company-logo_200_200/0/1657029511212?e=1677715200&v=beta&t=Jpuz8vEsXJ3x4zWTqDb9-sS-MQqWJ8DlpkARAk1apws"
df.loc[df.profileUrl == "https://www.linkedin.com/company/enbw/", "profileImg"] = "https://media-exp1.licdn.com/dms/image/C4E0BAQGOTQwlLPPsYw/company-logo_200_200/0/1659342744439?e=1677715200&v=beta&t=lD5wc8X4ERrWvYTUROO7WVmQZc32sAv3VoGWKnPo1L4"
df.loc[df.profileUrl == "https://www.linkedin.com/company/edf/", "profileImg"] = "https://media-exp1.licdn.com/dms/image/C560BAQEUXtrGCgAHtg/company-logo_200_200/0/1519855919046?e=1677715200&v=beta&t=TdCdSwy6NjEbaYig9Cd3SmaSSH4zMkAOQ49KmRPw6cE"
df.loc[df.profileUrl == "https://www.linkedin.com/company/vattenfall/", "profileImg"] = "https://media-exp1.licdn.com/dms/image/C560BAQG2Kguh_TApgg/company-logo_200_200/0/1557400339213?e=1677715200&v=beta&t=-Shl_rTZuxaB_2ueIAvDVc1j65YCeqqCKB3JERG0wis"
df.loc[df.profileUrl == "https://www.linkedin.com/company/nextera-energy-inc/", "profileImg"] = "https://media-exp1.licdn.com/dms/image/C510BAQF2kQU50Z1HMQ/company-logo_200_200/0/1519878816695?e=1677715200&v=beta&t=nwAmx2ovN4qsvTu-wT-py6DbYKbU1BhWGrtowpD5lMY"








#st.write(df.profileImg.value_counts())
df30 = df[df['date']>=(dt.datetime.now()-dt.timedelta(days=365))] #hours = 6,12, 24

df30['likeCount'] = df30['likeCount'].astype(int)
df30['commentCount'] = df30['commentCount'].astype(int)
df30['Total_Interactions'] = df30['Total_Interactions'].astype(int)



#st.write(df30.head())
#AgGrid(df30, height=500, fit_columns_on_grid_load=True)

if st.button('Show Data'):
    AgGrid(df30, height=500, fit_columns_on_grid_load=True)

#st.write(df30)
st.write(f'Total posts in last 12 Months: ', df30.shape[0])
#df5 = df['date'].last('24h')

st.subheader('No of Posts for each Companies from last 12 Months')



#st.write(df30.CEO.value_counts())

df12 = df30['Company'].value_counts()
st.bar_chart(df12)

# date_to_monitor = st.date_input('Choose a date to see the post that created after that',value=datetime.today() - timedelta(days=1))
# st.write(date_to_monitor)

number = st.number_input('Select the days you want to see the posts', min_value=1, max_value=360, value=5, step=1)
#st.write('The current number is ', number)

st.header(f'Post from last {int(number)} days')



df5 = df[df['date']>=(dt.datetime.now()-dt.timedelta(days=number))] #hours = 6,12, 24


cols = ['Company','postContent','postUrl','likeCount','commentCount','Total_Interactions','postDate','profileUrl', 'imgUrl','profileImg','type','action', 'repostCount']
df5 = df5[cols]
df5.sort_values(['Total_Interactions'], ascending=False, inplace=True)


#df5 = df5["imgUrl"].str.replace("<NA>","https://www.citypng.com/public/uploads/preview/download-horizontal-black-line-png-31631830482cvrhyz46le.png")

df5['likeCount'] = df5['likeCount'].astype(int)
df5['commentCount'] = df5['commentCount'].astype(int)
df5['Total_Interactions'] = df5['Total_Interactions'].astype(int)

df5 = df5.reset_index(drop=True)




if st.button(f'Show Data for past {int(number)} days'):
    st.write(df5)

#st.write(f'Number of posts in last {int(number)} days: ', df5.shape[0])

col3, col4 = st.columns(2)
col3.metric(f'Number of posts in last {int(number)} days: ',"", df5.shape[0])
#col4.metric(f'Number of Posts in last one year: ', df_CEO.shape[0])


#st.write(df5)
@st.cache
def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
    return df.to_csv().encode('utf-8')

csv = convert_df(df5)
st.download_button(
    label="Download data as CSV",
    data=csv,
    file_name='Companies_post_past24Hr.csv',
    mime='text/csv',
)






   



#st.write(a)




st.subheader(f'Total Interactions for each Companies : last {int(number)} days')
#x = df5.plot(kind='bar', x='CEO', y='Total_Interactions', figsize=(20,10), ylabel='View Counts')
st.bar_chart(df5, x='Company', y='Total_Interactions',use_container_width=True)
#st.sidebar.header('Input')

st.header(f'Top Interacting Posts in last {int(number)} days')


#defining three side-by-side columns

#col1, col2, col3 = st.columns(3)



num_posts = df5.shape[0]

if  num_posts>0:

     #splits = np.array_split(df5,5)
     splits = df5.groupby(df5.index // 3)
     for _, frames in splits:
          frames = frames.reset_index(drop=True)
          #print(frames.head())
          thumbnails = st.columns(frames.shape[0])
          for i, c in frames.iterrows():
               with thumbnails[i]:

                    if not pd.isnull(c['profileImg']):
                        st.image(c['profileImg'], width=150)
                    st.subheader(frames.Company[i])
                    #st.write('Company & Industry:  ',c['Company']) #postType
                    
                       

                    with st.expander('Post Content 📜'):
                         st.write(c['postContent'])  #postContent
                    st.write('Type of Post 📨:  ',c['type']) #postType
                    st.write('Total Interactions 📈:  ',c['Total_Interactions']) #totInteractions
                    st.write('Likes 👍:  ',c['likeCount']) #totInteractions
                    st.write('Comments 💬:  ',c['commentCount']) #totInteractions
                    st.write('Action 📌:  ',c['action']) #totInteractions
                    st.write('Publish Date & Time 📆:         ',c['postDate']) #publishDate
                    with st.expander('Link to this Post 📮'):
                        st.write(c['postUrl']) #linktoPost
                    with st.expander('Link to  Company Profile 🔗'):
                        st.write(c['profileUrl']) #linktoProfile
                    if not pd.isnull(c['imgUrl']):
                        st.image(c['imgUrl'])
                        st.write('Image from the Post  🗾')
                    
else:
     st.image('https://img.freepik.com/premium-vector/hazard-warning-attention-sign-with-exclamation-mark-symbol-white_231786-5218.jpg?w=2000', width =200)
     st.subheader(f'Oops... No new post found in last {int(number)} days.')
st.header('')
st.header('')

######################
#############
#################
st.header('Select Company to see all their posts in last 1 year')

makes = df30['Company'].drop_duplicates()
make_choice = st.selectbox('Select Company from list:', makes)

#st.write(make_choice)
df30.rename(columns={'Total_Interactions': 'Total Interactions'}, inplace=True)

df_CEO = df30.loc[df30.Company == make_choice]

df_CEO = df_CEO.reset_index(drop=True)


st.image(df_CEO.profileImg[0], width=200)
st.write(make_choice)

col1, col2 = st.columns(2)
col1.metric("Latest Post published On:", df_CEO.postDate[0])
col2.metric(f'Number of Posts in last one year: ', df_CEO.shape[0])


df_CEO.sort_values(['postDate'], ascending=False, inplace=True)




st.subheader(f'Total Interactions for each posts of {make_choice}')

st.area_chart(df_CEO, x='postDate', y='Total Interactions',use_container_width=True)



st.set_option('deprecation.showPyplotGlobalUse', False)
from wordcloud import WordCloud
import collections
import matplotlib.pyplot as plt
import spacy
from spacy.lang.de.examples import sentences

import nltk
from nltk.corpus import stopwords

stop_words = nltk.corpus.stopwords.words('english', 'german')

nlp = spacy.load('en_core_web_sm', disable = ['parser','ner'])
doc = nlp(sentences[0])

st.subheader('Select WordCloud')
tab1, tab2 = st.tabs(["Hashtgs", "Adjectives"])

with tab1:
   
   df_CEO['hash_tags'] = df_CEO['postContent'].str.findall(r'#.*?(?=\s|$)')
    #st.write(df_CEO['hash_tags'])
   hashtags = df_CEO.hash_tags.tolist()
   hashtags = [item for sublist in hashtags for item in sublist]
   hashtags = [str(x) for x in hashtags ]
   counter = collections.Counter(hashtags)
   def my_tf_color_func(dictionary):
    def my_tf_color_func_inner(word, font_size, position, orientation, random_state=None, **kwargs):
        return "hsl(%d, 50%%, 50%%)" % (240 * dictionary[word])
    return my_tf_color_func_inner
   def black_color_func(word, font_size, position, orientation, random_state=None, **kwargs):
            return("hsl(0,100%, 100%)")
            #return("hsl(0,100%, %)")

   most_common = counter.most_common(50)
   most_common = dict(most_common)
   adjs = most_common.keys()
   count = most_common.values()
   adj = {'Adjectives': adjs, 'Frequency': count}
   adj_df = pd.DataFrame(adj)
    #adj_df.to_csv('top_adjectives.csv', index=False)
        
        
   cloud = WordCloud(width=3000, height=2000, background_color='#273346')
   cloud.generate_from_frequencies(most_common)
   cloud.recolor(color_func=black_color_func)

   fig, ax = plt.subplots(figsize = (10, 4))
   ax.imshow(cloud)
    #plt.figure(figsize=[5,5])
   plt.axis("off")
   st.header("Most Frequent Used Hashtags")
   #plt.savefig('hastag_.svg', bbox_inches='tight')
    

    #fig = plt.imshow(cloud, interpolation="bilinear")
   st.pyplot(fig)

with tab2:
   
   df_CEO.dropna(how='any',subset=['postContent'],inplace=True)
   df_CEO.reset_index(drop=True,inplace=True)
   def remove_stopwords(text):
    words = [word for word in text.split() if word not in stop_words]
    return ' '.join(words)
   def removePunkt(text):
    words = [word for word in text.split() if word.isalnum()]
    return ' '.join(words)
   df_CEO.postContent = df_CEO.postContent.apply(removePunkt)
   df_CEO.postContent = df_CEO.postContent.apply(remove_stopwords)
   df_CEO.postContent= df_CEO.postContent.apply(lambda x: (' ').join([word for word in x.split() if len(word)>4]))
   
   df_CEO['Adjectives'] = df_CEO.postContent.apply(lambda x : [token.lemma_ for token in nlp(x) if token.pos_ in ['ADJ']])
   #st.write(df_CEO['Adjectives'])
   adjectives = df_CEO.Adjectives.tolist()
   adjectives = [item for sublist in adjectives for item in sublist]
   adjectives = [str(x) for x in adjectives ]
   
   counter1 = collections.Counter(adjectives)


   most_common1 = counter1.most_common(50)
   most_common1 = dict(most_common1)
   adjs1 = most_common1.keys()
   count1 = most_common1.values()
   #adj = {'Adjectives': adjs, 'Frequency': count}
   #adj_df = pd.DataFrame(adj)
   #adj_df.to_csv('top_adjectives.csv', index=False)
   
   cloud1 = WordCloud(width=3000, height=2000, background_color='#273346', color_func=my_tf_color_func(most_common1))

   cloud1.generate_from_frequencies(most_common1)
   cloud1.recolor(color_func=black_color_func)
   
   fig1, ax1 = plt.subplots(figsize = (10, 4))
   ax1.imshow(cloud1)
    #plt.figure(figsize=[5,5])
   plt.axis("off")
   st.header("Most Frequent Used Adjectives")
    

    #fig = plt.imshow(cloud, interpolation="bilinear")
   st.pyplot(fig1)


plt.imshow(cloud, interpolation="bilinear")







#st.write(df_CEO)

st.header('')


st.subheader(f'Posts from {make_choice} in last year')
num_posts_1 = df_CEO.shape[0]

if  num_posts_1>0:
    
     #splits = np.array_split(df5,5)
     #st.image(df_CEO.profileImg[0])
     splits_1 = df_CEO.groupby(df_CEO.index // 3)
     for _, frames_1 in splits_1:
          frames_1 = frames_1.reset_index(drop=True)
          #print(frames_1.head())
          thumbnails_1 = st.columns(frames_1.shape[0])
          for i, c in frames_1.iterrows():
               with thumbnails_1[i]:

                    # if not pd.isnull(c['profileImg']):
                    #     st.image(c['profileImg'], width=150)
                    # st.subheader(frames_1.CEO[i])
                    
                       
                    st.write('Publish Date & Time 📆:         ',c['postDate']) #publishDate
                    if not pd.isnull(c['imgUrl']):
                        st.image(c['imgUrl'])
                        st.write('Image from the Post  🗾', width=150)
                    with st.expander('Post Content  📜'):
                         st.write(c['postContent'])  #postContent
                    st.write('Type of Post  📨:  ',c['type']) #postType
                    st.write('Total Interactions  📈:  ',c['Total Interactions']) #totInteractions
                    st.write('Likes 👍:  ',c['likeCount']) #totInteractions
                    st.write('Comments 💬:  ',c['commentCount']) #totInteractions
                    st.write('Action  📌:  ',c['action']) #totInteractions
                    
                    with st.expander('Link to this Post  📮'):
                        st.write(c['postUrl']) #linktoPost
                    with st.expander('Link to  Profile 🔗'):
                        st.write(c['profileUrl']) #linktoProfile
                    
                    
else:
     
     st.write('Tut mir sehr sehr leid. No new post in last 24 hours.')



