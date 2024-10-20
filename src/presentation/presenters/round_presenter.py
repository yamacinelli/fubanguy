from core.interfaces.sound import SoundInterface
from infra.frameworks.py_game.adapters.pygame_sound import PyGameSound


class RoundPresenter:
    def __init__(self):
        self.current_round = 1
        self.round_active = True  # Para controlar se o round está ativo
        self.round_time = 3  # Tempo para contagem regressiva em segundos
        self._fight_fx = None

    def start_new_round(self, fight_fx: SoundInterface = PyGameSound()):
        self.round_active = True
        self.round_time = 3  # Resetar o tempo
        self._fight_fx = fight_fx
        self._fight_fx.play_sound()
        # TODO mudar para melhor volume
        self._fight_fx.volume_sound(1.0)
        

    def update_round(self, delta_time):
        if self.round_active:
            self.round_time -= delta_time
            if self.round_time <= 0:
                self.round_active = False
                self.current_round += 1  # Avançar para o próximo round

    def get_round(self):
        if self.round_active:
            # print(f"Round Atual: {self.current_round}")
            return self.current_round
        return ""
