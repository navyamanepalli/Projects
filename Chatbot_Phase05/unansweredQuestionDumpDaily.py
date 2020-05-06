from db_pull import db_csv
from EmailPython1 import emailAdmin

def unansweredDaily():
    
    db_csv("select hs_question, hs_studentID from history where strftime('%Y-%m-%d', hs_datestamp) = strftime('%Y-%m-%d','now','localtime') and hs_answer in ('Sorry, Can you be more specific?','Sorry I dint get you')","AnalyticalReports/UnansweredQuestions.csv")
    emailAdmin("gwsb234567@gmail.com","Unanswered Questions for the Day","AnalyticalReports/UnansweredQuestions.csv","Hi Team,\n\n The report for unanswered questions is attached here.\nReport includes email-id and the question from the student. \n\n Best Regards, \n Team ChatBot George")