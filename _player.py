import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import RoundsvsAvgDrives_LinReg  as lin_reg


class Player:
    
    def __init__(self, name, age, owgr, fedex_rank, years_pro):
        self.name = name
        self.age = age
        self.owgr = owgr
        self.fedex_rank = fedex_rank
        self.years_pro = years_pro
        
    def player_name_and_rank(self):
        return self.name, self.owgr
        
    def age_turned_pro(self):
        age_turned_pro = self.age - self.years_pro
        return age_turned_pro
        
    def avg_drive(self, drive_total, number_of_drives):
        drive_avg = drive_total / number_of_drives
        return drive_avg


def main():

    regression = lin_reg.LinRegression('AvgDrives.csv')
    regression.import_and_split_data(4, 5, 3)
    regression.find_set_shape()
    regression.fit_test_and_predict_results()
    regression.plot_results('Driving Averages', 'Driving Totals', 'Average Drive')

    # player = Player('Rickie Fowler', 29, 8, 15, 9)
    # player.player_name_and_rank()
    # player.age_turned_pro()
    # player.avg_drive(30000, 72)
    # player.plot_player_ranking()


if __name__ == "__main__":
    main()
