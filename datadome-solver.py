import capsolver
import requests

capsolver.api_key = "your pay per usage key"
PAGE_URL = "websiteURL"
CAPTCHA_URL = "geo captcha url"
PROXY = "http://username:password@host:port"

def solver_datadome(url,captchaURL, proxy):
    solution = capsolver.solve({
     "type": "DatadomeSliderTask",
    "websiteURL": url,
    "captchaUrl": captchaURL,
    "proxy": proxy,
    "userAgent": "MODERN_USER_AGENT_HERE"
    })
    return solution


def main():
    
    print("Solving Datadome...")
    solution = solver_datadome(PAGE_URL,CAPTCHA_URL,PROXY )
    print("Solution: ", solution)

if __name__ == "__main__":
    main()
