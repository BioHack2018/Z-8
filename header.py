#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 19 16:28:54 2018

@author: staskowiak
"""

class Region_with_SD():
    
    def __init__(self, sequence, sd_pos):
        self.sd_pos = sd_pos
        self.sequence = sequence

    def get_sequence(self):
        return self.sequence
    
    def get_position(self):
        return self.sd_pos
    

class Gene():
    
    def __init__(self, name, sequence, start, stop):
        self.sequence = sequence
        self.name = name
        self.start = start
        self.stop = stop
        
    def get_sequence(self):
        return self.sequence
    
    def get_name(self):
        return self.name
    
    def get_start(self):
        return self.start
    
    def get_stop(self):
        return self.stop
    
    
    
    
    
    