import dish_washer_manager.washers_manager as manager

class Updater:
    @staticmethod
    def update_and_print():
        washer_manager = manager.washers_manager(['Tommaso','Matteo','Michele'],'update')
        print(washer_manager.get_washer())

