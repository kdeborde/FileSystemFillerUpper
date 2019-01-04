import os
import time
from datetime import datetime

# TODO: Make an option for 'ALL' to just filler on up.
# TODO: Add option for user to choose path of file.
# TODO: Make some names more descriptive/trim it down.

file_name = datetime.now().strftime("%Y%m%d-%H%M%S.txt")


# Function to loop and add data to a file
def fillUpFileSystem(amount_to_add, start_time):
    add_data = 0
    count = 2

    absolute_path = os.path.abspath(file_name)
    print("\nWriting " + str(amount_to_add) + "M of data to file: " + absolute_path)
    log_open = open(start_time, 'w')

    # Loop through and add data to file.
    while add_data <= amount_to_add:
        start = time.time()
        add_data = getFileSize(file_name)
        log_open.write(str(count))
        count += count
        end = time.time()
        should_reset = getTimeToCompete(start, end)

        if should_reset > .0001:
            count = 2

    print("\nTotal size of file added is " + str(add_data) + "M\n")


# Function to ask the user how much data to add and ensure it's a valid number.
def dataToAdd():
    input_amount = ""
    # Verify an integer is entered.
    while input_amount == "":
        try:
            input_amount = input("Enter \"ALL\" to filler up.\nEnter the amount of data you would like to add in MB: ")
            input_amount = int(input_amount)
        except ValueError:
            print("Not a valid int!")
            input_amount = ""

    # TODO: Verify they'd like to do this because, why not?
    return input_amount


# Function to get the file size, convert to Mb and return.
def getFileSize(file_size):
    file_info = os.stat(file_size)
    file_info = os.path.getsize(file_size)
    file_info /= 1000000
    return file_info

def getTimeToCompete(start, end):
    should_reset = end - start
    print(should_reset)
    return should_reset


# Invoke function for user input of file size
# add_the_data = dataToAdd()

# Invoke function to start generating numbers in a file
fillUpFileSystem(dataToAdd(), file_name)

input("Press enter to close... ")