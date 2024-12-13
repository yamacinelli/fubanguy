'''
Módulo responsável por gerenciar a execução de estágios no jogo.
Este módulo seleciona um estágio aleatório ou um estágio específico,
baseando-se nas informações armazenadas em STAGES_DATA.

Funções:
- execute: Retorna um estágio com base no nome ou um aleatório.
'''
import random
from typing import Optional
from domain.entities.stage import Stage
from data.stage_data import STAGES_DATA


def execute(stage_name: Optional[str] = None) -> Stage:
    """
    Executa a lógica de seleção de um estágio. Se um nome de estágio for fornecido,
    retorna o estágio correspondente. Caso contrário, seleciona aleatoriamente um estágio
    e retorna suas informações.

    Parâmetros:
    stage_name (Optional[str]): O nome do estágio a ser selecionado. Se None, um estágio aleatório será escolhido.

    Retorna:
    Stage: Um objeto do tipo Stage com os dados do estágio, incluindo a imagem de fundo e a música.
    """
    __stage_name = stage_name

    if __stage_name is None:
        stage_type = random.choice(list(STAGES_DATA.keys()))
        return Stage(
            STAGES_DATA[stage_type]["background_image"],
            STAGES_DATA[stage_type]["music"],
        )

    __stage_data = STAGES_DATA.get(stage_name)

    return Stage(
        background_image=__stage_data["background_image"],
        music=__stage_data["music"],
    )
