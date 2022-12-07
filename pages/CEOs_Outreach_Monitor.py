import numpy as np
import altair as alt
import pandas as pd
import streamlit as st

from st_aggrid import AgGrid

import plotly.express as px

from streamlit_option_menu import option_menu

#import pandas_profiling
#from streamlit_pandas_profiling import st_profile_report

from datetime import datetime,timedelta
import pytz
import re

from germansentiment import SentimentModel

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



# 2. horizontal menu
selected2 = option_menu(None, ["CEOs Outreach", "Individual CEO Analysis", "Sentiment Analysis", 'Keyword Monitor'], 
    icons=['graph-up-arrow', 'bar-chart', "emoji-smile", 'search'], 
    menu_icon="cast", default_index=0, orientation="horizontal")

st.image(
    "https://upload.wikimedia.org/wikipedia/commons/thumb/c/ca/LinkedIn_logo_initials.png/640px-LinkedIn_logo_initials.png",
    width=100,
)
st.title('CEOs Outreach Monitoring in LinkedIn ')




#with st.expander('Monitoring Posts of CEOs from LinkedIn everyday'):
#st.success('Monitoring LinkedIn Activities everyday')

my_bar = st.progress(0)

for percent_complete in range(100):
     time.sleep(0.05)
     my_bar.progress(percent_complete + 1)





#st.balloons()

#st.header('`streamlit_pandas_profiling`')

st.header('RWE: Andere CEOs Posts last 12 Months')



df =pd.read_csv('https://phantombuster.s3.amazonaws.com/UhrenaxfEnY/srSVWXMBkcs3wTYIbYOPXA/AndereCEOs_outreach.csv')
#df2 =pd.read_csv('https://phantombuster.s3.amazonaws.com/UhrenaxfEnY/Vx2c6OJZ59781jp9zKPViw/Andere_CEOs_2.csv')
#df3 =pd.read_csv('https://phantombuster.s3.amazonaws.com/UhrenaxfEnY/JUeq71McCykmR5ZrlZTJdQ/Andere_CEOs_3.csv')

#frames = [df1, df2, df3]

#df = pd.concat(frames)

df = df.dropna(how='any', subset=['postContent'])


df.drop(['viewCount', 'sharedJobUrl', 'error', 'repostCount'], axis=1, inplace=True)


#st.write(df.profileUrl.value_counts())



df['CEO']  = df['action']

df.loc[df.profileUrl == "https://www.linkedin.com/in/assaadrazzouk/", "CEO"] = "Assaad Razzouk"
df.loc[df.profileUrl == "https://www.linkedin.com/in/markussteilemann/", "CEO"] = "Markus Steilemann"
df.loc[df.profileUrl == "https://www.linkedin.com/in/buschroland/", "CEO"] = "Roland Busch"
df.loc[df.profileUrl == "https://www.linkedin.com/in/bernardlooneybp/", "CEO"] = "Bernard Looney"
df.loc[df.profileUrl == "https://www.linkedin.com/in/ola-k%C3%A4llenius/", "CEO"] = "Ola Kaellenius"
df.loc[df.profileUrl == "https://www.linkedin.com/in/martenbunnemann/detail/recent-activity/shares/", "CEO"] = "Marten Bunnemann"
df.loc[df.profileUrl == "https://www.linkedin.com/in/jocheneickholt/recent-activity/", "CEO"] = "Jochen Eickholt"
df.loc[df.profileUrl == "https://www.linkedin.com/in/leo-birnbaum-885347b0/detail/recent-activity/", "CEO"] = "Leo Birnbaum"
df.loc[df.profileUrl == "https://www.linkedin.com/in/herbertdiess/", "CEO"] = "Herbert Diess"
df.loc[df.profileUrl == "https://www.linkedin.com/in/mike-crawley-a3308a2/recent-activity/shares/", "CEO"] = "Mike Crawley"
df.loc[df.profileUrl == "https://www.linkedin.com/in/miriam-teige-66117769/recent-activity/", "CEO"] = "Miriam Teige"
df.loc[df.profileUrl == "https://www.linkedin.com/in/werner-baumann/", "CEO"] = "Werner Baumann"
df.loc[df.profileUrl == "https://www.linkedin.com/in/katherina-reiche/detail/recent-activity/", "CEO"] = "Katherina Reiche"
df.loc[df.profileUrl == "https://www.linkedin.com/in/jeromepecresse/?originalSubdomain=fr", "CEO"] = "Jérôme Pécresse"
df.loc[df.profileUrl == "https://www.linkedin.com/in/marc-becker-3990826/", "CEO"] = "Marc Becker"
df.loc[df.profileUrl == "https://www.linkedin.com/in/richardlutzdb/", "CEO"] = "Dr. Richard Lutz"
df.loc[df.profileUrl == "https://www.linkedin.com/in/martin-brudermueller/detail/recent-activity/", "CEO"] = "Dr. Martin Brudermüller"
df.loc[df.profileUrl == "https://www.linkedin.com/in/hdsohn/recent-activity/shares/", "CEO"] = "Hans-Dieter Sohn"
df.loc[df.profileUrl == "https://www.linkedin.com/in/davidcarrascosafrancis/recent-activity/shares/", "CEO"] = "David Carrascosa"
df.loc[df.profileUrl == "https://www.linkedin.com/in/juan-gutierrez-sgre/recent-activity/", "CEO"] = "Juan Gutierrez"
df.loc[df.profileUrl == "https://www.linkedin.com/in/henrik-stiesdal-064a9374/recent-activity/", "CEO"] = "Henrik Stiesdal"
df.loc[df.profileUrl == "https://www.linkedin.com/in/hilde-merete-aasheim-b37b38203/recent-activity/shares/", "CEO"] = "Hilde Merete Aasheim"
df.loc[df.profileUrl == "https://www.linkedin.com/in/alistair-phillips-davies-14213871/recent-activity/", "CEO"] = "Alistair Phillips-Davies"
df.loc[df.profileUrl == "https://www.linkedin.com/in/annaborgvattenfall/", "CEO"] = "Anna Borg"
df.loc[df.profileUrl == "https://www.linkedin.com/in/giles-dickson-98607229/recent-activity/", "CEO"] = "Giles Dickson"
df.loc[df.profileUrl == "https://www.linkedin.com/in/jean-bernard-levy/", "CEO"] = "Jean-Bernard Lévy"
df.loc[df.profileUrl == "https://www.linkedin.com/in/florian-bieberbach/recent-activity/shares/", "CEO"] = "Florian Bieberbach"



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

