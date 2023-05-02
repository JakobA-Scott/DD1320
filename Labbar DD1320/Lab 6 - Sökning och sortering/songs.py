class Songs:
    def __init__(self, trackid, låtid, artistnamn, låttitel):
        self.trackid = trackid
        self.låtid = låtid
        self.artistnamn = artistnamn
        self.låttitel = låttitel

    def __lt__(self, other):
        #vad vill vi kolla här?
        if self.låttitel < other.låttitel:
            return True
        else:
            return False

        # metod5 string
    def __str__(self):  # här kan man lägga till fler attribut om man vill
        return "Trackid: " + str(self.trackid) + " låtid: " + str(self.låtid) + " artistnamn: " + str(self.artistnamn)\
               + "låttitel: " + str(self.låttitel)
