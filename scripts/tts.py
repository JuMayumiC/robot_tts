
import re
import subprocess
import tempfile
import wave

from pathlib import Path

from config import (
    PIPER,
    MODEL,
    VOICE,
    LENGTH_SCALE,
    NOISE_SCALE,
    NOISE_W,
    SENTENCE_SILENCE,
    PARAGRAPH_SILENCE,
    COMMA_SILENCE,
)


class TTS:

    def __init__(self):
        self.piper = PIPER
        self.model = MODEL

    def _generate_audio(self, text, output_file):

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

    def _merge_segments(self, audio_files, pauses, output_file):

        with wave.open(str(audio_files[0]), "rb") as first:
            params = first.getparams()

        with wave.open(str(output_file), "wb") as output:

            output.setnchannels(params.nchannels)
            output.setsampwidth(params.sampwidth)
            output.setframerate(params.framerate)
            output.setcomptype(params.comptype, params.compname)

            for index, audio_file in enumerate(audio_files):

                with wave.open(str(audio_file), "rb") as audio:

                    audio_params = audio.getparams()

                    if (
                        audio_params.nchannels != params.nchannels
                        or audio_params.sampwidth != params.sampwidth
                        or audio_params.framerate != params.framerate
                        or audio_params.comptype != params.comptype
                        or audio_params.compname != params.compname
                    ):
                        raise ValueError(
                            "Os arquivos de áudio possuem formatos diferentes."
                        )

                    output.writeframes(
                        audio.readframes(audio.getnframes())
                    )

                if index < len(pauses):

                    pause_frames = int(
                        params.framerate * pauses[index]
                    )

                    if params.sampwidth == 1:
                        silence_sample = b"\x80"
                    else:
                        silence_sample = bytes(params.sampwidth)

                    silence = (
                        silence_sample
                        * params.nchannels
                        * pause_frames
                    )

                    output.writeframes(silence)

    def synthesize(self, text, output_file=VOICE):

        paragraphs = [
            paragraph.strip()
            for paragraph in text.strip().split("\n\n")
            if paragraph.strip()
        ]

        if not paragraphs:
            raise ValueError("O texto está vazio.")

        output_file = Path(output_file)
        output_file.parent.mkdir(parents=True, exist_ok=True)

        # Divide os parágrafos nos pontos de vírgula.
        segments = []

        for paragraph_index, paragraph in enumerate(paragraphs):

            chunks = [
                chunk.strip()
                for chunk in re.split(r"(?<=,)", paragraph)
                if chunk.strip()
            ]

            for chunk_index, chunk in enumerate(chunks):

                # Pausa após vírgula ou entre parágrafos.
                if chunk_index < len(chunks) - 1:
                    pause = COMMA_SILENCE

                elif paragraph_index < len(paragraphs) - 1:
                    pause = PARAGRAPH_SILENCE

                else:
                    pause = 0

                segments.append((chunk, pause))

        with tempfile.TemporaryDirectory() as temp_dir:

            audio_files = []
            pauses = []

            for index, (segment, pause) in enumerate(segments):

                audio_file = Path(temp_dir) / f"segment_{index}.wav"

                self._generate_audio(segment, audio_file)

                audio_files.append(audio_file)

                if index < len(segments) - 1:
                    pauses.append(pause)

            # Se houver apenas um trecho, não precisa juntar arquivos.
            if len(audio_files) == 1:
                self._generate_audio(segments[0][0], output_file)
            else:
                self._merge_segments(
                    audio_files,
                    pauses,
                    output_file
                )

        return output_file

    def speak(self, text):

        from player import play_audio

        audio = self.synthesize(text)

        play_audio(audio)
