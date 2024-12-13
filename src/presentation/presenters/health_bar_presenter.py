"""
Este módulo contém a classe HealthBarPresenter, que é responsável 
por gerenciar as atualizações de saúde de um lutador e atualizar 
a visualização correspondente.
"""

from typing import Any, Type
from application.use_cases.update_health import UpdateHealthUseCase
from domain.entities.fighter import Fighter


class HealthBarPresenter:
    """
    Um presenter para gerenciar a barra de saúde de um lutador.

    Esta classe facilita a interação entre a visualização da barra de saúde 
    e o caso de uso para atualizar a saúde do lutador. Ela garante que 
    a visualização seja atualizada sempre que o lutador sofrer dano.
    """

    def __init__(
        self,
        view: Any,
        update_health_use_case: Type[UpdateHealthUseCase],
    ):
        """
        Inicializa o HealthBarPresenter.

        Args:
            view: A visualização responsável por renderizar a barra de saúde.
            update_health_use_case (Type[UpdateHealthUseCase]): O caso de uso
                para atualizar a saúde do lutador.
        """
        self.view = view
        self.update_health_use_case = update_health_use_case

    def on_damage_taken(self, fighter: Type[Fighter], damage: int):
        """
        Processa o dano recebido pelo lutador e atualiza a visualização da saúde.

        Este método executa o caso de uso para atualizar a saúde do lutador 
        e atualiza a exibição da barra de saúde.

        Args:
            fighter (Type[Fighter]): A instância do lutador que recebeu dano.
            damage (int): A quantidade de dano recebida pelo lutador.
        """
        self.update_health_use_case.execute(fighter, damage)
        self.view.update_health(fighter.health)
