class Physic:
    """
    Classe responsável por simular a física de movimento de um objeto no jogo.

    Esta classe gerencia o movimento horizontal e vertical de um objeto, levando em consideração
    a velocidade inicial, a aceleração e a gravidade. Ela atualiza a posição do objeto com base
    no tempo passado e nas forças aplicadas.

    Atributos:
        speed (float): A velocidade inicial do objeto.
        acceleration (float): A aceleração aplicada ao objeto.
        gravity (float): A aceleração devido à gravidade que afeta o movimento vertical.
        vertical_speed (float): A velocidade vertical do objeto.
    """

    def __init__(self, initial_speed: float, acceleration: float, gravity: float):
        """
        Inicializa os parâmetros de física para o objeto.

        Parâmetros:
            initial_speed (float): A velocidade inicial do objeto.
            acceleration (float): A aceleração aplicada ao objeto.
            gravity (float): A aceleração devido à gravidade.
        """
        self.speed = initial_speed
        self.acceleration = acceleration
        self.gravity = gravity
        self.vertical_speed: float = 0.0

    def update_horizontal(self, delta_time):
        """
        Atualiza o deslocamento horizontal do objeto com base no tempo.

        Calcula o deslocamento horizontal usando a fórmula do movimento uniformemente acelerado
        e atualiza a velocidade horizontal com base na aceleração.

        Parâmetros:
            delta_time (float): O tempo passado desde a última atualização.

        Retorna:
            float: O deslocamento horizontal calculado.
        """
        displacement: float = 0.0
        displacement += (
            self.speed * delta_time + self.acceleration * (delta_time**2) / 2
        )
        self.speed += self.acceleration * delta_time
        return displacement

    def update_vertical(self, delta_time):
        """
        Atualiza o deslocamento vertical do objeto com base no tempo.

        Calcula o deslocamento vertical levando em consideração a gravidade e a velocidade vertical
        do objeto. Atualiza também a velocidade vertical com base na aceleração da gravidade.

        Parâmetros:
            delta_time (float): O tempo passado desde a última atualização.

        Retorna:
            float: O deslocamento vertical calculado.
        """
        vertical_displacement: float = 0.0
        vertical_displacement += (
            self.vertical_speed * delta_time + 0.5 * self.gravity * (delta_time**2)
        )
        self.vertical_speed += (
            self.gravity * delta_time
        )  
        return vertical_displacement
