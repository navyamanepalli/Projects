import sqlite3
from EmailPython1 import emailAdmin
import numpy as np
import matplotlib.pyplot as plt

def happy_Meter():
    conn = sqlite3.connect('tablessss.db', check_same_thread=False)
    c = conn.cursor()
    c.execute("select count(*), hm_rating from happymeter where hm_rating!='' group by hm_rating order by hm_rating")

    rows = c.fetchall()    
    count1=rows[0][0]
    count2=rows[1][0] 
    count3=rows[2][0]
    count4=rows[3][0] 
    count5=0

    N = 5
    menMeans = (count1, count2, count3, count4, count5)

    ind = np.arange(N)    # the x locations for the groups
    width = 0.4       # the width of the bars: can also be len(x) sequence
    plt.figure(figsize=(12,8))
    p1 = plt.bar(ind, menMeans, width, color='lightgreen')
    #p2 = plt.bar(ind, womenMeans, width,
                 #bottom=menMeans, yerr=womenStd)
    plt.ylabel('No.Of Students')
    plt.xlabel('Rating Scale')
    plt.title('Feedback Ratings')
    plt.xticks(ind, (1,2,3,4,5))
    plt.yticks(np.arange(0, 25, 5))
    p1[1].set_color('lightblue')
    p1[2].set_color('orange')
    p1[3].set_color('lightpink')
    p1[4].set_color('violet')
    plt.legend((p1[0],p1[1],p1[2],p1[3],p1[4]),('Loved It', 'Liked It', 'Satisfied','Unsatisfied','Extremely Unsatisfied'))
    #plt.show()
    plt.savefig('AnalyticsImages/HappyMeter.png')
    emailAdmin("gwsb234567@gmail.com","Chatbot George Feedback","AnalyticsImages/HappyMeter.png","Hi Team,\n\n The pictorial report of student experince with the Chatbot is attached below.\n\n Best Regards, \n Team ChatBot George")
    conn.close()