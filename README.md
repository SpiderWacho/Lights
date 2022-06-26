# Lights
A project to make the Wiz Lights turn off and on in sync with a music file. Using librosa and pydub

Ussage:
*First, download a file in .wav, then pass the route to the file to the exportBeatTimes.py file.
*Then it will create a txt file with the first beat time and the time between beats, copy that to the audiorythm.py file in the empty variables 
(This is for perfomance, the librosa librarie perfom an analysis of the song and i decide to output the data to a 
file to copy that and skip the analysis in succesive runs of the program)


