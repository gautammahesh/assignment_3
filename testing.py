import logging

logging.basicConfig(filename='error_log.txt',filemode = 'w', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Custom exception class for handling resale data related errors
class ResaleDataException(Exception):
    pass

# ResaleData Class representing a resale data record
class ResaleData:
    # Initializing all instance variables
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
            # Converting floor area and resale price to float and checking for negative values
            self.__floor_area_sqm = float(floor_area_sqm)
            self.__resale_price = float(resale_price)
            if self.__floor_area_sqm < 0 or self.__resale_price < 0:
                raise ValueError("Negative Value")
            self.set_error_flag(False)
        except ValueError as e:  
            # Set error flag and log the error if value conversion fails or negative values are found
            self.set_error_flag(True)
            logging.error("Value error %s ", str(e))
            self.__error_message = f"Invalid data : {month} || {town} || {flat_type} || {block} || {street_name} || {storey_range} || {floor_area_sqm} || {flat_model} || {lease_commence_date} || {remaining_lease} || {resale_price}"
        
    # Method to set error flag
    def set_error_flag(self, value):
        self.__error_flag = value

    # Method to get error flag
    def get_error_flag(self):
        return self.__error_flag        

    # Method to get town
    def get_town(self):
        return self.__town
    
    # Method to get flat type
    def get_flat_type(self):
        return self.__flat_type
    
    # Method to get flat model
    def get_flat_model(self):
        return self.__flat_model
 
    # Method to get error message
    def get_error_message(self):
        return self.__error_message
    
    # String representation of the ResaleData class
    def __str__(self):
        return (f"{self.__month}, {self.__town}, {self.__flat_type}, {self.__block}, {self.__street_name}, {self.__storey_range}, {self.__floor_area_sqm}, {self.__flat_model}, {self.__lease_commence_date}, {self.__remaining_lease}, {self.__resale_price}")
    
# ResaleDataManager Class manages resale data operations
class ResaleDataManager: 

    # Method to read resale data from a file
    def read_resale_data(self, datafile):
        try:
            transactions = []
            with open(datafile, 'r') as file:
                lines = file.readlines()
                # for line in lines:
                for index, line in enumerate(lines):
                    if index == 0: 
                        continue
                    month, town, flat_type, block, street_name, storey_range, floor_area_sqm, flat_model, lease_commence_date, remaining_lease, resale_price = line.strip().split(',')

                    # Creating ResaleData object and adding it to transactions list
                    resale_data = ResaleData(month, town, flat_type, block, street_name, storey_range, floor_area_sqm, flat_model, lease_commence_date, remaining_lease, resale_price)    # new
                    transactions.append(resale_data)

                return transactions
        except Exception as e:
            print("An unexpected error occurred:", str(e))

    # Method to write error records to a file
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

    # Method to get all distinct towns 
    def get_town(self, transactions):
        town_set = set()
        for transaction in transactions:
            town_set.add(transaction.get_town())
        return town_set
        
    # Method to get all distinct flat types 
    def get_flat_type(self, transactions):
        flat_type_set = set()
        for transaction in transactions:
            flat_type_set.add(transaction.get_flat_type())
        return flat_type_set

    # Method to get all distinct flat models 
    def get_flat_model(self, transactions):
        flat_model_set = set()
        for transaction in transactions:
            flat_model_set.add(transaction.get_flat_model())
        return flat_model_set

    # Method to search for transactions based on user input
    def search(self, transactions):
        search_list = []
        town_list=[]
        flat_type_list=[]
        flat_model_list=[]
        town_search = input("Enter town name (not mandatory): ").strip().upper()
        flat_type_search = input("Enter flat type (not mandatory): ").strip().upper()
        flat_model_search = input("Enter flat model (not mandatory): ").strip().upper()
        isTownFound = False
        isFlatTypeFound = False
        isFlatModelFound = False 
        searchResult=""

        # Search by town
        if town_search:
            town_search_array = town_search.split(",")
            for i in range(len(town_search_array)):
                town_search_array[i] = town_search_array[i].strip()
            for resaleData in transactions:
                if resaleData.get_town() in town_search_array:
                    town_list.append(resaleData)
                    isTownFound= True
            if not  town_list:
                 searchResult= f"Town search input: {town_search_array} does not match the data \n"
            search_list.extend(town_list)
        else:
             isTownFound= True 
        
        # Search by flat type
        if flat_type_search:
            flat_type_search_array = flat_type_search.split(",")
            for i in range(len(flat_type_search_array)):
                flat_type_search_array[i] = flat_type_search_array[i].strip()
            for resaleData in search_list:
                if resaleData.get_flat_type() in flat_type_search_array:
                    flat_type_list.append(resaleData)
                    isFlatTypeFound= True 
            if not  flat_type_list:
                searchResult += f"Flat Type search input: {flat_type_search_array} does not match the data \n"
            else: 
                search_list = flat_type_list
        else:
            isFlatTypeFound= True 
        
        # Search by flat model
        if flat_model_search:
            flat_model_search_array = flat_model_search.split(",")
            for i in range(len(flat_model_search_array)):
                flat_model_search_array[i] = flat_model_search_array[i].strip()
            for resaleData in search_list:
                if resaleData.get_flat_model() in flat_model_search_array:
                    flat_model_list.append(resaleData)
                    isFlatModelFound = True 
            if not  flat_model_list:
                searchResult += f"Flat Model search input: {flat_model_search_array} does not match the data \n"
            else:
                search_list = flat_model_list
        else:
            isFlatModelFound= True 

        # Handling no search result
        if not search_list:
            if (not isTownFound) or (not isFlatTypeFound) or (not isFlatModelFound):
                raise ResaleDataException(searchResult)
            raise ResaleDataException("NO DATA FOUND FOR THE SEARCH PROVIDED")
        
        if (not isTownFound) or (not isFlatTypeFound) or (not isFlatModelFound):
            raise ResaleDataException(searchResult)

        for resaleData in search_list:
            print(resaleData.__str__())

def main():
    try:
        datafile = "Resale2024.csv"
        manager = ResaleDataManager()
        transactions = manager.read_resale_data(datafile)
        
        # Display the main menu
        while True:
            print("")
            print("Main Menu:")
            print("1. Get towns")
            print("2. Get floor type")
            print("3. Get floor model")
            print("4. Search")
            print("5. Exit program")

            # Getting user input
            options = int(input("Enter option (1-5): "))
            print("")

            # Execute actions based on user option
            if options == 1:
                print("Towns: ")
                town_set = manager.get_town(transactions)
                print(town_set)
            elif options == 2:
                print("Flat types: ")
                flat_type_set = manager.get_flat_type(transactions)
                print(flat_type_set)
            elif options == 3:
                print("Flat models: ")
                flat_model_set = manager.get_flat_model(transactions)
                print(flat_model_set)
            elif options == 4:
                try:
                    manager.search(transactions)
                    manager.write_error_records(transactions)
                except Exception as e:
                    print(e)
            elif options == 5:
                print("Thank You")
                break
            else:
                print("Invalid input. Please try again: ")
                
    except Exception as e:
        logging.error("Unexpected error %s", str(e))
        print("An unexpected error occurred:", e )

main()
 
