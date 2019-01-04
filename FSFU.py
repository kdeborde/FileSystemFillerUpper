import os
import time
from datetime import datetime

# TODO: Make an option for 'ALL' to just filler on up.
# TODO: Add option for user to choose path of file.
# TODO: Make some names more descriptive/trim it down.

file_name = datetime.now().strftime("%Y%m%d-%H%M%S.txt")


# Function to loop and add data to a file
def fill_up_file_system(amount_to_add, start_time):
    add_data = 0
    count = 2

    absolute_path = os.path.abspath(file_name)
    print("\nWriting " + str(amount_to_add) + "M of data to file: " + absolute_path)
    log_open = open(start_time, 'w')

    start_elapsed_time = time.time()
    # Loop through and add data to file.
    while add_data <= amount_to_add:
        start_write = time.time()
        add_data = get_file_size(file_name)
        log_open.write(str(count))
        count += count
        end_write = time.time()
        should_reset = get_time_to_reset(start_write, end_write)

        # Adjust time based on compute power.
        if should_reset > 1.0:
            count = 2

    end_elapsed_time = time.time()
    total_time_taken = round(elapsed_time(start_elapsed_time, end_elapsed_time), 3)
    print("\nTotal size of file added is " + str(add_data) + "M\n")
    print("Elapsed time: " + str(total_time_taken) + " seconds\n\n")


# Function to ask the user how much data to add and ensure it's a valid number.
def date_to_add():
    input_amount = ""
    # Verify an integer is entered.
    while input_amount == "":
        try:
            input_amount = input("Enter \"ALL\" to filler up.\nEnter the amount of data you would like to add in MB: ")
            input_amount = int(input_amount)
        except ValueError:
            print("Not a valid int!")
            input_amount = ""
    return input_amount


# Function to get the file size, convert to Mb and return.
def get_file_size(file_size):
    os.stat(file_size)
    file_info = os.path.getsize(file_size)
    file_info /= 1000000
    return file_info


# Function to compare start/end time to reset counter.
def get_time_to_reset(start_write, end_write):
    return end_write - start_write


# Get elapsed time of adding to file
def elapsed_time(start_elapsed_time, end_elapsed_time):
    return end_elapsed_time - start_elapsed_time


# Invoke function to start generating numbers in a file
fill_up_file_system(date_to_add(), file_name)


input("Press enter or Ctl + C to close... ")
