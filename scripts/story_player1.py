
from tts import TTS
from player import AudioPlayer

from config import OUTPUT


STORY = """
Era uma vez, em uma floresta muito distante, uma pequena raposa chamada Luna.

Todas as noites, ela observava as estrelas e imaginava o que existia além das montanhas.

Certa noite, enquanto caminhava pela floresta, Luna encontrou uma pequena luz brilhando entre as árvores. Curiosa, aproximou-se devagar, e descobriu uma estrelinha que havia caído do céu.

A estrelinha estava triste, pois não sabia como voltar para casa. Então Luna decidiu ajudá-la, mesmo sem saber como faria isso.

Primeiro, a raposinha procurou alguém que pudesse conhecer os caminhos até o céu. Depois de caminhar por algum tempo, encontrou uma velha coruja, que vivia no alto de uma árvore.

A coruja explicou que existia uma montanha muito alta ao norte da floresta. De seu topo, era possível enxergar o céu bem de perto. Talvez, aquele fosse o melhor lugar para a estrelinha conseguir voltar para casa.

Na manhã seguinte, Luna e sua nova amiga começaram a jornada. Juntas, atravessaram pequenos riachos, passaram por árvores enormes, e caminharam por trilhas cercadas de flores.

Durante o caminho, encontraram outros animais da floresta que ficaram encantados com o brilho da pequena estrela. Alguns até acompanharam as duas por um trecho da viagem.

Depois de uma longa caminhada, finalmente chegaram ao pé da montanha. O caminho até o topo era íngreme e cheio de pedras, mas Luna não desistiu.

A subida foi difícil. Em alguns momentos, o vento soprava tão forte que a estrelinha quase perdia o equilíbrio. Mesmo assim, Luna permaneceu ao seu lado, oferecendo ajuda sempre que necessário.

Quando finalmente alcançaram o topo, encontraram um céu escuro e repleto de estrelas. A pequena visitante começou a brilhar cada vez mais intensamente, como se estivesse reconhecendo o caminho de volta.

Uma luz dourada envolveu seu pequeno corpo, e lentamente, ela começou a flutuar em direção ao céu.

Antes de se juntar às outras estrelas, a pequena estrelinha, piscou três vezes como uma forma de agradecer à sua amiga.

Luna acompanhou sua subida, até que ela se tornasse apenas um pequeno ponto brilhante no céu.

Naquela noite, a raposinha percebeu que a floresta parecia ainda mais bonita. A aventura havia sido cansativa, mas também tinha ensinado algo muito especial sobre amizade, coragem, e generosidade.

Desde então, todas as noites, Luna continuou observando as estrelas. E sempre que encontrava um pequeno brilho diferente no céu, lembrava-se com carinho da estrelinha que um dia havia ajudado a encontrar o caminho de casa.

Fim.
"""


def main():

    tts = TTS()
    player = AudioPlayer()

    audio_file = OUTPUT / "historia_luna.wav"

    print("\nPreparando a história da Luna...")

    tts.synthesize(STORY, audio_file)

    print("Áudio preparado!\n")

    print("Comandos disponíveis:")
    print("start  - Iniciar reprodução")
    print("pause  - Pausar reprodução")
    print("resume - Continuar reprodução")
    print("stop   - Interromper reprodução")
    print("sair   - Encerrar programa")

    while True:

        command = input("\nComando: ").strip().lower()

        if command == "start":
            player.start(audio_file)

        elif command == "pause":
            player.pause()

        elif command == "resume":
            player.resume()

        elif command == "stop":
            player.stop()

        elif command == "sair":
            player.stop()
            print("Encerrando programa...")
            break

        else:
            print("Comando não reconhecido.")


if __name__ == "__main__":
    main()
