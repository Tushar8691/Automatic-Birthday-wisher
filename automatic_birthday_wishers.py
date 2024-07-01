import pandas as pd
import datetime
from smtplib import SMTP



def sendEmail(to, sub, msg):
    print(f"Email to {to} sent with subject: {sub} and message {msg}" )
    
    debuglevel = 0

    smtp = SMTP('smtp.example.com', 587)  # Replace 'smtp.example.com' with the actual SMTP server hostname
    smtp.starttls()  # Enable TLS encryption
    smtp.login('Enter Your email', 'Enter Your password')

    from_addr = "Enter Your email"
    smtp.sendmail(from_addr, to, f"Subject: {sub}\n\n{msg}")
    smtp.quit()

if __name__ == "__main__":
    df = pd.read_excel("data.xlsx")
    print(df)# It shows data of csv file

    today = datetime.datetime.now().strftime("%d-%m")
    yearNow = datetime.datetime.now().strftime("%Y")
    
    writeInd = []
    for index, item in df.iterrows():

        bday = item['Birthdate'].strftime("%d-%m")
        
        if(today == bday) and yearNow not in str(item['Year']):
            sendEmail(item['Email'], "Happy Birthday", item['Dialogue']) 
            writeInd.append(index)

    for i in writeInd:
        yr = df.loc[i, 'Year']
        df.loc[i, 'Year'] = str(yr) + ', ' + str(yearNow)

    df.to_excel('data.xlsx', index=False)   