import sqlite3
from EmailPython1 import emailAdmin
import numpy as np
import matplotlib.pyplot as plt

def onOffFootPrint():
    conn = sqlite3.connect('tablessss.db', check_same_thread=False)
    c = conn.cursor()
    c.execute("select count(distinct hs_studentID) as on_campus from history left join student on ( history.hs_studentID=student.st_email) where lower(st_location) like '%washington%' or lower(st_location) like '%dc%'")
    rows = c.fetchall()
    oncampus = rows[0][0]
    c.execute("select count(distinct hs_studentID) as off_campus from history left join student on ( history.hs_studentID=student.st_email) where lower(st_location) not like '%washington%' and lower(st_location) not like '%dc%'")
    rows = c.fetchall()
    offcampus=rows[0][0]
    N = 2
    menMeans = (oncampus, offcampus)

    ind = np.arange(N)    # the x locations for the groups
    width = 0.4       # the width of the bars: can also be len(x) sequence

    p1 = plt.bar(ind, menMeans, width, color='orange')
    #p2 = plt.bar(ind, womenMeans, width,
                 #bottom=menMeans, yerr=womenStd)

    plt.ylabel('No.Of Students')
    plt.title('On-Campus vs Off-Campus')
    plt.xticks(ind, ('On-Campus', 'Off-Campus'))
    plt.yticks(np.arange(0, 25, 5))
    p1[1].set_color('lightblue')
    plt.legend((p1[0],p1[1]),('On-Campus','Off-Campus'))
    plt.savefig('AnalyticsImages/BarGraph_OnOffCampus.png')
    emailAdmin("gwsb234567@gmail.com","On Campus vs Off Campus foot print","AnalyticsImages/BarGraph_OnOffCampus.png","Hi Team,\n\n The pictorial report for On campus vs Off-campus student log ins are attached below.\n\n Best Regards, \n Team ChatBot George")
    conn.close()