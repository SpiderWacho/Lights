import librosa

def export_beats():
    sourceFile = open('beats.txt', 'w')
    track = ""
    y, sr = librosa.load(track)
    tempo, beat_frames = librosa.beat.beat_track(y=y, sr=sr)
    beat_times = librosa.frames_to_time(beat_frames, sr=sr)

    print(beat_times)

    beat_saved = []
    for beat in beat_times:
        beat_saved.append(beat)

    time_between_beats = []
    for index, elem in enumerate(beat_saved):
        if (index+1 < len(beat_saved) and index - 1 >= 0):
            time_between_beats.append(float(beat_saved[index+1]) - float(elem))
    print(str(beat_times[0]) + '\n' + str(time_between_beats), file = sourceFile)
    sourceFile.close()

export_beats()