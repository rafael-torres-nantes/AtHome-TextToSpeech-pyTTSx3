"""Pipeline de ponta a ponta: grava do microfone, transcreve com Whisper e responde por voz."""

from src.speech_recognition_whisper import speechToText
from src.convert_textToVoice import textToSpeech
from src.utils_microphone import record_audio

if __name__ == '__main__':
    record_audio(saveAudioOn=True)
    text = speechToText()
    textToSpeech(text, audioReproduceOn=True)