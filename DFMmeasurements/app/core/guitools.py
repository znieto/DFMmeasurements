from ..config import global_settings as gs

class GUITool(object):
    def loadMainGUI(configfile): 
        #configfile=gs.CONFIG
        sections = configfile.sections()
        for each_section in sections:
           for (each_key, each_val) in configfile.items(each_section):
                print(each_key)
                print(each_val)



