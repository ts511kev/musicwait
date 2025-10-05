from typing import List, Tuple, Optional, Union
import threading
import time
import sys

import pyaudio as pa
import numpy as np


class Music:

    OH_SUSANNA = [
        ("C0", 8, "I've"),
        ("D0", 8, None),
        ("E0", 6, "come"),
        ("G0", 6, "from"),
        ("G0", 6, "Alabama"),
        ("A0", 6, None),
        ("G0", 6, None),
        ("E0", 6, None),
        ("C0", 5, "with"),
        ("D0", 8, "my"),
        ("E0", 6, "banjo"),
        ("E0", 6, None),
        ("D0", 6, "on"),
        ("C0", 6, "my"),
        ("D0", 3, "knee,"),
        ("C0", 8, "I'm"),
        ("D0", 8, None),
        ("E0", 6, "goin'"),
        ("G0", 6, "to"),
        ("G0", 6, "Louisiana,"),
        ("A0", 6, None),
        ("G0", 6, None),
        ("E0", 6, None),
        ("C0", 5, "My"),
        ("D0", 8, None),
        ("E0", 6, "true"),
        ("E0", 6, "love"),
        ("D0", 6, "for"),
        ("D0", 6, "to"),
        ("C0", 3, "see."),
        ("C0", 8, "It"),
        ("D0", 8, None),
        ("E0", 6, "rain'd"),
        ("G0", 6, "all"),
        ("G0", 6, "night"),
        ("A0", 6, "the"),
        ("G0", 6, "day"),
        ("E0", 6, "I"),
        ("C0", 5, "left,"),
        ("D0", 8, "the"),
        ("E0", 6, "weather"),
        ("E0", 6, None),
        ("D0", 6, "it"),
        ("C0", 6, "was"),
        ("D0", 3, "dry."),
        ("C0", 8, "The"),
        ("D0", 8, None),
        ("E0", 6, "sun"),
        ("G0", 6, "so"),
        ("G0", 6, "hot"),
        ("A0", 6, "I"),
        ("G0", 6, "froze"),
        ("E0", 6, None),
        ("C0", 5, "to"),
        ("D0", 8, "death,"),
        ("E0", 6, "Susanna,"),
        ("E0", 6, None),
        ("D0", 6, "don't"),
        ("D0", 6, "you"),
        ("C0", 4, "cry."),
        ("C#0", 8, None),
        ("D0", 8, None),
        ("D#0", 8, None),
        ("E0", 8, None),
        ("F0", 4, "Oh!"),
        ("F0", 4, "Susanna,"),
        ("A0", 6, None),
        ("A0", 4, None),
        ("A0", 6, "Oh,"),
        ("G0", 5, "don't"),
        ("G0", 8, "you"),
        ("E0", 6, "cry"),
        ("C0", 6, "for"),
        ("D0", 3, "me."),
        ("C0", 8, "I've"),
        ("D0", 8, None),
        ("E0", 6, "come"),
        ("G0", 6, "from"),
        ("G0", 6, "Alabama"),
        ("A0", 6, None),
        ("G0", 6, None),
        ("E0", 6, None),
        ("C0", 5, "with"),
        ("D0", 8, "my"),
        ("E0", 6, "banjo"),
        ("E0", 6, None),
        ("D0", 6, "on"),
        ("D0", 6, "my"),
        ("C0", 3, "knee."),
    ]

    DE_CAMPTOWN_RACES = [
        ("G0", 6, "De camptown"),
        ("G0", 6, None),
        ("E0", 6, "ladies"),
        ("G0", 6, None),
        ("A0", 6, "sing"),
        ("G0", 6, "dis"),
        ("E0", 4, "song,"),
        ("E0", 6, "doo-dah!"),
        ("D0", 3, None),
        ("E0", 6, "doo-dah!"),
        ("D0", 3, None),
        ("G0", 6, "De camptown"),
        ("G0", 6, None),
        ("E0", 6, "racetrack"),
        ("G0", 6, None),
        ("A0", 6, "five"),
        ("G0", 6, "miles"),
        ("E0", 4, "long,"),
        ("D0", 4, "oh!"),
        ("E0", 6, "doo-dah day!"),
        ("D0", 6, None),
        ("C0", 2, None),
        ("G0", 6, "I come"),
        ("G0", 6, "down"),
        ("E0", 6, "dah"),
        ("G0", 6, "wid my"),
        ("A0", 6, "hat"),
        ("G0", 6, "caved"),
        ("E0", 4, "in,"),
        ("E0", 6, "doo-dah!"),
        ("D0", 3, None),
        ("E0", 6, "doo-dah!"),
        ("D0", 3, None),
        ("G0", 6, "I go"),
        ("G0", 6, "back"),
        ("E0", 6, "home"),
        ("G0", 6, "wid a"),
        ("A0", 6, "pocket"),
        ("G0", 6, "full of"),
        ("E0", 4, "tin,"),
        ("D0", 5, "oh!"),
        ("F0", 8, "doo-dah day!"),
        ("E0", 6, None),
        ("D0", 6, None),
        ("C0", 6, None),
        ("E0", 6, None),
        ("C0", 4, None),
        ("C0", 5, "Gwine"),
        ("C0", 8, "to"),
        ("E0", 6, "run"),
        ("G0", 6, "all"),
        ("C1", 2, "night!"),
        ("A0", 5, "Gwine"),
        ("A0", 8, "to"),
        ("C1", 6, "run"),
        ("A0", 6, "all"),
        ("G0", 3, "day!"),
        ("E0", 8, "I'll"),
        ("F0", 8, None),
        ("G0", 6, "bet"),
        ("G0", 6, "my"),
        ("E0", 6, "money"),
        ("G0", 6, "on de"),
        ("A0", 6, "bob-tail"),
        ("G0", 6, None),
        ("E0", 4, "nag,"),
        ("D0", 6, "somebody"),
        ("E0", 8, None),
        ("F0", 8, None),
        ("E0", 6, "bet on"),
        ("D0", 6, "de"),
        ("C0", 2, "bay!"),
    ]

    ANNIE_LAURIE = [
        ("E0", 5, None),
        ("D0", 8, None),
        ("C0", 3, None),
        ("C0", 6, None),
        ("C1", 3, None),
        ("B0", 6, None),
        ("B0", 4, None),
        ("A0", 2, None),
        ("A0", 4, None),
        ("G0", 3, None),
        ("E0", 6, None),
        ("E0", 4, None),
        ("D0", 6, None),
        ("C0", 6, None),
        ("D0", 1, None),
        ("E0", 5, None),
        ("D0", 8, None),
        ("C0", 3, None),
        ("C0", 6, None),
        ("C1", 3, None),
        ("B0", 6, None),
        ("B0", 4, None),
        ("A0", 2, None),
        ("A0", 4, None),
        ("G0", 3, None),
        ("E0", 6, None),
        ("E0", 3, None),
        ("D0", 6, None),
        ("C0", 1, None),
        ("G0", 4, None),
        ("C1", 3, None),
        ("C1", 6, None),
        ("D1", 3, None),
        ("D1", 6, None),
        ("E1", 1, None),
        ("G0", 4, None),
        ("C1", 3, None),
        ("C1", 6, None),
        ("D1", 3, None),
        ("D1", 6, None),
        ("E1", 1, None),
        ("E1", 5, None),
        ("D1", 8, None),
        ("C1", 3, None),
        ("B0", 6, None),
        ("A0", 4, None),
        ("C1", 6, None),
        ("A0", 6, None),
        ("G0", 4, None),
        ("E0", 2, None),
        ("E0", 6, None),
        ("D0", 6, None),
        ("C0", 6, None),
        ("C1", 4, None),
        ("E0", 6, None),
        ("E0", 3, None),
        ("D0", 6, None),
        ("C0", 1, None),
    ]

    THE_ENTERTAINER_INTRO = [
        ("D2", 6, None),
        ("E2", 6, None),
        ("C2", 6, None),
        ("A1", 4, None),
        ("B1", 6, None),
        ("G1", 4, None),
        ("D1", 6, None),
        ("E1", 6, None),
        ("C1", 6, None),
        ("A0", 4, None),
        ("B0", 6, None),
        ("G0", 4, None),
        ("D0", 6, None),
        ("E0", 6, None),
        ("C0", 6, None),
        ("A-1", 4, None),
        ("B-1", 6, None),
        ("A-1", 6, None),
        ("G#-1", 6, None),
        ("G-1", 2, None),
        ("G0", 4, None),
    ]

    THE_ENTERTAINER_A = [
        ("D0", 6, None),
        ("D#0", 6, None),
        ("E0", 6, None),
        ("C1", 4, None),
        ("E0", 6, None),
        ("C1", 4, None),
        ("E0", 6, None),
        ("C1", 1, None),
        ("C1", 6, None),
        ("D1", 6, None),
        ("D#1", 6, None),
        ("E1", 6, None),
        ("C1", 6, None),
        ("D1", 6, None),
        ("E1", 4, None),
        ("B0", 6, None),
        ("D1", 4, None),
        ("C1", 1, None),
        ("D0", 6, None),
        ("D#0", 6, None),
        ("E0", 6, None),
        ("C1", 4, None),
        ("E0", 6, None),
        ("C1", 4, None),
        ("E0", 6, None),
        ("C1", 1, None),
        ("A0", 6, None),
        ("G0", 6, None),
        ("F#0", 6, None),
        ("A0", 6, None),
        ("C1", 6, None),
        ("E1", 4, None),
        ("D1", 6, None),
        ("C1", 6, None),
        ("A0", 6, None),
        ("D1", 1, None),
        ("D0", 6, None),
        ("D#0", 6, None),
        ("E0", 6, None),
        ("C1", 4, None),
        ("E0", 6, None),
        ("C1", 4, None),
        ("E0", 6, None),
        ("C1", 1, None),
        ("C1", 6, None),
        ("D1", 6, None),
        ("D#1", 6, None),
        ("E1", 6, None),
        ("C1", 6, None),
        ("D1", 6, None),
        ("E1", 4, None),
        ("B0", 6, None),
        ("D1", 4, None),
        ("C1", 1, None),
        ("C1", 6, None),
        ("D1", 6, None),
        ("E1", 6, None),
        ("C1", 6, None),
        ("D1", 6, None),
        ("E1", 4, None),
        ("C1", 6, None),
        ("D1", 6, None),
        ("C1", 6, None),
        ("E1", 6, None),
        ("C1", 6, None),
        ("D1", 6, None),
        ("E1", 4, None),
        ("C1", 6, None),
        ("D1", 6, None),
        ("C1", 6, None),
        ("E1", 6, None),
        ("C1", 6, None),
        ("D1", 6, None),
        ("E1", 4, None),
        ("B0", 6, None),
        ("D1", 4, None),
        ("C1", 1, None),
    ]

    THE_ENTERTAINER_B = [
        ("E1", 6, None),
        ("F1", 6, None),
        ("F#1", 6, None),
        ("G1", 4, None),
        ("A1", 6, None),
        ("G1", 4, None),
        ("E1", 6, None),
        ("F1", 6, None),
        ("F#1", 6, None),
        ("G1", 4, None),
        ("A1", 6, None),
        ("G1", 4, None),
        ("E1", 6, None),
        ("C1", 6, None),
        ("G0", 6, None),
        ("A0", 6, None),
        ("B0", 6, None),
        ("C1", 6, None),
        ("D1", 6, None),
        ("E1", 6, None),
        ("D1", 6, None),
        ("C1", 6, None),
        ("D1", 6, None),
        ("G0", 6, None),
        ("E1", 6, None),
        ("F1", 6, None),
        ("G1", 6, None),
        ("A1", 6, None),
        ("G1", 6, None),
        ("E1", 6, None),
        ("F1", 6, None),
        ("G1", 4, None),
        ("A1", 6, None),
        ("G1", 4, None),
        ("E1", 6, None),
        ("F1", 6, None),
        ("F#1", 6, None),
        ("G1", 4, None),
        ("A1", 6, None),
        ("G1", 4, None),
        ("G1", 6, None),
        ("A1", 6, None),
        ("A#1", 6, None),
        ("B1", 6, None),
        ("B1", 5, None),
        ("r", 6, None),
        ("B1", 4, None),
        ("A1", 6, None),
        ("F#1", 6, None),
        ("D1", 6, None),
        ("G1", 2, None),
        ("r", 6, None),
        ("E1", 6, None),
        ("F1", 6, None),
        ("F#1", 6, None),
        ("G1", 4, None),
        ("A1", 6, None),
        ("G1", 4, None),
        ("E1", 6, None),
        ("F1", 6, None),
        ("F#1", 6, None),
        ("G1", 4, None),
        ("A1", 6, None),
        ("G1", 4, None),
        ("E1", 6, None),
        ("C1", 6, None),
        ("G0", 6, None),
        ("A0", 6, None),
        ("B0", 6, None),
        ("C1", 6, None),
        ("D1", 6, None),
        ("E1", 6, None),
        ("D1", 6, None),
        ("C1", 6, None),
        ("D1", 6, None),
        ("C1", 2, None),
        ("r", 6, None),
        ("G0", 6, None),
        ("F#0", 6, None),
        ("G0", 6, None),
        ("C1", 4, None),
        ("A0", 6, None),
        ("C1", 4, None),
        ("A0", 6, None),
        ("C1", 6, None),
        ("A0", 6, None),
        ("G0", 6, None),
        ("C1", 6, None),
        ("E1", 6, None),
        ("G1", 4, None),
        ("E1", 6, None),
        ("C1", 6, None),
        ("G0", 6, None),
        ("A0", 4, None),
        ("C1", 4, None),
        ("E1", 6, None),
        ("D1", 4, None),
    ]

    THE_ENTERTAINER = (
        []
        # + _ENTERTAINER_PRE
        + THE_ENTERTAINER_A * 2
        + THE_ENTERTAINER_B
        + [
            ("C1", 3, None),
        ]
        + THE_ENTERTAINER_B
        + [
            ("C1", 4, None),
            ("C2", 4, None),
        ]
    )

    RING_RING_DE_BANJO = [
        ("C1", 6, "De"),
        ("C1", 6, "time"),
        ("A0", 6, "is"),
        ("F0", 5, "nebber"),
        ("G0", 8, None),
        (
            "A0",
            6,
            "dreary,",
        ),
        ("C1", 4, None),
        ("C1", 6, "If"),
        ("D1", 6, "de"),
        ("C1", 6, "darkey"),
        ("A0", 5, "nebber"),
        ("F0", 8, None),
        ("G0", 3, "groans,"),
        ("G0", 6, "De"),
        ("F0", 6, "ladies"),
        ("G0", 6, None),
        ("A0", 6, "nebber"),
        ("A#0", 6, None),
        ("C1", 6, "weary,"),
        ("F1", 4, None),
        ("D1", 6, "Wid"),
        ("C1", 6, "de"),
        ("A0", 6, "rattle"),
        ("G0", 5, "ob"),
        ("G0", 8, "de"),
        ("F0", 3, "hones"),
        ("C1", 6, "Den"),
        ("C1", 6, "dome"),
        ("A0", 6, "again"),
        ("F0", 5, None),
        ("G0", 8, "Susanna,"),
        ("A0", 6, None),
        ("C1", 4, None),
        ("C1", 8, "By"),
        ("C1", 8, "de"),
        ("D1", 6, "gaslights"),
        ("C1", 6, None),
        ("A0", 5, "ob"),
        ("F0", 8, "de"),
        ("G0", 3, "moon,"),
        ("G0", 6, "We'll"),
        ("F0", 5, "tum"),
        ("G0", 8, "de"),
        ("A0", 6, "old"),
        ("A#0", 6, "Piano"),
        ("C1", 6, None),
        ("F1", 4, "When"),
        ("D1", 6, "de"),
        ("C1", 6, "banjo's"),
        ("A0", 6, None),
        ("G0", 5, "out"),
        ("G0", 8, "ob"),
        ("F0", 2, "tune."),
        ("C1", 4, "Ring,"),
        ("C1", 5, "ring"),
        ("C1", 8, "de"),
        ("A0", 6, "banjo!"),
        ("C1", 4, None),
        ("C1", 6, "I"),
        ("D1", 6, "like"),
        ("C1", 6, "dat"),
        ("A0", 6, "good"),
        ("F0", 6, "old"),
        ("G0", 2, "song,"),
        ("F0", 5, "Come"),
        ("G0", 8, "again"),
        ("A0", 6, None),
        ("A#0", 6, "my"),
        ("C1", 6, "true"),
        ("F1", 4, "lub,"),
        ("D1", 6, "Oh!"),
        ("C1", 5, "wha"),
        ("A0", 8, "you"),
        ("G0", 5, "been"),
        ("G0", 8, "so"),
        ("F0", 3, "long."),
    ]

    TIPPERARY = [
        ("A#0", 6, "Up"),
        ("D1", 6, "to"),
        ("C1", 6, "mighty"),
        ("A#0", 6, None),
        ("G0", 6, "London"),
        ("F0", 6, None),
        ("D0", 6, "came"),
        ("D#0", 6, "an"),
        ("F0", 6, "Irish"),
        ("G0", 6, None),
        ("F0", 6, "man"),
        ("D0", 6, "one"),
        ("F0", 2, "day,"),
        ("A#0", 6, "As"),
        ("D1", 6, "the"),
        ("C1", 6, "street"),
        ("A#0", 6, "are"),
        ("G0", 6, "paved"),
        ("F0", 6, "with"),
        ("D0", 6, "gold,"),
        ("D#0", 6, "sure"),
        ("A0", 6, "everyone"),
        ("A#0", 6, None),
        ("A0", 6, None),
        ("E0", 6, "was"),
        ("A0", 2, "gay."),
        ("A#0", 6, "Singing"),
        ("D1", 6, None),
        ("C1", 6, "songs"),
        ("A#0", 6, "of"),
        ("G0", 6, "Piccadilly,"),
        ("F0", 6, None),
        ("D0", 6, None),
        ("D#0", 6, None),
        ("A0", 6, "Strand"),
        ("A#0", 6, "and"),
        ("A0", 6, "Leicester"),
        ("E0", 6, None),
        ("A0", 3, "Square,"),
        ("C1", 6, "Till"),
        ("D1", 6, "Paddy"),
        ("C1", 6, None),
        ("A#0", 6, "got"),
        ("A0", 6, "excited,"),
        ("C1", 6, None),
        ("A#0", 6, None),
        ("C1", 6, "then"),
        ("D1", 6, "he"),
        ("A0", 6, "shouted"),
        ("G0", 6, None),
        ("A0", 6, "to"),
        ("A#0", 6, "them"),
        ("C1", 4, "their:"),
        ("D0", 6, '''"It's'''),
        ("D#0", 6, "a"),
        ("F0", 4, "long"),
        ("F0", 3, "way"),
        ("F0", 6, "to"),
        ("G0", 6, "Tipperary,"),
        ("A0", 6, None),
        ("A#0", 4, None),
        ("D1", 2, None),
        ("D1", 6, "It's"),
        ("C1", 6, "a"),
        ("A#0", 4, "long"),
        ("G0", 2, "way"),
        ("A#0", 4, "to"),
        ("F0", 1, "go;"),
        ("D0", 6, "It's"),
        ("D#0", 6, "a"),
        ("F0", 4, "long"),
        ("F0", 3, "way"),
        ("F0", 6, "to"),
        ("G0", 6, "Tipperary,"),
        ("A0", 6, None),
        ("A#0", 4, None),
        ("D1", 2, None),
        ("A#0", 6, "To"),
        ("B0", 6, "the"),
        ("C1", 4, "sweetest"),
        ("G0", 4, None),
        ("A0", 4, "girl"),
        ("A#0", 4, "I"),
        ("C1", 0, "know!"),
        ("F0", 4, "Goodbye"),
        ("F0", 2, None),
        ("G0", 6, "Piccadilly,"),
        ("A0", 6, None),
        ("A#0", 4, None),
        ("D1", 1, None),
        ("D#1", 4, "Farewell"),
        ("G0", 4, None),
        ("A#0", 4, "Leicester"),
        ("C1", 4, None),
        ("D1", 1, "Square,"),
        ("A#0", 6, "It's"),
        ("C1", 6, "a"),
        ("D1", 4, "long,"),
        ("D1", 4, "long"),
        ("D1", 6, "way"),
        ("A#0", 6, "to"),
        ("C1", 6, "Tipperary,"),
        ("A#0", 6, None),
        ("G0", 2, None),
        ("F0", 4, None),
        ("A#0", 4, "But"),
        ("D1", 4, "my"),
        ("A#0", 2, "heart's"),
        ("C1", 4, "right"),
        ("A#0", 0, 'there!"'),
    ]


