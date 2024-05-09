filename = input("Enter the filename to process: ")
try:
    with open(filename, "r") as user_file:
        for line in user_file.readlines():
            #print(line.strip())
            current_list = line.strip().split(",")
            #print(current_list)
            try:
                calculate_sum = int(current_list[0]) / int(current_list[1])
            except ZeroDivisionError as zero_division_details:
                print("Error details:")
                print(zero_division_details.__doc__)
                print(zero_division_details.__str__)
                calculate_sum = "Zero denominator"
            except ValueError:
                calculate_sum = "Non-numeric value in line"
            print(calculate_sum)
except FileNotFoundError:
    print("ERROR: File not found")
except Exception as error_details:
    print(f"ERROR: Unknown exception: {error_details}" )
finally:
    print("Program execution completed!")
