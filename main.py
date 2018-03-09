import dish_washer_manager.washers_manager as manager

def main():
    washer_manager = manager.washers_manager(['Tommaso','Matteo','Michele'])
    washer_manager.get_washer()



if __name__ == "__main__":
    main()
