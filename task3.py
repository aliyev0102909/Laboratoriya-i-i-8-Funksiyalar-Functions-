def build_username(first, last, year=""):
    return first.lower() + "." + last.lower() + str(year)
first_name = input("Adınızı daxil edin: ")
last_name = input("Soyadınızı daxil edin: ")
year_val = input("İl daxil edin (istəyə bağlı): ")
print(build_username(first_name, last_name, year_val))
print(build_username("Aysel", "Mammadova"))
print(build_username("Kamran", "Aliyev", 2005))
