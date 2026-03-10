import librosa
import numpy as np

def export_clean_beats(track_path="Betos_Horns.mp3", output_file="beats.py", lead=0.08):
    y, sr = librosa.load(track_path)
    y_harmonic, y_percussive = librosa.effects.hpss(y)
    onset_env = librosa.onset.onset_strength(y=y_percussive, sr=sr)
    tempo, beat_frames = librosa.beat.beat_track(onset_envelope=onset_env, sr=sr)
    beat_times = librosa.frames_to_time(beat_frames, sr=sr)
    beat_times = beat_times - lead
    beat_times = np.clip(beat_times, 0, None)

    # Save as a Python list
    with open(output_file, "w") as f:
        f.write("beat_times = [\n")
        for bt in beat_times:
            f.write(f"    {bt:.6f},\n")
        f.write("]\n")

    print(f"Exported {len(beat_times)} beats as a Python list in {output_file}")
    return beat_times

# Example usage
beat_times = export_clean_beats()
print("First 10 beat times:", beat_times[:10])
