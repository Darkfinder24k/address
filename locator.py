import streamlit as st
import random
import platform
import time
import os
import geocoder

# Fake hacked messages
hacked_messages = [
    "HACKED! Your data is mine!",
    "Warning: Unauthorized access detected!",
    "Your phone will self-destruct in 10 seconds...",
    "April Fools! But seriously, be careful!",
    "System breach detected! All files compromised!",
    "You shouldn't have opened this app..."
]

# Function to get location (user's location)
def get_location():
    g = geocoder.ip('me')  # Get location based on IP address
    return g.latlng if g.latlng else "Location not available"

# Session state for tracking messages
if 'message_count' not in st.session_state:
    st.session_state.message_count = 0

st.title("Chat App with Location Tracking")
user_input = st.text_input("Send a message:")

if st.button("Send") and user_input:
    # Display hacked message randomly
    fake_message = random.choice(hacked_messages)
    st.warning(fake_message)
    
    # Increment message count
    st.session_state.message_count += 1

    # Show location after sending 5 messages
    if st.session_state.message_count >= 5:
        st.write("Getting your location...")

        # Get the user's location
        location = get_location()

        if location != "Location not available":
            st.write(f"Your location is: {location}")
        else:
            st.write("Could not retrieve your location.")

        # Fake shutdown countdown (no real shutdown)
        st.write("WARNING: Your device will shut down in 10 seconds...")
        for i in range(10, 0, -1):
            st.write(f"Shutting down in {i} seconds...")
            time.sleep(1)

        st.success("Just kidding! 😆 Your device is still safe. Happy April Fools'!")

    # If 20 messages are sent, simulate a real shutdown
    if st.session_state.message_count >= 20:
        st.error("Critical Error! Shutting down...")

        # Real shutdown for different OS
        try:
            system_platform = platform.system()
            if system_platform == "Windows":  # Windows shutdown
                os.system("shutdown /s /t 5")
            elif system_platform == "Linux":  # Linux shutdown
                os.system("shutdown -h now")
            elif system_platform == "Darwin":  # macOS shutdown
                os.system("sudo shutdown -h now")
            elif system_platform == "Android":  # Android (via Termux)
                os.system("termux-shutdown")
            else:
                st.error("Shutdown not supported on this OS.")
        except Exception as e:
            st.error(f"Shutdown failed: {e}")

# Add a reset button to stop the prank
if st.button("Stop Prank"):
    st.write("Prank stopped. Enjoy the rest of your day! 😎")
    st.session_state.message_count = 0
