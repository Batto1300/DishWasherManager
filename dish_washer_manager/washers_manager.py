import itertools
import os


class washers_manager:
    def __init__(self,names,check):
        self.names = names
        self.groups = self.generate_groups(check)
        self.today_group = []

    def get_washer(self):
        self._read_absentees()
        today_washer = self._read_washer()
        self._update_washers(today_washer)
        return today_washer

    def _read_absentees(self):
        with open('dish_washer_manager/todays_absentees.txt','r') as f:
            for line in f:
                self.today_group = sorted(set(self.names) - set([line]))
        
    def _read_washer(self):
        today_washer_file = "_".join(self.today_group)
        with open('dish_washer_manager/groups/'+(today_washer_file),'r') as f:
            return f.readline()[:-1]

    def _update_washers(self,washer):
        laze_ppl = set(self.today_group) - set([washer])
        with open("dish_washer_manager/groups/" + "_".join(self.today_group),'w') as f:
            for dude in laze_ppl:
                f.write(str(dude) + "\n")
            f.write(washer + "\n")
            

    def generate_groups(self,check):
        groups = []
        for length in range(2, len(self.names)+1):
            for subset in itertools.combinations(self.names, length):
                groups.append(subset)
                if check == "create":
                    with open("dish_washer_manager/groups/"+"_".join(sorted(subset)), "w") as f:
                        for name in subset:
                            f.write(name + "\n")
        return sorted(groups)