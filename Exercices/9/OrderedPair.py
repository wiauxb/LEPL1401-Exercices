#@/----------------
#   $$author: wiauxb
#----------------/@#


def set_a(self,n_a):
    self.p.a = n_a
    self.ordered = self.p.a<=self.p.b
    
def set_b(self,n_b):
    self.p.b = n_b
    self.ordered = self.p.a<=self.p.b
