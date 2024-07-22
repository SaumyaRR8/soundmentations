import librosa

def load_audio(file_path):
    """
    Load audio file from the given file path.

    Args:
        file_path (str): Path to the audio file.

    Returns:
        numpy.ndarray: Loaded audio data.
    """
    audio_data, sample_rate = librosa.load(file_path, sr=None)
    print(audio_data.shape, sample_rate)
    #return audio_data
