row1 = {'ID': 1, 'Name': 'Bob Smith', 'Email': 'bsmith@notmail.com', 'city': 'Portland', ("birth_year", "birth_month"):[1979, "April"]}

if __name__ == "__main__":
    for key, value in row1.items():
        print(f"Key: {key} \t Value: {value}") 