# Digita algo e o programa fala

from tts import TTS


def main():

    tts = TTS()

    while True:

        text = input("\nDigite algo ('sair' para terminar): ")

        if text.lower() == "sair":
            break

        tts.speak(text)


if __name__ == "__main__":
    main()