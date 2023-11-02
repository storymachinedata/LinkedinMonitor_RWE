import numpy as np
import altair as alt
import pandas as pd
import streamlit as st

#from st_aggrid import AgGrid

import plotly.express as px

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

st.title('RWE:Energiewirtschaft/Influencer Energie CEOs Outreach Monitoring')

st.image(
    "https://upload.wikimedia.org/wikipedia/commons/thumb/c/ca/LinkedIn_logo_initials.png/640px-LinkedIn_logo_initials.png",
    width=100,
)


#with st.expander('Monitoring Posts of CEOs from LinkedIn everyday'):
st.success('Monitoring LinkedIn Activities everyday')

my_bar = st.progress(0)

for percent_complete in range(100):
     time.sleep(0.05)
     my_bar.progress(percent_complete + 1)





#st.balloons()

#st.header('`streamlit_pandas_profiling`')

st.header('Andere CEOs Posts last 12 Months')



df =pd.read_csv('https://phantombuster.s3.amazonaws.com/UhrenaxfEnY/YJvJADn9fiMUjJP4CVyEBA/influencer_energie_RWE_monitor.csv')
#df2 =pd.read_csv('https://phantombuster.s3.amazonaws.com/UhrenaxfEnY/Vx2c6OJZ59781jp9zKPViw/Andere_CEOs_2.csv')
#df3 =pd.read_csv('https://phantombuster.s3.amazonaws.com/UhrenaxfEnY/JUeq71McCykmR5ZrlZTJdQ/Andere_CEOs_3.csv')

#frames = [df1, df2, df3]

#df = pd.concat(frames)

df = df.dropna(how='any', subset=['postContent'])


df.drop(['viewCount', 'error', 'repostCount'], axis=1, inplace=True)
#, 'sharedJobUrl'

#st.write(df.profileUrl.value_counts())



df['CEO']  = df['action']

df.loc[df.profileUrl == "https://www.linkedin.com/in/siegfried-russwurm/detail/recent-activity/", "CEO"] = "Siegfried Russwurm"
df.loc[df.profileUrl == "https://www.linkedin.com/in/fatih-birol/detail/recent-activity/", "CEO"] = "Fatih Birol"
df.loc[df.profileUrl == "https://www.linkedin.com/company/bloombergnef/", "CEO"] = "BloombergNEF"
df.loc[df.profileUrl == "https://www.linkedin.com/company/world-economic-forum/", "CEO"] = "World Economic Forum"
df.loc[df.profileUrl == "https://www.linkedin.com/company/cdp-worldwide/", "CEO"] = "CDP"
df.loc[df.profileUrl == "https://www.linkedin.com/in/dr-joachim-lang-1b202217a/detail/recent-activity/", "CEO"] = "Dr. Joachim Lang"
df.loc[df.profileUrl == "https://www.linkedin.com/in/kerstin-andreae/detail/recent-activity/", "CEO"] = "Kerstin Andreae"
df.loc[df.profileUrl == "https://www.linkedin.com/in/s%C3%B6nke-meschkat/detail/recent-activity/", "CEO"] = "Sönke Meschkat"
df.loc[df.profileUrl == "https://www.linkedin.com/in/williamhgates/detail/recent-activity/", "CEO"] = "Bill Gates"
df.loc[df.profileUrl == "https://www.linkedin.com/in/gerard-reid-62164b9/detail/recent-activity/", "CEO"] = "Gerard Reid"
df.loc[df.profileUrl == "https://www.linkedin.com/in/alessandro-blasi-6579a66/detail/recent-activity/", "CEO"] = "Alessandro Blasi"
df.loc[df.profileUrl == "https://www.linkedin.com/in/laurent-segalen-2b090a24/detail/recent-activity/", "CEO"] = "Laurent Segalen"
df.loc[df.profileUrl == "https://www.linkedin.com/in/andreas-kuhlmann-91249579/detail/recent-activity/", "CEO"] = "Andreas Kuhlmann"
df.loc[df.profileUrl == "https://www.linkedin.com/in/dan-mcgrail-4807bb2b/", "CEO"] = "Dan McGrail"




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





