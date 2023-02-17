#!/usr/bin/env python3

import requests
import json
import os
import sys
import argparse


def bypass(text):
    model = "text-davinci-003"
    max_tokens = 4000
    temperature = 1.0

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {os.environ['OPENAI_API_KEY']}"
    }
    try:
        data = {
            "model": model,
            "prompt": text,
            "max_tokens": max_tokens,
            "temperature": temperature
        }
    
        response = requests.post("https://api.openai.com/v1/completions", headers=headers, data=json.dumps(data))
        response.raise_for_status()

        result = response.json()
        txt = result["choices"][0]["text"].strip()
        print(f"[+] INPUT : {text}")
        print(txt)
    except Exception as e:
        print(f"Bypass Exception :{e}")


def main():
    parser = argparse.ArgumentParser(description="simple bypass chatgpt")
    parser.add_argument("text",help="Enter the your cuestion")
    args = parser.parse_args()
    
    bypass(args.text)

    
            
if __name__ == "__main__":
    main()
