from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

PIPER = ROOT / "bin" / "piper" / "piper"
MODEL = ROOT / "models" / "pt_BR-faber-medium.onnx"

OUTPUT = ROOT / "output"
OUTPUT.mkdir(exist_ok=True)

VOICE = OUTPUT / "voice.wav"