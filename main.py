import streamlit as st
from PIL import Image
import os
from functions import st_button, load_css

st.set_page_config(
    page_title="🦜🔗 David's Tooklit",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="expanded",
)

hide_menu_style = """
        <style>
        #MainMenu {visibility: hidden;}
        </style>
        """
st.markdown(hide_menu_style, unsafe_allow_html=True)
image = Image.open("images/course-banner-1920.jpg")
st.image(image, caption='created by MJ')

# setup the CSS
icon_size = 20
load_css()


col1, col2, col3 = st.columns(3)
with col1:
   st.caption('')


with col2:
    st.markdown("""
                ##
                ##

                ## Empowering Conversation
                
                #### Opening doors to a better future .... 
                ## 
                ##
                ##

                """)

    
with col3:
   st.caption('')



col1, col2 = st.columns(2)
with col1:
    image = Image.open("images/space-banner.jpg")
    st.image(image)


with col2:
    # st.markdown('#### Content Creation')
    # st.markdown('######  fast, consistent, versatile, high-quality, and cost-effective tool for content creation.')  
    image = Image.open("images/doc-64.png")
    st.image(image)

    st.markdown("""
                ### ChatGPT for content creation  
                ## 
                ##### Here are some use cases:

                - **Blog Posts**: generate blog posts by topics.  

                - **Social Media Content**: creating social media content.  
                
                - **Descriptions**: generating product and service descriptions.  
                - **Email Marketing**: crafting persuasive email marketing.  
                - **News Articles**: generate news articles or summaries on trending topics.  
                - **Creative Writing**: generate stories, scripts and creative writing pieces.  
                - **SEO Content**: creating search engine optimized content by  keywords.  
                - **Technical Writing**: generating  documentation, user manuals,instructions.  
                - **Copywriting**: creating landing pages, web content forarketing materials.  
                - **Content Analysis**:  expanding existing content by providing additional insights and ideas.  

                
               """)
    

col1 , col2, col3 = st.columns(3)
with col1:
    image = Image.open("images/wp-64.png")
    st.image(image)
    st.markdown("""
                #### **:blue[Blog Posts]**  
                - Create blog content posts by topics for daily marketing or seo ranking.  
                - Prompt : N/A
                """)


    st_button('medium', 'https://import-2-vector.streamlit.app', 'Try it', icon_size)


with col2:
    image = Image.open("images/ads-64.png")
    st.image(image)
    st.markdown("""
                #### **:blue[Online Marketing Campaign]**  
                - Create SEM Ads statements (keywords, description) by business type.  
                - Prompt : 網頁製作 - 編寫新建公司網站簡約文章.txt
                """)

    st_button('medium', 'https://prompt-runner.streamlit.app/', 'Try it', icon_size)

with col3:
    image = Image.open("images/sales-doc-64.png")
    st.image(image)
    st.markdown("""
                #### **:blue[Sales & Marketing Script]**  
                - Create SEM Ads statements (keywords, description) by business type.  
                - Prompt : 商業應用 - 市場推廣， 編寫銷售文章.txt
                """)

    st_button('medium', 'https://import-2-vector.streamlit.app', 'Try it', icon_size)



# with col3:
#    st.caption('col3')

    


    # st.write('<p style="color:red;">Here is some red text</p>', 
    #         unsafe_allow_html=True)
    # st.write('<p style="font-size:26px; color:red;">Here is some red text</p>',
    # unsafe_allow_html=True)
    # # No \n or 2 space  - all in a line
    # st.write("""Line AAAAAAAAA
    #         Line BBBBB
    #         Line CCCCCC
    #         """)
    # # \n - double line 
    # st.write("""Line 1111111111
    #         \n Line 222222222222
    #         \n Line 33333333
    #         """)
    # # 2 space - only line feed
    # st.write("""Line 1111111111  
    #         Line 22222222222  
    #         Line 33333333  
    #         """)
    
    # st.write('## 2x# ')
    # st.write('### 3x# ')
    # st.write('### 4x# ')
    # st.write("""
    #          # 1x#
    #          ## 2x#
    #          ### 3x#
    #          #### 4x#
    #          """)
    
    # st.write('Here is some more **markdown** text. *And here is some more in italics*')

    # # add a new line for next paragraph
    # st.write("""
    #          ### I really like using Markdown.

    #         I think I'll use it to format all of my documents from now on.I think I'll use it to format all of my documents from now on.I think I'll use it to format all of my documents from now on.I think I'll use it to format all of my documents from now on.I think I'll use it to format all of my documents from now on.I think I'll use it to format all of my documents from now on.I think I'll use it to format all of my documents from now on.I think I'll use it to format all of my documents from now on.
             
    #          """)

 