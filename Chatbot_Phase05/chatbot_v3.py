#!/usr/bin/python
# -*- coding: UTF-8 -*-
import nltk
import sqlite3
import time
import datetime
import re
import random
from IPython.core.display import display, HTML
from nltk.chat.util import Chat, reflections
import csv 
import os
from EmailPython1 import emailAdmin

conn = sqlite3.connect('tablessss.db', check_same_thread=False)
c = conn.cursor()


pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, How are you today ?",]
    ],
    [
        r"(name|what is your name?)",
        ["My name is Chatty and I'm a chatbot ?",]
    ],
    [  
        r"(thank you|thank you very much|thanks)",
        ["Welcome"]
    ],
    [
        r"how are you ?",
        ["I'm doing good\nHow about You ?",]
    ],    [
        r"sorry (.*)",
        ["Its alright","Its OK, never mind",]
    ],
    [
        r"i'm (.*) doing good(.*)",
        ["Nice to hear that","Alright :)",]
    ],
    
    [
        r"hi|hey|hello",
        ["Hello", "Hey there",]
    ],
    [
        r"(.*)(foundation courses|course curriculum|electives|prerequisite|required courses)(.*)",
        ["Please Visit <a href=\"http://bulletin.gwu.edu/business/graduate-programs/information-systems-technology-ms/#requirementstext\">MSIST course details</a>"]

    ],
        [
        r"(.*)(credit|classes|class|courses)(.*)(part time|part-time|full-time|full time)(.*)",
        ["Part-time students usually enroll in 1-2 classes (3-6 credits) per semester depending upon their personal and professional commitments and availability.\nFull-time students take 3 classes (9 credits) in the fall and spring semesters.",]
    ],
    [
        r"(.*)(courses available|graduate courses|graduate subjects|under graduate|graduate degree|course details|research|research options|online courses|course details|courses)(.*)",
        ["Please visit <a href=\"https://business.gwu.edu/academics/programs\">Academic programs</a>"]
    ],

    [
        r"(.*)(class timing|building|classes held|classes take place|class location)|(.*)(classes held|classes meet)",
        ["GWSB classes are offered on the Foggy Bottom campus in downtown Washington, D.C.\n Classes are held once or twice a week, often starting in the late afternoon or early evening."]

    ],
     [
        r"(.*)(summer|fall|spring|course schedule|course information|msist course information)(.*)(course|course schedule|course information| )(.*)",
        ["Please Visit <a href=\"https://business.gwu.edu/academics/programs/specialized-masters/msist/academic-program\">MSIST Course Information</a>"]

    ],
       [
        r"(.*)(procedure|apply|certification|eligib|enroll)(.*)(certification|certificate|requirement)(.*)",
        ["Any professional  can  enroll in a part-time/full-time GW School of Business graduate certificate program.For answers to questions about the application process or admission requirements, contact the GW School of Business Graduate Admissions Office at (202) 994-1212 or business@gwu.edu. "]

    ],
       [
        r"(.*)(certificat)(.*)(another|other|different)(.*)",
        ["Please contact your academic advisor Brittany Johnson. Email-id: brittanyjohnson@gwu.edu "]

    ],
        [
        r"(.*)(electiv|course)(.*)(other|another|different)(.*)",
        [" If you have an approval letter from your academic advisor,you can enroll in electives from other department.\nFor instructions on how to register for classes please review the<a href=\"https://t.e2ma.net/click/9kl4nb/98nmuu/hj9vqd\">Registering for Courses</a>page on the GWSB website."]
    ],
        [
        r"(.*)(graduate certification|certification|professional|graduate|prerequisite|prerequisites)(.*)(courses|certificate|certification)",
        ["Please Visit <a href=\"https://business.gwu.edu/academics/programs\">Certfication Prerequisites</a>"]

    ],
  
    
    [
        r"(.*)(fee|tuition fee|due|tuition due|Account balance|balance)",
        ["You can see your account information in <a href=\"https://t.e2ma.net/click/xfxwlb/98nmuu/xra7nd\">GWeb</a> under student records information.\nThe Colonial Central site has information from the Offices of Student Accounts, Financial Aid and the Registrar."]

    ],
        [
        r"(.*)(campus|oncampus|on campus|)(.*)housing|dorm|stay(.*)(|campus|oncampus|on campus)",
        ["GW offers undergraduate student housing. For graduate housing contact the GWU housing services."]
    ],
    
        [
        r"(.*)(oncampus|on-campus|on campus|job)(.*)(job|employment|openings|)(.*)",
        ["The Career Center handles all campus jobs, including work-study and non-work-study positions for graduate and undergraduate students.\nFor information about campus jobs, please visit the Career Service website - <a href=\"https://careerservices.gwu.edu/students\">Career Services</a>"]
    ],
 
      [
        r"(.*)part time|part-time|full time|full-time(.*)",
        ["If you enroll for part-time/full-time study you can register for any courses.For instructions on how to register for classes please review the <a href=\"https://t.e2ma.net/click/9kl4nb/98nmuu/hj9vqd\">Registering for Courses</a>page on the GWSB website. "]

    ],
       [
        r"(.*)(academic|account|hold|holds)(.*)(academic|account|hold)",
        ["To check if there is a hold on your account, please visit GWeb:\n1.Choose Student Records \n2.choose Student Records Information Menu\n3.Choose View Administrative Holds.\nPlease contact your academic advisor if you have a hold.  "]

    ],
    [
        r"(.*)eligibility(.*)dual degree(.*)",
        ["please contact your academic advisor and to know about requirements visit <a href=\"https://business.gwu.edu/msist-degree-requirements\">Dual Degree Elegibility</a>"]
    ],
    [
        r"(.*)dual degree|dual course(.*)",
        ["Submit an NOC(No Objection Certificate) from your program coordinator and submit it to MSIST academic advisor - Brittany Johnson."]
    ],
    [
        r"(.*)mba(.*)(msist|istm|ist|msistm|)",
        ["please contact your academic advisor and to know about requirements to join MSIST program visit <a href=\"https://business.gwu.edu/msist-degree-requirements\"Degree Requirements</a>\nTo join MBA program, current MSIST students apply before completing 24 credits or two years and meet MBA admissions requirements, including the GRE.\nConsult your advisor if you are interested in pursuing a joint degree."]
    ],

     [
        r"(.*)(class strength|strength|count|class limit|seat)(.*)",
        ["When you register for classes you will be able to see the class limit.\nFor instructions on how to register for classes please review <a href=\"https://t.e2ma.net/click/9kl4nb/98nmuu/hj9vqd\">Registering for Courses</a>page on the GWSB website."]
    ],
        [
        r"(.*)(extra|additional)(.*)(credit|class|course)(.*)",
        ["Yes, with the permission of the advisor you can take extra credits. But, graduate students are advised to take 9 credits per semester inorder to not get overloaded with the coursework."]
    ],
