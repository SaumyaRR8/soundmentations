import sys
import pytest
sys.path.append("/home/saumya/projects/soundmentations/")

from soundmentations.core.audio_loading import load_audio
import os

# Load audio file
load_audio(os.path.join("/home/saumya/projects/soundmentations/tests/data/sample.wav"))

