import streamlit as st
from PIL import Image
import os
from functions import st_button, load_css

st.set_page_config(
    page_title="🦜🔗 David's Basic Tooklit",
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

                ##  ....  Empowering Your Conversation
                
                ###  Opening doors to a better future .... 
                ## 
                ##

                """)

    
with col3:
   st.caption('')


########
#  ROW 1
########

col1, col2 = st.columns(2)
with col1:
    image = Image.open("images/space-banner.jpg")
    st.image(image)

with col2:
    # st.markdown('#### Content Creation')
    # st.markdown('######  fast, consistent, versatile, high-quality, and cost-effective tool for content creation.')  
    # image = Image.open("images/doc-64.png")
    # st.image(image)

    st.markdown("""
                # ChatGPT for commerical content  
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
                **remark : above  use baisc use basic completion without embedding.  

                more ...
                
               """)
    
########
#  ROW 2
########
col1 , col2, col3 = st.columns(3)
with col1:
    image = Image.open("images/wp-64.png")
    st.image(image)
    st.markdown("""
                #### **:blue[Blog Posts]**  
                - Create blog content posts by topics for daily marketing or seo ranking.  
                - Prompt : Embedded in program.
                """)


    st_button('medium', 'https://blog-maker.streamlit.app/', 'Try it', icon_size)

with col2:
    image = Image.open("images/ads-64.png")
    st.image(image)
    st.markdown("""
                #### **:blue[Online Marketing Campaign]**  
                - Create SEM Ads statements (keywords, description).  
                - Prompt : 商業應用 - 市場推廣， SEM AdsWord 搜尋引擎...txt

                """)

    st_button('medium', 'https://prompt-runner.streamlit.app/', 'Try it', icon_size)

with col3:
    image = Image.open("images/sales-doc-64.png")
    st.image(image)
    st.markdown("""
                #### **:blue[Sales & Marketing Script]**  
                - Create detail product & service marketing script for promotion.  
                - Prompt : 商業應用 - 市場推廣， 編寫銷售文章.txt
                """)

    st_button('medium', 'https://prompt-runner.streamlit.app/', 'Try it', icon_size)





########
#  ROW 2
########

col1 , col2, col3 = st.columns(3)
with col1:
    image = Image.open("images/test-64.png")
    st.image(image)
    st.markdown("""
                #### **:blue[MC Test maker]**  
                - Generate a Multiple Choice Test with question and answer by user given content.  
                - Prompt : 問與答 - 按提供文本生成測驗試題.txt
                """)
    st_button('medium', 'https://prompt-runner.streamlit.app/', 'Try it', icon_size)


with col2:
    image = Image.open("images/questionnaire-64.png")
    st.image(image)
    st.markdown("""
                #### **:blue[Questionnaire Maker]**  
                - Create a series of question for basic understanding by age, output in Json format.  
                - Prompt : 問與答 - 環境與物件認知問卷.txt
                """)

    st_button('medium', 'https://prompt-runner.streamlit.app/', 'Try it', icon_size)

with col3:
    image = Image.open("images/happy-64.png")
    st.image(image)
    st.markdown("""
                #### **:blue[Causual Writer]**  
                - Create a 300 words in english and chinese to Uplift Your Happiness Level by emtions.  
                - Prompt : 文章製作 - 每天開心300字文章生成
                """)

    st_button('medium', 'https://import-2-vector.streamlit.app', 'Try it', icon_size)



st.markdown("""
            ## 
            ##
            ##

""")

########
#  ROW 4
########

col1, col2 = st.columns(2)
with col1:
    # image = Image.open("images/analysis-64.png")
    # st.image(image)

    st.markdown("""
                # ChatGPT for Classification, Sentiment analysis, Translation & Formatting 
                ## 
                ##### Here are some use cases:

                - **Extaction**: extract your define information.  

                - **Customer service**: Analyzing customer feedbacks for improvement.  

                - **Sentiment Analysis**: Classifying reviews as positive or negative.  

                - **Political analysis**: Analyzing public opinion on political issues.  
                - **Tourism**: Providing translations for tourists visiting.  
                - **Education**: Translating educational materials for overseas students.  
                - **Data storage**: JSON format for interoperability with other applications.  
                - **Image Recognition**: Classifying images and object detection. 

                more ...

                
               """)
with col2:
    image = Image.open("images/analysis-banner.jpg")
    st.image(image)


########
#  ROW 5
########
col1 , col2, col3 = st.columns(3)
with col1:
    image = Image.open("images/email-64.png")
    st.image(image)
    st.markdown("""
                #### **:blue[Business Administration ]**  
                - Classifying emails, identify intent, sugguest followup and extract information.  
                - Prompt : 訊息分析 - 電子郵撮要，分類，評估意圖，處理方法.txt
                """)
    st_button('medium', 'https://prompt-runner.streamlit.app/', 'Try it', icon_size)


with col2:
    image = Image.open("images/face-64.png")
    st.image(image)
    st.markdown("""
                #### **:blue[Product Analysis]**  
                - Brand monitoring by social media or product review determine overall sentiment ranking.  
                - Prompt : 訊息分析 - 產品使用後評論，情感分析，重點撮要.txt
                """)

    st_button('medium', 'https://prompt-runner.streamlit.app/', 'Try it', icon_size)

with col3:
    image = Image.open("images/translate-64.png")
    st.image(image)
    st.markdown("""
                #### **:blue[HR resume screening]**  
                - Extract & translate job applicant personal information, background, skills, and output Josn format.
                - Prompt : 訊息分析 - 提取個人簡歷內容、翻譯 、 (Json) 格式輸出.txt  

                """)

    st_button('medium', 'https://import-2-vector.streamlit.app', 'Try it', icon_size)




########
#  ROW 6
########
col1 , col2, col3 = st.columns(3)
with col1:
    image = Image.open("images/like-64.png")
    st.image(image)
    st.markdown("""
                #### **:blue[Public Relation]**  
                - Analyzing media news and social opinion on company issues , write internal letter (mockup purpose).  
                - Prompt : 事件評估 - 分析媒體資訊，撰寫內部公司通訊.txt
                """)
    st_button('medium', 'https://prompt-runner.streamlit.app/', 'Try it', icon_size)


with col2:
    image = Image.open("images/money-64.png")
    st.image(image)
    st.markdown("""
                #### **:blue[Account Department]**  
                - Create an overdue tution fee payment reminder with overdue interest calucation.  
                - Prompt : 商業應用 - 發出「逾期學費付款+逾期收費通知」.txt
                """)

    st_button('medium', 'https://prompt-runner.streamlit.app/', 'Try it', icon_size)

with col3:
    st.caption('')

st.markdown("""
            ## 
            ##
            ##

""")



col1, col2 = st.columns(2)
with col1:
    image = Image.open("images/story-banner.jpg")
    st.image(image)

with col2:
    # st.markdown('#### Content Creation')
    # st.markdown('######  fast, consistent, versatile, high-quality, and cost-effective tool for content creation.')  
    # image = Image.open("images/creative-64.png")
    # st.image(image)

    st.markdown("""
                # ChatGPT for Creative Story  
                ## 
                ##### Here are some use cases:

                - **Comic book creation**: generate story ideas, character and dialogue .  

                - **Writing prompts**: generate writing prompts for inspiration.  
                
                - **Storyboarding:**: create storyboards for films, animations.  
                - **Artistic inspiration**: crafting persuasive email marketing.  
                - **News Articles**: generate prompts or idea for AI tool such as midJourney.  

                more ...
                
               """)
    

########
#  ROW 5
########
col1 , col2, col3 = st.columns(3)
with col1:
    image = Image.open("images/writer-64.png")
    st.image(image)
    st.markdown("""
                #### **:blue[Outline Maker]**  
                - By enter title and era of the story, generate Synopsis, story outline and createive story reveiew.  
                - Prompt : implemented at Langchain 
                """)
    st_button('medium', 'https://storymaker-by-david.streamlit.app/', 'Try it', icon_size)


with col2:
    image = Image.open("images/comic-64.png")
    st.image(image)
    st.markdown("""
                #### **:blue[Comics Story Maker]**  
                - generate story ideas, character names, and even dialogue for comic book creators.  
                - Prompt : MidJourney 故事大綱製作，場景，人物及對話.txt
                """)

    st_button('medium', 'https://storymaker-by-david.streamlit.app/', 'Try it', icon_size)

with col3:
    image = Image.open("images/ppt-64.png")
    st.image(image)
    st.markdown("""
                #### **:blue[Comic Book Presentation]**  
                - Real example of using Comics Story Maker to generate idea, sences, character, dialogue .
                - Prompt : N/A

                """)

    st_button('medium', 'https://story-ppt-david.streamlit.app/', 'Try it', icon_size)


st.markdown("""
            ## 
            ##
            ##
            ##

""")





################################################################
#  Business Automation 
################################################################

st.markdown("""
            ## 
            ##
            ##

""")


col1, col2 = st.columns(2)
with col1:
    image = Image.open("images/website-banner.jpg")
    st.image(image)
with col2:
    # image = Image.open("images/research-64.png")
    # st.image(image)

    st.markdown("""
                # Business Automation -  Proposal , Market research and website content 
                ## 
                ##### Here are some use cases:

                - **Proposal writing**: generating proposal drafts by providing suggestions.  

                - **Market Research**: identifying trends, patterns, and insights.  

                - **Competitive Analysis**: analyze competitors, strengths and weaknesses.  

                - **Website content**: generate product descriptions,optimized for search engines.  
                - **Blog posts**: identifying trending topics and generating new ideas for blog posts.  
                - **Landing pages**: optimized for conversions and provide a clear call-to-action .  

                more ...

                
               """)

st.markdown("""
            ## 
            ##

""")

col1 , col2, col3 = st.columns(3)
with col1:
    image = Image.open("images/target-64.png")
    st.image(image)
    st.markdown("""
                #### **:blue[Market Research & SWOT]**  
                - Generate marketing research, use cases, Preparation procedures and Swot analysis  
                - Prompt : 商業自動化 - 市場分析、創業籌備要求、機會探討 ( chatgpt, langchain and zapier).txt
                """)
    st_button('medium', 'https://prompt-runner.streamlit.app/', 'Try it', icon_size)


with col2:
    image = Image.open("images/Proposal-64.png")
    st.image(image)
    st.markdown("""
                #### **:blue[Proposal  Generator]**  
                - Based on User requirement, generate a detail proposal for Business Automation with creative services and solution to targret current popular use case using AI, ChatGPT.  
                - Prompt : 商業自動化 - 編寫自動化服務(根據行業）技術要求分析.txt
                """)

    st_button('medium', 'https://prompt-runner.streamlit.app/', 'Try it', icon_size)

with col3:
    image = Image.open("images/website-64.png")
    st.image(image)
    st.markdown("""
                #### **:blue[Website Content Generator]**  
                -  Create Landing page, About Us page, Service Summary page and Why Choose us page by busines type.  
                - Prompt : 商業自動化 - 編寫公司網頁內容文章 (front page, about us, services, contact us).txt  

                """)

    st_button('medium', 'https://prompt-runner.streamlit.app/', 'Try it', icon_size)





################################################################
#  Event Planning
################################################################

st.markdown("""
            ## 
            ##
            ##

""")


col1, col2 = st.columns(2)
with col1:
    image = Image.open("images/event-banner.jpg")
    st.image(image)

with col2:
    st.markdown("""
            # ChatGPT for event planning 
            ## 
            ##### Here are some use cases:

            - **Generating ideas**: themes, activities, and entertainment based on goals.  

            - **Recommendations**:  venues, catering and  suppliers based on the budget.  

            - **Marketing**: promotion strategies,  social media  and email marketing.  

            - **Real-time updates**: logistics, schedule changes and transportation arrangements.  
            - **Customer Support**:  handling complaints or issues that arise during the event.  
            - **Post-event surveys**: gathering feedback to improve future events.  

            more ...

            
            """)




st.markdown("""
            ## 
            ##

""")

col1 , col2, col3 = st.columns(3)
with col1:
    image = Image.open("images/event-proposal-64.png")
    st.image(image)
    st.markdown("""
                #### **:blue[Event Proposal Generator]**  
                - Theme inspiration, Proposed Venue, Time Schedule, Online Marketing Strategy, Sponsorship, Rundown, venue.
                - Prompt : 商業應用 - 活動策劃建議書，主題，時間表，活動場地.txt
                """)
    st_button('medium', 'https://prompt-runner.streamlit.app/', 'Try it', icon_size)


with col2:
    image = Image.open("images/manpower-64.png")
    st.image(image)
    st.markdown("""
                #### **:blue[event day rundown and manpower allocation]**  
                - Generate detail daily rundown (Preparation, Live, and Post. activities), include tasks and manpower.  
                - Prompt : 商業應用 - 編寫活動日流程 ，人手安排.txt
                """)

    st_button('medium', 'https://prompt-runner.streamlit.app/', 'Try it', icon_size)

with col3:
    image = Image.open("images/risk-64.png")
    st.image(image)
    st.markdown("""
                #### **:blue[Event Risk assessment]**  
                - discovery of possible risks, available actions , arrange manpower to handle this problem.  
                - Prompt : 商業應用 - 編寫活動風險管理評估.txt  

                """)

    st_button('medium', 'https://prompt-runner.streamlit.app/', 'Try it', icon_size)





################################################################
#  Access and Query the interet 
################################################################

st.markdown("""
            ## 
            ##
            ##

""")


col1, col2 = st.columns(2)
with col1:
    st.markdown("""
            # Explore the Internet
            ## 
            ##### Here are some use cases:

            - **Finding answers**: Ask FAQ questions.  

            - **Troubleshooting**: Searching solution for technical issues.  
                
            - **Requesting information**: Applying for job positions.  

            - **Law**: getting updates on latest policy .  
            - **Insurance**: find protection amount ? What Illness Covered.  

            more ...

            
            """)

with col2:
    image = Image.open("images/internet-banner.jpg")
    st.image(image)





st.markdown("""
            ## 
            ##

""")

col1 , col2, col3 = st.columns(3)
with col1:
    image = Image.open("images/website-64.png")
    st.image(image)
    st.markdown("""
                #### **:blue[Website Reader]**  
                - Enter Url of Website, and you can Query information about this web content. Reference WebSite: Governement, Insurance policy, Service charges, user manual ...
                - Prompt : You provide. Use Vector DB and Langchain implementation.
                """)
    st_button('medium', 'https://website-reader.streamlit.app/', 'Try it', icon_size)


with col2:
    image = Image.open("images/google-64.png")
    st.image(image)
    st.markdown("""
                #### **:blue[Google Search]**  
                - Finding specific information about a topic, such as historical events, scientific concepts, or current events or Seeking advice or opinions  
                - Prompt : You provide. Use Vector DB,  Langchain and Serpapi implementation.
                """)

    st_button('medium', 'https://search-by-david.streamlit.app/', 'Try it', icon_size)

with col3:
    image = Image.open("images/fin-question-64.png")
    st.image(image)
    st.markdown("""
                #### **:blue[Stock Research Use Case]**  
                - With your given financial questions, ask Google and LLM to research company background, competitors and performance before making a purchase decisionm.  
                - Prompt : You provide. Use Langchain and Serpapi implementation.

                """)

    st_button('medium', 'https://search-finance-news.streamlit.app', 'Try it', icon_size)





################################################################
#  Ask your Files 
################################################################

st.markdown("""
            ## 
            ##
            ##

""")


col1, col2 = st.columns(2)
with col1:
    # image = Image.open("images/research-64.png")
    # st.image(image)
    st.markdown("""
            # Chat your Documents
            ## 
            ##### Here are some use cases:

            - **Extraction**: Searching for specific data or information.  

            - **Searching**:  Searching for specific tables or figures.  
                
            - **Marketing**: promotion strategies,  social media  and email marketing.  

            - **Real-time updates**: logistics, schedule changes and transportation arrangements.  
            - **Customer Support**:  handling complaints or issues that arise during the event.  
            - **Post-event surveys**: gathering feedback to improve future events.  

            more ...

            
            """)
    st.caption(""" :red[remark : **Do not upload data with confidential information !!!!!]  
                Using Local LLM, embedding and vector Storage can protect data privacy . 
                """)
with col2:
    image = Image.open("images/import_banner.jpg")
    st.image(image)





st.markdown("""
            ## 
            ##

""")

col1 , col2, col3 = st.columns(3)
with col1:
    image = Image.open("images/txt-64.png")
    st.image(image)
    st.markdown("""
                #### **:blue[Ask your (txt) file]**  
                - Upload your TXT file and ask question (in plain english) about the content.
                - Sample test Data file : office-automation.txt
                """)
    st_button('medium', 'https://prompt-runner.streamlit.app/', 'Try it', icon_size)


with col2:
    image = Image.open("images/csv-64.png")
    st.image(image)
    st.markdown("""
                #### **:blue[Ask your (CSV) file]**  
                - Upload your CSV file and ask question (in structure format) related to content.
                - Sample test Data file : client-orders.csv
                """)

    st_button('medium', 'https://simple-csv-reader.streamlit.app', 'Try it', icon_size)

with col3:
    image = Image.open("images/pdf-64.png")
    st.image(image)
    st.markdown("""
                #### **:blue[Ask your (PDF)]**  
                - Upload your (PDF) file and ask question (in plain english) about the content.
                - Sample test Data file : job_post_01.pdf

                """)

    st_button('medium', 'https://pdf-chat.streamlit.app', 'Try it', icon_size)




################################################################
#  Data Analysis
################################################################

st.markdown("""
            ## 
            ##
            ##

""")


col1, col2 = st.columns(2)
with col1:
    image = Image.open("images/data-analysis-banner.jpg")
    st.image(image)


with col2:
    # image = Image.open("images/research-64.png")
    # st.image(image)
    st.markdown("""
            # Data Insight by Pandas + ChatGPT
            ## 
            ##### Here are some use cases:

            - **Insights**: Answering questions about data.  

            - **visualizations**: Generate chart in Pandas DataFrame.  
                
            - **Data cleaning**: Handle missing or invalid data.  

            - **Trends and patterns**: identifying correlations or anomalies.  
            - **Automating workflows:**:  providing code snippets for common tasks.  

            more ...

            
            """)
    st.caption(""" :red[remark : **Do not upload data with confidential information !!!!!]  
                Using Local LLM, embedding and vector Storage can protect data privacy . 
                """)




st.markdown("""
            ## 
            ##

""")

col1 , col2, col3 , col4 = st.columns(4)
with col1:
    image = Image.open("images/calendar-64.png")
    st.image(image)
    st.markdown("""
                #### **:blue[Study Plan Summarization]**  
                - ChatGPT provide data Summarization for common question and answer.
                - Sample test Data file : study.csv
                """)
    st_button('medium', 'https://ask-studyplan.streamlit.app/', 'Try it', icon_size)


with col2:
    image = Image.open("images/orders-64.png")
    st.image(image)
    st.markdown("""
                #### **:blue[Purchase Order Summarization]**  
                - Upload your CSV file and ask question (in structure format) related to content.
                - Sample test Data file : client-orders.csv
                """)
    
    st_button('medium', 'https://ask-orders-csv.streamlit.app/', 'Try it', icon_size)

with col3:
    image = Image.open("images/sqldb-64.png")
    st.image(image)
    st.markdown("""
                #### **:blue[High performance by Sql Datase]**  
                - Just Upload any CSV, your Query will transform to SQL Query for high performance.
                - Sample test Data file : Any CSV

                """)

    st_button('medium', 'https://csv-sqldb.streamlit.app/', 'Try it', icon_size)



with col4:
    image = Image.open("images/pandas-64.png")
    st.image(image)
    st.markdown("""
                #### **:blue[Smart Query by Pandas AI]**  
                - Using plain english query with Pandas AI create the Structure SQL Query.
                - Sample test Data file : titanic.csv

                """)

    st_button('medium', 'https://smart-csv.streamlit.app/', 'Try it', icon_size)










################################################################
#  News API extract and summary
################################################################

st.markdown("""
            ## 
            ##
            ##

""")


col1, col2 = st.columns(2)
with col1:
    # image = Image.open("images/research-64.png")
    # st.image(image)
    st.markdown("""
            # News Scraping and Summarize 
            ## 
            ##### Features:

            - **News API**: Live feed capture by invoke RestAPI endpoints.  

            - **web scraping**: Extract valuebale website content.  
                
            - **Pinecone**: create vectors and embedding.  

            - **Summarize**: Extract the main points.  

            - **Extraction**: Provide main ideas and keywords .  

            more ...
            
            """)
    st_button('medium', 'https://import-2-vector.streamlit.app', 'Try it', icon_size)
with col2:
    image = Image.open("images/news-extract-banner.jpg")
    st.image(image)

################################################################
#  Product Recommnation
################################################################

st.markdown("""
            ## 
            ##
            ##

""")


col1, col2 = st.columns(2)
with col1:
    image = Image.open("images/news-extract-banner2.jpg")
    st.image(image)

with col2:
    # image = Image.open("images/research-64.png")
    # st.image(image)
    st.markdown("""
            # Product Recommendations 
            ## 
            ##### Features:
            - **Database Access**: Collect various data sources.  

            - **Embedding**: Create embedding for Customer Order, Product and enquiry.  

            - **Similarity Search**: Perform matching Customer Orders and Products.  
                
            - **Recommendations**: Create the matching recommendations.  

            - **Summarize**: Create final statement with product and discount.  

            more ...
            
            """)
    st_button('medium', 'https://recommend-cs.streamlit.app/', 'Try it', icon_size)


################################################################
#  Customer Service ChatBot
################################################################

col1, col2 = st.columns(2)
with col1:
    image = Image.open("images/cs-chatbot-1-banner.jpg")
    st.image(image)

with col2:
    st.markdown("""
            # CS Chatbot 
            ## 
            ##### Features:

            - **7x24 Services**: servicing your client non-stop.  

            - **Smart**: Understand your client need, response instantly.  
                
            - **Extension**: Can extend business functionalities (Enquiry, Complaint, Order and helpDesk)

            more ...
            
            """)
    st_button('medium', 'https://asking-chatbot-1.streamlit.app', 'Try it', icon_size)




################################################################
#  Data visualization
################################################################

st.markdown("""
            ## 
            ##
            ##

""")


col1, col2 = st.columns(2)
with col1:
    # image = Image.open("images/research-64.png")
    # st.image(image)
    st.markdown("""
            # Data visualization
            ## 
            ##### Features:

            - **UI/UX**: Dashbord style for better nagviation.  

            - **Chart**: figure presentation with dynamic update.  
                
            - **Recommendations**: create NLP 

            more ...
            
            """)
    st_button('medium', 'https://xls-loader.streamlit.app/', 'Try it', icon_size)

with col2:
    image = Image.open("images/chart-ui-banner.jpg")
    st.image(image)






st.write('You can download the Prompt text and sample data files here:')
st.write('prompt  : https://drive.google.com/drive/u/2/folders/1g4dY-98nV5gl4RUT5l0aNmdXBfW73k6v')
st.write(' csv, txt, pdf file  : https://drive.google.com/drive/u/2/folders/1s3GLfc61m7a0AOzOThMrheoQDjjLcKrC')







 
    
 
 
