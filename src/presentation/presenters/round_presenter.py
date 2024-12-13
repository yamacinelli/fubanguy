from core.interfaces.sound import SoundInterface
from infra.frameworks.py_game.adapters.pygame_sound import PyGameSound


class RoundPresenter:
    """
    Um presenter para gerenciar os rounds de uma partida.

    Esta classe é responsável por controlar o andamento dos rounds, 
    incluindo a contagem regressiva e a transição para o próximo round. 
    Também gerencia o efeito sonoro do início de cada round.
    """

    def __init__(self):
        """
        Inicializa o RoundPresenter com os valores iniciais do round.

        O round começa no round 1, o tempo do round é 3 segundos e 
        o round está ativo.
        """
        self.current_round = 1
        self.round_active = True  # Para controlar se o round está ativo
        self.round_time = 3  # Tempo para contagem regressiva em segundos
        self._fight_fx = None

    def start_new_round(self, fight_fx: SoundInterface = PyGameSound()):
        """
        Inicia um novo round, tocando um efeito sonoro e reiniciando a contagem.

        Este método reinicia o tempo de contagem regressiva para o novo round,
        ativa o efeito sonoro de início de round e ajusta o volume.

        Args:
            fight_fx (SoundInterface, opcional): O efeito sonoro a ser tocado no início do round.
                Por padrão, é usado PyGameSound.
        """
        self.round_active = True
        self.round_time = 3  # Resetar o tempo
        self._fight_fx = fight_fx
        self._fight_fx.play_sound()
        # TODO mudar para melhor volume
        self._fight_fx.volume_sound(1.0)

    def update_round(self, delta_time):
        """
        Atualiza o estado do round com base no tempo decorrido.

        Este método decrementa o tempo do round e, caso o tempo chegue a zero, 
        desativa o round atual e inicia o próximo round.

        Args:
            delta_time (float): O tempo decorrido desde a última atualização.
        """
        if self.round_active:
            self.round_time -= delta_time
            if self.round_time <= 0:
                self.round_active = False
                self.current_round += 1  # Avançar para o próximo round

    def get_round(self):
        """
        Retorna o número do round atual, caso o round esteja ativo.

        Returns:
            str: O número do round atual se o round estiver ativo, ou uma string vazia caso contrário.
        """
        if self.round_active:
            return self.current_round
        return ""
