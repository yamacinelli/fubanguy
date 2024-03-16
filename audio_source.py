from abc import ABC, abstractmethod


class AudioSource(ABC):
    """_summary_
    """

    @abstractmethod
    def load_sound(self, path_sound):
        """_summary_
        """
        raise ValueError("Should implement method: load_sound")

    @abstractmethod
    def load_music(self, path_music):
        """_summary_
        """
        raise ValueError("Should implement method: load_music")

    @abstractmethod
    def play_sound(self):
        """_summary_
        """
        raise ValueError("Should implement method: play_sound")

    @abstractmethod
    def play_music(self, loop):
        """_summary_
        """
        raise ValueError("Should implement method: play_music")

    @abstractmethod
    def up_sound_volume(self, volume):
        """_summary
        """
        raise ValueError("Should implement method: up_sound_volume")

    @abstractmethod
    def down_sound_volume(self, volume):
        """_summary
        """
        raise ValueError("Should implement method: down_sound_volume")

    @abstractmethod
    def up_music_volume(self, volume):
        """_summary
        """
        raise ValueError("Should implement method: up_music_volume")

    @abstractmethod
    def down_music_volume(self, volume):
        """_summary
        """
        raise ValueError("Should implement method: down_music_volume")

    @abstractmethod
    def get_path_sound(self):
        """_summary_
        """
        raise ValueError("Should implement method: get_path_sound")

    @abstractmethod
    def set_path_sound(self, path_sound):
        """_summary_
        """
        raise ValueError("Should implement method: set_path_sound")

    @abstractmethod
    def get_path_music(self):
        """_summary_
        """
        raise ValueError("Should implement method: get_path_music")

    @abstractmethod
    def set_path_music(self, path_music):
        """_summary_
        """
        raise ValueError("Should implement method: set_path_music")
    