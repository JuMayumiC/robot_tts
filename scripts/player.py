import subprocess


def play_audio(audio_file):

    subprocess.run(
        [
            "aplay",
            str(audio_file)
        ],
        check=True,
    )