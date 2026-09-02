import sys
from pathlib import Path
import numpy as np
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from src.knn_regressor import euclidean_distance,mahalanobis_distance
from src.locally_weighted_regression import gaussian_kernel
from src.candidate_elimination import CandidateElimination
from src.kdtree import KDTreeScratch
def test_euclidean(): assert euclidean_distance(np.array([0,0]),np.array([3,4]))==5.0
def test_mahalanobis_zero(): assert mahalanobis_distance(np.array([1.,2.]),np.array([1.,2.]),np.eye(2))==0.0
def test_kernel_at_zero(): assert abs(gaussian_kernel(0.,1.)-1.)<1e-12
def test_candidate_elimination_positive(): assert CandidateElimination([['Low','High'],['Low','High']]).update(('High','Low'),'High')[0]==['High','Low']
def test_kdtree_exact_nearest():
    idx,_=KDTreeScratch(np.array([[0.,0.],[3.,4.],[1.,1.]])).query(np.array([.2,.1])); assert idx==0
