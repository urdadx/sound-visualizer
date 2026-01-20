import pygame
import numpy as np
from config import (SCREEN_WIDTH, SCREEN_HEIGHT, NUM_BARS, BAR_SPACING, 
                   BACKGROUND_COLOR, BAR_COLOR, PEAK_COLOR, 
                   DB_FLOOR, SMOOTHING_FACTOR, GRAVITY)


class Renderer:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Real-Time Sound Wave Visualizer")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, 24)
        
        self.bar_heights = np.zeros(NUM_BARS)
        self.peak_heights = np.zeros(NUM_BARS)
        self.peak_timers = np.zeros(NUM_BARS)
        
        self.bar_width = (SCREEN_WIDTH - BAR_SPACING * (NUM_BARS + 1)) // NUM_BARS
        
    def _db_to_screen_height(self, db_value):
        normalized = (db_value - DB_FLOOR) / (-DB_FLOOR)
        return int(normalized * SCREEN_HEIGHT)
        
    def update(self, db_values):
        for i in range(NUM_BARS):
            target_height = self._db_to_screen_height(db_values[i])
            
            if target_height > self.bar_heights[i]:
                self.bar_heights[i] = target_height
            else:
                self.bar_heights[i] = max(target_height, 
                                         self.bar_heights[i] - GRAVITY)
                
            if self.bar_heights[i] > self.peak_heights[i]:
                self.peak_heights[i] = self.bar_heights[i]
                self.peak_timers[i] = 30  # ~500ms at 60 FPS
                
            if self.peak_timers[i] > 0:
                self.peak_timers[i] -= 1
            else:
                self.peak_heights[i] = max(self.peak_heights[i] - GRAVITY, 0)
                
    def render(self, fps=None):
        self.screen.fill(BACKGROUND_COLOR)
        
        for i in range(NUM_BARS):
            x = BAR_SPACING + i * (self.bar_width + BAR_SPACING)
            bar_height = int(self.bar_heights[i])
            peak_height = int(self.peak_heights[i])
            
            if bar_height > 0:
                bar_rect = pygame.Rect(x, SCREEN_HEIGHT - bar_height, 
                                      self.bar_width, bar_height)
                pygame.draw.rect(self.screen, BAR_COLOR, bar_rect)
                
            if peak_height > 0:
                peak_rect = pygame.Rect(x, SCREEN_HEIGHT - peak_height - 3, 
                                       self.bar_width, 3)
                pygame.draw.rect(self.screen, PEAK_COLOR, peak_rect)
        
        # Render FPS and Gravity info
        if fps is not None:
            fps_text = self.font.render(f"FPS: {fps:.1f}", True, PEAK_COLOR)
            fps_rect = fps_text.get_rect(right=SCREEN_WIDTH - 10, top=10)
            self.screen.blit(fps_text, fps_rect)
            
        gravity_text = self.font.render(f"Gravity: {GRAVITY}", True, PEAK_COLOR)
        gravity_rect = gravity_text.get_rect(right=SCREEN_WIDTH - 10, top=40)
        self.screen.blit(gravity_text, gravity_rect)
                
        pygame.display.flip()
        
    def get_fps(self):
        return self.clock.get_fps()
        
    def tick(self):
        self.clock.tick(60)