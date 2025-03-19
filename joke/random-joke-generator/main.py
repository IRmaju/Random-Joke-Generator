import streamlit as st  # Streamlit for web app
import requests  # Requests for API calls

def get_random_joke():
    """Fetch a random joke from API"""
    try:
        response = requests.get("https://v2.jokeapi.dev/joke/Any?safe-mode")
        if response.status_code == 200:
            joke_data = response.json()
            if joke_data["type"] == "single":
                return joke_data["joke"]
            else:
                return f"{joke_data['setup']} \n\n {joke_data['delivery']}"
        else:
            return "Failed to fetch a joke. Please try again later."
    except:
        return "Why do Java developers wear glasses? \n Because they can't C#"

def main():
    """Main function for Streamlit app"""
    # Custom CSS for styling
    st.markdown(
        """
        <style>
            .main-title {
                text-align: center;
                font-size: 36px;
                font-weight: bold;
                color: #FF5733;
            }
            .button-container {
                text-align: center;
                margin-top: 20px;
            }
            .joke-text {
                background-color: #f8f9fa;
                border-left: 5px solid #FF5733;
                padding: 10px;
                margin: 20px 0;
                font-size: 18px;
                color: #333;
            }
            .footer {
                text-align: center;
                margin-top: 30px;
                font-size: 14px;
                color: #555;
            }
        </style>
        """, unsafe_allow_html=True
    )
    
    st.markdown("<h1 class='main-title'>Random Joke Generator</h1>", unsafe_allow_html=True)
    st.write("Click the button below to get a joke!")
    
    if st.button("Generate Joke"):
        joke = get_random_joke()
        st.markdown(f"<div class='joke-text'>{joke}</div>", unsafe_allow_html=True)
    
    st.divider()
    
    st.markdown(
        """
        <div class='footer'>
            <p>Joke from JokeAPI</p>
            <p>Built with ❤️ using Streamlit</p>
        </div>
        """, unsafe_allow_html=True
    )

if __name__ == "__main__":
    main()
