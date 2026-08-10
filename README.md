# Robot TTS

Módulo de síntese de voz offline para o projeto de um robô contador de histórias.

Atualmente o projeto utiliza o **Piper TTS** com a voz **pt_BR-faber-medium**, permitindo gerar e reproduzir fala em português brasileiro sem necessidade de conexão com a internet.

---

## Objetivo

Este módulo será responsável por toda a geração de voz do robô.

Nesta primeira versão o objetivo é apenas:

- sintetizar texto em fala;
- reproduzir o áudio gerado;
- servir como base para futura integração com a face animada do robô.

No futuro este módulo será integrado ao sistema responsável pelas expressões faciais, permitindo sincronizar os visemas (movimentos da boca) com a fala.

---

## Estrutura do projeto

```
robot_tts/
│
├── bin/
│   └── piper/
│       ├── piper
│       ├── bibliotecas do Piper
│       └── dependências
│
├── models/
│   ├── pt_BR-faber-medium.onnx
│   └── pt_BR-faber-medium.onnx.json
│
├── output/
│   └── voice.wav
│
└── scripts/
    ├── config.py
    ├── player.py
    ├── tts.py
    ├── demo_tts.py
    └── test_tts.py
```

---

## Descrição dos arquivos

### config.py

Centraliza todos os caminhos utilizados pelo projeto.

Define:

- diretório raiz;
- executável do Piper;
- modelo de voz;
- pasta de saída;
- arquivo WAV gerado.

---

### tts.py

Classe responsável pela síntese de voz.

Funções:

- receber um texto;
- chamar o Piper;
- gerar um arquivo `.wav`;
- reproduzir o áudio utilizando o player.

---

### player.py

Responsável apenas pela reprodução do áudio.

Atualmente utiliza:

```
aplay
```

para reproduzir arquivos WAV no Linux.

---

### demo_tts.py

Programa demonstrativo.

Permite digitar frases diretamente no terminal para serem sintetizadas.

Exemplo:

```
Digite algo:

Olá! Eu sou um robô contador de histórias.
```

---

### test_tts.py

Arquivo destinado aos testes rápidos durante o desenvolvimento.

Pode ser utilizado para validar novas funcionalidades sem alterar a demonstração principal.

---

## Funcionamento

Fluxo atual do sistema:

```
Texto digitado
        │
        ▼
     TTS.py
        │
        ▼
     Piper TTS
        │
        ▼
   voice.wav
        │
        ▼
   player.py
        │
        ▼
 reprodução do áudio
```

---

## Dependências

- Linux
- Python 3
- Piper TTS
- modelo `pt_BR-faber-medium`
- `aplay`

---

## Executando

Entre na pasta:

```bash
cd robot_tts/scripts
```

Execute:

```bash
python3 demo_tts.py
```

Digite uma frase:

```
Olá!
```

Para encerrar:

```
sair
```

---

## Voz utilizada

Modelo:

```
pt_BR-faber-medium
```

Características:

- Português Brasileiro
- Offline
- Boa inteligibilidade
- Baixo consumo computacional
- Adequado para Raspberry Pi

---

## Próximas etapas

As próximas versões do projeto deverão incluir:

- sincronização da boca com a fala;
- geração de visemas;
- controle de emoções da voz;
- integração com a face animada;
- integração com ROS2;
- sistema de filas para múltiplas falas.

---

## Status

✔ Piper funcionando

✔ Síntese offline

✔ Reprodução de áudio

✔ Demonstração interativa

⬜ Sincronização labial

⬜ Integração com a face

⬜ Integração com ROS2
