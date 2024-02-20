import requests
import json

def fetch_aws_ip_ranges(url="https://ip-ranges.amazonaws.com/ip-ranges.json"):
    """Fetches the current list of AWS IP ranges from the specified URL."""
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception("Failed to fetch IP ranges")

def generate_nginx_deny_rules(ip_ranges):
    """Generates Nginx deny rules for the provided IP ranges."""
    deny_rules = []
    for ip_range in ip_ranges:
        deny_rules.append(f"deny {ip_range};")
    return "\n".join(deny_rules)

def update_nginx_configuration(deny_rules, output_location):
    """Updates the Nginx configuration with the generated deny rules."""
    with open(output_location, "w") as file:
        file.write(deny_rules)

def main():
    nginx_output_location = "/data/web/nginx/server.aws-blacklist"  # Update this path

    aws_data = fetch_aws_ip_ranges()
    ip_ranges = [prefix["ip_prefix"] for prefix in aws_data["prefixes"] if prefix["service"] == "AMAZON"]

    deny_rules = generate_nginx_deny_rules(ip_ranges)

    update_nginx_configuration(deny_rules, nginx_output_location)

    print(f"Nginx deny rules generated and saved to {nginx_output_location}")

if __name__ == "__main__":
    main()
