import socket
import requests
import json
import subprocess
import argparse
import os

def read_domains(filename):
    with open(filename, 'r') as file:
        domains = [line.strip() for line in file if line.strip()]
    return domains

def check_domain(domain):
    try:
        ip_address = socket.gethostbyname(domain)
        response = requests.get(f"http://{domain}", timeout=5)
        return {
            "domain": domain,
            "ip_address": ip_address,
            "http_status": response.status_code
        }
    except requests.exceptions.RequestException:
        return {
            "domain": domain,
            "ip_address": "N/A",
            "http_status": "N/A"
        }

def run_custom_tools(domain):
    results = {}
    try:
        ping_output = subprocess.check_output(["ping", "-c", "1", domain], text=True)
        results["ping"] = ping_output
    except subprocess.CalledProcessError as e:
        results["ping"] = str(e)
    try:
        nslookup_output = subprocess.check_output(["nslookup", domain], text=True)
        results["ping"] = nslookup_output
    except subprocess.CalledProcessError as e:
        results["ping"] = str(e)
    return results

def search_domains():
    domains = read_domains("domains.txt")
    results = []

    for domain in domains:
        domain_info = check_domain(domain)
        domain_info.update(run_custom_tools(domain))
        results.append(domain_info)

    with open("results.json", 'w', encoding='utf-8') as file:
        json.dump(results, file, indent=4, ensure_ascii=False)

    print("Поиск доменов завершен. Результаты сохранены в results.json")

def search_custom():
    # Вставьте здесь ваш код для поиска данных по определенным доменам и сайтам
    print("Пользовательский поиск доменов и сайтов")

def settings():
    # Вставьте здесь ваш код для настройки поиска
    print("Настройки поиска")

def main():
    parser = argparse.ArgumentParser(description="Поиск информации")
    subparsers = parser.add_subparsers(dest="command")

    search_parser = subparsers.add_parser("search")
    search_parser.add_argument("option", type=int, choices=[1, 2, 3], help="Опция поиска: 1 - поиск по данным, 2 - поиск по определенным доменам и сайтам, 3 - настройки")

    args = parser.parse_args()

    if args.command == "search":
        if args.option == 1:
            search_domains()
        elif args.option == 2:
            search_custom()
        elif args.option == 3:
            settings()

if __name__ == "__main__":
    main()