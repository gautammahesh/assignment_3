import logging

logging.basicConfig(filename='error_log.txt', filemode='w', level=logging.ERROR, format='%(levelname)s - %(message)s')

class ResaleData:
    def __init__(self, datafile=None, month=None, town=None, flat_type=None, block=None, street_name=None, storey_range=None, floor_area_sqm=None, flat_model=None, lease_commence_date=None, remaining_lease=None, resale_price=None):
        self.transactions = []
        if datafile:
            self.read_resale_data(datafile)
        else:
            self.__month = month
            self.__town = town
            self.__flat_type = flat_type
            self.__block = block
            self.__street_name = street_name
            self.__storey_range = storey_range
            self.__flat_model = flat_model
            self.__lease_commence_date = lease_commence_date
            self.__remaining_lease = remaining_lease

            try:
                self.__floor_area_sqm = float(floor_area_sqm)
                self.__resale_price = float(resale_price)
                if self.__floor_area_sqm < 0 or self.__resale_price < 0:
                    raise ValueError("Negative Value")
                self.__iserror = False
            except ValueError:
                self.__iserror = True
                error_message = f"Invalid data: {month} || {town} || {flat_type} || {block} || {street_name} || {storey_range} || {floor_area_sqm} || {flat_model} || {lease_commence_date} || {remaining_lease} || {resale_price}"
                logging.error(error_message)

    def read_resale_data(self, datafile):
        with open(datafile, 'r') as file:
            lines = file.readlines()
            for index, line in enumerate(lines):
                if index == 0:  # Skip the first line (headers)
                    continue
                data = line.strip().split(',')
                resale_data = ResaleData(month=data[0], town=data[1], flat_type=data[2], block=data[3], street_name=data[4], storey_range=data[5], floor_area_sqm=data[6], flat_model=data[7], lease_commence_date=data[8], remaining_lease=data[9], resale_price=data[10])
                if not resale_data.is_error():
                    self.transactions.append(resale_data)

    def get_town(self):
        return self.__town
    
    def get_flat_type(self):
        return self.__flat_type
    
    def get_flat_model(self):
        return self.__flat_model
    
    def is_error(self):
        return self.__iserror
    
    def display(self):
        return (f"{self.__month}, {self.__town}, {self.__flat_type}, {self.__block}, {self.__street_name}, {self.__storey_range}, {self.__floor_area_sqm}, {self.__flat_model}, {self.__lease_commence_date}, {self.__remaining_lease}, {self.__resale_price}")

    def get_unique_values(self, attribute):
        unique_values = set()
        for transaction in self.transactions:
            unique_values.add(getattr(transaction, attribute)())
        return unique_values

    def search(self):
        search_list = []
        temp_list = []
        town_search = input("Enter town name (not mandatory): ").strip().upper()
        flat_type_search = input("Enter flat type (not mandatory): ").strip().upper()
        flat_model_search = input("Enter flat model (not mandatory): ").strip().upper()
        print("<-->", town_search, "<-->", flat_type_search, "<-->", flat_model_search, "<-->")

        if town_search != "":
            for resaleData in self.transactions:
                if resaleData.get_town() == town_search:
                    search_list.append(resaleData)
            temp_list = search_list
            search_list = []

        if flat_type_search != "":
            for resaleData in temp_list:
                if resaleData.get_flat_type() == flat_type_search:
                    search_list.append(resaleData)
            temp_list = search_list
            search_list = []

        if flat_model_search != "":
            for resaleData in temp_list:
                if resaleData.get_flat_model() == flat_model_search:
                    search_list.append(resaleData)
            print(len(search_list))
            temp_list = search_list

        if len(search_list) == 0:
            search_list = temp_list

        if len(search_list) == 0:
            print("NO DATA FOUND FOR THE SEARCH PROVIDED")

        for resaleData in search_list:
            print(resaleData.display())

def main():
    datafile = "Resale2024.csv"
    resale = ResaleData(datafile)
    
    town_set = resale.get_unique_values('get_town')
    print(town_set, "\n")

    flat_type_set = resale.get_unique_values('get_flat_type')
    print(flat_type_set, "\n")

    flat_model_set = resale.get_unique_values('get_flat_model')
    print(flat_model_set)

    resale.search()

main()
