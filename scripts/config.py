from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

PIPER = ROOT / "bin" / "piper" / "piper"
MODEL = ROOT / "models" / "pt_BR-faber-medium.onnx"

OUTPUT = ROOT / "output"
OUTPUT.mkdir(exist_ok=True)

VOICE = OUTPUT / "voice.wav"

# Configurações da voz
LENGTH_SCALE = 1.1
NOISE_SCALE = 0.667
NOISE_W = 1.0
SENTENCE_SILENCE = 0.5
PARAGRAPH_SILENCE = 0.5
COMMA_SILENCE = 0.03