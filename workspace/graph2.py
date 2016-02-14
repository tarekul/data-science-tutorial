from collections import Counter

import csv
import matplotlib.pyplot as plt
import numpy as np

MY_FILE = "../data/sample_sfpd_incident_all.csv"


def parse(raw_file, delimiter):
    """Parses a raw CSV file to a JSON-like object"""

    # Open CSV file, and safely close it when we're done
    opened_file = open(raw_file)

    # Read the CSV data
    csv_data = csv.reader(opened_file, delimiter=delimiter)

    # Setup an empty list
    parsed_data = []

    # Skip over the first line of the file for the headers
    fields = csv_data.next()

    # Iterate over each row of the csv file, zip together field -> value
    for row in csv_data:
        parsed_data.append(dict(zip(fields, row)))

    # Close the CSV file
    opened_file.close()

    return parsed_data






def visualize_days():
	data_file=parse(MY_FILE, ",")    

	counter=Counter(item["DayOfWeek"] for item in data_file)

	data_list=[
				counter["Monday"],
                counter["Tuesday"],
                counter["Wednesday"],
                counter["Thursday"],
                counter["Friday"],
                counter["Saturday"],
                counter["Sunday"]
			   ]

	day_tuple = tuple(["Mon", "Tues", "Wed", "Thurs", "Fri", "Sat", "Sun"])
	
	plt.plot(data_list)
	plt.xticks(range(len(day_tuple)),day_tuple)
	
	#save the plot!
	plt.savefig("Days.png")

	#close figure
	plt.clf()

def visualize_type():
	"""Visualize data by category in a bar graph"""

	#grab our parsed data	
	data_file=parse(MY_FILE, ",")

	counter=Counter(item["Category"] for item in data_file)
	labels=tuple(counter.keys())

	xlocations=np.arange(len(labels))+0.5
	width=0.4
	plt.bar(xlocations, counter.values(),width=width)
	plt.xticks(xlocations + width / 2, labels, rotation=90)
	plt.subplots_adjust(bottom=0.4)
	plt.rcParams['figure.figsize']=12, 8
	plt.savefig("Type.png")
	plt.clf()




def main():
    visualize_type()

if __name__ == "__main__":
    main()	

	
