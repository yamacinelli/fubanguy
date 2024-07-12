import random
from domain.entities.stage import Stage
from data.stage_assets import STTAGE_DATA


class StageFactory:
    def create_random_stage(self):
        # Escolher aleatoriamente um dos cenários configurados
        stage_type = random.choice(list(STTAGE_DATA.keys()))
        return Stage(
            STTAGE_DATA[stage_type]["background_image"],
            STTAGE_DATA[stage_type]["music"],
        )
