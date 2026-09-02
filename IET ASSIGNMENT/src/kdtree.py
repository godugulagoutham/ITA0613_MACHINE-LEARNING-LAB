import numpy as np
class KDNode:
    def __init__(self,point,index,axis,left=None,right=None): self.point,self.index,self.axis,self.left,self.right=point,index,axis,left,right
class KDTreeScratch:
    def __init__(self,X): self.X=np.asarray(X,float); self.root=self._build([(self.X[i],i) for i in range(len(self.X))],0)
    def _build(self,items,depth):
        if not items:return None
        axis=depth%self.X.shape[1]; items.sort(key=lambda z:z[0][axis]); mid=len(items)//2; p,i=items[mid]
        return KDNode(p,i,axis,self._build(items[:mid],depth+1),self._build(items[mid+1:],depth+1))
    def query(self,q):
        best=[float("inf"),None]; q=np.asarray(q,float)
        def visit(node):
            if node is None:return
            d2=float(np.sum((node.point-q)**2))
            if d2<best[0]:best[:]=[d2,node.index]
            diff=q[node.axis]-node.point[node.axis]; near,far=(node.left,node.right) if diff<0 else (node.right,node.left); visit(near)
            if diff*diff<best[0]:visit(far)
        visit(self.root); return best[1],best[0]**.5
