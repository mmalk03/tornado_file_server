import pygame

from src import config
from src.circular_buffer_service import CircularBufferService
# from signal_service import GpioService
from src.gpio_service import GpioService


# TODO: swap imports above

class MusicService:
    circular_buffer_service = None
    gpio_service = None

    def __init__(self):
        print('Starting music service')
        pygame.mixer.init()
        self.gpio_service = GpioService()
        self.circular_buffer_service = CircularBufferService(self, self.gpio_service)
        self.gpio_service.register_on_upper_click(self.circular_buffer_service.next_service)
        self.gpio_service.register_on_left_click(self.circular_buffer_service.on_left_click)
        self.gpio_service.register_on_right_click(self.circular_buffer_service.on_right_click)

    @staticmethod
    def play(song):
        print('Playing: ' + song)
        pygame.mixer.music.load(config.CONFIG['song_dir'] + '/' + song)
        pygame.mixer.music.play()

    @staticmethod
    def set_volume(volume):
        print('Setting volume to: ' + str(volume))
        pygame.mixer.music.set_volume(volume)

    @staticmethod
    def pause():
        print('Pause')
        pygame.mixer.music.pause()

    @staticmethod
    def resume():
        print('Resume')
        pygame.mixer.music.unpause()
