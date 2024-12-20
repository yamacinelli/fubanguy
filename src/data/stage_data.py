import os
from core.settings import IMAGE_DIR
from core.settings import SOUND_DIR

# __STAGE__
STAGES_DATA = {
    "forest": {
        "background_image": os.path.join(IMAGE_DIR, "stage_forest.jpg"),
        "music": os.path.join(SOUND_DIR, "madruga_theme.mp3"),
    },
    "desert": {
        "background_image": os.path.join(IMAGE_DIR, "hell.jpg"),
        "music": os.path.join(SOUND_DIR, "chaves_theme.mp3"),
    },
    "vila": {
        "background_image": os.path.join(IMAGE_DIR, "vila.png"),
        "music": os.path.join(SOUND_DIR, "quico_theme.mp3"),
    },
}