df.loc[df.profileUrl == "https://www.linkedin.com/in/assaadrazzouk/", "profileImg"] = "https://media-exp1.licdn.com/dms/image/C4D03AQHZCSQaliXdiQ/profile-displayphoto-shrink_800_800/0/1516255427468?e=2147483647&v=beta&t=eSxGSIqW9vW7rHx79J5Z7gcNrCyUGVtZEVr8-rDHh4E"

df.loc[df.profileUrl == "https://www.linkedin.com/in/markussteilemann/", "profileImg"] = "https://media-exp1.licdn.com/dms/image/C4E03AQHXgF5NlZrRqQ/profile-displayphoto-shrink_400_400/0/1616592958472?e=1674086400&v=beta&t=04uxVnwfDbkTEjJAj0qy0-Le0KuSGUNLlR8ao2SqQWQ"
df.loc[df.profileUrl == "https://www.linkedin.com/in/buschroland/", "profileImg"] = "https://media-exp1.licdn.com/dms/image/C4D03AQHt7A5wyfZ62Q/profile-displayphoto-shrink_400_400/0/1649329185717?e=1674086400&v=beta&t=etoCOkPNa5G9Z8b8HJ-CQLRyjzgzlvLgy-VA-uODFT8"
df.loc[df.profileUrl == "https://www.linkedin.com/in/bernardlooneybp/", "profileImg"] = "https://media-exp1.licdn.com/dms/image/C4E03AQEYAcA6GHI1VQ/profile-displayphoto-shrink_400_400/0/1626105106123?e=1674086400&v=beta&t=ahiCRCiVckr2D3VhTDATY_2b9CuxJL5sfE6T427kU_g"
df.loc[df.profileUrl == "https://www.linkedin.com/in/ola-k%C3%A4llenius/", "profileImg"] = "https://media-exp1.licdn.com/dms/image/C4D03AQEmslz1nw9Xcg/profile-displayphoto-shrink_400_400/0/1643731137701?e=1674086400&v=beta&t=3M-JWsoXg7r0tHbJ7RNdb7a3q8puKcCw8FJUTBF8Hzg"
df.loc[df.profileUrl == "https://www.linkedin.com/in/martenbunnemann/detail/recent-activity/shares/", "profileImg"] = "https://media-exp1.licdn.com/dms/image/C4D03AQEEFMfjUbmLsA/profile-displayphoto-shrink_400_400/0/1585913949824?e=1674086400&v=beta&t=fMWpbCEnskPus45UOQB8tjK65seeUL5bgboR5iMVVdY"
df.loc[df.profileUrl == "https://www.linkedin.com/in/jocheneickholt/recent-activity/", "profileImg"] = "https://media-exp1.licdn.com/dms/image/D4D03AQE7I0g99vQF7A/profile-displayphoto-shrink_400_400/0/1664128016463?e=1674086400&v=beta&t=zGoZCh7OVXmwWWYeNGjNGy6C_WN8EyYaJuq8p2nNAcQ"
df.loc[df.profileUrl == "https://www.linkedin.com/in/leo-birnbaum-885347b0/detail/recent-activity/", "profileImg"] = "https://media-exp1.licdn.com/dms/image/C4E03AQE7yP63OXfavA/profile-displayphoto-shrink_400_400/0/1643105401117?e=1674086400&v=beta&t=8lt5v2zUGpmq279UuG5ZV122YbctFKmrXn3Rqy95bB0"
df.loc[df.profileUrl == "https://www.linkedin.com/in/herbertdiess/", "profileImg"] = "https://media-exp1.licdn.com/dms/image/C4D03AQGwevkEVF9SLg/profile-displayphoto-shrink_400_400/0/1604501451969?e=1674086400&v=beta&t=KfjkItv4RipG8wTO5IG7QaMFQWe3qarjOgCLSymASiU"
df.loc[df.profileUrl == "https://www.linkedin.com/in/mike-crawley-a3308a2/recent-activity/shares/", "profileImg"] = "https://media-exp1.licdn.com/dms/image/C5603AQHdigGQiJWq4g/profile-displayphoto-shrink_400_400/0/1516245033117?e=1674086400&v=beta&t=W4GlchB3P4xvyjnyCIT4mGrq4mTXA6eYP2FZS5z8dSY"
df.loc[df.profileUrl == "https://www.linkedin.com/in/miriam-teige-66117769/recent-activity/", "profileImg"] = "https://profile-images.xing.com/images/e361dbb99b1048cc5b97668087ac9b59-5/miriam-teige.256x256.jpg"
df.loc[df.profileUrl == "https://www.linkedin.com/in/werner-baumann/", "profileImg"] = "https://media-exp1.licdn.com/dms/image/C5603AQGI_4YXr7uMIA/profile-displayphoto-shrink_400_400/0/1631806128361?e=1674086400&v=beta&t=EjqN-uz3hJ7qBRIQVCLbxA4C8lJCpwesaTn3RR_TUWw"
df.loc[df.profileUrl == "https://www.linkedin.com/in/katherina-reiche/detail/recent-activity/", "profileImg"] = "https://media-exp1.licdn.com/dms/image/C4D03AQFOOt3UwR4FpQ/profile-displayphoto-shrink_400_400/0/1601888597608?e=1674086400&v=beta&t=Uvd6erXkPyYJBJoEluRZKF3fcHU7drBeCUvvwFaPUas"
df.loc[df.profileUrl == "https://www.linkedin.com/in/jeromepecresse/?originalSubdomain=fr", "profileImg"] = "https://media-exp1.licdn.com/dms/image/C5603AQG7UwEhvr5bxw/profile-displayphoto-shrink_400_400/0/1591286963133?e=1674086400&v=beta&t=gG_d-hk4nKan7m7M8gXBnkdXtbTFk2NclmOridFbrE0"
df.loc[df.profileUrl == "https://www.linkedin.com/in/marc-becker-3990826/", "profileImg"] = "https://www.wfo-helgoland.eu/2017/files/2017/08/Dr.-Marc-Becker-e1501844444352-390x390.jpg"
df.loc[df.profileUrl == "https://www.linkedin.com/in/richardlutzdb/", "profileImg"] = "https://media-exp1.licdn.com/dms/image/D4E03AQG6-ESIrvZGnw/profile-displayphoto-shrink_400_400/0/1667416495067?e=1674086400&v=beta&t=yWZ-GLMN7lh7Cd5BzoJAVHYK39DKDnoY1jhqdMUy-lg"
df.loc[df.profileUrl == "https://www.linkedin.com/in/martin-brudermueller/detail/recent-activity/", "profileImg"] = "https://media-exp1.licdn.com/dms/image/C4E03AQHjIB2XUqA9bg/profile-displayphoto-shrink_400_400/0/1616417524648?e=1674086400&v=beta&t=G7peaOsq6pl9XKOEgAeQwS8GZ6BQdBPkHdJSPQO8VEc"
df.loc[df.profileUrl == "https://www.linkedin.com/in/hdsohn/recent-activity/shares/", "profileImg"] = "https://media-exp1.licdn.com/dms/image/C4E03AQFLOYyqYyLN2g/profile-displayphoto-shrink_400_400/0/1604417604865?e=1674086400&v=beta&t=5hYyozi-rYn2Abt1z7AHrP-VHw4wO0bK8BGVPIkGvgI"
df.loc[df.profileUrl == "https://www.linkedin.com/in/davidcarrascosafrancis/recent-activity/shares/", "profileImg"] = "https://media-exp1.licdn.com/dms/image/C5103AQGi0NnyRoRJPA/profile-displayphoto-shrink_400_400/0/1517228600139?e=1674086400&v=beta&t=mQWCKWusvkyvtELcqx6otmAp0P5s7XxRj89twgUGwJc"
df.loc[df.profileUrl == "https://www.linkedin.com/in/juan-gutierrez-sgre/recent-activity/", "profileImg"] = "https://nawindpower.com/wp-content/uploads/2020/03/Gutierrez_J-0004-scaled.jpg"
df.loc[df.profileUrl == "https://www.linkedin.com/in/henrik-stiesdal-064a9374/recent-activity/", "profileImg"] = "https://upload.wikimedia.org/wikipedia/commons/9/99/Henrik_Stiesdal%2C_Siemens_Windpower_Division_CTO%2C_Press_Image_2012.jpg"
df.loc[df.profileUrl == "https://www.linkedin.com/in/hilde-merete-aasheim-b37b38203/recent-activity/shares/", "profileImg"] = "https://media-exp1.licdn.com/dms/image/C4E03AQHahchcmPw3pA/profile-displayphoto-shrink_400_400/0/1610534026461?e=1674086400&v=beta&t=vs0LmRvESXecSEVPGt3_aZhFSYuvuQHKVMdUVT2K8Ro"
df.loc[df.profileUrl == "https://www.linkedin.com/in/alistair-phillips-davies-14213871/recent-activity/", "profileImg"] = "https://media-exp1.licdn.com/dms/image/C5603AQEGqafzcqRo2Q/profile-displayphoto-shrink_400_400/0/1612302162253?e=1674086400&v=beta&t=dl1pZ2QX-Nf5h0l17nyqaIPP8tRsRPEK3YJfSwbGQck"
df.loc[df.profileUrl == "https://www.linkedin.com/in/annaborgvattenfall/", "profileImg"] = "https://media-exp1.licdn.com/dms/image/D4D03AQFH0lwTjUWnAw/profile-displayphoto-shrink_400_400/0/1666804754880?e=1674086400&v=beta&t=WoQB2g8S4Hk_C1xgmg-uApOgRE0vOSji8Wa9ZzhSjS0"
df.loc[df.profileUrl == "https://www.linkedin.com/in/giles-dickson-98607229/recent-activity/", "profileImg"] = "https://media-exp1.licdn.com/dms/image/C4E03AQGhOcNb1JtCqw/profile-displayphoto-shrink_400_400/0/1645023119636?e=1674086400&v=beta&t=McqVYoA8BJK2bXyClkuytosxfjBCjYiNCGClmj_DXUc"
df.loc[df.profileUrl == "https://www.linkedin.com/in/jean-bernard-levy/", "profileImg"] = "https://media-exp1.licdn.com/dms/image/C4E03AQHrXZwpUycaZg/profile-displayphoto-shrink_400_400/0/1574177430159?e=1674086400&v=beta&t=Qxn0Bsm-BoqsWHBuezA85_LFm8YgdhpUQU0od0EUMOA"
df.loc[df.profileUrl == "https://www.linkedin.com/in/florian-bieberbach/recent-activity/shares/", "profileImg"] = "https://media-exp1.licdn.com/dms/image/C4D03AQFc9lmuT5toVw/profile-displayphoto-shrink_400_400/0/1627920577752?e=1674086400&v=beta&t=RnClEIBVElHEjoDDIBLhqeHXUps3DLJa_Gxr-xikvfs"