[
        r"(.*)(limit|restrictions|penalty|last date|deadline)(.*)(add|drop)(.*)",
        ["Add/Drop should be done before the first week of the class.\nStudents may have to pay a penalty fee if they delay to Add/Drop courses. "]
    ],
    [
        r"(.*)(add|drop)(.*)",
        ["Add/Drop should be done before the first week of the class.\nStudents may have to pay a penalty fee if they delay to Add/Drop courses.\nLog in to GWeb and click the ‘Student Records & Registration Menu,’ then ‘Registration Menu.’\nClick ‘Register, Drop and/or Add Classes’ and choose the semester.\nTo drop, use the 'Web Drop' option in the Action column next to the course you wish to drop."]
    ],
        [
        r"(.*)(course limit|course|credit limit|credit)(.*)(semester|)(.*)",
        ["Based on the number of credits per course the count varies.However,with the permission of the advisor you can take extra credits.\nFor example: Graduate students are advised to take 3 courses(each 3 credits) per semester inorder to not get overloaded with the coursework"]
    ],
        [
        r"(.*)(tuition|financial)(.*)plan(.*)",
        ["Visit <a href=\"https://business.gwu.edu/prospective-students/specialized-masters/msist-admission/tuition-financial-planning\">Financial Planning</a>"]

    ],
        [
        r"(.*)Tuition(.*)",
        ["GW's tuition rates are available on the Student Accounts website- <a href=\"https://studentaccounts.gwu.edu/tuition-rates\">Tuition Rates</a>\nTuition does vary based on the student's program. You can also reach out to your program about specific costs. "]
    ],
        [
        r"(.*)(IT support|IT help|IT service|Information Technology)(.*)",
        ["Phone: 202-994-GWIT (4948) Email-id: ithelp@gwu.edu "]
    ],
        [
        r"(.*)(Holidays|holiday)(.*)",
        ["For detailed information about important academic dates check out the <a href=\"https://www.gwu.edu/academic-calendar\">Academic Calendar</a>"]
    ],
        [
        r"(.*)(scholarship|aid)(.*)(financial aid|)",
        ["You can contact financial aid department by email finaid@gwu.edu or by phone at 202-994-6620 for questions about specific scholarships offered by George Washington University.\n For MSIST department scholarship contact faculty advisior."]
    ],

        [
        r"(.*)(apply|)(.*)financial aid(.*)",
        ["For incoming undergraduate students, the FAFSA and CSS Profile are required to apply for financial aid.\nOther tax documents are also needed, so be sure to log in to your GWeb account to keep track of any necessary documentation requirements.\nFor continuing undergraduate students, the FAFSA is only needed unless a student has been selected by the Department of Education for verification.\nGraduate students need to submit the FAFSA.\nFor information, visit our<a href=\"https://financialaid.gwu.edu/how-apply\"> How to Apply website</a>."]
    ],

        [
        r"(.*)payroll|salary|stipend(.*)",
        ["Reach out to your Supervisor/Manager "]
    ],

     [
        r"(.*)colonial health center|health center|medical(.*)",
        ["Marvin Center Ground Floor\n800 21st Street, NW\nWashington, DC 20052\nPhone: 202-994-5300 (24/7)\n<a href=\"https://healthcenter.gwu.edu\">Colonial Health Center</a>"]
    ],
           [
        r"(.*)Disability support center|disability support|disability(.*)",
        ["Rome Hall\n801 22nd Street, NW Suite 102\nWashington, DC 20052\nPhone: 202-994-8250\ndss@gwu.edu"]
    ],
        [
        r"(.*)event(.*)",
        ["Please Visit <a href=\"https://business.gwu.edu/news-events\">Upcoming Events</a>.\nTo know more about MSIST events check academic advisor's weekly newsletter."]
    ],
        [
        r"(.*)(program|MSIST|credit|length|duration)(.*)(completion|complete|)",
        ["Students must complete 33 credits of the following coursework to be eligible for graduation. And Complete all degree requirements within five (5) years."]
    ],   
    [
        r"(.*)(orientation|inaugur)(.*)(date|schedule|time|)",
        ["Half-day orientation session is hosted for the incoming fall and spring classes generally 1-2 weeks prior to the semester start date. Visit <a href=\"https://business.gwu.edu/academics/programs/international/international-student-services/incoming-international-students/orientation-and-newsletters\">orientation schedule</a>"]
    ],
        [
        r"(.*)(veteran|military)(.*)",
        ["You will find support at the Office of Military and Veteran Students."]

    ],
        [
        r"(.*)(additional|more)(.*)(questions|information)",
        ["Please email us at msist@gwu.edu for assistance."]

    ],
        [
        r"(.*)non-degree|non degree(.*)",
        ["GW offers the option to enroll as a non-degree student.\nNon-degree students must first apply to the Office of Non-Degree Students.\nOnce admitted, submit a Registration Transaction Form to MSIST for registration approval.\nSpecific MSIST courses are available to non-degree students.\nContact us at msist@gwu.edu to learn more."]

    ],

        [
        r"(.*)Stem(.*)",
        ["MS ISTM provides stem extension of 2 years addition to one year of OPT post graduation."]
    ],
        [
        r"(.*)grade|grades|score|gpa|cgpa(.*)",
        ["Grades are typically posted five business days after the end of the semester.\nYou can see your grades in <a href=\"https://t.e2ma.net/click/xfxwlb/98nmuu/xra7nd\">GWeb</a> after the instructor submits them for a specific semester.\nGo to the Student Records menu and choose Display Grades.\nYou can also see your full class history by clicking Transcripts in the Student Records menu."]
    ],
        [
        r"(.*)blackboard(.*)(access|)",
        ["Blackboard is GW's official course management system. Students can find answers to most Blackboard questions on the <a href=\"https://itl.gwu.edu/student-blackboard-faqs#I%20can't%20see%20my%20course(s%29)\">Blackboard Student FAQ</a>. Faculty can receive assistance with Blackboard from the <a href=\"https://itl.gwu.edu/blackboard-course-management\">Instructional Technology Lab</a>."]
    ],
        [
        r"(.*)newsletter|news-letter|news letter(.*)",
        ["To know more about MSIST events check academic advisor's weekly news-letter."]
    ],
        [
        r"(.*)(unofficial|official|)(.*)transcript(.*)",
        ["You can see your transcripts in <a href=\"https://t.e2ma.net/click/xfxwlb/98nmuu/xra7nd\">Gweb</a> after the instructor submits them for a specific semester.\nGo to the Student Records menu and choose Display Grades.\nYou can also see your full class history by clicking Transcripts in the Student Records menu."]
    ],
       [
        r"(.*)opt|cpt(.*)",
        ["Contact International services office(ISO) Email-id: iso@gwu.edu\n Vist <a href=\"https://internationalservices.gwu.edu/optional-practical-training-opt\">International Services</a>"]
    ],
    [
        r"(.*)(Advisor|Academic advisor|MSIST Advisor|Brit)(.*)",
        ["Brittany Johnson is the advisor for the MSIST department.\nOffice hours:Mon-Fri, 9Am to 5 PM \nemail:brittanyjohnson@gwu.edu \nLocation:Duques Hall, School of Business 2201 G St. NW\nSuite 550 Washington, D.C. 20052"]
    ],
 
    [
        r"(.*)(procedure|steps|graduate|)(.*)(early|late|late graduation|early graduation)(.*)",
        ["Students typically complete degree requirements in the following time frames: Part-Time: 30-48 months and Full-Time: 18-24 months.\n For early/late graduation you should contact your academic advisor and get an approval."]
    ],
    [
        r"(.*)break(.*)",
        ["You should get approval from the department stating the reason for your break.\nFor approval please contact the academic advisor"]
    ],
    [
        r"(.*)(graduat|commencement)(.*)",
        ["Visit <a href=\"https://t.e2ma.net/click/xfxwlb/98nmuu/xra7nd\">GWeb</a> to apply and know the last date.Submit a <a href=\"https://registrar.gwu.edu/sites/g/files/zaxdzs2171/f/GradAppLate_2020.pdf\">Late (Paper) Graduation Application</a>.\nFor commencement schedule visit <a href=\"https://commencement.gwu.edu/commencement-details\">Graduation ceremony</a>"]
    ],

    [
        r"(.*)(LOA|Leave of Absence)(.*)",
        ["If you're considering taking time off, meet with your academic advisor to talk about your future plans.\nFor details about the formal process for taking time off, visit the Registrar's website or get in touch with the Student Financial and Registration Services team by registrar@gwu.edu"]
    ],

    [
        r"(.*)(study abroad|study abroad program)(.*)",
        ["All students must meet GW’s <a href=\"https://studyabroad.gwu.edu/node/106\">eligibility requirements</a> for study abroad.\n Students may register their desire to study abroad and apply for GW approval by starting an application for each program they are applying for on < a href=\"http://passport.gwu.edu\">GW Passport</a>."]
    ],
    [
        r"(.*)(pass|fail)(.*)(policy|criteria|eligib|)(.*)",
        ["The grading criteria varies between professors. You will be able to see your grade on the blackboard and in GWeb. For assistance with your academic performance contact your academic advisor."]
    ],
        [
        r"(.*)(transfer credits|transfer credit|credit transfer)",
        ["Procedures for transferring credit hours vary depending on when you took the credit hours, before or after enrolling at GW.\nStudents in other colleges and graduate students should speak with their academic advisor. "]
    ],
    
    [
        r"(.*)transfer(.*)",
        ["Please contact you academic advisor to know about transfering procedure."]
    ],
    
    [
        r"(.*)(professor|faculty|instructor)",
        ["Please Visit<a href=\"............\">Professor Information</a>"]
    ],
    
    [
        r"(.*)(TA|Teaching assistant)",
        ["Please Visit<a href=\"............\">TA Information</a>"]
    ],
    [
        r"quit",
        ["Bye take care. See you soon :) ","It was nice talking to you. See you soon :)"]
    ],
    [
        r"(.*)",
        ["Sorry I dint get you", "Sorry, Can you be more specific?"]
    ],

]

