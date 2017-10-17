import app.config.configtools as ct
import app.config.global_settings as gs

class MeasurementTools(object):
    """Class containing methods to setup and run a measurament"""
    def LoadWorkingDirectories(section):
        config = ct.AppConfig(gs.DEFAULT_CONFIG_PATH).Config
        #check if relative or ... 
        gs.M_SREFFILEPATH

        #gs.M_SDATABASE = ct.AppConfig.getOption(section,"")
        #gs.M_SSTOREPATH
        #gs.M_STEMPPATH





