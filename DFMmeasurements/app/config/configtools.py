import pathlib
import configparser


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

    def save_option(self, section, option, value):
            """
            Write the specified Section.Option to the config file specified by path.
            Replace any previous value.  If the path doesn't exist, create it.
            Also add the option the the in-memory config.
            """
            if not config.has_section(section):
                config.add_section(section)
            config.set(section, option, value)
            fp = open(path, 'w')
            config.write(fp)
            fp.close()
            if not self.has_section(section):
                self.add_section(section)
            self.set(section, option, value)

    def save_option(self, path, section, option, value):
            """
            Write the specified Section.Option to the config file specified by path.
            Replace any previous value.  If the path doesn't exist, create it.
            Also add the option the the in-memory config.
            """
            config = ConfigParser.SafeConfigParser()
            config.read(path)
            if not config.has_section(section):
                config.add_section(section)
            config.set(section, option, value)
            fp = open(path, 'w')
            config.write(fp)
            fp.close()
            if not self.has_section(section):
                self.add_section(section)
            self.set(section, option, value)

    def configSectionMap(section,Config):
        dict1 = {}
        options = Config.options(section)
        for option in options:
            try:
                dict1[option] = Config.get(section, option)
                if dict1[option] == -1:
                    DebugPrint("skip: %s" % option)
            except:
                print("exception on %s!" % option)
                dict1[option] = None
        return dict1

    def getOption(self,section, option):
        try:
            value = config.get(section, option)
        except:
            print("exception on %s!" % option)
            value = ''
        return value

    def loadWorkingDirectories(self,section, filesdirectory):

        ORG_REF_FILE_PATH = self.getOption(section,"REF_FILE_PATH")
        REF_FILE_PATH = self.getAbsoluteDir(ORG_REF_FILE_PATH,filesdirectory)
        ##if directories are no the same, then copy procesed on ini.
        #if ORG_REF_FILE_PATH!=REF_FILE_PATH:
        #   Config.set(section, "REF_FILE_PATH", REF_FILE_PATH)


    def getAbsoluteDir(self,directory, rootdirectory):
        import os

        #check that directory string is not empty.
        if not directory:
            #is abasulte path? if not add root dir
            isabs= os.path.isabs(directory)
            if not isabs:                
                directory =  os.path.join(rootdirectory, directory)

        return directory
