import pygame
from audio_source import AudioSource

class AudioSourcePGImpl(AudioSource):
    """class to implements methods from interface AudioSource
    """

    _sound = None
    _music = None
    _path_sound = None
    _path_music = None

    def load_sound(self, path_sound) -> None :
        """_summary_
        """
        self._sound = pygame.mixer.Sound(path_sound)

    def load_music(self, path_music) -> None :
        """_summary_
        """
        self._music = pygame.mixer.music.load(path_music)
    
    def play_sound(self) -> None :
        """_summary_
        """
        self._sound.play()

    def play_music(self, loop = 0) -> None :
        """_summary_
        """
        pygame.mixer.music.play(loop)

    def up_sound_volume(self, volume) -> None :
        """_summary
        """
        self._sound.set_volume(volume)

    def down_sound_volume(self, volume) -> None :
        """_summary
        """
        self._sound.set_volume(-volume)

    def up_music_volume(self, volume) -> None :
        """_summary
        """
        pygame.mixer.music.set_volume(volume)

    def down_music_volume(self, volume) -> None :
        """_summary
        """
        pygame.mixer.music.set_volume(-volume)

    def get_path_sound(self):
        """_summary_
        """
        return self._path_sound

    def set_path_sound(self, path_sound) -> None :
        """_summary_
        """
        self._path_sound = path_sound

    def get_path_music(self):
        """_summary_
        """
        return self._path_music

    def set_path_music(self, path_music) -> None :
        """_summary_
        """
        self._path_music = path_music
