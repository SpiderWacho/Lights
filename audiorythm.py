import asyncio
from pywizlight import wizlight, PilotBuilder
import numpy as np
from pydub import AudioSegment
import sounddevice as sd
from dotenv import load_dotenv
import time
import os
from beats import beat_times

# Configuración
LEAD = 0.08  # adelanto para compensar latencia de luces (en segundos)
BLINK_DURATION = 0.05  # duración del parpadeo`

load_dotenv() 

light_1 = os.getenv('FIRST_LIGHT')
light_2 = os.getenv('SECOND_LIGHT')

# Cargar audio
audio = AudioSegment.from_file("audio_sample.mp3")
samples = np.array(audio.get_array_of_samples())
if audio.channels > 1:
    samples = samples.reshape((-1, audio.channels))

# Beat times absolutos (segundos)
beat_times = [b - LEAD for b in beat_times]  # compensar latencia de luces

async def lights(light_1, light_2, beat_times):
    start_time = time.time()
    for beat in beat_times:
        # Esperar hasta el beat
        while (time.time() - start_time) < beat:
            await asyncio.sleep(0.001)  # spin-wait con sleep muy corto
        # Parpadeo
        await light_1.turn_on(PilotBuilder(rgb=(255, 0, 0)))
        await light_2.turn_on(PilotBuilder(rgb=(255, 0, 0)))
        await asyncio.sleep(BLINK_DURATION)
        await light_1.turn_off()
        await light_2.turn_off()

async def main():
    light_1 = wizlight(light_1)
    light_2 = wizlight(light_2)

    # Iniciar audio
    sd.play(samples, samplerate=audio.frame_rate)
    
    # Iniciar luces
    await lights(light_1, light_2, beat_times)
    
    sd.wait()

asyncio.run(main())
