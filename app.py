import streamlit as st  
import pandas as pd  


# Add a title to the app  
st.title("¡Digame!") 
# Add a gif graphic
st.markdown("![snoopy flipping through a book](https://media.giphy.com/media/9X6OGGZ2SNyQ8/giphy.gif)")

# Load the data backing this app
file = r"C:\Users\folder\file.csv"  
df = pd.read_csv(file, encoding='unicode_escape') 

# Create a text input field for the user to enter an acronym 
search_term = st.text_input('Enter an acronym:')  
if search_term:  
    # Filter the df to only show rows where the acronym column contains the search term 
    results = df[df['acronym'].str.contains(search_term, case=False)]  

    if results.empty:  
        st.write('No results found.')  
    else:  
        # For each row in the filtered dataframe, display the acronym and definition
        for index, row in results.iterrows():  
            st.write(row['acronym'], ' - ', row['definition'])  



