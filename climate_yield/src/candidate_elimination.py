class CandidateElimination:
    def __init__(self,domains,positive_class="High"):
        self.domains=domains; self.positive_class=positive_class; self.S=[None]*len(domains); self.G=[tuple("?" for _ in domains)]
    @staticmethod
    def covers(h,x): return all(a=="?" or a==b for a,b in zip(h,x))
    def update(self,x,label):
        x=tuple(x)
        if label==self.positive_class:
            if all(v is None for v in self.S): self.S=list(x)
            else:
                self.S=["?" if v!=x[i] else v for i,v in enumerate(self.S)]
            self.G=[g for g in self.G if self.covers(g,x)]
        else:
            new=[]
            for g in self.G:
                if self.covers(g,x):
                    for i,dom in enumerate(self.domains):
                        for val in dom:
                            if val!=x[i]:
                                h=list(g); h[i]=val
                                if all(s is None or s=="?" or h[j]=="?" or h[j]==s for j,s in enumerate(self.S)): new.append(tuple(h))
                else: new.append(g)
            self.G=list(dict.fromkeys(new))
        return self.S,self.G