df['Company']  = df['action']

df.loc[df.profileUrl == "https://www.linkedin.com/in/assaadrazzouk/", "Company"] = "Gurīn Energy - Renewable Energy"
df.loc[df.profileUrl == "https://www.linkedin.com/in/markussteilemann/", "Company"] = "Covestro - Chemical Manufacturing"
df.loc[df.profileUrl == "https://www.linkedin.com/in/buschroland/", "Company"] = "Siemens AG - Automation Machinery Manufacturing"
df.loc[df.profileUrl == "https://www.linkedin.com/in/bernardlooneybp/", "Company"] = "bp - Oil and Gas"
df.loc[df.profileUrl == "https://www.linkedin.com/in/ola-k%C3%A4llenius/", "Company"] = "Mercedes-Benz - Motor Vehicle Manufacturing"
df.loc[df.profileUrl == "https://www.linkedin.com/in/martenbunnemann/detail/recent-activity/shares/", "Company"] = "Avacon AG - Utilities"
df.loc[df.profileUrl == "https://www.linkedin.com/in/jocheneickholt/recent-activity/", "Company"] = "Siemens Gamesa - Renewable Energy"
df.loc[df.profileUrl == "https://www.linkedin.com/in/leo-birnbaum-885347b0/detail/recent-activity/", "Company"] = "E.ON - Utilities"
df.loc[df.profileUrl == "https://www.linkedin.com/in/herbertdiess/", "Company"] = "Volkswagen AG - Motor Vehicle Manufacturing"
df.loc[df.profileUrl == "https://www.linkedin.com/in/mike-crawley-a3308a2/recent-activity/shares/", "Company"] = "Northland Power Inc - Renewable Energy"
df.loc[df.profileUrl == "https://www.linkedin.com/in/miriam-teige-66117769/recent-activity/", "Company"] = "EnBW - Utilities"
df.loc[df.profileUrl == "https://www.linkedin.com/in/werner-baumann/", "Company"] = "Bayer - Chemical Manufacturing"
df.loc[df.profileUrl == "https://www.linkedin.com/in/katherina-reiche/detail/recent-activity/", "Company"] = "Westenergie AG - Utilities"
df.loc[df.profileUrl == "https://www.linkedin.com/in/jeromepecresse/?originalSubdomain=fr", "Company"] = "GE - Industrial Machinery Manufacturing"
df.loc[df.profileUrl == "https://www.linkedin.com/in/marc-becker-3990826/", "Company"] = "Siemens Gamesa - Renewable Energy"
df.loc[df.profileUrl == "https://www.linkedin.com/in/richardlutzdb/", "Company"] = "Deutsche Bahn - Transportation"
df.loc[df.profileUrl == "https://www.linkedin.com/in/martin-brudermueller/detail/recent-activity/", "Company"] = "BASF - Chemical Manufacturing"
df.loc[df.profileUrl == "https://www.linkedin.com/in/hdsohn/recent-activity/shares/", "Company"] = "WAB e.V. - Renewable Energy"
df.loc[df.profileUrl == "https://www.linkedin.com/in/davidcarrascosafrancis/recent-activity/shares/", "Company"] = "Saitec - Wind Electric Power Generation"
df.loc[df.profileUrl == "https://www.linkedin.com/in/juan-gutierrez-sgre/recent-activity/", "Company"] = "Siemens Gamesa - Renewable Energy"
df.loc[df.profileUrl == "https://www.linkedin.com/in/henrik-stiesdal-064a9374/recent-activity/", "Company"] = "Siemens- Renewable Energy"
df.loc[df.profileUrl == "https://www.linkedin.com/in/hilde-merete-aasheim-b37b38203/recent-activity/shares/", "Company"] = "Norsk Hydro - Mining"
df.loc[df.profileUrl == "https://www.linkedin.com/in/alistair-phillips-davies-14213871/recent-activity/", "Company"] = "SSE plc - Utilities"
df.loc[df.profileUrl == "https://www.linkedin.com/in/annaborgvattenfall/", "Company"] = "Vattenfall - Utilities"
df.loc[df.profileUrl == "https://www.linkedin.com/in/giles-dickson-98607229/recent-activity/", "Company"] = "WindEurope - Renewable Energy"
df.loc[df.profileUrl == "https://www.linkedin.com/in/jean-bernard-levy/", "Company"] = "EDF - Electric Power Generation"
df.loc[df.profileUrl == "https://www.linkedin.com/in/florian-bieberbach/recent-activity/shares/", "Company"] = "Stadtwerke München GmbH - Utilities"




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

