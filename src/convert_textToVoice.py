import pyttsx3

def textToSpeech(textFile, audioSaveOn=False, audioName='output_audio.wav', audioReproduceOn=False, volume=0.5):
    """Converte texto em fala, com opção de salvar em arquivo e/ou reproduzir na hora."""

    # Object creation
    reproducerText = pyttsx3.init()
    current_volume = getVolume(reproducerText)

    directory = 'audio_folder/'
    file_path = directory + audioName

    if volume != current_volume:
        volumeChange(reproducerText, volume)

    if audioSaveOn == True:
        saveAudio(reproducerText, textFile, file_path)

    if audioReproduceOn == True:
        reproduceAudio(reproducerText, textFile)

def reproduceAudio(reproducerText, textFile):
    reproducerText.say(textFile)
    reproducerText.runAndWait()

def saveAudio(reproducerText, textFile, file_path):
    reproducerText.save_to_file(textFile, file_path)
    reproducerText.runAndWait()

def getVolume(reproducerText):
    # Retorna o volume atual
    return reproducerText.getProperty('volume')

def volumeChange(reproducerText, volume):
    # min = 0 and max = 1.0
    reproducerText.setProperty('volume', volume)
    print(f'O volume passou a ser: [{volume * 100}%]')
    return reproducerText