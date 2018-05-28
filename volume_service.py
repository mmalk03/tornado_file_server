class VolumeService:
    min_volume = 0.0
    max_volume = 1.0
    cur_volume = 0.5
    volume_delta = 0.1
    music_service = None

    def __init__(self, music_service):
        print('Starting volume service')
        self.music_service = music_service

    def on_left_click(self):
        print('Volume down')
        if self.cur_volume > self.min_volume:
            self.cur_volume -= self.volume_delta
            self.music_service.set_volume(self.cur_volume)
        else:
            self.cur_volume = 0

    def on_right_click(self):
        print('Volume up')
        if self.cur_volume < self.max_volume:
            self.cur_volume += self.volume_delta
            self.music_service.set_volume(self.cur_volume)
        else:
            self.cur_volume = 1.0
