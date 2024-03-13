import pygame
from audio_source import AudioSource


class AudioSourcePGImpl(AudioSource):
    """_summary_
    """
    
    _sound = None
    _music = None

    def load_sound(self, path_sound):
        """_summary_
        """
        self._sound = path_sound
        print("load sound")

    def load_music(self, path_music):
        """_summary_
        """
        self._music = path_music
        print("load sound")
    
    def play(self):
        """_summary_
        """
        print("play sound")

    def up_sound_volume(self, volume):
        """_summary
        """
        self._sound.set_volume(volume)

    def down_sound_volume(self, volume):
        """_summary
        """
        self._sound.set_volume(-volume)

    def up_music_volume(self, volume):
        """_summary
        """
        pygame.mixer.music.set_volume(volume)

    def down_music_volume(self, volume):
        """_summary
        """
        pygame.mixer.music.set_volume(-volume)

    @property
    def _sound(self):
        """_summary_
        """
        return self._sound

    @_sound.setter
    def _sound(self, path_sound):
        """_summary_
        """
        self._sound = pygame.mixer.Sound(path_sound)

    @_music.setter
    def _music(self, path_music):
        """_summary_
        """
        self._sound = pygame.mixer.music.load(path_music)
