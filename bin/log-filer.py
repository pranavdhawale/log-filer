import datetime as dt

# Main Function
def main():

    # Used to return timestamp
    def getDate():
        return dt.datetime.now()
    
    # Function for Diet Category
    def diet(name):
        
        # Function to Set Diet Log
        def setDietLog(name):
            timestamp = str(getDate())
            with open(name + "_dietlog.txt", "a") as f:
                diet_content = input("Enter your diet : ")
                print("===========================================================")
                f.write(timestamp + " " + diet_content + "\n")
            log_filer()
        
        # Function to Get Diet Log
        def getDietLog(name):
            with open(name + "_dietlog.txt", "r") as f:
                log = f.read()
                print(log)
                print("===========================================================")
            log_filer()
        
        print("1. Set Log\n2. Get Log\n")
        menu_category = int(input("Select what you want to do : "))
        print("===========================================================")
        
        if menu_category == 1 : setDietLog(name)
        elif menu_category == 2 : getDietLog(name)
    
    # Function for Exercise Category
    def exercise(name):
        
        # Function to Set Exercise Log
        def setExerciseLog(name):
            timestamp = str(getDate())
            with open(name + "_exerciselog.txt", "a") as f:
                exercise = input("Enter your exercise : ")
                print("===========================================================")
                f.write(timestamp + " " + exercise + "\n")
            log_filer()
        
        # Function to Get Exercise Log
        def getExerciseLog(name):
            with open(name + "_exerciselog.txt", "r") as f:
                log = f.read()
                print(log)
                print("===========================================================")
            log_filer()
        
        print("1. Set Log\n2. Get Log\n")
        menu_category = int(input("Select what you want to do : "))
        print("===========================================================")
        
        if menu_category == 1 : setExerciseLog(name)
        elif menu_category == 2 : getExerciseLog(name)
    
    # Main Menu of the log-filer
    def log_filer():
        
        print("Select the Name of the Client\n1. Harry\n2. Rohan\n3. Shyam\n4. Back\n")
        name_category = int(input("Enter number : "))
        print("===========================================================")
        
        if name_category == 1 : name = "harry"
        elif name_category == 2 : name = "rohan"
        elif name_category == 3 : name = "shyam"
        elif name_category == 4 : main()
        
        print("1. Diet\n2. Exercise\n")
        log_category = int(input("Enter Option : "))
        print("===========================================================")
        
        if log_category == 1 : diet(name)
        elif log_category == 2 : exercise(name)
    
    # Welcome Page of log-filer
    print("\t\t\tLog Filer")
    print("===========================================================")
    print("1. Menu\n2. Exit\n")
    menu = int(input("Enter Option : "))
    print("===========================================================")

    if menu == 1 : log_filer()
    elif menu == 2 : quit()

main()