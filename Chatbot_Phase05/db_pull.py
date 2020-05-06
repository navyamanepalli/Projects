import csv
import sqlite3

def db_csv(query,filename):
    conn = sqlite3.connect('tablessss.db', check_same_thread=False)
    c = conn.cursor()
    c.execute(query)
    with open(filename, "w", newline='') as csv_file:  # Python 3 version    
#with open("out.csv", "wb") as csv_file:              # Python 2 version
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow([i[0] for i in c.description]) # write headers
        csv_writer.writerows(c)
    conn.close()