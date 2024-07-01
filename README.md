# Automatic-Birthday-wisher

This is a Python project that automatically sends birthday wishes via email. It uses the pandas, smtplib, and datetime libraries to read a list of birthdays, check if today is someone's birthday, and send an email if it is.

## Features

- Reads a list of birthdays from a CSV file
- Checks if today is someone's birthday
- Sends an email to the birthday person using an SMTP server

## Prerequisites

- Python 3.12.3
- pandas library
- smtplib library (comes with Python's standard library)
- datetime library (comes with Python's standard library)

## Installation

1. Clone the repository:
   
    git clone https://github.com/Tushar8691/automatic-birthday-wisher.git

2. Navigate to the project directory:
    bash
    cd automatic-birthday-wisher

3. Install the required libraries:
    pip install pandas
    pip install matplotlib 
    

## Usage

1. Prepare a CSV file named Data.csv with the following structure:
    csv
    Name	Birthdate	Dialogue	Year	Email
    Shivam,1982-04-17,"Wishing you a day filled with love, joy, and all your favorite things. Happy Birthday!",2024,Shivam@example.com
   
2. Update the email credentials and SMTP settings in the script:
    python
    smtp.login('Enter Your email', 'Enter Your password')
    SMTP_SERVER = "smtp.example.com"
    SMTP_PORT = 587
    
3. Run the script:
    python birthday_wisher.py
    
