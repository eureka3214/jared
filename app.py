import streamlit as st
# import hydralit_components as hc
from streamlit_option_menu import option_menu
import streamlit.components.v1 as html
# from streamlit_card import card
import openai
import os
openai.api_key =  os.getenv("APIKEY")
st.set_page_config(page_title="My App", page_icon=":rocket:", layout="wide",initial_sidebar_state="expanded"  )
st.write('<style>div.block-container{padding-top:2rem;}</style>', unsafe_allow_html=True)

st.markdown(
    f"""
    <style>
    #MainMenu {{visibility: hidden;}}

    .stApp {{
        background-image: url("data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' version='1.1' xmlns:xlink='http://www.w3.org/1999/xlink' xmlns:svgjs='http://svgjs.com/svgjs' width='1440' height='560' preserveAspectRatio='none' viewBox='0 0 1440 560'%3e%3cg mask='url(%26quot%3b%23SvgjsMask1776%26quot%3b)' fill='none'%3e%3crect width='1440' height='560' x='0' y='0' fill='url(%23SvgjsRadialGradient1777)'%3e%3c/rect%3e%3cpath d='M1440 0L1075.24 0L1440 200.66z' fill='rgba(255%2c 255%2c 255%2c .1)'%3e%3c/path%3e%3cpath d='M1075.24 0L1440 200.66L1440 385.78999999999996L805.3299999999999 0z' fill='rgba(255%2c 255%2c 255%2c .075)'%3e%3c/path%3e%3cpath d='M805.3299999999999 0L1440 385.78999999999996L1440 475.81999999999994L426.23999999999995 0z' fill='rgba(255%2c 255%2c 255%2c .05)'%3e%3c/path%3e%3cpath d='M426.24 0L1440 475.81999999999994L1440 482.0899999999999L240.93 0z' fill='rgba(255%2c 255%2c 255%2c .025)'%3e%3c/path%3e%3cpath d='M0 560L572.89 560L0 514.51z' fill='rgba(0%2c 0%2c 0%2c .1)'%3e%3c/path%3e%3cpath d='M0 514.51L572.89 560L658.02 560L0 246.98000000000002z' fill='rgba(0%2c 0%2c 0%2c .075)'%3e%3c/path%3e%3cpath d='M0 246.98000000000002L658.02 560L685.54 560L0 165.40000000000003z' fill='rgba(0%2c 0%2c 0%2c .05)'%3e%3c/path%3e%3cpath d='M0 165.40000000000003L685.54 560L1030.17 560L0 132.26000000000005z' fill='rgba(0%2c 0%2c 0%2c .025)'%3e%3c/path%3e%3c/g%3e%3cdefs%3e%3cmask id='SvgjsMask1776'%3e%3crect width='1440' height='560' fill='white'%3e%3c/rect%3e%3c/mask%3e%3cradialGradient cx='0%25' cy='50%25' r='1466.97' gradientUnits='userSpaceOnUse' id='SvgjsRadialGradient1777'%3e%3cstop stop-color='rgba(248%2c 186%2c 246%2c 1)' offset='0'%3e%3c/stop%3e%3cstop stop-color='rgba(248%2c 78%2c 242%2c 1)' offset='1'%3e%3c/stop%3e%3c/radialGradient%3e%3c/defs%3e%3c/svg%3e");
        
    }}

    .sidebar .sidebar-content {{
                background: rgba( 0, 0, 0, 0 );
                width: 200px;

            }}

    .stButton {{
        background-color: linear-gradient(to right, #9B59B6, #f63633);
    }}

    .stTextArea {{ 
            font-size:20px; 
            font-weight:bold; 

            }}
    </style>
    """,
    unsafe_allow_html=True
    )
# st.markdown("<style> .stTextArea > label {font-size:14px; font-weight:bold;} </style> ",unsafe_allow_html=True) 
   
