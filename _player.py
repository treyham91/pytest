# -*- coding: utf-8 -*-
"""
Created on Mon Apr  2 12:15:22 2018

@author: treyh
"""

class Player:
    
    def __init__(self, name, age, owgr, fedex_rank, years_pro):
        self.name = name
        self.age = age
        self.owgr = owgr
        self.fedex_rank = fedex_rank
        self.years_pro = years_pro
        
    def playerNameAndRank(self):
        print('{} is currently ranked {} in the world, and {} in the Fedex Cup Standings'
              .format(self.name, self.owgr, self.fedex_rank))
        
    def ageTurnedPro(self):
        self.age_turned_pro = self.age - self.years_pro
        print('{} was {} years old when he turned pro'.format(self.name, self.age_turned_pro))
        
    def avgDrive(self):
        self.avg_drive = self.drive_total / self.number_of_drives
        print('{} average drive this year is {}'.format(self.name, self.avg_drive))
        
    def plotPlayerRanking(self):
        x = self.owgr
        y = self.years_pro
        fig, ax = plt.subplots()
        ax.plot(x, y)
        ax.set_title('Ranking vs Years Pro')
    


player = Player('Rickie Fowler', 29, 8, 15, 9)
player.playerNameAndRank()
player.ageTurnedPro()
player.plotPlayerRanking()
        

        
    
