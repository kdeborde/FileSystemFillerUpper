from datetime import datetime
import os
import shutil
import time

# TODO: Add option for user to choose path of file.
# TODO: Actually calculate MB or MiB properly.

file_name = datetime.now().strftime("%Y%m%d-%H%M%S.txt")


# Function to loop and add data to a file
def fill_up_file_system(amount_to_add, start_time):
    add_data = 0
    count = 2
    progress_update = 1

    absolute_path = os.path.abspath(file_name)
    print("\nWriting " + str(amount_to_add) + " M of data to file: " + absolute_path + "\n\n")
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

        # Print current progress
        progress_update += 1
        if progress_update == 50:
            get_progress(add_data, amount_to_add)
            progress_update = 1

        # Adjust time based on compute power.
        if should_reset > 1.0:
            count = 2

    end_elapsed_time = time.time()
    total_time_taken = round(elapsed_time(start_elapsed_time, end_elapsed_time), 3)
    print("\n\nTotal size of file added is " + str(add_data) + "M\n")
    print("Elapsed time: " + str(total_time_taken) + " seconds\n\n")


def get_disk_statistics():
    total, used, free = shutil.disk_usage("\\")
    total /= 1000000
    used /= 1000000
    free /= 1000000
    return int(total), int(used), int(free)


# Function to ask the user how much data to add and ensure it's a valid number.
def data_to_add():
    input_amount = ""
    # Verify an integer is entered.
    while input_amount == "":
        try:
            input_amount = input("Enter \"ALL\" to fill it up.\nEnter the amount of data you would like to add in MB: ")
            if input_amount == 'ALL':
                input_amount = get_disk_statistics()[2]
                break
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


# Print percentage and size completed.
def get_progress(current_progress, max_progress):
    current_progress = round(current_progress, 1)
    size_progress = str(current_progress) + " of " + str(max_progress) + "M"
    progress_percentage = round(((current_progress * 100) / max_progress), 1)
    print("Completion: " + str(progress_percentage) + "% ----- " + size_progress, end="\r")


# print disk statistics
print("\nDisk Statistics: \n")
print("Total disk size: " + str(get_disk_statistics()[0]) + " M")
print("Used disk space: " + str(get_disk_statistics()[1]) + " M")
print("Free disk space: " + str(get_disk_statistics()[2]) + " M\n")


# Invoke function to start generating numbers in a file
fill_up_file_system(data_to_add(), file_name)


input("Press enter or Ctl + C to close... ")
