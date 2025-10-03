from typing import List, Tuple, Optional
import threading

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

    CAMPTOWN_RACES = [
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
        ("G0", 6, "I go "),
        ("G0", 6, "back"),
        ("E0", 6, "home"),
        ("G0", 6, "wid a"),
        ("A0", 6, "pocket"),
        ("G0", 6, "full of"),
        ("E0", 4, "tin,"),
        ("D0", 4, "oh,"),
        ("E0", 6, "doo-dah day!"),
        ("D0", 6, None),
        ("C0", 2, None),
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


class MusicWait:

    def __init__(
        self,
        music: List[Tuple[str, int, Optional[str]]] = Music.OH_SUSANNA,
        lyrics: bool = False,
    ):

        self._play = False
        self._lyrics = lyrics
        self._music = music
        self._audio = MusicWait.Audio(bpm=10)
        self._scales = self._audio.make_scale()
        self._notes = self._audio.make_note()

        self._thread: Optional[threading.Thread] = None

        self.play()

    def __enter__(self):
        return self

    def __exit__(self, ex_type, ex_value, trace):
        self.stop()

    def play(self):
        self._play = True
        self._thread = threading.Thread(target=self.loop_music)

        self._thread.start()

    def stop(self):
        self._play = False
        if self._thread is not None:
            self._thread.join()
            self._thread = None

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
            return notes

        # 音階
        def make_scale(self):
            res = {}
            octave = -1
            for n in range(0, 13):
                hz = self.a_hz * 2 ** ((n - 9) / 12)
                if (n % 12) == 0:
                    octave += 1
                name = self.code_names[n % 12] + str(octave)
                res[name] = hz
            return res

        def play(self, hz, note, text: None | str = None, gain=1.0):
            if text is not None:
                print(text)
            self.stream.write(self.__tone(hz, note, gain).astype(np.float32).tobytes())

    def loop_music(self):

        while self._play:
            for hz, note, text in self._music:
                if not self._play:
                    return
                self._audio.play(
                    self._scales[hz], self._notes[note], text if self._lyrics else None
                )
