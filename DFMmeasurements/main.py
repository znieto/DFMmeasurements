import app.config.configtools as ct
from app.forms.gui_main import gui_main 
import app.config.global_settings as g
import app.utils.guitools as gt



config = ct.AppConfig(g.DEFAULT_CONFIG_PATH)
gui_main.mainWindow(config.Config)




