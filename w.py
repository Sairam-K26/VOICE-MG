import streamlit as st
import sounddevice as sd
import numpy as np
import wavio
import whisper
import os
import base64
import requests
from bs4 import BeautifulSoup
import time

def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
        f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
        background-size: 150px 150px;
        background-position: bottom right;
        background-repeat: no-repeat;
    }}
    </style>
    """,
        unsafe_allow_html=True
    )

def record_audio(output_filename, duration, sample_rate):
    st.write("Recording...")
    audio_data = sd.rec(int(duration * sample_rate),
                        samplerate=sample_rate, channels=1)
    sd.wait()  # Wait until recording is finished
    st.write("Recording finished.")

    # Save the recorded audio to a WAV file
    wavio.write(output_filename, audio_data, sample_rate, sampwidth=2)

def main():
    st.title("Speech-to-Text and Grammar Checking")
    add_bg_from_local("bg 1.png")

    # Sidebar input for recording duration
    recording_duration = st.sidebar.number_input("Recording Duration (seconds)", value=5, min_value=1)

    # Record audio button
    if st.sidebar.button("Record Audio"):
        output_file = "recorded_audio.wav"  # Specify the output file name
        sample_rate = 44100  # Sampling rate (samples per second)

        record_audio(output_file, recording_duration, sample_rate)
        st.sidebar.write("Audio saved as:", output_file)

        # Verify if the audio file exists
        if os.path.exists(output_file):
            # Load the Whisper model
            model = whisper.load_model('small')

            # Show the "Recording finished" message and start the spinner
            st.write("Recording finished.")
            with st.spinner("Processing your audio..."):
                # Simulate processing delay (you can remove this)
                time.sleep(2)

                # Transcribe the audio using the loaded model
                transcribed_text = model.transcribe(output_file)

            # Stop the spinner after transcription is complete
            st.spinner(False)

            st.success("Transcription Complete!")
            st.write("Transcribed Text:")
            st.write(transcribed_text['text'])
        else:
            st.sidebar.write("Audio file not found. Please record audio first.")

if __name__ == "__main__":
    main()
