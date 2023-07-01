import azure.cognitiveservices.speech as speechsdk
import moviepy.editor as mp

def extractAudioFromVideo(videoPath, audioPath):
    my_clip = mp.VideoFileClip(videoPath)
    my_clip.audio.write_audiofile(audioPath)

def convertingAudioToText(audioPath):
    speech_config = speechsdk.SpeechConfig(subscription="", region="")
    speech_config.speech_recognition_language="en-US"

    audio_config = speechsdk.audio.AudioConfig(filename=audioPath)
    speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_config)
    toStop = False
    result = speech_recognizer.recognize_once()
    text = ''
    print("Transcribing the Audio:")
    while not toStop:
        if result.reason == speechsdk.ResultReason.Canceled:
            toStop = True
            break
        result = speech_recognizer.recognize_once()
        print(result.text)
        text += result.text
    return text


videoPath = ""
audioPath = ""
extractAudioFromVideo(videoPath=videoPath, audioPath=audioPath)
Captions = convertingAudioToText(audioPath=audioPath)



