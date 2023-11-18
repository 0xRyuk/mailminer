import requests
import re
import argparse


def fetch_webpage(url):
    resp = requests.get(url)
    return resp.text
    

def extract_email(webpage):
    pattern = re.compile(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}")
    matches = pattern.findall(webpage)
    return list(set(matches))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-u", "--url", metavar="", dest="url", help="Enter website url")


    args = parser.parse_args()

    if not args.url:
        parser.print_help()
        return

    webpage = fetch_webpage(args.url)
    emails = extract_email(webpage)
    
    print(f"Total emails found: {len(emails)}")
    for email in emails:
        print(email)
 

if __name__ == "__main__":
    print("MailMiner - Email Extractor v0.1.0")
    main()