from abc import ABC, abstractmethod


class AudioSource(ABC):
    """_summary_
    """
    
    @abstractmethod
    def load_sound(self, path_sound):
        """_summary_
        """
        pass

    @abstractmethod
    def load_music(self, path_music):
        """_summary_
        """
        pass
    
    @abstractmethod
    def play(self):
        """_summary_
        """
        pass
    
    @abstractmethod
    def up_sound_volume(self, volume):
        """_summary
        """
        pass

    @abstractmethod
    def down_sound_volume(self, volume):
        """_summary
        """
        pass

    @abstractmethod
    def up_music_volume(self, volume):
        """_summary
        """
        pass

    @abstractmethod
    def down_music_volume(self, volume):
        """_summary
        """
        pass