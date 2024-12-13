'''
Módulo responsável por executar a lógica de atualização da saúde de um lutador.
'''
from domain.entities.fighter import Fighter
class UpdateHealthUseCase:
    """
    Caso de uso responsável por atualizar a saúde de um lutador após receber dano.
    A saúde do lutador não pode ficar abaixo de zero.

    Métodos:
    - execute: Atualiza a saúde do lutador com base no dano recebido.
    """

    def execute(self, fighter: Fighter, damage: int):
        """
        Executa a lógica de atualização da saúde de um lutador após ele receber dano.

        Parâmetros:
        fighter (Fighter): O lutador que terá sua saúde atualizada.
        damage (int): A quantidade de dano a ser subtraída da saúde do lutador.

        A saúde do lutador será reduzida pelo valor de `damage`, mas nunca ficará abaixo de 0.
        """
        fighter.health = max(0, fighter.health - damage)
