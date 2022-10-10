# -*- coding: utf-8 -*-
import numpy as np
import sys
import os
from cobaya.likelihood import Likelihood


class UnionLike(Likelihood):
    def initialize(self):
        self.z, self.mu = np.loadtxt(self.dataset_file, usecols=[1, 2], unpack=True)
        self.invcov = np.loadtxt(self.cov_file)
    
    def get_requirements(self):
        return {'angular_diameter_distance': {"z": self.z}}

    def logp(self, **params_values):
        DA = self.provider.get_angular_diameter_distance(self.z)
        dL = (1+self.z)*(1+self.z)*DA
        mu = 5*np.log10(dL) + 25.
        delta = self.mu - mu 
        return -0.5*delta.dot(self.invcov).dot(delta.T)