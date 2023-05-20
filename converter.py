import streamlit as st
from pydub import AudioSegment
from io import BytesIO

def mp3_to_wav(mp3_file):
    audio = AudioSegment.from_mp3(mp3_file)
    wav_file = BytesIO()
    audio.export(wav_file, format="wav")
    return wav_file

def main():
    st.title("MP3 to WAV Converter")
    st.write("Select an MP3 file to convert to WAV")

    # File uploader
    mp3_file = st.file_uploader("Upload an MP3 file", type=["mp3"])

    if mp3_file is not None:
        # Convert the file
        wav_file = mp3_to_wav(mp3_file)
        st.success("Conversion successful!")

        # Provide download link for the converted WAV file
        st.download_button("Download WAV file", wav_file, file_name="converted.wav")

if __name__ == "__main__":
    main()
