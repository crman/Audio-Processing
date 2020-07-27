#Importing required libraries
import numpy as np
from pydub import AudioSegment
from pydub.playback import play
import matplotlib.pyplot as plt
from scipy.io import wavfile
from scipy.io.wavfile import write
import speech_recognition as sr
import glob

#Importing and exporting audio
def Audio_Import(path):
    #Importing and Exporting Audio File
    TestAudio = AudioSegment.from_mp3(path)
    play(TestAudio) 


#Plotting the audio file in time series and frequency domain
def Audio_Plotting(path):
    sampleFreq, signalData = wavfile.read(path)

    plt.subplot(211)
    plt.plot(signalData)
    plt.xlabel('Sample Index')
    plt.ylabel('Amplitude')
    plt.title('Graph of Wav File')

    plt.subplot(212)
    plt.specgram(signalData, Fs=sampleFreq)
    plt.xlabel('Amplitude')
    plt.ylabel('Frequncy')
    plt.title('Time Series Plot')
    plt.show()


#Different operations on audio file
def Audio_Operations(path):
    #Different operations on audio file

    #Importing and Exporting Audio File
    TestAudio = AudioSegment.from_mp3(path)

    #Slicing the audio
    F10 = TestAudio[:10000]
    L5 = TestAudio[-5000:]

    #boost volume by 6dB
    Beginning = F10 + 6
    #reduce volume by 3dB
    End = L5 - 3

    #Concatenation of audio
    FinalFE = Beginning + End

    #Saving the output
    FinalFE.export(r'D:/FinalFE.mp3', format="mp3")

    #Crossfade the audio
    WithStyle = Beginning.append(End, crossfade=1500)

    #Saving the output
    WithStyle.export(r'D:/Mashup.mp3', format="mp3")


#Generating synthetic audio from random numpy array
def Synthetic_Audio(path):
    data = np.random.uniform(-1, 1, 44100)

    scaled = np.int16(data/np.max(np.abs(data)) * 32767)
    write(path, 44100, scaled)


#Crossfading 10 songs in one audio file
def Audio_10_Import(path):
    #importing 10 Songs
    allSongs = glob.glob(path)
    Songs10 = []    

    #Storing 10 songs in a list
    for i in allSongs:
        Songs10.append(AudioSegment.from_mp3(i))

    #Song Number 1
    Song1 = Songs10.pop(0)
    StartingSong1 = Song1[:30000]   #Extracting Starting of Song 1

    #Final CrossFaded Song
    finalSong = StartingSong1

    #Making Final CrossFaded Song
    for song in Songs10:
        finalSong = finalSong.append(song, crossfade=10000)

    finalSong = finalSong.fade_out(30)

    #Exporting Final Song
    finalSong.export(r'D:/10CrossFaded.mp3', format="mp3")
    print("Final Crossfaded Song Exported!!!")


#performing speech to text
def Speech_To_Text(path):
    #intializing recognizer
    recognizer = sr.Recognizer()

    #Importing audio file and storing it into variable
    with sr.AudioFile(path) as source:
        #Extracting text from audio
        AudioText = recognizer.listen(source)
        print('Converting to Text...')
        try:
            text = recognizer.recognize_google(AudioText)
            print(text)
        except:
            print("Error!!!")


#Importing and exporting audio
Audio_Import(r'D:/DanceMonkey.mp3')

#Plotting the audio file in time series and frequency domain
Audio_Plotting(r'D:/CowMoo.wav')

#Different operations on audio file
Audio_Operations(r'D:/DanceMonkey.mp3')

#Generating synthetic audio
Synthetic_Audio(r'D:/SyntheticAudio.wav')

#Crossfading 10 songs in one audio file
Audio_10_Import(r'D:/10Songs/*.mp3')

#performing speech to text
Speech_To_Text(r'D:/AudioForSTT.wav')
