# Email-Simulation

## **Problem Statement**
Create application which sends email by accepting receiver's email.

## **Functional Requirements**
1. Should be able to login via gmail credentials
2. should be able to send email

## **Classes**
  - App : for root window
  - Start_window : for playing starting GIF
  - login_winodw : for logging into gmail account

## **Keywords**
  - smtp = to create server for sending email using smtplib
  - sender_email = email address of sender
  - password = password of sender_email
  - receiver_email = email address of receiver
  - body = text body of the email
  - subject = subject line of email

## **Abstract**
&nbsp; &nbsp; Using `tkinter` we created GUI for sending email.  
&nbsp; &nbsp; When user runs the program first it opens start window which displays GIF of email. After that login window is opened which takes login credentials of the sender. If the credentials given by the user is invalid then a message box is displayed which says that _Login is Unsuccessful_.  
&nbsp; &nbsp; Logging in into user’s account it displays menu window which has compose option after clicking on compose button, Compose Window is opened which has recipient part, subject line part, body of email and send button. After the Email is sent, a message box is displayed saying _Email sent Successfully_.   
&nbsp; &nbsp; Internet Connectivity is Essential for the program else it shows a message box saying “No Internet Connectivity”.


## **Module-wise Description**
  - Smtplib Module: This module defines an SMTP client session object that can be used to send mail to any internet machine with an SMTP or ESMTP listener daemon. An SMTP instance encapsulates an SMTP connection. It has methods that support a full repertoire of SMYP and ESMPTP operaions.
  - Email Module: The Email package is library for managing email messages. It is specifically not designed to do any sending of email messages to SMTP .The Email package attempts to be as RFC -Complaint as possible.
  - Message submodule: The application interacts with the package Email primarilty through the object model interface defined in message submodule.
  - Policy Module: the control component is the policy module. Every EmailMessage, every generator and every parser has an associated policy object that controls its behaviour.
  - Tkinter Module: Tkinter is a Python module which helps in creating GUI .Tkinter represents Toolkit Interface for GUI . It is the easiest way to create GUI Applications.


## **Technologies Selected and Technology features covered**
  - `tkinter`
    - Frame
    - Label
    - Button 
  - `PIL`
    - Image
  - `smtplib`
      


## **References**
  - https://docs.python.org/3/library/tkinter.html
  - https://www.pythontutorial.net/tkinter/
  - https://www.freecodecamp.org/news/send-emails-using-code-4fcea9df63f/
