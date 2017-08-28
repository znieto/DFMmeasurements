import app.config.configtools as ct
from app.forms.gui_main import gui_main 
import app.config.global_settings as g
import app.core.guitools as gt



config = ct.AppConfig(g.DEFAULT_CONFIG_PATH)
gt.GUITool.loadMainGUI(config.Config)
gui_main.mainWindow()




