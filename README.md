# Check USCIS case status

There are various scrapers for the USCIS website on GitHub but the ones I was finding did not seem to work properly. Perhaps, USCIS changed something in the past few years, and trying to connect to the undocumented API results constantly in error messages.
Because I'm really anxious about my visa, I dedicated a few hours to write a scraper that sends me an email as soon as the USCIS case status changes. Here's a short breakdown of the code:

Main script is `check_status.py`. It uses Selenium to check on the USCIS website, look for the case number and identify case status and description.
It reads the lat entry of the `status_check.csv` file. If the case status has changed, it sends an email notifying about the change.
Every time it runs it writes the data to a `status_check.csv` file.

