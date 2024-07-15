from pydub import AudioSegment

def trim_audio(input_file, output_file, start_time, end_time):
    audio = AudioSegment.from_file(input_file)
    trimmed_audio = audio[start_time:end_time]
    trimmed_audio.export(output_file, format="wav")

# Example usage
input_file = "/path/to/input/audio.wav"
output_file = "/path/to/output/trimmed_audio.wav"
start_time = 5000  # Start time in milliseconds
end_time = 10000  # End time in milliseconds

trim_audio(input_file, output_file, start_time, end_time)