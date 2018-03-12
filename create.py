import dish_washer_manager.washers_manager as manager

class Initializer:
    @staticmethod
    def initialize():
        manager.washers_manager(['Tommaso','Matteo','Michele'],'create')
