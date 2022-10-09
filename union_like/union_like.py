# -*- coding: utf-8 -*-
import numpy as np
import sys
import os
from cobaya.likelihood import Likelihood


class UnionLike(Likelihood):
    def initialize(self):
        PATH = "/Users/pablo/Code/Cosmo/Union_cobaya/union_like"
        self.z, self.mu = np.loadtxt(os.path.join(PATH, "union_data/sn_z_mu_dmu_plow_union2.1.txt"), usecols=[1, 2], unpack=True)
        self.invcov = np.loadtxt(os.path.join(PATH, "union_data/sn_wmat_nosys_union2.1.txt"))
        #self.invcov = np.linalg.inv(cov)
    
    def get_requirements(self):
        return {'angular_diameter_distance': {"z": self.z}}

    def logp(self, **params_values):
        DA = self.provider.get_angular_diameter_distance(self.z)
        dL = (1+self.z)*(1+self.z)*DA
        mu = 5*np.log10(dL) + 25.
        delta = self.mu - mu 
        #print(delta[:5])
        #print(self.invcov[:5, :5])
        return -0.5*delta.dot(self.invcov).dot(delta.T)