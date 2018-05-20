import os


class SongService:
    songs = []
    cur_song = ''
    cur_song_index = ''
    song_dir = ''
    music_service = None

    def __init__(self, song_dir, music_service):
        self.song_dir = song_dir
        self.music_service = music_service

    def get_songs(self):
        files = []
        for (root, directories, file_names) in os.walk(self.song_dir):
            for file_name in file_names:
                if file_name.endswith('.mp3'):
                    files.append(file_name)
        return files

    def on_left_click(self):
        print('Previous song')
        songs = self.get_songs()
        cur_index = 0
        if self.cur_song in songs:
            cur_index = songs.index(self.cur_song)
            cur_index -= 1
            if cur_index < 0:
                cur_index = len(songs) - 1
        try:
            self.cur_song = songs[cur_index]
            self.music_service.play(self.cur_song)
        except IndexError:
            pass

    def on_right_click(self):
        print('Next song')
        songs = self.get_songs()
        cur_index = 0
        if self.cur_song in songs:
            cur_index = songs.index(self.cur_song)
            cur_index += 1
            if cur_index >= len(songs):
                cur_index = 0
        try:
            self.cur_song = songs[cur_index]
            self.music_service.play(self.cur_song)
        except IndexError:
            pass