#st.write(df.profileImg.value_counts())


################################
## OUT REACH ANALYSIS 

mapper = {'liked':'Liked a Comment', 'likes': 'Liked','Reacted': 'Reacted this Post',

            'commented': 'Commented', 'replied': 'Replied',
             'reposted': 'Reposted'}



def rename_reactions(reactions):

    if 'liked' in reactions:

        return mapper['liked']

    elif 'likes' in reactions:

        return mapper['likes']

    elif 'commented' in reactions:

        return mapper['commented']

    elif 'replied'in reactions:

        return mapper['replied']

    elif 'celebrates' in reactions:

        return 'Reacted'

    elif 'supports' in reactions:

        return 'Reacted'

    elif 'insightful' in reactions:

        return 'Reacted'

    elif 'curious' in reactions:

        return 'Reacted'

    elif 'loves' in reactions:

        return 'Reacted'

    elif 'reposted' in reactions:

        return 'Reposted'




    else:

        return reactions

df['Activity'] = 'Own post'    #df.action.apply(rename_reactions)

#st.write(df['Activity'].value_counts())
#################################

#st.write(df30.head())
#AgGrid(df30, height=500, fit_columns_on_grid_load=True)

df30 = df[df['date']>=(dt.datetime.now()-dt.timedelta(days=365))] #hours = 6,12, 24

df30['likeCount'] = df30['likeCount'].astype(int)
df30['commentCount'] = df30['commentCount'].astype(int)
df30['Total_Interactions'] = df30['Total_Interactions'].astype(int)

if st.button('Show Data'):
    st.write(df30)

#st.write(df30)
st.write(f'Total Activities in last 12 Months: ', df30.shape[0])
#df5 = df['date'].last('24h')

#st.subheader('Total Own Posts for each CEOs from last 12 Months')



#st.write(df30.CEO.value_counts())
df12 = df30.loc[df30.action == "Post"]
df12 = df12['CEO'].value_counts()
#st.bar_chart(df12)

# date_to_monitor = st.date_input('Choose a date to see the post that created after that',value=datetime.today() - timedelta(days=1))
# st.write(date_to_monitor)

st.header('')

col1, col2 = st.columns(2)

with col1:
   st.header("Select Time Range")
   
   number = st.number_input('Select the days you want to see the posts', min_value=1, max_value=360, value=1, step=1)
   if number:
            df5 = df[df['date']>=(dt.datetime.now()-dt.timedelta(days=number))] #hours = 6,12, 24
            st.success(f'Monitor Posts from last {int(number)} Days', icon="✅")

with col2:
   st.header("Select CEOs for Monitor")
   #st.warning('Please choose selection below to proceed', icon="⚠️")
   all = st.checkbox('Select all CEOs' ,value = True)

   if all:
        
        df5= df5
        st.success('All CEOs Selected to Monitor', icon="✅")
        st.info('Untick the checbox to multiselect individual CEOs from list', icon="ℹ️")
   else:
        st.write('OR')
        CEO_options = df5['CEO'].unique().tolist()
        CEO_select = st.multiselect('Select Individual CEOs from list', CEO_options)
        df5= df5[df5['CEO'].isin(CEO_select)]
        
        


#st.write('The current number is ', number)








#cols = ['CEO','postContent','postUrl','likeCount','commentCount','Total_Interactions','postDate','profileUrl', 'imgUrl','profileImg','type','action', 'Company','Activity']
#df5 = df5[cols]
#df5.sort_values(['Total_Interactions'], ascending=False, inplace=True)


#df5 = df5["imgUrl"].str.replace("<NA>","https://www.citypng.com/public/uploads/preview/download-horizontal-black-line-png-31631830482cvrhyz46le.png")

