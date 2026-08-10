from tts import PiperTTS
from player import AudioPlayer


class Voice:

    def __init__(self):
        self.tts = PiperTTS()
        self.player = AudioPlayer()

    def say(self, text: str):

        audio = self.tts.speak_to_file(text)

        self.player.play(audio)