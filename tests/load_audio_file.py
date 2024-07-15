import sys
sys.path.append("/home/saumya/projects/soundmentations/")

from core.audio_loading import load_audio
import os

# Load audio file
load_audio(os.path.join("/home/saumya/projects/soundmentations/tests/data/"))

