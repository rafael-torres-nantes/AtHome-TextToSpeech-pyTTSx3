import os
import whisper

def speechToText(audioName='input_audio.wav', directoryName='audio_folder/'):
    """Transcreve um arquivo de áudio para texto usando o Whisper."""

    audioFile = os.path.join(directoryName, audioName)

    if not os.path.isfile(audioFile):
        raise FileNotFoundError(f"'{audioFile}' não encontrado. Grave o áudio antes de transcrever.")
   
    # Models
    # tiny - base - small - medium
    model = whisper.load_model("small")
    
    # transcribe audio
    text = whisper.transcribe(model=model,audio=audioFile)
    print(text['text'])

    return text['text']

