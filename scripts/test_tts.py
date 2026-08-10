from tts import TTS


def main():

    tts = TTS()

    while True:

        text = input("\nDigite um texto ('sair' para encerrar): ")

        if text.lower() == "sair":
            break

        tts.speak(text)


if __name__ == "__main__":
    main()