df5['likeCount'] = df5['likeCount'].astype(int)
df5['commentCount'] = df5['commentCount'].astype(int)
df5['Total_Interactions'] = df5['Total_Interactions'].astype(int)

df5.rename(columns={'Total_Interactions': 'Total Interactions'}, inplace=True)

df5['action'] = df5['action'].str.replace('Post', 'Own Post')

df5 = df5.reset_index(drop=True)

st.header('')
st.header(f'Post from last {int(number)} days')

col1, col2 = st.columns(2)

with col1:
   st.metric(f'Total Activities in last {int(number)} days: ','',df5.shape[0] )
   if st.button(f'Show Data for past {int(number)} days'):
        st.write(df5)


   

with col2:
   @st.cache
   def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
        return df.to_csv().encode('utf-8')

   csv = convert_df(df5)
   st.download_button(
        label="Download data as CSV",
        data=csv,
        file_name='CEOS_post_past24Hr.csv',
        mime='text/csv',
    )
st.header('')
st.header('')

############### Tab ########################




#################### GRAPH ###############################################

# fig = px.bar(

#     df5,x="Total Interactions",y="CEO",color = "Activity", orientation='h')


# fig.update_layout(showlegend=False, plot_bgcolor='rgba(0,0,0,0)', width=500)

# #st.plotly_chart(fig)
# #df5,x="CEO",y="Activity",color = "Activity",animation_frame="postDate", animation_group="CEO")
# #HOW TO ANIMATE PLOTLY https://www.youtube.com/watch?v=VZ_tS4F6P2A
# #st.subheader(f'Type of Outreach for each CEOs : last {int(number)} days')

# total = df5.groupby(['CEO','Activity']).size().unstack(fill_value=0)
# fig1 = px.bar(

#     total,color = "Activity")

# fig1.update_layout(showlegend=True, plot_bgcolor='rgba(0,0,0,0)', width=500)
# fig1.update_yaxes(visible=False, showticklabels=True)
# #st.plotly_chart(fig1)

# # col1, col2 = st.columns(2)

# # with col1:
# #    st.subheader(f'Total Interactions: past {int(number)} days')
# #    st.plotly_chart(fig)

# # with col2:
# #    st.subheader(f'Type of Outreach: past {int(number)} days')
# #    st.plotly_chart(fig1)



#st.header('')


#defining three side-by-side columns

#col1, col2, col3 = st.columns(3)
####################################################
## OUTREACH

df_post = df5.loc[df5.Activity == "Post"]
df_post = df_post.reset_index(drop=True)

df_liked = df5.loc[df5.Activity == "Liked"]
df_liked = df_liked.reset_index(drop=True)

df_reacted = df5.loc[df5.Activity == "Reacted"]
df_reacted = df_reacted.reset_index(drop=True)

df_lcomment = df5.loc[df5.Activity == "Liked a Comment"]
df_lcomment = df_lcomment.reset_index(drop=True)

df_commented = df5.loc[df5.Activity == "Commented"]
df_commented = df_commented.reset_index(drop=True)

df_replied = df5.loc[df5.Activity == "Replied"]
df_post = df_post.reset_index(drop=True)

df_repost = df5.loc[df5.Activity == "Reposted"]
df_repost = df_repost.reset_index(drop=True)



st.subheader(f'Select Activity to See Posts Related with in Past {int(number)} days')

#tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8 = st.tabs(["Own Post 📃", "Liked a Post 👍", "Liked a Comment 🤝", "Commented 💬", "Replied 📝", "Reposted  📌", "Reacted 🫶","All Activities 🗂"])
tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8 = st.tabs(["All Activities 🗂", "Own Post 📃", "Liked a Post 👍", "Liked a Comment 🤝", "Commented 💬", "Replied 📝", "Reposted  📌","Reacted 🫶"])

