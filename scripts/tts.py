
import subprocess

from config import (
    PIPER,
    MODEL,
    VOICE,
    LENGTH_SCALE,
    NOISE_SCALE,
    NOISE_W,
    SENTENCE_SILENCE,
)


class TTS:

    def __init__(self):

        self.piper = PIPER
        self.model = MODEL

    def synthesize(self, text, output_file=VOICE):

        command = [
            str(self.piper),
            "--model", str(self.model),
            "--output_file", str(output_file),

            "--length_scale", str(LENGTH_SCALE),
            "--noise_scale", str(NOISE_SCALE),
            "--noise_w", str(NOISE_W),
            "--sentence_silence", str(SENTENCE_SILENCE),
        ]

        subprocess.run(
            command,
            input=text.encode("utf-8"),
            check=True,
        )

        return output_file

    def speak(self, text):

        from player import play_audio

        audio = self.synthesize(text)

        play_audio(audio)
