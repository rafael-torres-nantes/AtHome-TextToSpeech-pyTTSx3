# 🔊 AraraBots@AtHome-SpeechRecognition

Pipeline de voz do robô da equipe AraraBots (RoboCup @Home): grava áudio do microfone, transcreve com Whisper e responde por síntese de fala com `pyttsx3`.

## 📂 Estrutura do repositório

- `control_program.py` — ponto de entrada: grava, transcreve e fala, em sequência.
- `src/utils_microphone.py` — gravação/reprodução/limpeza de áudio (`sounddevice`, `soundfile`, `scipy`).
- `src/speech_recognition_whisper.py` — transcrição de fala para texto via Whisper.
- `src/convert_textToVoice.py` — síntese de texto para fala via `pyttsx3`, com opção de salvar em WAV e/ou reproduzir na hora.
- `audio_folder/` — áudios de entrada/saída (gitignorado, exceto `placeholder.txt`).
- `env/` — scripts de instalação por dependência (`install_tts.sh`, `install_whisper.sh`, `install_sounddevice.sh`), pensados para Debian/Ubuntu.

## 🚀 Configuração

```bash
git clone https://github.com/rafael-torres-nantes/AtHome-TextToSpeech-pyTTSx3.git
cd AtHome-TextToSpeech-pyTTSx3
pip install -r requirements.txt
```

Em Linux, `pyttsx3` depende do `espeak` no sistema (`sudo apt install espeak`) — ver `env/install_tts.sh`. No Windows, `pyttsx3` usa o SAPI5 nativo, sem dependência extra.

## 🛠️ Uso

```bash
python control_program.py
```

Isso grava 10s do microfone padrão, transcreve com o modelo Whisper `small` e fala a transcrição de volta.

## 🛠️ Problemas conhecidos

- `pyttsx3` depende de driver de áudio do sistema operacional — comportamento pode variar entre Windows/Linux/Mac.
- O modelo Whisper `small` (~500 MB) é baixado na primeira execução.
