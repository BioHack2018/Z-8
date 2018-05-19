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
    