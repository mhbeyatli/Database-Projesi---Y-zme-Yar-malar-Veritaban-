class Medals:
    def __init__(self, id, year, gold="", silver="", bronze=""):
        self.id = id
        self.year = year
        self.gold = gold
        self.silver = silver
        self.bronze = bronze

class Medal_Records:
    def __init__(self, id, bscore, mid):
        self.id = id
        self.bscore = bscore
        self.mid = mid