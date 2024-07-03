# By Phi Zhang.
# This program processes a text file with each line in the format
# Continent:RegionName-RegionCode,RegionName-RegionCode... and prints
# NZ resident traveller arrival data for those continents/regions based
# on numbers in files named in the format RegionCode_Month.txt.
# Written for COMPSCI 130.

def main():
    months_list = ['NOV', 'DEC', 'JAN', 'FEB']
    filename = input("Enter a filename: ")
    print("NZ-resident traveller arrivals")
    print()

    file_content = open(filename, "r")
    continent_lines = file_content.read().split("\n")
    file_content.close()

    continents = []
    for line in continent_lines:
        continent_name, regions = line.split(":")[0], line.split(":")[1]
        regions = regions.split(",")
        continent = Continent(continent_name)
        for region in regions:
            name, code = region.split("-")[0], region.split("-")[1]
            continent.process(name, code, months_list)
        continents.append(str(continent))
    print("\n\n".join(continents))

class Arrival:
    def __init__(self, month = "JAN", number_of_arrivals = 0):
        self.month = month
        self.number_of_arrivals = number_of_arrivals

    def get_number_of_arrivals(self):
        return self.number_of_arrivals

    def __str__(self):
        return f"{self.month:^3}:{self.number_of_arrivals:>7}"

class Region:
    def __init__(self, region_name, region_code, months_list):
        self.region_name = region_name
        self.region_code = region_code
        self.arrivals_list = []
        self.process(months_list)

    def get_arrivals_list(self):
        return self.arrivals_list

    def add_arrival(self, month, value):
        self.arrivals_list.append(Arrival(month, value))

    def get_total_number_of_arrivals(self):
        arrivals_sum = 0
        for arrival in self.arrivals_list:
            arrivals_sum += arrival.get_number_of_arrivals()
        return arrivals_sum

    def __str__(self):
        total_arrivals = self.get_total_number_of_arrivals()
        arrivals_str_list = [f"{self.region_code}({total_arrivals})"]
        for arrival in self.arrivals_list:
            arrivals_str_list.append(str(arrival))
        return "\t".join(arrivals_str_list)

    def process_data_per_month(self, month_name):
        input_file = open(self.region_code + "_" + month_name + ".txt", "r")
        arrival_data = input_file.read().split()
        input_file.close()
        arrival_data = [int(number) for number in arrival_data]
        self.arrivals_list.append(Arrival(month_name, sum(arrival_data)))

    def process(self, months_list):
        for month in months_list:
            self.process_data_per_month(month)

class Continent:
    def __init__(self, name):
        self.name = name
        self.regions_list = []

    def process(self, region_name, region_code, months_list):
        new_region = Region(region_name, region_code, months_list)
        self.regions_list.append(new_region)

    def get_regions_list(self):
        return self.regions_list

    def get_total_arrivals(self):
        total_arrivals = 0
        for region in self.regions_list:
            total_arrivals += region.get_total_number_of_arrivals()
        return total_arrivals

    def __str__(self):
        continent_str = f"{self.name}(Total: {self.get_total_arrivals()})"
        for region in self.regions_list:
            continent_str += ("\n" + str(region))
        return continent_str

main()
