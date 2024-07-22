import numpy as np

from soundmentations.augmentations.time_and_pitch.trim import trim

class TestTrim:
    def test_trim(self):
        audio_data = np.random.randn(1000)
        trimmed_audio = trim(audio_data)
        assert trimmed_audio.shape[0] < audio_data.shape[0]
        assert trimmed_audio.shape[0] > 0