class MusicWait:

    def __init__(
        self,
        music: Union[
            List[Tuple[str, int, Optional[str]]], List[Tuple[str, int, None]]
        ] = Music.OH_SUSANNA,
        bpm: int = 8,
        lyrics: bool = False,
    ):

        try:
            self._play = False
            self._lyrics = lyrics
            self._music = music
            self._audio = MusicWait.Audio(bpm=bpm)
            self._scales = self._audio.make_scale()
            self._notes = self._audio.make_note()

            self._thread: Optional[threading.Thread] = None
        except:
            print("Failed to start MusicWait...")

    def __enter__(self):
        try:
            self.play()
        except:
            print("Failed to enter MusicWait...")
        finally:
            return self

    def __exit__(self, ex_type, ex_value, trace):
        try:
            self.stop()
        except:
            print("Failed to exit MusicWait...")

    def play(self):
        try:
            self._play = True
            self._thread = threading.Thread(target=self.loop_music)

            self._thread.start()
        except:
            print("Failed to play music...")

    def stop(self):
        try:
            self._play = False
            if self._thread is not None:
                self._thread.join()
                self._thread = None

            if self._lyrics:
                print("")
        except:
            print("Failed to stop music...")

    class Audio:

        def __init__(self, bpm=30):
            self.audio = pa.PyAudio()
            self.a_hz = 440 * 2 ** (5 / 12)
            self.smpl_rate = 44100
            self.bpm = bpm
            self.code_names = (
                "C",
                "C#",
                "D",
                "D#",
                "E",
                "F",
                "F#",
                "G",
                "G#",
                "A",
                "A#",
                "B",
            )
            self.stream = self.audio.open(
                format=pa.paFloat32,
                channels=1,
                rate=self.smpl_rate,
                frames_per_buffer=1024,
                output=True,
            )

        def __tone(self, hz, note, gain=1.0):
            slen = int(note * self.smpl_rate)
            t = float(hz) * np.pi * 2 / self.smpl_rate
            return np.sin(np.arange(slen) * t) * gain

        # 音符
        def make_note(self):
            self.note1 = 60 / (self.bpm * 4)
            notes = []
            notes.append(self.note1)
            notes.append(self.note1 / 2 * 1.5)
            notes.append(self.note1 / 2)
            notes.append(self.note1 / 4 * 1.5)
            notes.append(self.note1 / 4)
            notes.append(self.note1 / 8 * 1.5)
            notes.append(self.note1 / 8)
            notes.append(self.note1 / 16 * 1.5)
            notes.append(self.note1 / 16)
            notes.append(self.note1 / 32 * 1.5)
            notes.append(self.note1 / 32)
            return notes

        # 音階
        def make_scale(self):
            res = {"r": None}
            octave = -2
            for n in range(0, 48):
                hz = self.a_hz * 2 ** ((n - 9) / 12 - 1)
                if (n % 12) == 0:
                    octave += 1
                name = self.code_names[n % 12] + str(octave)
                res[name] = hz
            return res

        def play(self, hz, note, text: Optional[str] = None, gain=1.0):
            if text is not None:
                print(text, end=" ")
                sys.stdout.flush()

            if hz is None:
                time.sleep(note)
                return
            note2 = note * 0.9
            self.stream.write(self.__tone(hz, note2, gain).astype(np.float32).tobytes())
            time.sleep(note * 0.1)

    def loop_music(self):

        try:
            while self._play:
                for hz, note, text in self._music:
                    if not self._play:
                        return
                    self._audio.play(
                        self._scales[hz],
                        self._notes[note],
                        text if self._lyrics else None,
                    )
        except:
            print("Failed to loop music...")
            return