df['Activity'] = df.action.apply(rename_reactions)

#st.write(df['Activity'].value_counts())
#################################

#st.write(df30.head())
#AgGrid(df30, height=500, fit_columns_on_grid_load=True)

df30 = df[df['date']>=(dt.datetime.now()-dt.timedelta(days=365))] #hours = 6,12, 24

df30['likeCount'] = df30['likeCount'].astype(int)
df30['commentCount'] = df30['commentCount'].astype(int)
df30['Total_Interactions'] = df30['Total_Interactions'].astype(int)

if st.button('Show Data'):
    AgGrid(df30, height=500, fit_columns_on_grid_load=True)

#st.write(df30)
st.write(f'Total posts in last 12 Months: ', df30.shape[0])
#df5 = df['date'].last('24h')

st.subheader('Total Own Posts for each CEOs from last 12 Months')



#st.write(df30.CEO.value_counts())
df12 = df30.loc[df30.action == "Post"]
df12 = df12['CEO'].value_counts()
st.bar_chart(df12)

# date_to_monitor = st.date_input('Choose a date to see the post that created after that',value=datetime.today() - timedelta(days=1))
# st.write(date_to_monitor)

number = st.number_input('Select the days you want to see the posts', min_value=1, max_value=360, value=2, step=1)
#st.write('The current number is ', number)

