import datetime as dt
import qrcode 
import random
from random import randint
from django.conf import settings
from .models import VerificationCodes
import termcolor
import matplotlib
import matplotlib.pyplot as plt  
import numpy as np

# def send_email(to_email, message):
#     s = smtplib.SMTP('smtp.gmail.com', 587)
#     s.starttls()
#     s.login(settings.FROM_EMAIL, settings.EMAIL_PASSWORD)
#     s.sendmail('Test message',to_email, message)


# def send_otp(email):
#     rand=random.randint(1000,9999)
    
#     # To add the random otp in our table 
#     VerificationCodes.objects.create(
#             email = email,
#             otp = rand,
#         )
#     msg=f"Your One Time Password(OTP) is {rand}"

#     send_email(to_email=email, message=msg)

def feedback_type(overall,servicing,behaviour):
    rating = int(overall) + int(servicing) + int(behaviour)
    if rating >= 9 :
        return "positive"
    else:
        return "negative"

def generate_qrcode(loc):

    features = qrcode.QRCode(version = 1, box_size = 40, border = 3)

    features.add_data(f'127.0.0.1:8000/feedback?city={loc}')

    features.make(fit = True)

    generated = features.make_image()
    generated.save(f"mainapp/static/images/qrcodes/{loc}.png")


def generate_graph(cities,total_feedbacks):
    cities = cities
    feedback=total_feedbacks
    fig = plt.figure(figsize = (10, 5),facecolor='#BCB88A')
    plt.rcParams.update({'font.size' : 13})
    # creating the bar plot
    plt.bar(cities,feedback, edgecolor ='BLACK',color ='#254117',width = 0.4)
    plt.xlabel("Cities",fontweight='bold')
    plt.ylabel("No. of Feedback",fontweight='bold')
    plt.title("Total feedbacks of cities",fontweight='bold')
    # plt.show()
    plt.savefig('mainapp/static/images/graphs/feedback_graph.png')
    plt.close()
# matplotlib.use('Agg')


def generate_piechart(city,pos,neg):
    
    feedback=["Postive Feedback","Negative Feedback"]
    feedbackvalues=[pos,neg]
    # Creating explode data
    explode = (0.1, 0.2)
    # Creating color parameters
    colors = ( "orange", "BLUE")
    # Wedge properties
    wp = { 'linewidth' : 2, 'edgecolor' : "white" }
    # Creating autocpt arguments
    def func(pct, allvalues):
        absolute = int(pct / 100.*np.sum(allvalues))
        return "{:.1f}%".format(pct, absolute) 
        # Creating plot
    fig, ax = plt.subplots(figsize =(10, 7))
    plt.rcParams.update({'font.size' : 11})
    fig.patch.set_facecolor("White")
    wedges, texts, autotexts = ax.pie(feedbackvalues,autopct = lambda pct: func(pct,feedbackvalues),explode = explode,labels = feedback,shadow = True,colors = colors,startangle = 90,wedgeprops = wp,textprops = dict(color ="WHITE"))
        # Adding legend
    ax.legend(wedges,feedback,title =city,loc ="center left",bbox_to_anchor =(1, 0))
    plt.setp(autotexts, size = 15, weight ="bold")
    print("djba")
    ax.set_title(city) 
        # show plot
    # plt.show()
    plt.savefig('mainapp/static/images/graphs/feedback_pichart.png')
    plt.close()

def send_otp(phone):
    

    generated_otp=random.randint(0000,9999)
    VerificationCodes.objects.create(
             phone = phone,
             otp = generated_otp,
         )
    try:
        import pywhatkit
    except:
        pass

    try:
        
        number = str(phone)
        numb1 = '+91' + number
        hour = dt.datetime.now()
        
        hours = hour.hour
 
        min = hour.minute
        min1 = min + 1
        pywhatkit.sendwhatmsg(numb1, "*GUJARAT POLICE DEPARTMENT*\n\nYOUR OTP IS : "+str(generated_otp), hours, min1)
            # sending whatsapp msg to registered phone number
    except:
        print("internet lost")
        
