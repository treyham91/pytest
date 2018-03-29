# -*- coding: utf-8 -*-
"""
Created on Sun Mar 25 23:40:49 2018

@author: treyh
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import time

machines = {'Ext': ['EXT001','EXT002','EXT003','EXT004','EXT005',
                    'EXT006','EXT007','EXT008','EXT009','EXT010',],
            'Mixer': ['MIX001','MIX002','MIX003'],
            'Rec': ['REC001','REC002','REC003','REC004','REC005',
                    'REC006','REC007','REC008','REC009','REC010',],
            'Strt': ['STRT001','STRT002','STRT003']}

locations = {'Bay': ['BAY01','BAY02','BAY03','BAY04','BAY05'],
             'Lane': ['LN001','LN002','LN003','LN004','LN005',
                      'LN006','LN007','LN008','LN009','LN010'],
             'Org': ['Apple Valley','Annex','Lakeville','Hutchinson']}

class Extruder:
    
    def __init__(self, name, location):
        self.name = name
        self.location = location
        
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value):
        
        if value.isalpha():
            
            self.__name = value
            
        else:
            print("Please enter a valid value")
        
    def running(self, status):
        self.__status = status
        
        if status == 1:
            print("Extruder is currently running")
            # record data and set timer for every 60 seconds
            
        elif status == 2:
            print("Extruder is currently retired")
            
        else:
            print("Extruder is not available for scheduling")
            
    def openLogFile(self, file):
        self.file = file
        file = open("{}_log.txt".format(self.name),"w")
        while file.write == True:
            if self.__status == 1:
                file.write("You opened the file!")
                # TODO: Other stuff...
                file.close()
                
class Mixer:
    
    def __init__(self, name, location):
        self.name = name
        self.location = location
        
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value):
        
        if value.isalpha():
            
            self.__name = value
            
        else:
            print("Please enter a valid value")
        
    def running(self, status):
        self.__status = status
        
        if status == 1:
            print("Mixer is currently running")
            # record data and set timer for every 60 seconds
            
        elif status == 2:
            print("Mixer is currently retired")
            
        else:
            print("Mixer is not available for scheduling")
            
    def openLogFile(self, file):
        self.__file = file
        file = open("{}_log.txt".format(self.name),"w")
        while file.write == True:
            if self.__status == 1:
                file.write("You opened the file!")
                # TODO: Other stuff...
                file.close()
        
def main():
    
    ext = Extruder(machines['Ext'][0], locations['Bay'][0] + ' ' +locations['Org'][0] + ' ' + locations['Lane'][0])
    
    ext.running(status=1)
    ext.openLogFile("{}_log.txt".format(machines['Ext'][0]))
    
    mix = Mixer(machines['Mixer'][0], locations['Bay'][1] + ' ' +locations['Org'][0] + ' ' + locations['Lane'][9])
    
    mix.running(status=1)
    mix.openLogFile("{}_log.txt".format(machines['Mixer'][0]))
    
    
        
        