st.header(f'Post from last {int(number)} days')



df5 = df[df['date']>=(dt.datetime.now()-dt.timedelta(days=number))] #hours = 6,12, 24


cols = ['CEO','postContent','postUrl','likeCount','commentCount','Total_Interactions','postDate','profileUrl', 'imgUrl','profileImg','type','action', 'Company','Activity']
df5 = df5[cols]
df5.sort_values(['postDate'], ascending=False, inplace=True)


#df5 = df5["imgUrl"].str.replace("<NA>","https://www.citypng.com/public/uploads/preview/download-horizontal-black-line-png-31631830482cvrhyz46le.png")

df5['likeCount'] = df5['likeCount'].astype(int)
df5['commentCount'] = df5['commentCount'].astype(int)
df5['Total_Interactions'] = df5['Total_Interactions'].astype(int)

df5.rename(columns={'Total_Interactions': 'Total Interactions'}, inplace=True)

df5 = df5.reset_index(drop=True)




if st.button(f'Show Data for past {int(number)} days'):
    st.write(df5)

st.write(f'Number of posts in last {int(number)} days: ', df5.shape[0])
#st.write(df5)
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






   



#st.write(a)




#st.subheader(f'Total Interactions for each CEOs : last {int(number)} days')
#x = df5.plot(kind='bar', x='CEO', y='Total_Interactions', figsize=(20,10), ylabel='View Counts')
#st.bar_chart(df5, x='CEO', y='Total_Interactions',use_container_width=True)
#st.sidebar.header('Input')




# fig = px.bar(
#     df5,
#     x="CEO",
#     y="Total_Interactions",
#     color = "Total_Interactions",
#     #color_discrete_sequence=["red", "blue","green"]
#     width=1000, 
#     height=600
# )
fig = px.bar(

    df5,x="Total Interactions",y="CEO",color = "Activity", orientation='h')


fig.update_layout(showlegend=False, plot_bgcolor='rgba(0,0,0,0)', width=600)

#st.plotly_chart(fig)

#st.subheader(f'Type of Outreach for each CEOs : last {int(number)} days')
fig1 = px.bar(

    df5,x="CEO",y="Activity",color = "Activity")

