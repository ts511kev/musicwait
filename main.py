from musicwait import Music, MusicWait

from tqdm import tqdm
import time

with MusicWait(music=Music.CAMPTOWN_RACES, lyrics=False):
    for _ in tqdm(range(100)):
        time.sleep(0.2)

print("Done!")
