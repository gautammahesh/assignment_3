import logging

logging.basicConfig(filename='error_log.txt',filemode = 'w', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# rise exception when towns are not matching
# pass two or more towns in search
# commands to be included
# grandfather execpetion

class ResaleDataException(Exception):
    pass

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
                raise ValueError("Negative Value")
            self.set_error_flag(False)
        except ValueError as e:  
            self.set_error_flag(True)
            logging.error("Value error %s ", str(e))
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
 
        if town_search:
            town_search_array = town_search.split(",")
            # print(" search len(town_search_array) :::: ",len(town_search_array))
            for i in range(len(town_search_array)):
                town_search_array[i] = town_search_array[i].strip()
            for resaleData in transactions:
                if resaleData.get_town() in town_search_array:
                    town_list.append(resaleData)
                    isTownFound= True

            if not  town_list:
                 searchResult= f"Town search not matching with the input passed {town_search_array}\n"

            search_list.extend(town_list)
        else:
             isTownFound= True 
        
        if flat_type_search:
            flat_type_search_array = flat_type_search.split(",")
 
            for i in range(len(flat_type_search_array)):
                flat_type_search_array[i] = flat_type_search_array[i].strip()
            for resaleData in search_list:
                if resaleData.get_flat_type() in flat_type_search_array:
                    flat_type_list.append(resaleData)
                    isFlatTypeFound= True 
            if not  flat_type_list:
                 searchResult+= f"Flat Type search not matching with the input passed {flat_type_search_array}\n"
            else: 
                search_list = flat_type_list
        else:
            isFlatTypeFound= True 
        
        if flat_model_search:
            flat_model_search_array = flat_model_search.split(",")
            # print(" search len(flat_model_search_array) :::: ",len(flat_model_search_array),"<----->" ,flat_model_search_array)

            for i in range(len(flat_model_search_array)):
                flat_model_search_array[i] = flat_model_search_array[i].strip()

            for resaleData in search_list:
                if resaleData.get_flat_model() in flat_model_search_array:
                    flat_model_list.append(resaleData)
                    isFlatModelFound = True 
            if not  flat_model_list:
                 searchResult+= f"Flat Model search not matching with the input passed {flat_model_search_array}"
            else:
                search_list = flat_model_list
        else:
            isFlatModelFound= True 
 
        if not search_list:
            if (not isTownFound) or (not isFlatTypeFound) or (not isFlatModelFound):
                raise ResaleDataException(searchResult)
            raise ResaleDataException("NO DATA FOUND FOR THE SEARCH PROVIDED")
        
        if (not isTownFound) or (not isFlatTypeFound) or (not isFlatModelFound):
            raise ResaleDataException(searchResult)

        for resaleData in search_list:
            #print( type(resaleData))
            print(resaleData.display())

def main():
    try:
        datafile = "Resale2024.csv"
        manager = ResaleDataManager()
        transactions = manager.read_resale_data(datafile)
        
        while True:
            print("")
            print("Main Menu:")
            print("1. Get towns")
            print("2. Get floor type")
            print("3. Get floor model")
            print("4. Search")
            print("5. Exit program")

            options = int(input("Enter option (1-5): "))
            print("")

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
                
    except Exception as e:
        logging.error("Unexpected error %s", str(e))
        print("An unexpected error occurred:", e )

main()
 
