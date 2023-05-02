import streamlit as st
import wttr

st.title("Weather Forecast")

# Create a text input field for the city name
city = st.text_input("Enter City Name:")

# Check if the user has entered a city name
if city:
    # Use the wttr module to get the weather forecast for the city
    report = wttr.get_report(city)
    weather = report.text.replace('\n', '<br>')
    
    # Display the weather forecast in HTML format
    st.write(f"<h2>Weather Forecast for {city.title()}:</h2>", unsafe_allow_html=True)
    st.write(f"<p>{weather}</p>", unsafe_allow_html=True)
