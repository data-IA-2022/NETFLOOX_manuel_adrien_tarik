from pathlib import Path
import streamlit as st
from streamlit.components.v1 import html
from PIL import Image
import pandas as pd
import mydbconnection as mdbcon
from sqlalchemy import text

def reco_page(style):
    conn = mdbcon.connect_to_db("config.yaml", "mysql_azure_netfloox")
    selected_option = ""

    with open("assets/reco_page_style.css") as style:
        # reco_page_html = f"""
        # <!DOCTYPE html>
        # <html>
        # <head>
        # <style>{style.read()}</style>
        # <script src="https://unpkg.com/htmx.org/dist/htmx.min.js"></script>
        # </head>
        # <body>

        # <h1>This is a heading</h1>
        # <p>This is a paragraph.</p>

        # </body>
        # </html>
        # """
        with st.form(key='my_form'):
            # Define the search box for the user's input
            user_input = ""
            
            # Define the SQL query to retrieve the movie titles based on the user's input
            query = text("""
                SELECT originalTitle
                FROM table_list_films
                WHERE originalTitle LIKE :user_input
                ;
            """)
            
            # Execute the SQL query with the user's input as a parameter
            options = conn.execute(query, {'user_input': f"%{user_input}%"})
            options = [option[0] for option in options]
            
            # Add the select box to display the movie titles
            option = st.selectbox('Select a movie title:', options, key='title_select')
            submit_button = st.form_submit_button(label='Submit')

        if submit_button:
            st.write('You selected:', option)
        
        # html(reco_page_html)
        
        
        
