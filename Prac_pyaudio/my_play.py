import pyaudio
import wave
# pyaudio tutorial: https://realpython.com/playing-and-recording-sound-python/#pyaudio

filename = input("Enter file name: ")
print("Reading", filename)

# filename='output.wav'

# Set chunk size of 1024 samples per data frame
chunk = 1024  

# Open the sound file 
wf = wave.open(filename, 'rb')

# Create an interface to PortAudio
p = pyaudio.PyAudio()

# Open a .Stream object to write the WAV file to
# 'output = True' indicates that the sound will be played rather than recorded
stream = p.open(format = p.get_format_from_width(wf.getsampwidth()),
                channels = wf.getnchannels(),
                rate = wf.getframerate(),
                output = True)

# Read data in chunks
data = wf.readframes(chunk)

print("Press 's' to stop")
stop = ''
# Read until there is no more data to read - https://people.csail.mit.edu/hubert/pyaudio/docs/
while len(data) > 0:
    try:
        stream.write(data)
        data = wf.readframes(chunk)
    except (KeyboardInterrupt):
        print("KeyboardInterrupt")
        break
    

print("Reading complete")
# Close and terminate the stream
stream.stop_stream()
stream.close()
p.terminate()
