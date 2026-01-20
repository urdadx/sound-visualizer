import pyaudio
import numpy as np
from config import CHUNK_SIZE, SAMPLE_RATE, CHANNELS, FORMAT


class AudioStream:
    def __init__(self):
        self.pa = pyaudio.PyAudio()
        self.stream = None
        self.is_active = False
        
    def start(self):
        format_map = {"int16": pyaudio.paInt16}
        
        self.stream = self.pa.open(
            format=format_map[FORMAT],
            channels=CHANNELS,
            rate=SAMPLE_RATE,
            input=True,
            frames_per_buffer=CHUNK_SIZE
        )
        
        self.is_active = True
        
    def read_chunk(self):
        if not self.is_active or not self.stream:
            return None
            
        try:
            raw_bytes = self.stream.read(CHUNK_SIZE, exception_on_overflow=False)
            
            audio_array = np.frombuffer(raw_bytes, dtype=np.int16)
            
            normalized = audio_array.astype(np.float32) / 32768.0
            
            return normalized
            
        except Exception as e:
            print(f"Audio read error: {e}")
            return None
            
    def stop(self):
        if self.stream:
            self.stream.stop_stream()
            self.stream.close()
        self.is_active = False
        
    def __del__(self):
        self.stop()
        self.pa.terminate()