with st.sidebar:
    choose = option_menu("App Gallery", ["Write For Me", "Idea Generator", "Promotion Ideas", "Account", "Log Out"],
                         icons=['cpu', 'lightbulb fill', 'bar-chart fill', 'book','person dash'],
                         menu_icon="app-indicator", default_index=0,
                         styles={
        "container": {"padding": "5!important","background": "rgba(255, 255, 255, 0.2)","border-radius": "16px","box-shadow": "0 4px 30px rgba(0, 0, 0, 0.1)","backdrop-filter": "blur(5px)","-webkit-backdrop-filter": "blur(5px)","border": "1px solid rgba(255, 255, 255, 0.3)"},
        "icon": {"font-color":"Grey", "font-size": "14px", "border-radius":"50%"}, 
        "nav-link": {"font-size": "12px","font-weight":"700", "border-radius":"10px", "font-color":"Grey", "text-align": "left", "margin":"10px", "--hover-color": "#FF69B4", "--hover-box-shadow": "0 0 35px rgba(145, 92, 182, .4)"},
        "nav-link-selected": {"background": " linear-gradient(to right, #9B59B6, #f63633);"},
    }
    )

    # with st.container():
    #     box=option_menu("Trial Pack", ["Click to subscribe"],
    #                      icons=['currency-exchange'],
    #                      menu_icon="activity", default_index=0,
    #                     styles={
    #     "container": {"padding": "5!important","background": "rgba(255, 255, 255, 0.2)","border-radius": "16px","box-shadow": "0 4px 30px rgba(0, 0, 0, 0.1)","backdrop-filter": "blur(5px)","-webkit-backdrop-filter": "blur(5px)","border": "1px solid rgba(255, 255, 255, 0.3)"},
    #     "icon": {"font-color":"Grey", "font-size": "15px", "border-radius":"50%"}, 
    #     "nav-link": {"font-size": "12px","font-weight":"700", "border-radius":"10px", "font-color":"Grey", "text-align": "left", "margin":"10px", "--hover-color": "#FF69B4", "--hover-box-shadow": "0 0 35px rgba(145, 92, 182, .4)"},
    #     "nav-link-selected": {"background": " linear-gradient(to right, #9B59B6, #f63633);"},
    # }
    # )



if choose == "Write For Me":

    col1, col2,= st.columns(2)
    with col1:
        usecase = st.selectbox("Use Case",  ('Email', 'Home phone', 'Mobile phone'),label_visibility='visible' )
    with col2:
        tone = st.selectbox("Select Tone",  ('Email', 'Home phone', 'Mobile phone'),label_visibility='visible')

    descript = st.text_area("Description",label_visibility='visible')

    output = st.text_area("Heres your Text",label_visibility='visible')
    save = st.button("Save")
    if save:
        query = str(usecase) + str(tone) + str(descript)
        st.write(query)

    # columa, columb = st.columns([10,1])
    # with columb:
        
        
            






# col1, col2,= st.columns(2)

# if choose == "Write For Me":
#     # with col1:
#     st.subheader('Write for me')
#     des=st.text_area(label='Description',label_visibility='collapsed' )
#     if st.button('Submit'):
#         reply = openai.Completion.create(
#                                     engine="text-davinci-003",
#                                     prompt=des,
#                                     max_tokens=3600,
#                                     n=1,
#                                     stop=None,
#                                     temperature=0.5,
#                                     )
#         explan= reply.choices[0].text.strip()
#         # st.code(explan)
#     # with col2:
#     st.subheader('Generated OutPuts')

#     try:
#         explan= reply.choices[0].text.strip()
#         st.code(explan)
#     except:
#         st.code("Input something and click submit")
#         # st.code(explan)
#             # st.stop()
                
# elif choose == "Idea Generator":
#     with col1:

#         st.subheader('Idea Generator')
#         src = st.text_input("source Link")
#         des=st.text_area(label='Description',label_visibility='collapsed' )
#         if st.button('Submit'):
#             prompt = str(des) + " " + " Response should be based from this source :" + str(src)
#             reply = openai.Completion.create(
#                                         engine="text-davinci-003",
#                                         prompt=des,
#                                         max_tokens=3600,
#                                         n=1,
#                                         stop=None,
#                                         temperature=0.5,
#                                         )
#             idea= reply.choices[0].text.strip()
#             # st.code(explan)
#     with col2:
#         st.subheader('Generated OutPuts')

#         try:
#             idea= reply.choices[0].text.strip()
#             st.code(idea)
#         except:
#             st.code("Input something and click submit")
#         # st.code(explan)
# # st.stop()


# elif choose == "Promotion Ideas":
#     with col1:
#         st.subheader('Promotion Ideas')
#         string_list = ['OnlyFans mass Message', 'Caption For Instagram Post', 'Reply for a Tweet or Message']
#         selected_option = st.selectbox('Select an option', string_list, label_visibility ='collapsed')
# # Define the options for the select box
#         options = [' That Would arrouse and turn on the guy who is reading it and make him ask for nudes ', ' that Would grab the attention of the person who is reads it and well suits the caption ', ' a sarcastic response']
#         des=st.text_area(label='Description',label_visibility='collapsed' ,placeholder='Specify under which context')
#         promp = "Generate a " + selected_option + ' ' + options[string_list.index(selected_option)] + ' Under the following context' + des
#         if st.button('Submit'):
#             reply = openai.Completion.create(
#                                         engine="text-davinci-003",
#                                         prompt=str(promp),
#                                         max_tokens=3600,
#                                         n=1,
#                                         stop=None,
#                                         temperature=0.5,
#                                         )
#             explan= reply.choices[0].text.strip()
#             # st.code(explan)
#     with col2:
#         st.subheader('Generated OutPuts')

#         try:
#             explan= reply.choices[0].text.strip()
#             st.code(explan)
#         except:
#             st.code("Input something and click submit")
