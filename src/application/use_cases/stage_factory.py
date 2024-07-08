import random
from domain.entities.stage import Stage
from infra.assets.scene_assets import SCENES_ASSETS


class StageFactory:
    def create_random_stage(self):
        # Escolher aleatoriamente um dos cenários configurados
        stage_type = random.choice(list(SCENES_ASSETS.keys()))
        return Stage(
            SCENES_ASSETS[stage_type]["background_image"],
            SCENES_ASSETS[stage_type]["music"],
        )
