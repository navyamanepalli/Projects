import schedule 
import time 
from EmailPython1 import emailAdmin
from unansweredQuestionsCountWeekly import weeklyCount
from unansweredQuestionDumpDaily import unansweredDaily
from on_OffCampus import onOffFootPrint
from PieChart_Report2 import piechart_report2  
from freq_area import freq_area
from HappyMeterReport import happy_Meter
# Functions setup 

      
def everyminute(): 
    print("Schedule runs evry minute") 
  
# Task scheduling 
# After every 10mins geeks() is called.  
#schedule.every(1).minutes.do(emailAdmin) 
#schedule.every().saturday.at("01:08").do(emailAdmin) 
#schedule.every().day.at("10:30").do(emailAdmin)
schedule.every().day.at("10:30").do(weeklyCount)  
schedule.every().day.at("10:33").do(unansweredDaily)  
schedule.every().day.at("10:37").do(onOffFootPrint)  
schedule.every().day.at("10:42").do(piechart_report2)  
schedule.every().day.at("10:46").do(freq_area)  
schedule.every().day.at("10:48").do(happy_Meter)  
  
# Every tuesday at 18:00 sudo_placement() is called 
#schedule.every().tuesday.at("18:00").do(sudo_placement) 
  
# Loop so that the scheduling task 
# keeps on running all time. 
while True: 
  
    # Checks whether a scheduled task  
    # is pending to run or not 
    schedule.run_pending() 
    time.sleep(1)
