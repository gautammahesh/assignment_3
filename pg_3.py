import logging

logging.basicConfig(filename='error_log.txt',filemode = 'w', level=logging.ERROR, format='%(levelname)s - %(message)s')
class ResaleData:
    def __init__(self, month, town, flat_type, block, street_name, storey_range, floor_area_sqm, flat_model, lease_commence_date, remaining_lease, resale_price):
        self.__month = month
        self.__town = town
        self.__flat_type = flat_type
        self.__block = block
        self.__street_name = street_name
        self.__storey_range = storey_range
        # self.__floor_area_sqm = floor_area_sqm
        self.__flat_model = flat_model
        self.__lease_commence_date = lease_commence_date
        self.__remaining_lease = remaining_lease
        
        # self.__resale_price = resale_price
        try:
            self.__floor_area_sqm = float(floor_area_sqm)
            self.__resale_price = float(resale_price)
            if self.__floor_area_sqm < 0 or self.__resale_price < 0:
                raise ValueError("Negative Value")
            self.__iserror = False
        except ValueError:
            self.__iserror = True
            error_message = f"Invalid data: {month} || {town} || {flat_type} || {block} || {street_name} || {storey_range} || {floor_area_sqm} || {flat_model} || {lease_commence_date} || {remaining_lease} || {resale_price}"
            # self.log_error(error_message)
            logging.error(error_message)
            

            



    def get_town(self):
        return self.__town
    
    def get_flat_type(self):
        return self.__flat_type
    
    def get_flat_model(self):
        return self.__flat_model
    
    def is_error(self):
        return self.__iserror
    
    # def log_error(self, message):
    #     with open('error_log.txt', 'a') as log_file:
    #         log_file.write(message + '\n')
            

    def display(self):
        return (f"{self.__month}, {self.__town}, {self.__flat_type}, {self.__block}, {self.__street_name}, {self.__storey_range}, {self.__floor_area_sqm}, {self.__flat_model}, {self.__lease_commence_date}, {self.__remaining_lease}, {self.__resale_price}")
    
def read_resale_data(datafile):
    transactions = []
    with open(datafile, 'r') as file:
        lines = file.readlines()
        # for line in lines:
        for index, line in enumerate(lines):
            if index == 0:  # Skip the first line (headers)
                continue
            month, town, flat_type, block, street_name, storey_range, floor_area_sqm, flat_model, lease_commence_date, remaining_lease, resale_price = line.strip().split(',')
            resale_data = ResaleData(month, town, flat_type, block, street_name, storey_range, floor_area_sqm, flat_model, lease_commence_date, remaining_lease, resale_price)    # new
            if not resale_data.is_error():
                transactions.append(resale_data)

        return transactions
    

def get_town(transactions):
    town_set = set()
    for transaction in transactions:
        # print(hdbflat.get_town())
        town_set.add(transaction.get_town())
    return town_set
    
def get_flat_type(transactions):
    flat_type_set = set()
    for transaction in transactions:
        flat_type_set.add(transaction.get_flat_type())
    return flat_type_set

def get_flat_model(transactions):
    flat_model_set = set()
    for transaction in transactions:
        flat_model_set.add(transaction.get_flat_model())
    return flat_model_set

def search(transactions):
    search_list = []
    temp_list = []
    town_search = input("Enter town name (not mandatory): ").strip().upper()
    flat_type_search = input("Enter flat type (not mandatory): ").strip().upper()
    flat_model_search = input("Enter flat model (not mandatory): ").strip().upper()
    print("<-->", town_search, "<-->", flat_type_search, "<-->", flat_model_search, "<-->")

    #ResaleData resaleData;
    if town_search != "":
        for resaleData in transactions:
            if resaleData.get_town() == town_search:
                search_list.append(resaleData)
        temp_list = search_list
        # search_list = None
        search_list = []

    if flat_type_search != "":
        for resaleData in temp_list:
            if resaleData.get_flat_type() == flat_type_search:
                search_list.append(resaleData)

        temp_list = search_list # check this out
        search_list = []

    if flat_model_search != "":
        for resaleData in temp_list:
            # print("inside flat model")
            if resaleData.get_flat_model() == flat_model_search:
                # print("inside flat model: INSIDE IF ")
                search_list.append(resaleData)

        print(len(search_list))
        temp_list = search_list # check this out
        # search_list = []

    if len(search_list) == 0:
        search_list = temp_list

    if len(search_list) == 0:
        # search_list = temp_list
        print("NO DATA FOUND FOR THE SEARCH PROVIDED")


    for resaleData in search_list:
        print(resaleData.display())


def main():
    datafile = "Resale2024.csv"
    transactions = read_resale_data(datafile)
    # for transaction in transactions:
    #     print(transaction.display())
    
    town_set = get_town(transactions)
    print(town_set,"\n")

    flat_type_set = get_flat_type(transactions)
    print(flat_type_set,"\n")

    flat_model_set = get_flat_model(transactions)
    print(flat_model_set)

    search(transactions)


main()