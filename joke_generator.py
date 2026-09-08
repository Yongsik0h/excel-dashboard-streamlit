"""
Random Joke Generator using External API
외부 API를 사용한 랜덤 농담 생성기
"""

import streamlit as st
import requests
import json

st.set_page_config(
    page_title="Random Joke Generator",
    page_icon="😂",
    layout="centered"
)

st.title("😂 Random Joke Generator")
st.markdown("**Get random jokes from the internet!**")

# Sidebar - API Selection
st.sidebar.header("⚙️ Settings")
api_source = st.sidebar.selectbox(
    "Select Joke API",
    ["JokeAPI", "Official Joke API", "Dad Jokes"]
)

joke_type = "general"
if api_source == "JokeAPI":
    joke_type = st.sidebar.selectbox(
        "Joke Type",
        ["general", "programming", "knock-knock", "spooky", "christmas"]
    )

# Function to get joke from different APIs
def get_joke_jokeapi(joke_type="general"):
    """Get joke from JokeAPI"""
    try:
        url = f"https://v2.jokeapi.dev/joke/{joke_type}"
        response = requests.get(url, timeout=5)
        
        if response.status_code == 200:
            data = response.json()
            
            if data.get('type') == 'single':
                return {
                    'joke': data.get('joke'),
                    'category': data.get('category'),
                    'source': 'JokeAPI'
                }
            else:
                return {
                    'joke': f"{data.get('setup')} ... {data.get('delivery')}",
                    'category': data.get('category'),
                    'source': 'JokeAPI'
                }
        else:
            return None
    except Exception as e:
        st.error(f"❌ Error: {str(e)}")
        return None

def get_joke_official():
    """Get joke from Official Joke API"""
    try:
        url = "https://official-joke-api.appspot.com/random_joke"
        response = requests.get(url, timeout=5)
        
        if response.status_code == 200:
            data = response.json()
            return {
                'joke': f"{data.get('setup')} ... {data.get('punchline')}",
                'category': data.get('type'),
                'source': 'Official Joke API'
            }
        else:
            return None
    except Exception as e:
        st.error(f"❌ Error: {str(e)}")
        return None

def get_joke_dadjokes():
    """Get joke from Dad Jokes API"""
    try:
        url = "https://icanhazdadjoke.com/"
        headers = {'Accept': 'application/json'}
        response = requests.get(url, headers=headers, timeout=5)
        
        if response.status_code == 200:
            data = response.json()
            return {
                'joke': data.get('joke'),
                'category': 'Dad Joke',
                'source': 'Dad Jokes API'
            }
        else:
            return None
    except Exception as e:
        st.error(f"❌ Error: {str(e)}")
        return None

# Main content
col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    if st.button("🎭 Get New Joke", use_container_width=True):
        with st.spinner("Fetching a joke..."):
            joke_data = None
            
            if api_source == "JokeAPI":
                joke_data = get_joke_jokeapi(joke_type)
            elif api_source == "Official Joke API":
                joke_data = get_joke_official()
            elif api_source == "Dad Jokes":
                joke_data = get_joke_dadjokes()
            
            if joke_data:
                # Display joke in a nice box
                st.markdown("---")
                st.markdown(f"### 😄 {joke_data['joke']}")
                
                col1, col2 = st.columns(2)
                with col1:
                    st.caption(f"📂 Category: {joke_data['category']}")
                with col2:
                    st.caption(f"📡 Source: {joke_data['source']}")
                
                st.markdown("---")
            else:
                st.error("❌ Failed to fetch joke. Please try again!")

# Info section
with st.expander("ℹ️ About the APIs"):
    st.markdown("""
    ### Available APIs:
    
    **1. JokeAPI**
    - Categories: General, Programming, Knock-Knock, Spooky, Christmas
    - Mixed format (single-line and setup/delivery jokes)
    - Website: https://jokeapi.dev/
    
    **2. Official Joke API**
    - Simple setup/punchline format
    - Various joke types
    - Website: https://official-joke-api.appspot.com/
    
    **3. Dad Jokes**
    - Classic dad joke generator
    - Single-line format
    - Website: https://icanhazdadjoke.com/
    """)

# Footer
st.divider()
st.markdown("""
    <div style='text-align: center; color: #666; font-size: 12px;'>
        <p>Random Joke Generator | Powered by Streamlit & External APIs</p>
    </div>
""", unsafe_allow_html=True)
