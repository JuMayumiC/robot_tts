
import subprocess
import signal


def play_audio(audio_file):
    subprocess.run(
        ["aplay", str(audio_file)],
        check=True,
    )


class AudioPlayer:

    def __init__(self):
        self.process = None
        self.paused = False

    def start(self, audio_file):

        if self.process is not None and self.process.poll() is None:

            if self.paused:
                print("O áudio está pausado. Use 'resume' para continuar.")
            else:
                print("O áudio já está sendo reproduzido.")

            return

        self.process = subprocess.Popen(
            ["aplay", str(audio_file)]
        )

        self.paused = False

        print("Reprodução iniciada!")

    def pause(self):

        if self.process is None or self.process.poll() is not None:
            print("Não existe áudio em reprodução.")
            return

        if self.paused:
            print("O áudio já está pausado.")
            return

        self.process.send_signal(signal.SIGSTOP)
        self.paused = True

        print("Reprodução pausada!")

    def resume(self):

        if self.process is None or self.process.poll() is not None:
            print("Não existe áudio para continuar.")
            return

        if not self.paused:
            print("O áudio não está pausado.")
            return

        self.process.send_signal(signal.SIGCONT)
        self.paused = False

        print("Reprodução retomada!")

    def stop(self):

        if self.process is None or self.process.poll() is not None:
            print("Não existe áudio em reprodução.")
            return

        if self.paused:
            self.process.send_signal(signal.SIGCONT)

        self.process.terminate()

        try:
            self.process.wait(timeout=2)
        except subprocess.TimeoutExpired:
            self.process.kill()
            self.process.wait()

        self.paused = False

        print("Reprodução interrompida!")
