# marketplace-scraper

7/29/25

Before Using:
 - Be sure that the most recent ChromeDriver (found at https://storage.googleapis.com/chrome-for-testing-public/142.0.7444.59/win64/chromedriver-win64.zip) is installed and added to your PATH variables.
 - Install the selenium module using "pip install selenium" in the command line.

## Details

If the script cannot locate "marketplace.csv", try running with administrator privilges through the command line.

The script will open the Facebook page for you to log into and then prompt you to hit enter in the script after landing on the main Facebook Marketplace page. It will then open each listing and extract
information from it, writing it into the "marketplace.csv" file. The data extracted contains listing price, title, description, location, and how long the listing has been up, in addition to links to
both the listing itself and the profile of the one who listed it. The script is set to run for the first 20 listings (including sponsorships, which will be skipped over), but that number can be modified
on line 38.

The "marketplace.csv" file here has real data, I removed the links to the seller profiles for their privacy.
