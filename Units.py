## SI UNITS

class Length:
    def __init__(self,length = 0):
        self.length = length
    
    def __str__(self):
        return str(self.length)+"M"
    
    def set_m(self,m):
        self.length = m

    def set_nm(self,nm):
        self.length = nm * 1e-9
    
    def get_nm(self):
        return self.length * 1e9

    def get_m(self):
        return self.length

## Constants

C = 299792458