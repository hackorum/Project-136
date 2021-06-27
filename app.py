import csv

final_star_list = []
rows = []
with open("final_stars.csv", "r") as f:
    csvreader = csv.reader(f)
    for row in csvreader:
        rows.append(row)

headers = rows[0]
star_data_rows = rows[1:]
for star_data in star_data_rows:
    temp_dictionary = {
        "name": star_data[1],
        "distance": star_data[2],
        "mass": star_data[3],
        "radius": star_data[4],
        "gravity": star_data[5],
    }
    final_star_list.append(temp_dictionary)
print(final_star_list)