# def create_history():
#     c.execute('CREATE TABLE IF NOT EXISTS history (datestamp TEXT,question TEXT, answer TEXT )')
#     conn.commit()

def insert_data(dat,eml, que, ans):
    c.execute("INSERT INTO history (hs_datestamp,hs_studentID,hs_question, hs_answer) VALUES(?, ?, ?, ?)",(dat, eml, que, ans))
    conn.commit()

class ChatChild(Chat):
    def converse(self,ui_converse,email,quit="quit"):
        bot_response=""
        user_input = ""
        
        while user_input != quit:
            user_input=ui_converse
            query = user_input
            print("User Input:%s"%query)
            if user_input:
                while user_input[-1] in "!.":
                    user_input = user_input[:-1]
                bot_response=self.respond(user_input)
                reply = bot_response
                print ("Chatbot Response:%s"%reply)
            user_input = quit
        time1 = time.time()
        date1 = str(datetime.datetime.fromtimestamp(time1).strftime('%Y-%m-%d %H:%M:%S'))
        insert_data(date1, email, query, reply)
        return bot_response

def chatty(user_input, email):
    
    # create_history()
    chat = ChatChild(pairs, reflections)
    output_response=chat.converse(user_input,email)

    # Create CSV for user transcripts
    line_1=email +":"+user_input
    line_2="George"+":"+output_response
    print (line_1)
    print (line_2)
    with open('user_transcript.csv','a+', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([line_1])
        writer.writerow([line_2])
    if user_input=="quit":
        f.close()
        sub="Chat Transcript from the MSIST Chatbot"
        emailAdmin(email,sub, "user_transcript.csv", "Hi User,\n\n Please find attached your chat trasnscript.\n\nBest Regards\nTeam ChatBot George")
        os.remove('user_transcript.csv')

    return output_response
