import geocoder
import csv

with open('fall_2013.csv', 'w') as csvfile_w:
    writer = csv.writer(csvfile_w)
    with open('Fallecidos_2013.csv', 'r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            direccion = row[10] +", " + row[1] + ", Uruguay"
            g = geocoder.google(direccion)
            if g.lat == 0.0:
                b = geocoder.bing(direccion)
                row.append(b.lat)
                row.append(b.lng)
            else:
                row.append(g.lat)
                row.append(g.lng)
            print row
            writer.writerow(row)
