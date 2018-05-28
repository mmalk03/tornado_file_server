import config
from power_service import PowerService
from song_service import SongService
from volume_service import VolumeService


class CircularBufferService:
    items = []
    index = 0
    gpio_service = None

    def __init__(self, music_service, gpio_service):
        print('Starting circular buffer service')
        self.items = [None] * 3
        self.items[0] = PowerService(music_service)
        self.items[1] = SongService(config.CONFIG['song_dir'], music_service)
        self.items[2] = VolumeService(music_service)
        self.gpio_service = gpio_service
        self.set_diodes()

    def set_diodes(self):
        if self.index == 0:
            self.gpio_service.select_red()
        elif self.index == 1:
            self.gpio_service.select_blue()
        else:
            self.gpio_service.select_green()

    def next_service(self, signum=None, frame=None):
        if self.index >= 2:
            self.index = 0
        else:
            self.index += 1
        self.set_diodes()

    def on_left_click(self, signum=None, frame=None):
        self.items[self.index].on_left_click()

    def on_right_click(self, signum=None, frame=None):
        self.items[self.index].on_right_click()
