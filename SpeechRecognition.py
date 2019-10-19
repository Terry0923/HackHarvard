import io
import os
from google.cloud import speech
from google.cloud.speech import enums
from google.cloud.speech import types
from pydub import AudioSegment
import librosa

os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="My First Project-854b30065e6e.json"

def speechToText():
    client = speech.SpeechClient()
    dirname = os.path.dirname(__file__)
    sound = AudioSegment.from_mp3(os.path.join(dirname, 'audio/pabloTestAudio.mp3'))
    sound.export(os.path.join(dirname, 'audio/pabloTestAudio.wav'), format="wav")
    file_name = os.path.join(
        os.path.dirname(__file__),
        'audio',
        'pabloTestAudio.wav')
    with io.open(file_name, 'rb') as audio_file:
        content = audio_file.read()
        audio = types.RecognitionAudio(content=content)
    config = types.RecognitionConfig(
        encoding=enums.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=44100,
        language_code='en-US',
        audio_channel_count=2)
    response = client.recognize(config, audio)
    s = ""
    for result in response.results:
        s += '{}'.format(result.alternatives[0].transcript)
    return s
