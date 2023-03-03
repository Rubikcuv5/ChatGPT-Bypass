#!/usr/bin/env python3

import requests
import json
import os
import sys
import argparse
from colorama import init, Fore, Style
from sty import fg, bg, ef, rs

OPENAI_API_KEY="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"

def bypass(text):
    model = "text-davinci-003"
    max_tokens = 4000
    temperature = 1.0

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {OPENAI_API_KEY}"
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
        print(f"=> {text}\n")
        #print(f"\n{fg.li_green}{txt}{rs.all}") # Agrega color verde claro al texto
        print(f"{fg(255,224,102)}Respuesta:\n {rs.all}{fg.cyan}{bg(49,55,61)}{ef.bold} {txt} {rs.all}")
    except Exception as e:
        print(f"{fg.li_red}Bypass Exception: {e}{rs.all}") # Agrega color rojo claro al texto


def main():
    parser = argparse.ArgumentParser(description="simple bypass chatgpt")
    parser.add_argument("text",help="Enter the your cuestion")
    args = parser.parse_args()

    # Cambia la fuente de la entrada de texto
    init(autoreset=True)
    print(f"{fg(255,224,102)}Ingresa tu pregunta: {rs.all}{fg.cyan}{bg(49,55,61)}{ef.bold} {args.text} {rs.all}")
    
    bypass(args.text)

    
            
if __name__ == "__main__":
    main()

