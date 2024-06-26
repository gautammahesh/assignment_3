# import logging

# logging.basicConfig(filename='error_log.txt',filemode = 'w', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


class ResaleData:
    def __init__(self, month, town, flat_type, block, street_name, storey_range, floor_area_sqm, flat_model, lease_commence_date, remaining_lease, resale_price):
        self.__month = month
        self.__town = town
        self.__flat_type = flat_type
        self.__block = block
        self.__street_name = street_name
        self.__storey_range = storey_range
        self.__floor_area_sqm = floor_area_sqm
        self.__flat_model = flat_model
        self.__lease_commence_date = lease_commence_date
        self.__remaining_lease = remaining_lease
        self.__error_flag = False
        self.__error_message=""

        self.__resale_price = resale_price
        try:
            self.__floor_area_sqm = float(floor_area_sqm)
            self.__resale_price = float(resale_price)
            if self.__floor_area_sqm < 0 or self.__resale_price < 0:
                # logging.info("Exception Caught for checking negative value")
                raise ValueError("Negative Value")
            self.set_error_flag(False)
        except ValueError as e:  
            self.set_error_flag(True)
            #print("An exception occurred:", str(e))
            # logging.error("Value error %s ", str(e))
            self.__error_message = f"Invalid data : {month} || {town} || {flat_type} || {block} || {street_name} || {storey_range} || {floor_area_sqm} || {flat_model} || {lease_commence_date} || {remaining_lease} || {resale_price}"
        
        
    def set_error_flag(self, value):
        self.__error_flag = value

    def get_error_flag(self):
        return self.__error_flag        

    def get_town(self):
        return self.__town
    
    def get_flat_type(self):
        return self.__flat_type
    
    def get_flat_model(self):
        return self.__flat_model
 
    def get_error_message(self):
        return self.__error_message
    
   
    def display(self):
        return (f"{self.__month}, {self.__town}, {self.__flat_type}, {self.__block}, {self.__street_name}, {self.__storey_range}, {self.__floor_area_sqm}, {self.__flat_model}, {self.__lease_commence_date}, {self.__remaining_lease}, {self.__resale_price}")
    
class ResaleDataManager: 

    def read_resale_data(self, datafile):
        try:
            transactions = []
            with open(datafile, 'r') as file:
                lines = file.readlines()
                # for line in lines:
                for index, line in enumerate(lines):
                    if index == 0:  # Skip the first line (headers)
                        continue
                    month, town, flat_type, block, street_name, storey_range, floor_area_sqm, flat_model, lease_commence_date, remaining_lease, resale_price = line.strip().split(',')
                    resale_data = ResaleData(month, town, flat_type, block, street_name, storey_range, floor_area_sqm, flat_model, lease_commence_date, remaining_lease, resale_price)    # new
                    #if not resale_data.get_error_flag():
                    transactions.append(resale_data)

                return transactions
        except Exception as e:
            print("An unexpected error occurred:", str(e))


    def write_error_records(self, transactions):
        try:
            with open("ResaleData.error.txt", "w") as error_file:
                for transaction in transactions:
                    if transaction.get_error_flag() == True:
                        error_file.write(transaction.get_error_message() + '\n')
        except FileNotFoundError as fnfe:
            print("File not found.")
            return fnfe
        except IOError as ioe:
            print("Error reading the file.")
            return ioe


    def get_town(self, transactions):
        town_set = set()
        for transaction in transactions:
            # print(hdbflat.get_town())
            town_set.add(transaction.get_town())
        return town_set
        
    def get_flat_type(self, transactions):
        flat_type_set = set()
        for transaction in transactions:
            flat_type_set.add(transaction.get_flat_type())
        return flat_type_set

    def get_flat_model(self, transactions):
        flat_model_set = set()
        for transaction in transactions:
            flat_model_set.add(transaction.get_flat_model())
        return flat_model_set

    def search(self, transactions):
        search_list = []
        temp_list = []
        town_search = input("Enter town name (not mandatory): ").strip().upper()
        if town_search is not empty
            town_search_array=town_search.split(",")
        #bishan
        #bishan, Yishun
        flat_type_search = input("Enter flat type (not mandatory): ").strip().upper()
        flat_model_search = input("Enter flat model (not mandatory): ").strip().upper()
        #print("<-->", town_search, "<-->", flat_type_search, "<-->", flat_model_search, "<-->")

        #ResaleData resaleData;
        if town_search != "":
            for resaleData in transactions:
                # if town_search_array.index(resaleData.get_town()) >=0:
                #     print("Got it")
                for town in town_search_array:
                    if resaleData.get_town() == town:
                        search_list.append(resaleData)
            
            if search_list is null
                raise Exception
                
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

            # print(len(search_list))
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
    try:
        datafile = "Resale2024.csv"
        manager = ResaleDataManager()
        transactions = manager.read_resale_data(datafile)
        
        while True:
            print("Main Menu:")
            print("1. Get towns")
            print("2. Get floor type")
            print("3. Get floor model")
            print("4. Search")
            print("5. Exit program")

            options = int(input("Enter option (1-5):"))
            if options == 1:
                town_set = manager.get_town(transactions)
                print(town_set,"\n")
            elif options == 2:
                flat_type_set = manager.get_flat_type(transactions)
                print(flat_type_set,"\n")
            elif options == 3:
                flat_model_set = manager.get_flat_model(transactions)
                print(flat_model_set)
            elif options == 4:
                manager.search(transactions)
                manager.write_error_records(transactions)
            elif options == 5:
                print("Thank You")
                break
                
    except Exception as e:
        # logging.error("Unexpected error %s", str(e))
        print("An unexpected error occurred:", str(e))

        # datafile = "Resale2024.csv"
        # manager = ResaleDataManager()
        # transactions = manager.read_resale_data(datafile)
        
       
        # # for transaction in transactions:
        # #     print(transaction.display())
        
        # print("")
        # town_set = manager.get_town(transactions)
        # print(town_set,"\n")

        # flat_type_set = manager.get_flat_type(transactions)
        # print(flat_type_set,"\n")

        # flat_model_set = manager.get_flat_model(transactions)
        # print(flat_model_set)

        # manager.search(transactions)

        # manager.write_error_records(transactions)
    # except Exception as e:
    #     # logging.error("Unexpected error %s", str(e))
    #     print("An unexpected error occurred:", str(e))


main()
