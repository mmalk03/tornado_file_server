class PowerService:
    music_service = None

    def __init__(self, music_service):
        self.music_service = music_service

    def on_left_click(self):
        self.music_service.pause()

    def on_right_click(self):
        self.music_service.resume()
