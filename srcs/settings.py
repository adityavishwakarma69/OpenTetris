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
        self.diffsec = self.config['DIFF']
        self.optsec = self.config['OPTIONS']
        self.filesec = self.config['FILES']

    def getdiffthold(self):
        return int(self.optsec['progress_period'])
    def getdiffs(self):
        return [int(self.diffsec['level1']),
                int(self.diffsec['level2']),
                int(self.diffsec['level3']),
                int(self.diffsec['level4']),
                int(self.diffsec['level5']),
                int(self.diffsec['level6']),
                int(self.diffsec['level7']),
                int(self.diffsec['level8']),
                int(self.diffsec['level9']),
                int(self.diffsec['level10']),
                int(self.diffsec['level11']),
                int(self.diffsec['level12']),
                ]

    def bgmusic(self):
        return self.filesec['bgmusic']

    def placesound(self):
        return self.filesec['placesound']
    
    def spinsound(self):
        return self.filesec['spinsound']

    def getCellColors(self):
        return [self.coldict['cell'],
                self.coldict['l'],
                self.coldict['j'],
                self.coldict['i'],
                self.coldict['o'],
                self.coldict['s'],
                self.coldict['t'],
                self.coldict['z']]

    def color(self, key):
        return self.coldict[key]

    def margin(self):
        return int(self.vissec['margin'])
