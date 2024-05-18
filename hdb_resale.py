import logging

class Hdbflat:
    def __init__(self):
        self.__month = None
        self.__town = None
        self.__flat_type = None
        self.__block = None
        self.__street_name = None
        self.__storey_range = None
        self.__floor_area_sqm = None
        self.__flat_model = None
        self.__lease_commence_date = None
        self.__remaining_lease = None
        self.__resale_price = None

    # Getters and setters for each attribute
    def get_month(self):
        return self.__month
    
    def set_month(self, new_month):
        self.__month = new_month

    def get_town(self):
        return self.__town
    
    def set_town(self, new_town):
        self.__town = new_town

    def get_flat_type(self):
        return self.__flat_type
    
    def set_flat_type(self, new_flat_type):
        self.__flat_type = new_flat_type

    def get_block(self):
        return self.__block
    
    def set_block(self, new_block):
        self.__block = new_block

    def get_street_name(self):
        return self.__street_name
    
    def set_street_name(self, new_street_name):
        self.__street_name = new_street_name

    def get_storey_range(self):
        return self.__storey_range
    
    def set_storey_range(self, new_storey_range):
        self.__storey_range = new_storey_range

    def get_floor_area_sqm(self):
        return self.__floor_area_sqm
    
    def set_floor_area_sqm(self, new_floor_area_sqm):
        self.__floor_area_sqm = float(new_floor_area_sqm)

    def get_flat_model(self):
        return self.__flat_model
    
    def set_flat_model(self, new_flat_model):
        self.__flat_model = new_flat_model

    def get_lease_commence_date(self):
        return self.__lease_commence_date
    
    def set_lease_commence_date(self, new_lease_commence_date):
        self.__lease_commence_date = int(new_lease_commence_date)

    def get_remaining_lease(self):
        return self.__remaining_lease
    
    def set_remaining_lease(self, new_remaining_lease):
        self.__remaining_lease = new_remaining_lease

    def get_resale_price(self):
        return self.__resale_price
    
    def set_resale_price(self, new_resale_price):
        self.__resale_price = new_resale_price

    def set_floor_area_sqm(self, new_floor_area_sqm):
        try:
            self.__floor_area_sqm = float(new_floor_area_sqm)
        except ValueError:
            # Handle cases where the input cannot be converted to a float
            # For example, you could assign a default value or skip the data
            self.__floor_area_sqm = None  # Assigning None for problematic data

# Function to read CSV file and create Hdbflat instances
def read_csv(filename):
    hdbflats_list = []
    with open(filename, 'r') as file:
        next(file)  # Skip header row
        for line in file:
            fields = line.strip().split(',')
            hdbflat = Hdbflat()
            hdbflat.set_month(fields[0])
            hdbflat.set_town(fields[1])
            hdbflat.set_flat_type(fields[2])
            hdbflat.set_block(fields[3])
            hdbflat.set_street_name(fields[4])
            hdbflat.set_storey_range(fields[5])
            hdbflat.set_floor_area_sqm(fields[6])
            hdbflat.set_flat_model(fields[7])
            hdbflat.set_lease_commence_date(fields[8])
            hdbflat.set_remaining_lease(fields[9])
            hdbflat.set_resale_price(fields[10])

            # if hdbflat.get_floor_area_sqm() == float(hdbflat.get_floor_area_sqm()):
            
            hdbflats_list.append(hdbflat)
            
    return hdbflats_list

def get_town( hdbflats_list):
    town_set = set()
    for hdbflat in hdbflats_list:
        # print(hdbflat.get_town())
        town_set.add(hdbflat.get_town())
    return town_set

def get_flat_type( hdbflats_list):
    flat_type_set = set()
    for hdbflat in hdbflats_list:
        flat_type_set.add(hdbflat.get_flat_type())
    return flat_type_set

def get_flat_model( hdbflats_list):
    flat_model_set = set()
    for hdbflat in hdbflats_list:
        flat_model_set.add(hdbflat.get_flat_model())
    return flat_model_set

def main():
    # Example usage:
    filename = "Resale2024.csv"
    hdbflats_list = read_csv(filename)
    # for hdbflat in hdbflats:
        # print(hdbflat.get_town(), hdbflat.get_resale_price())

    town_set = get_town(hdbflats_list)
    print(town_set,"\n")
    # for town in town_set:
    #     print(town)


    flat_type_set = get_flat_type(hdbflats_list)
    print(flat_type_set,"\n")

    flat_model_set = get_flat_model(hdbflats_list)
    print(flat_model_set)

main()
