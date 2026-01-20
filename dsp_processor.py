import numpy as np
from config import CHUNK_SIZE, SAMPLE_RATE, NUM_BARS, F_MIN_FREQUENCY, F_MAX_FREQUENCY, DB_FLOOR


class DSPProcessor:
    def __init__(self):
        self.hann_window = np.hanning(CHUNK_SIZE)
        self.freq_bins = self._create_logarithmic_bins()
        
    def _create_logarithmic_bins(self):
        freq_boundaries = np.logspace(
            np.log10(F_MIN_FREQUENCY),
            np.log10(F_MAX_FREQUENCY),
            NUM_BARS + 1
        )
        
        fft_indices = []
        for i in range(NUM_BARS):
            freq_start = freq_boundaries[i]
            freq_end = freq_boundaries[i + 1]
            
            idx_start = int(freq_start * CHUNK_SIZE / SAMPLE_RATE)
            idx_end = int(freq_end * CHUNK_SIZE / SAMPLE_RATE)
            
            fft_indices.append((idx_start, idx_end))
            
        return fft_indices
        
    def process_audio_chunk(self, audio_chunk):
        if audio_chunk is None:
            return np.zeros(NUM_BARS)
            
        windowed = audio_chunk * self.hann_window
        
        fft_result = np.fft.rfft(windowed)
        magnitude = np.abs(fft_result)
        
        db_magnitude = 20 * np.log10(magnitude + 1e-6)
        db_magnitude = np.maximum(db_magnitude, DB_FLOOR)
        
        bar_values = np.zeros(NUM_BARS)
        for i, (start_idx, end_idx) in enumerate(self.freq_bins):
            if start_idx < len(db_magnitude):
                end_idx = min(end_idx, len(db_magnitude))
                if end_idx > start_idx:
                    bar_values[i] = np.mean(db_magnitude[start_idx:end_idx])
                    
        return bar_values