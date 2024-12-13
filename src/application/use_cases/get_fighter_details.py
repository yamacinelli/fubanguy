"""
Este módulo fornece funcionalidade para criar instâncias de Fighter com base em dados predefinidos.

O módulo importa os dados dos lutadores de `data.fighter_assets` e define uma função
para criar instâncias de Fighter utilizando esses dados.

Funções:
    execute(fighter_name: str, jump_fx, land_fx, swoosh_fx, sound_fx_list, sprite_sheet) -> Fighter:
        Cria e retorna uma instância de Fighter com base no nome do lutador fornecido.
"""

from application.use_cases import animation_handler
from data.fighter_data import FIGHTERS_DATA
from domain.entities.fighter import Fighter

def execute(fighter_name: str, jump_fx, land_fx, swoosh_fx, sound_fx_list, sprite_sheet) -> Fighter:
    """
    Cria e retorna uma instância de Fighter com base no nome do lutador fornecido.

    Args:
        fighter_name (str): O nome do lutador a ser criado.
        jump_fx: Efeito sonoro para o salto do lutador.
        land_fx: Efeito sonoro para o pouso do lutador.
        swoosh_fx: Efeito sonoro para os ataques do lutador.
        sound_fx_list: Lista de efeitos sonoros adicionais para o lutador.
        sprite_sheet: Sprite sheet associada ao lutador.

    Returns:
        Fighter: Uma instância da classe Fighter com atributos carregados a partir de FIGHTERS_DATA.

    Raises:
        ValueError: Se nenhum lutador com o nome fornecido for encontrado em FIGHTERS_DATA.

    Exemplo:
        fighter = execute(
            fighter_name="Ryu",
            jump_fx=jump_sound,
            land_fx=land_sound,
            swoosh_fx=swoosh_sound,
            sound_fx_list=[punch_sound, kick_sound],
            sprite_sheet=ryu_sprite_sheet
        )
    """
    _fighter_data = FIGHTERS_DATA.get(fighter_name)

    if not _fighter_data:
        raise ValueError(f"\033[0;31m No fighter found with name: {fighter_name}\033[m")

    animations = animation_handler.execute(_fighter_data.get("animations"))

    return Fighter(
        name=_fighter_data["name"],
        health=_fighter_data["health"],
        position=_fighter_data["position"],
        size=_fighter_data["size"],
        attack_power=_fighter_data["attack_power"],
        animations=animations,
        sprite_sheet=sprite_sheet,
        jump_fx=jump_fx,
        land_fx=land_fx,
        swoosh_fx=swoosh_fx,
        sound_fx_list=sound_fx_list,
    )
