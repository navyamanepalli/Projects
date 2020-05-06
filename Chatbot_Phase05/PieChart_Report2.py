import sqlite3
import matplotlib.pyplot as plt
from EmailPython1 import emailAdmin

def piechart_report2():
    conn = sqlite3.connect('tablessss.db', check_same_thread=False)
    c = conn.cursor()
    c.execute("select count(distinct(hs_studentID)) as Number,st_level from history left join student on ( history.hs_studentID=student.st_email) group by st_level")

    rows = c.fetchall()
    #for row in rows:
        #print(row)

    labels = ['Under Graduate', 'Graduate','Others']
    sizes = [rows[2][0], rows[1][0], rows[0][0]]
    colors = ['yellowgreen','lightskyblue','orange']
    patches, texts = plt.pie(sizes, colors=colors, shadow=True, startangle=90)
    plt.legend(patches, labels, loc="best")
    plt.axis('equal')
    plt.tight_layout()
    plt.savefig('AnalyticsImages/PieChart_StudentFootPrint.png')
    emailAdmin("gwsb234567@gmail.com","Report Student Foot Print till date","AnalyticsImages/PieChart_StudentFootPrint.png"," Hi Team,\n\n Please find attached Student footprint.\n\nBest Regards\nTeam ChatBot George")
    conn.close()