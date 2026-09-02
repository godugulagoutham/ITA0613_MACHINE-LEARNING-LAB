class CandidateElimination:
    def __init__(self,domains,positive_class="High"): self.domains=domains; self.positive_class=positive_class; self.S=[None]*len(domains); self.G=[tuple("?" for _ in domains)]
    @staticmethod
    def covers(h,x): return all(a=="?" or a==b for a,b in zip(h,x))
    def update(self,x,label):
        x=tuple(x)
        if label==self.positive_class:
            if all(v is None for v in self.S): self.S=list(x)
            else:
                for j,v in enumerate(x):
                    if self.S[j]!=v: self.S[j]="?"
            self.G=[g for g in self.G if self.covers(g,x)]
        else:
            new_g=[]
            for g in self.G:
                if self.covers(g,x):
                    for j,dom in enumerate(self.domains):
                        if g[j]=="?":
                            for val in dom:
                                if val!=x[j]:
                                    h=list(g); h[j]=val
                                    compatible=all(self.S[t] is None or self.S[t]=="?" or h[t]=="?" or h[t]==self.S[t] for t in range(len(self.domains)))
                                    if compatible: new_g.append(tuple(h))
                else: new_g.append(g)
            self.G=list(dict.fromkeys(new_g))
        return self.S,self.G
