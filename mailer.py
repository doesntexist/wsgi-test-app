# Send an HTML email with an embedded image and a plain text message for
# email clients that don't want to display the HTML.

from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEImage import MIMEImage

# Define these once; use them twice!
strFrom = 'noreply@github.com' # Who is this email coming from
strTo = 'someone@example.com' # who are you sending it to

# Create the root message and fill in the from, to, and subject headers
msgRoot = MIMEMultipart('related')
msgRoot['Subject'] = 'test message'
msgRoot['From'] = strFrom
msgRoot['To'] = strTo
msgRoot.preamble = 'This is a multi-part message in MIME format.'

# Encapsulate the plain and HTML versions of the message body in an
# 'alternative' part, so message agents can decide which they want to display.
msgAlternative = MIMEMultipart('alternative')
msgRoot.attach(msgAlternative)

msgText = MIMEText('This is the alternative plain text message.')
msgAlternative.attach(msgText)

# Send the email (this example assumes SMTP authentication is required)
import smtplib
smtp = smtplib.SMTP()
smtp.connect('domainnameOrIpOfYourMailHost') # Your smtp server
smtp.login('Your email login', 'yourPassword') # If you were to login to your mail server, this would be it
smtp.sendmail(strFrom, strTo, msgRoot.as_string())
smtp.quit()