fig1.update_layout(showlegend=True, plot_bgcolor='rgba(0,0,0,0)', width=550)

#st.plotly_chart(fig1)

col1, col2 = st.columns(2)

with col1:
   st.subheader(f'Total Interactions: past {int(number)} days')
   st.plotly_chart(fig)

with col2:
   st.subheader(f'Type of Outreach: past {int(number)} days')
   st.plotly_chart(fig1)



st.header('')


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
tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8 = st.tabs(["Own Post 📃", "Liked a Post 👍", "Liked a Comment 🤝", "Commented 💬", "Replied 📝", "Reposted  📌", "Reacted 🫶","All Activities 🗂"])

with tab1:
   st.subheader("Own Posts")
   
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

                     if not pd.isnull(c['profileImg']):
                        st.image(c['profileImg'], width=150)
                     st.subheader(frames_1.CEO[i])
                     st.write('Company & Industry:  ',c['Company']) #postType
                    
                       

                     st.write('Post Content 📜')
                     st.info(c['postContent'])  #postContent
                     
                     st.write('Type of Post 📨:  ',c['type']) #postType
                     st.write('Total Interactions 📈:  ',c['Total Interactions']) #totInteractions
                     st.write('Likes 👍:  ',c['likeCount']) #totInteractions
                     st.write('Comments 💬:  ',c['commentCount']) #totInteractions
                     st.write('Action 📌:  ',c['action']) #totInteractions
                     #st.write('Activity 📌:  ',c['Activity']) #totInteractions
                     st.write('Publish Date & Time 📆:         ',c['postDate']) #publishDate
                     with st.expander('Link to this Post 📮'):
                         st.write(c['postUrl']) #linktoPost
                     with st.expander('Link to  Profile 🔗'):
                         st.write(c['profileUrl']) #linktoProfile
                     if not pd.isnull(c['imgUrl']):
                        st.image(c['imgUrl'])
                        st.write('Image from the Post  🗾')
                    
   else:
        
        st.image('https://img.freepik.com/premium-vector/hazard-warning-attention-sign-with-exclamation-mark-symbol-white_231786-5218.jpg?w=2000', width =200)
        st.subheader(f'Oops... No  post found in last {int(number)} days.')


with tab2:
   st.subheader("Liked a Post")
   
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

                     if not pd.isnull(c['profileImg']):
                        st.image(c['profileImg'], width=150)
                     st.subheader(frames_1.CEO[i])
                     st.write('Company & Industry:  ',c['Company']) #postType
                     st.warning(c['action'])
                    
                       

                     st.write('Post Content 📜')
                     st.info(c['postContent'])  #postContent
                     st.write('Type of Post 📨:  ',c['type']) #postType
                     st.write('Total Interactions 📈:  ',c['Total Interactions']) #totInteractions
                     st.write('Likes 👍:  ',c['likeCount']) #totInteractions
                     st.write('Comments 💬:  ',c['commentCount']) #totInteractions
                     #st.write('Action 📌:  ',c['action']) #totInteractions
                     #st.write('Activity 📌:  ',c['Activity']) #totInteractions
                     st.write('Publish Date & Time 📆:         ',c['postDate']) #publishDate
                     with st.expander('Link to this Post 📮'):
                         st.write(c['postUrl']) #linktoPost
                     with st.expander('Link to  Profile 🔗'):
                         st.write(c['profileUrl']) #linktoProfile
                     if not pd.isnull(c['imgUrl']):
                        st.image(c['imgUrl'])
                        st.write('Image from the Post  🗾')
                    
   else:
        
        st.image('https://img.freepik.com/premium-vector/hazard-warning-attention-sign-with-exclamation-mark-symbol-white_231786-5218.jpg?w=2000', width =200)
        st.subheader(f'Oops... No  post found in last {int(number)} days.')

with tab3:
   st.subheader("Liked a Comment pn these Posts")
   
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

                     if not pd.isnull(c['profileImg']):
                        st.image(c['profileImg'], width=150)
                     st.subheader(frames_1.CEO[i])
                     st.write('Company & Industry:  ',c['Company']) #postType
                     st.warning(c['action'])
                       

                     st.write('Post Content 📜')
                     st.info(c['postContent'])  #postContent
                     st.write('Type of Post 📨:  ',c['type']) #postType
                     st.write('Total Interactions 📈:  ',c['Total Interactions']) #totInteractions
                     st.write('Likes 👍:  ',c['likeCount']) #totInteractions
                     st.write('Comments 💬:  ',c['commentCount']) #totInteractions
                     #st.write('Action 📌:  ',c['action']) #totInteractions
                     #st.write('Activity 📌:  ',c['Activity']) #totInteractions
                     st.write('Publish Date & Time 📆:         ',c['postDate']) #publishDate
                     with st.expander('Link to this Post 📮'):
                         st.write(c['postUrl']) #linktoPost
                     with st.expander('Link to  Profile 🔗'):
                         st.write(c['profileUrl']) #linktoProfile
                     if not pd.isnull(c['imgUrl']):
                        st.image(c['imgUrl'])
                        st.write('Image from the Post  🗾')
                    
   else:
        
        st.image('https://img.freepik.com/premium-vector/hazard-warning-attention-sign-with-exclamation-mark-symbol-white_231786-5218.jpg?w=2000', width =200)
        st.subheader(f'Oops... No  post found in last {int(number)} days.')

