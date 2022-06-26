import asyncio, librosa, random
import threading
from pywizlight import wizlight, PilotBuilder, discovery
from pydub import AudioSegment
from pydub.playback import play
from concurrent.futures import ProcessPoolExecutor


track = ""
sound = AudioSegment.from_file(track, format="wav")


time_between_beats = []

first_beat = ''

async def lights():
    light_1 = wizlight("")
    light_2 = wizlight("")
    await asyncio.sleep(first_beat)
    await light_1.turn_on(PilotBuilder(rgb = (255, 0, 0)))
    await light_2.turn_on(PilotBuilder(rgb = (255, 0, 0)))
    for time in time_between_beats:
        await light_1.turn_on()
        await light_2.turn_on()
        await light_1.turn_off()
        await light_2.turn_off()
        await asyncio.sleep(time)

t = threading.Thread(target=play, args=(sound,))
t.start()
asyncio.run(lights())



