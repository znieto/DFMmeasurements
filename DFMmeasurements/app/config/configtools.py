import pathlib
import configparser
import logging


class AppConfig(object):
    """
    Class representing a this application and its configuration.
    """
    def __init__(self,pathToFile):
        """
        the path should be in the following form: "C:\\Windows\\redir.txt" 
        """
        path = pathlib.Path(pathToFile)
        if path.exists():
            #File already exists
            self.Config = configparser.SafeConfigParser()
            self.Config.read(pathToFile)
            self.path=pathToFile
        else:            
            print('Init file does not exist under this directory', pathToFile)

    def reload(self):
            self.Config = configparser.SafeConfigParser()
            self.Config.read(self.path)

    def save_option(self, section, option, value):
            """
            Write the specified Section.Option to the config file specified by path.
            Replace any previous value.  If the path doesn't exist, create it.
            Also add the option the the in-memory config.
            """
            config=self.Config
            if not config.has_section(section):
                config.add_section(section)
            config.set(section, option, value)
            fp = open(self.path, 'w')
            config.write(fp)
            fp.close()
            if not config.has_section(section):
                config.add_section(section)
            config.set(section, option, value)

    #def save_option(self, path, section, option, value):
    #        """
    #        Write the specified Section.Option to the config file specified by path.
    #        Replace any previous value.  If the path doesn't exist, create it.
    #        Also add the option the the in-memory config.
    #        """
    #        config = ConfigParser.SafeConfigParser()
    #        config.read(path)
    #        if not config.has_section(section):
    #            config.add_section(section)
    #        config.set(section, option, value)
    #        fp = open(path, 'w')
    #        config.write(fp)
    #        fp.close()
    #        if not self.has_section(section):
    #            self.add_section(section)
    #        self.set(section, option, value)

    def configSectionMap(self,section):
        dict1 = {}
        Config=self.Config
        options = Config.options(section)
        for option in options:
            try:
                dict1[option] = Config.get(section, option)
                if dict1[option] == -1:
                    DebugPrint("skip: %s" % option)
            except:
                e = sys.exc_info()[0]
                logging.exception(e)
                dict1[option] = None
        return dict1

    def getOption(self,section, option):
        try:
            value = self.Config.get(section, option)
        except:
            e = sys.exc_info()[0]
            logging.exception(e)
            value = ''
        return value

