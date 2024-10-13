class RoundPresenter:
    def __init__(self):
        self.current_round = 1
        self.round_active = True  # Para controlar se o round está ativo
        self.round_time = 3  # Tempo para contagem regressiva em segundos

    def start_new_round(self):
        self.round_active = True
        self.round_time = 3  # Resetar o tempo

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