with tab4:
   st.subheader("Commented on these Posts")
   
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

                     if not pd.isnull(c['profileImg']):
                        st.image(c['profileImg'], width=150)
                     st.subheader(frames_1.CEO[i])
                     st.write('Company & Industry:  ',c['Company']) #postType
                     st.warning(c['action'])
                       

                     st.write('Post Content 📜')
                     st.info(c['postContent'])  #postContent
                     st.write('Type of Post 📨:  ',c['type']) #postType
                     st.write('Total Interactions 📈:  ',c['Total Interactions']) #totInteractions
                     st.write('Likes 👍:  ',c['likeCount']) #totInteractions
                     st.write('Comments 💬:  ',c['commentCount']) #totInteractions
                     #st.write('Action 📌:  ',c['action']) #totInteractions
                     #st.write('Activity 📌:  ',c['Activity']) #totInteractions
                     st.write('Publish Date & Time 📆:         ',c['postDate']) #publishDate
                     with st.expander('Link to this Post 📮'):
                         st.write(c['postUrl']) #linktoPost
                     with st.expander('Link to  Profile 🔗'):
                         st.write(c['profileUrl']) #linktoProfile
                     if not pd.isnull(c['imgUrl']):
                        st.image(c['imgUrl'])
                        st.write('Image from the Post  🗾')
                    
   else:
        
        st.image('https://img.freepik.com/premium-vector/hazard-warning-attention-sign-with-exclamation-mark-symbol-white_231786-5218.jpg?w=2000', width =200)
        st.subheader(f'Oops... No  post found in last {int(number)} days.')

with tab5:
   st.subheader("Replied to these Posts")
   
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

                     if not pd.isnull(c['profileImg']):
                        st.image(c['profileImg'], width=150)
                     st.subheader(frames_1.CEO[i])
                     st.write('Company & Industry:  ',c['Company']) #postType
                     st.warning(c['action'])
                       

                     st.write('Post Content 📜')
                     st.info(c['postContent'])  #postContent
                     st.write('Type of Post 📨:  ',c['type']) #postType
                     st.write('Total Interactions 📈:  ',c['Total Interactions']) #totInteractions
                     st.write('Likes 👍:  ',c['likeCount']) #totInteractions
                     st.write('Comments 💬:  ',c['commentCount']) #totInteractions
                     #st.write('Action 📌:  ',c['action']) #totInteractions
                     #st.write('Activity 📌:  ',c['Activity']) #totInteractions
                     st.write('Publish Date & Time 📆:         ',c['postDate']) #publishDate
                     with st.expander('Link to this Post 📮'):
                         st.write(c['postUrl']) #linktoPost
                     with st.expander('Link to  Profile 🔗'):
                         st.write(c['profileUrl']) #linktoProfile
                     if not pd.isnull(c['imgUrl']):
                        st.image(c['imgUrl'])
                        st.write('Image from the Post  🗾')
                    
   else:
        
        st.image('https://img.freepik.com/premium-vector/hazard-warning-attention-sign-with-exclamation-mark-symbol-white_231786-5218.jpg?w=2000', width =200)
        st.subheader(f'Oops... No  post found in last {int(number)} days.')

with tab6:
   st.subheader("Reposted these Posts")
   
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

                     if not pd.isnull(c['profileImg']):
                        st.image(c['profileImg'], width=150)
                     st.subheader(frames_1.CEO[i])
                     st.write('Company & Industry:  ',c['Company']) #postType
                     st.warning(c['action'])
                       

                     st.write('Post Content 📜')
                     st.info(c['postContent'])  #postContent
                     st.write('Type of Post 📨:  ',c['type']) #postType
                     st.write('Total Interactions 📈:  ',c['Total Interactions']) #totInteractions
                     st.write('Likes 👍:  ',c['likeCount']) #totInteractions
                     st.write('Comments 💬:  ',c['commentCount']) #totInteractions
                     #st.write('Action 📌:  ',c['action']) #totInteractions
                     #st.write('Activity 📌:  ',c['Activity']) #totInteractions
                     st.write('Publish Date & Time 📆:         ',c['postDate']) #publishDate
                     with st.expander('Link to this Post 📮'):
                         st.write(c['postUrl']) #linktoPost
                     with st.expander('Link to  Profile 🔗'):
                         st.write(c['profileUrl']) #linktoProfile
                     if not pd.isnull(c['imgUrl']):
                        st.image(c['imgUrl'])
                        st.write('Image from the Post  🗾')
                    
   else:
        
        st.image('https://img.freepik.com/premium-vector/hazard-warning-attention-sign-with-exclamation-mark-symbol-white_231786-5218.jpg?w=2000', width =200)
        st.subheader(f'Oops... No  post found in last {int(number)} days.')

