# PySoundXY - Real-Time Audio Visualizer

A simple real-time audio visualizer built with Python that captures live microphone input and transforms it into dynamic frequency-based visualizations using Fast Fourier Transform (FFT) analysis. You can check out the mini research I did for the project to understand the fundamentals here 👉 [Mini Research Dump](https://docs.google.com/document/d/1Dq2ZcLPa4CcfuNNo_l4u7hNDIz_rdLAKrx2mYbj9pfE/edit?usp=sharing)


![Python](https://img.shields.io/badge/Python-3.12+-blue.svg)
![Pygame](https://img.shields.io/badge/Pygame-2.0+-green.svg)
![NumPy](https://img.shields.io/badge/NumPy-1.24+-orange.svg)

## Features

- **Real-time Audio Processing**: Captures live microphone input using PyAudio
- **Frequency Analysis**: FFT-based frequency spectrum analysis with logarithmic frequency bins
- **Smooth Animations**: Gravity-based bar animations with peak detection
- **Configurable Visualization**: Customizable colors, bar count, and visual parameters
- **Performance Monitoring**: Real-time FPS display and performance metrics

## Architecture

The application is built with a modular architecture consisting of four main components:

### Core Components

- **`AudioStream`** (`audio_stream.py`): Handles real-time audio capture from microphone input
- **`DSPProcessor`** (`dsp_processor.py`): Performs Fast Fourier Transform and frequency analysis
- **`Renderer`** (`renderer.py`): Manages pygame-based visualization rendering and animations
- **`main.py`**: Application entry point and main event loop

### Configuration

All settings are centralized in `config.py`:
- Audio stream parameters (sample rate, chunk size, channels)
- DSP processing settings (frequency ranges, smoothing)
- Visualization options (screen dimensions, colors, bar count)

## Installation

### Prerequisites

- Python 3.12 or higher
- System audio drivers and microphone access
- [uv](https://docs.astral.sh/uv/) Python package manager

### Setup

1. Install uv (if not already installed):
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

2. Clone the repository:
```bash
git clone <repository-url>
cd sound-visualizer/py-soundxy
```

3. Create virtual environment and install dependencies:
```bash
uv sync
```

### Running the Application

```bash
uv run python main.py
```

### Development Setup

For development with additional tools:
```bash
uv sync --dev
```

## Usage

### Controls

- **ESC** or **Close Window**: Exit the application
- The visualizer will automatically start capturing audio from your default microphone

### Configuration

Edit `config.py` to customize

## Dependencies

- **pygame**: Graphics rendering and window management
- **numpy**: Numerical computations and FFT operations
- **pyaudio**: Real-time audio input capture
- **ruff**: Code formatting and linting (development)

## Troubleshooting

### Common Issues

1. **No Audio Input**:
   - Check microphone permissions in your system
   - Ensure microphone is not muted
   - Verify PyAudio can access your audio device

2. **Performance Issues**:
   - Reduce `CHUNK_SIZE` for lower latency
   - Decrease `NUM_BARS` for less computational load
   - Lower `FPS` target in config

3. **Installation Errors**:
   - Install system audio development libraries
   - On Linux: `sudo apt-get install portaudio19-dev`
   - On macOS: `brew install portaudio`

### Audio Device Selection

The application uses your default recording device. To use a specific device, modify the `AudioStream` class to accept device indices.

## Development

### Code Style

This project uses Ruff for code formatting and linting. Run checks with:
```bash
uv run ruff check .
uv run ruff format .
```


## License

This project is open source under MIT License. 
## Contributing

Contributions are welcome! Please:
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Ensure all tests pass
5. Submit a pull request

## Future Enhancements

- Multiple visualization modes (waveform, circular, particles)
- Audio file playback support
- Advanced audio effects (filters, reverb visualization)# sound-visualizer
