import os 
import app.config.configtools as ct
from app.forms.gui_main import gui_main 
import app.config.global_settings as g
import app.utils.guitools as gt



g.ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

# Default images path
g.IMAGE_PATH = os.path.join(g.ROOT_DIR, g.DEFAULT_IMAGES_PATH)

g.DEFAULT_MEASUREMENT_PATH = os.path.join(g.ROOT_DIR,g.DEFAULT_MEASUREMENT_PATH)
config = ct.AppConfig(g.DEFAULT_CONFIG_PATH)
gui_main.mainWindow(config.Config)