with tab2:
   st.subheader("Own Posts")
   st.info('Most recent posts appear first', icon="ℹ️")
   num_posts_1 = df_post.shape[0]
   st.metric(f'Count in last {int(number)} days: ','',num_posts_1 )

   if  num_posts_1>0:
        
        #splits = np.array_split(df5,5)
        #st.image(df_CEO.profileImg[0])
        splits_1 = df_post.groupby(df_post.index // 3)
        for _, frames_1 in splits_1:
            frames_1 = frames_1.reset_index(drop=True)
            #print(frames_1.head())
            thumbnails_1 = st.columns(frames_1.shape[0])
            for i, c in frames_1.iterrows():
                with thumbnails_1[i]:

                     
                     st.subheader(frames_1.CEO[i])
                     #st.write('Company & Industry:  ',c['Company']) #postType
                     st.warning(c['action'])
                        #st.write('Image from the Post  🗾')
                     if not pd.isnull(c['imgUrl']):
                        st.image(c['imgUrl']) 
                     #st.write('Post Content 📜')
                     st.info(c['postContent'])  #postContent
                     st.write('Publish Date & Time 📆:         ',c['postDate']) #publishDate
                     st.write('Type of Post 📨:  ',c['type']) #postType
                     st.write('Total Interactions 📈:  ',c['Total Interactions']) #totInteractions
                     st.write('Likes 👍:  ',c['likeCount']) #totInteractions
                     st.write('Comments 💬:  ',c['commentCount']) #totInteractions
                     with st.expander('Link to this Post 📮'):
                         st.write(c['postUrl']) #linktoPost
                     with st.expander('Link to  Profile 🔗'):
                         st.write(c['profileUrl']) #linktoProfile
                     
                    
   else:
        
        st.image('https://img.freepik.com/premium-vector/hazard-warning-attention-sign-with-exclamation-mark-symbol-white_231786-5218.jpg?w=2000', width =200)
        st.subheader(f'Oops... No  post found in last {int(number)} days.')


with tab3:
   st.subheader("Liked a Post")
   st.info('Most recent posts appear first', icon="ℹ️")
   num_posts_1 = df_liked.shape[0]
   st.metric(f'Count in last {int(number)} days: ','',num_posts_1 )

   if  num_posts_1>0:
        
        #splits = np.array_split(df5,5)
        #st.image(df_CEO.profileImg[0])
        splits_1 = df_liked.groupby(df_liked.index // 3)
        for _, frames_1 in splits_1:
            frames_1 = frames_1.reset_index(drop=True)
            #print(frames_1.head())
            thumbnails_1 = st.columns(frames_1.shape[0])
            for i, c in frames_1.iterrows():
                with thumbnails_1[i]:

                     st.subheader(frames_1.CEO[i])
                     #st.write('Company & Industry:  ',c['Company']) #postType
                     st.warning(c['action'])
                        #st.write('Image from the Post  🗾')
                     if not pd.isnull(c['imgUrl']):
                        st.image(c['imgUrl']) 
                     #st.write('Post Content 📜')
                     st.info(c['postContent'])  #postContent
                     st.write('Publish Date & Time 📆:         ',c['postDate']) #publishDate
                     st.write('Type of Post 📨:  ',c['type']) #postType
                     st.write('Total Interactions 📈:  ',c['Total Interactions']) #totInteractions
                     st.write('Likes 👍:  ',c['likeCount']) #totInteractions
                     st.write('Comments 💬:  ',c['commentCount']) #totInteractions
                     with st.expander('Link to this Post 📮'):
                         st.write(c['postUrl']) #linktoPost
                     with st.expander('Link to  Profile 🔗'):
                         st.write(c['profileUrl']) #linktoProfile
                    
   else:
        
        st.image('https://img.freepik.com/premium-vector/hazard-warning-attention-sign-with-exclamation-mark-symbol-white_231786-5218.jpg?w=2000', width =200)
        st.subheader(f'Oops... No  post found in last {int(number)} days.')

with tab4:
   st.subheader("Liked a Comment pn these Posts")
   st.info('Most recent posts appear first', icon="ℹ️")
   num_posts_1 = df_lcomment.shape[0]
   st.metric(f'Count in last {int(number)} days: ','',num_posts_1 )

   if  num_posts_1>0:
        
        #splits = np.array_split(df5,5)
        #st.image(df_CEO.profileImg[0])
        splits_1 = df_lcomment.groupby(df_lcomment.index // 3)
        for _, frames_1 in splits_1:
            frames_1 = frames_1.reset_index(drop=True)
            #print(frames_1.head())
            thumbnails_1 = st.columns(frames_1.shape[0])
            for i, c in frames_1.iterrows():
                with thumbnails_1[i]:

                     st.subheader(frames_1.CEO[i])
                     #st.write('Company & Industry:  ',c['Company']) #postType
                     st.warning(c['action'])
                        #st.write('Image from the Post  🗾')
                     if not pd.isnull(c['imgUrl']):
                        st.image(c['imgUrl']) 
                     #st.write('Post Content 📜')
                     st.info(c['postContent'])  #postContent
                     st.write('Publish Date & Time 📆:         ',c['postDate']) #publishDate
                     st.write('Type of Post 📨:  ',c['type']) #postType
                     st.write('Total Interactions 📈:  ',c['Total Interactions']) #totInteractions
                     st.write('Likes 👍:  ',c['likeCount']) #totInteractions
                     st.write('Comments 💬:  ',c['commentCount']) #totInteractions
                     with st.expander('Link to this Post 📮'):
                         st.write(c['postUrl']) #linktoPost
                     with st.expander('Link to  Profile 🔗'):
                         st.write(c['profileUrl']) #linktoProfile
                    
   else:
        
        st.image('https://img.freepik.com/premium-vector/hazard-warning-attention-sign-with-exclamation-mark-symbol-white_231786-5218.jpg?w=2000', width =200)
        st.subheader(f'Oops... No  post found in last {int(number)} days.')

with tab5:
   st.subheader("Commented on these Posts")
   st.info('Most recent posts appear first', icon="ℹ️")
   num_posts_1 = df_commented.shape[0]
   st.metric(f'Count in last {int(number)} days: ','',num_posts_1 )

   if  num_posts_1>0:
        
        #splits = np.array_split(df5,5)
        #st.image(df_CEO.profileImg[0])
        splits_1 = df_commented.groupby(df_commented.index // 3)
        for _, frames_1 in splits_1:
            frames_1 = frames_1.reset_index(drop=True)
            #print(frames_1.head())
            thumbnails_1 = st.columns(frames_1.shape[0])
            for i, c in frames_1.iterrows():
                with thumbnails_1[i]:

                     st.subheader(frames_1.CEO[i])
                     #st.write('Company & Industry:  ',c['Company']) #postType
                     st.warning(c['action'])
                        #st.write('Image from the Post  🗾')
                     if not pd.isnull(c['imgUrl']):
                        st.image(c['imgUrl']) 
                     #st.write('Post Content 📜')
                     st.info(c['postContent'])  #postContent
                     st.write('Publish Date & Time 📆:         ',c['postDate']) #publishDate
                     st.write('Type of Post 📨:  ',c['type']) #postType
                     st.write('Total Interactions 📈:  ',c['Total Interactions']) #totInteractions
                     st.write('Likes 👍:  ',c['likeCount']) #totInteractions
                     st.write('Comments 💬:  ',c['commentCount']) #totInteractions
                     with st.expander('Link to this Post 📮'):
                         st.write(c['postUrl']) #linktoPost
                     with st.expander('Link to  Profile 🔗'):
                         st.write(c['profileUrl']) #linktoProfile
                    
   else:
        
        st.image('https://img.freepik.com/premium-vector/hazard-warning-attention-sign-with-exclamation-mark-symbol-white_231786-5218.jpg?w=2000', width =200)
        st.subheader(f'Oops... No  post found in last {int(number)} days.')

with tab6:
   st.subheader("Replied to these Posts")
   st.info('Most recent posts appear first', icon="ℹ️")
   num_posts_1 = df_replied.shape[0]
   st.metric(f'Count in last {int(number)} days: ','',num_posts_1 )

   if  num_posts_1>0:
        
        #splits = np.array_split(df5,5)
        #st.image(df_CEO.profileImg[0])
        splits_1 = df_replied.groupby(df_replied.index // 3)
        for _, frames_1 in splits_1:
            frames_1 = frames_1.reset_index(drop=True)
            #print(frames_1.head())
            thumbnails_1 = st.columns(frames_1.shape[0])
            for i, c in frames_1.iterrows():
                with thumbnails_1[i]:

                     st.subheader(frames_1.CEO[i])
                     #st.write('Company & Industry:  ',c['Company']) #postType
                     st.warning(c['action'])
                        #st.write('Image from the Post  🗾')
                     if not pd.isnull(c['imgUrl']):
                        st.image(c['imgUrl']) 
                     #st.write('Post Content 📜')
                     st.info(c['postContent'])  #postContent
                     st.write('Publish Date & Time 📆:         ',c['postDate']) #publishDate
                     st.write('Type of Post 📨:  ',c['type']) #postType
                     st.write('Total Interactions 📈:  ',c['Total Interactions']) #totInteractions
                     st.write('Likes 👍:  ',c['likeCount']) #totInteractions
                     st.write('Comments 💬:  ',c['commentCount']) #totInteractions
                     with st.expander('Link to this Post 📮'):
                         st.write(c['postUrl']) #linktoPost
                     with st.expander('Link to  Profile 🔗'):
                         st.write(c['profileUrl']) #linktoProfile
                    
   else:
        
        st.image('https://img.freepik.com/premium-vector/hazard-warning-attention-sign-with-exclamation-mark-symbol-white_231786-5218.jpg?w=2000', width =200)
        st.subheader(f'Oops... No  post found in last {int(number)} days.')

with tab7:
   st.subheader("Reposted these Posts")
   st.info('Most recent posts appear first', icon="ℹ️")
   num_posts_1 = df_repost.shape[0]
   st.metric(f'Count in last {int(number)} days: ','',num_posts_1 )

   if  num_posts_1>0:
        
        #splits = np.array_split(df5,5)
        #st.image(df_CEO.profileImg[0])
        splits_1 = df_repost.groupby(df_repost.index // 3)
        for _, frames_1 in splits_1:
            frames_1 = frames_1.reset_index(drop=True)
            #print(frames_1.head())
            thumbnails_1 = st.columns(frames_1.shape[0])
            for i, c in frames_1.iterrows():
                with thumbnails_1[i]:

                     st.subheader(frames_1.CEO[i])
                     #st.write('Company & Industry:  ',c['Company']) #postType
                     st.warning(c['action'])
                        #st.write('Image from the Post  🗾')
                     if not pd.isnull(c['imgUrl']):
                        st.image(c['imgUrl']) 
                     #st.write('Post Content 📜')
                     st.info(c['postContent'])  #postContent
                     st.write('Publish Date & Time 📆:         ',c['postDate']) #publishDate
                     st.write('Type of Post 📨:  ',c['type']) #postType
                     st.write('Total Interactions 📈:  ',c['Total Interactions']) #totInteractions
                     st.write('Likes 👍:  ',c['likeCount']) #totInteractions
                     st.write('Comments 💬:  ',c['commentCount']) #totInteractions
                     with st.expander('Link to this Post 📮'):
                         st.write(c['postUrl']) #linktoPost
                     with st.expander('Link to  Profile 🔗'):
                         st.write(c['profileUrl']) #linktoProfile
                    
   else:
        
        st.image('https://img.freepik.com/premium-vector/hazard-warning-attention-sign-with-exclamation-mark-symbol-white_231786-5218.jpg?w=2000', width =200)
        st.subheader(f'Oops... No  post found in last {int(number)} days.')

with tab8:
   st.subheader("Reacted these Posts")
   st.info('Most recent posts appear first', icon="ℹ️")
   num_posts_1 = df_reacted.shape[0]
   st.metric(f'Count in last {int(number)} days: ','',num_posts_1 )

   if  num_posts_1>0:
        
        #splits = np.array_split(df5,5)
        #st.image(df_CEO.profileImg[0])
        splits_1 = df_reacted.groupby(df_reacted.index // 3)
        for _, frames_1 in splits_1:
            frames_1 = frames_1.reset_index(drop=True)
            #print(frames_1.head())
            thumbnails_1 = st.columns(frames_1.shape[0])
            for i, c in frames_1.iterrows():
                with thumbnails_1[i]:

                     st.subheader(frames_1.CEO[i])
                     #st.write('Company & Industry:  ',c['Company']) #postType
                     st.warning(c['action'])
                        #st.write('Image from the Post  🗾')
                     if not pd.isnull(c['imgUrl']):
                        st.image(c['imgUrl']) 
                     #st.write('Post Content 📜')
                     st.info(c['postContent'])  #postContent
                     st.write('Publish Date & Time 📆:         ',c['postDate']) #publishDate
                     st.write('Type of Post 📨:  ',c['type']) #postType
                     st.write('Total Interactions 📈:  ',c['Total Interactions']) #totInteractions
                     st.write('Likes 👍:  ',c['likeCount']) #totInteractions
                     st.write('Comments 💬:  ',c['commentCount']) #totInteractions
                     with st.expander('Link to this Post 📮'):
                         st.write(c['postUrl']) #linktoPost
                     with st.expander('Link to  Profile 🔗'):
                         st.write(c['profileUrl']) #linktoProfile
                    
   else:
        
        st.image('https://img.freepik.com/premium-vector/hazard-warning-attention-sign-with-exclamation-mark-symbol-white_231786-5218.jpg?w=2000', width =200)
        st.subheader(f'Oops... No  post found in last {int(number)} days.')

with tab1:
   st.subheader("Posts from All Activities")
   st.info('Most recent posts appear first', icon="ℹ️")
   df5.sort_values(['postDate'], ascending=False, inplace=True)
   num_posts_1 = df5.shape[0]
   st.metric(f'Count in last {int(number)} days: ','',num_posts_1 )

   if  num_posts_1>0:
        
        #splits = np.array_split(df5,5)
        #st.image(df_CEO.profileImg[0])
        splits_1 = df5.groupby(df5.index // 3)
        for _, frames_1 in splits_1:
            frames_1 = frames_1.reset_index(drop=True)
            #print(frames_1.head())
            thumbnails_1 = st.columns(frames_1.shape[0])
            for i, c in frames_1.iterrows():
                with thumbnails_1[i]:

                     st.subheader(frames_1.CEO[i])
                     #st.write('Company & Industry:  ',c['Company']) #postType
                     st.warning(c['action'])
                        #st.write('Image from the Post  🗾')
                     if not pd.isnull(c['imgUrl']):
                        st.image(c['imgUrl']) 
                     #st.write('Post Content 📜')
                     st.info(c['postContent'])  #postContent
                     st.write('Publish Date & Time 📆:         ',c['postDate']) #publishDate
                     st.write('Type of Post 📨:  ',c['type']) #postType
                     st.write('Total Interactions 📈:  ',c['Total Interactions']) #totInteractions
                     st.write('Likes 👍:  ',c['likeCount']) #totInteractions
                     st.write('Comments 💬:  ',c['commentCount']) #totInteractions
                     with st.expander('Link to this Post 📮'):
                         st.write(c['postUrl']) #linktoPost
                     with st.expander('Link to  Profile 🔗'):
                         st.write(c['profileUrl']) #linktoProfile
                    
   else:
        
        st.image('https://img.freepik.com/premium-vector/hazard-warning-attention-sign-with-exclamation-mark-symbol-white_231786-5218.jpg?w=2000', width =200)
        st.subheader(f'Oops... No  post found in last {int(number)} days.')
####################################################