with tab7:
   st.subheader("Reacted these Posts")
   
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

                     if not pd.isnull(c['profileImg']):
                        st.image(c['profileImg'], width=150)
                     st.subheader(frames_1.CEO[i])
                     st.write('Company & Industry:  ',c['Company']) #postType
                     st.warning(c['action'])
                       

                     st.write('Post Content 📜')
                     st.info(c['postContent'])  #postContent
                     st.write('Type of Post 📨:  ',c['type']) #postType
                     st.write('Total Interactions 📈:  ',c['Total Interactions']) #totInteractions
                     st.write('Likes 👍:  ',c['likeCount']) #totInteractions
                     st.write('Comments 💬:  ',c['commentCount']) #totInteractions
                     #st.write('Action 📌:  ',c['action']) #totInteractions
                     #st.write('Activity 📌:  ',c['Activity']) #totInteractions
                     st.write('Publish Date & Time 📆:         ',c['postDate']) #publishDate
                     with st.expander('Link to this Post 📮'):
                         st.write(c['postUrl']) #linktoPost
                     with st.expander('Link to  Profile 🔗'):
                         st.write(c['profileUrl']) #linktoProfile
                     if not pd.isnull(c['imgUrl']):
                        st.image(c['imgUrl'])
                        st.write('Image from the Post  🗾')
                    
   else:
        
        st.image('https://img.freepik.com/premium-vector/hazard-warning-attention-sign-with-exclamation-mark-symbol-white_231786-5218.jpg?w=2000', width =200)
        st.subheader(f'Oops... No  post found in last {int(number)} days.')

with tab8:
   st.subheader("Posts from All Activities")
   
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

                     if not pd.isnull(c['profileImg']):
                        st.image(c['profileImg'], width=150)
                     st.subheader(frames_1.CEO[i])
                     st.write('Company & Industry:  ',c['Company']) #postType
                     st.warning(c['action'])
                       

                     st.write('Post Content 📜')
                     st.info(c['postContent'])  #postContent
                     st.write('Type of Post 📨:  ',c['type']) #postType
                     st.write('Total Interactions 📈:  ',c['Total Interactions']) #totInteractions
                     st.write('Likes 👍:  ',c['likeCount']) #totInteractions
                     st.write('Comments 💬:  ',c['commentCount']) #totInteractions
                     #st.write('Action 📌:  ',c['action']) #totInteractions
                     #st.write('Activity 📌:  ',c['Activity']) #totInteractions
                     st.write('Publish Date & Time 📆:         ',c['postDate']) #publishDate
                     with st.expander('Link to this Post 📮'):
                         st.write(c['postUrl']) #linktoPost
                     with st.expander('Link to  Profile 🔗'):
                         st.write(c['profileUrl']) #linktoProfile
                     if not pd.isnull(c['imgUrl']):
                        st.image(c['imgUrl'])
                        st.write('Image from the Post  🗾')
                    
   else:
        
        st.image('https://img.freepik.com/premium-vector/hazard-warning-attention-sign-with-exclamation-mark-symbol-white_231786-5218.jpg?w=2000', width =200)
        st.subheader(f'Oops... No  post found in last {int(number)} days.')
####################################################


# num_posts = df5.shape[0]

# if  num_posts>0:

#      #splits = np.array_split(df5,5)
#      splits = df5.groupby(df5.index // 3)
#      for _, frames in splits:
#           frames = frames.reset_index(drop=True)
#           #print(frames.head())
#           thumbnails = st.columns(frames.shape[0])
#           for i, c in frames.iterrows():
#                with thumbnails[i]:

#                     if not pd.isnull(c['profileImg']):
#                         st.image(c['profileImg'], width=150)
#                     st.subheader(frames.CEO[i])
#                     st.write('Company & Industry:  ',c['Company']) #postType
                    
                       

#                     with st.expander('Post Content 📜'):
#                          st.write(c['postContent'])  #postContent
#                     st.write('Type of Post 📨:  ',c['type']) #postType
#                     st.write('Total Interactions 📈:  ',c['Total Interactions']) #totInteractions
#                     st.write('Likes 👍:  ',c['likeCount']) #totInteractions
#                     st.write('Comments 💬:  ',c['commentCount']) #totInteractions
#                     st.write('Action 📌:  ',c['action']) #totInteractions
#                     st.write('Activity 📌:  ',c['Activity']) #totInteractions
#                     st.write('Publish Date & Time 📆:         ',c['postDate']) #publishDate
#                     with st.expander('Link to this Post 📮'):
#                         st.write(c['postUrl']) #linktoPost
#                     with st.expander('Link to  Profile 🔗'):
#                         st.write(c['profileUrl']) #linktoProfile
#                     if not pd.isnull(c['imgUrl']):
#                         st.image(c['imgUrl'])
#                         st.write('Image from the Post  🗾')
                    
# else:
#      st.image('https://img.freepik.com/premium-vector/hazard-warning-attention-sign-with-exclamation-mark-symbol-white_231786-5218.jpg?w=2000', width =200)
#      st.subheader(f'Oops... No new post found in last {int(number)} days.')
# st.header('')
# st.header('')
