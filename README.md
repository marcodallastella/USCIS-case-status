# Check USCIS case status

There are various scrapers for the USCIS website on GitHub but the ones I was finding did not seem to work properly. Perhaps, USCIS changed something in the past few years, and trying to connect to the undocumented API results constantly in error messages.
Because I'm really anxious about my visa, I dedicated a few hours to write a scraper that sends me an email as soon as the USCIS case status changes. Here's a short breakdown of the code:

Main script is `check_status.py`. It uses Selenium to check on the USCIS website, look for the case number and identify case status and description.
It reads the lat entry of the `status_check.csv` file. If the case status has changed, it sends an email notifying about the change.
Every time it runs it writes the data to a `status_check.csv` file.

Remember to replace the following variables with the correct information in among the GitHub Secrets.

* CASE_NUMBER: your USCIS case number
* FROM_EMAIL: the email you are sending from (must be authenticated on SendGrid)
* TO_EMAIL: the email you are sending to
* SENDGRID_API_KEY: your SendGrid API Key. For more info on how to send emails from Python with SendGrid there's [this short and easy video](https://www.youtube.com/watch?v=xCCYmOeubRE).
