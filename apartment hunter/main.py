import apartmentBot
import apartmentSorter
import time
def main():
    dataframe = apartmentBot.df.copy()
    print("Welcome to My Apartment Hunter Project")
    time.sleep(1)
    print("This app takes in an absolute path name and")
    time.sleep(1)
    print("returns an excel sheet of over 300 apartments in Toronto")
    time.sleep(1)
    print("This excel sheet can be unsorted.")
    time.sleep(1)
    print("or sorted based on one of 4 criteria")
    time.sleep(1)
    print("1. Most expensive 2. Least expensive")
    print("3. Most Rooms     4. Largest Area (ft²)   ")
    time.sleep(1)
    num = input("Enter a number corrosponding to your desired sorting criteria: ")
    if (num == "1"):
        print("by most expensive")
        df = apartmentSorter.sortByExpensive(dataframe)
    elif (num == "2"):
        print("by cheapest")
        df =apartmentSorter.sortByCheapest(dataframe)
    elif (num == "3"):
        print("by rooms")
        df = apartmentSorter.sortByMostRooms(dataframe)
    elif (num == "4"):
        print("by Area (ft²)")
        df = apartmentSorter.sortByBiggest(dataframe)
    else:
        print("Unsorted")
        df = dataframe



    time.sleep(2)
    path = input("Please enter an absolute path name for your sheet must end in .csv: ")
    df.to_csv(path)

    time.sleep(1)
    print(df)
    print("Your sheet is ready thank you!")

if __name__ == "__main__":
    main()