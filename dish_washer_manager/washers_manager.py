import itertools
import os


class washers_manager:
    def __init__(self,names):
        self.names = names
        self.groups = self._generate_groups()
        self.today_group = None

    def get_washer(self):
        absentees = self._read_absentees()
        self._calculate_washer(absentees)       

    def _read_absentees(self):
        with open('todays_absentees.txt','r') as f:
            for line in f:
                self.today_group = list(set(self.names) - set(line))
        
    def _calculate_washer(self,absentees):
        pass

    def _generate_groups(self):
        groups = []
        for length in range(2, len(self.names)+1):
            for subset in itertools.combinations(self.names, length):
                open("_".join(subset), "w").close()
                groups.append(subset)
        return groups