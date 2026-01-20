import pygame
import sys
from audio_stream import AudioStream
from dsp_processor import DSPProcessor
from renderer import Renderer


def main():
    print("Starting Real-Time Sound Wave Visualizer...")
    
    audio_stream = AudioStream()
    dsp_processor = DSPProcessor()
    renderer = Renderer()
    
    try:
        audio_stream.start()
        print("Audio stream started successfully")
        
        running = True
        frame_count = 0
        
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
                        
            audio_chunk = audio_stream.read_chunk()
            db_values = dsp_processor.process_audio_chunk(audio_chunk)
            
            renderer.update(db_values)
            
            frame_count += 1
            fps = renderer.get_fps()
            renderer.render(fps)
            renderer.tick()
                
    except KeyboardInterrupt:
        print("\nShutting down...")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        audio_stream.stop()
        pygame.quit()
        sys.exit()


if __name__ == "__main__":
    main()