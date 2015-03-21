import ConfigParser

config = ConfigParser.ConfigParser()                                                                                                                                       |   ~

config.read( environment_conf )                                                                                                                                            |   ~
                                                                                                                                                                                   |   ~
print  config.get("Settings", "env")
