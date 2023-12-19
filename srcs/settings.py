import configparser
from ast import literal_eval

class Settings:
    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read('data/settings.ini')

        self.colsec = self.config['COLORS']
        self.coldict = {}
        for col in self.colsec:
            self.coldict[col] = literal_eval(self.colsec[col])


        self.vissec = self.config['VISUALS']
        self.confsec = self.config['CONFIG']
        self.optsec = self.config['OPTIONS']


    def diffmode():
        return self.optsec['mode']
    def diffstarting():
        return self.optsec['starting_difficulity']
    def difficulity(level):
        return int(self.confsec[level])

    def getCellColors(self):
        return [self.coldict['cell'], self.coldict['l'], self.coldict['j'], self.coldict['i'], self.coldict['o'], self.coldict['s'], self.coldict['t'], self.coldict['z']]

    def color(self, key):
        return self.coldict[key]

    def margin(self):
        return int(self.vissec['margin'])
