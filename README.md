
# AWS IP Ranges Blocker for Nginx

This Python application automatically fetches the current list of AWS IP ranges and generates Nginx deny rules to block them. It is particularly useful for administrators looking to restrict access from AWS-hosted services to their web servers.

## Installation

1. Clone the repository:
```bash
git clone https://github.com/hpowernl/aws-blocker.git
```

2. Change into the directory:
```bash
cd aws-blocker
```

## Usage

To use this script, follow these steps:

1. Open the script in a text editor and set the `nginx_output_location` variable in the `main` function to the path where you want the deny rules to be saved. This should be within your Nginx configuration directory.

2. Run the script:
```bash
python3 aws_ip_ranges_blocker.py
```

The script will fetch the latest AWS IP ranges, generate deny rules for Nginx, and save them to the specified location. Remember to reload your Nginx configuration to apply the changes.

## Cron

To automate the process of updating the deny rules, you can set up a cron job as follows:

1. Open the crontab editor:
```bash
crontab -e
```

2. Add the following line to execute the script daily (you can adjust the frequency as needed):
```bash
0 0 * * * cd /path/to/aws-blocker && /usr/bin/python3 aws_ip_ranges_blocker.py
```

Replace `/path/to/aws-blocker` with the actual path to where the script is located.

## Features

- Automatically fetches the latest AWS IP ranges.
- Generates Nginx deny rules to block traffic from these ranges.
- Can be automated with cron to keep the deny list up-to-date.
- Easy to integrate into existing Nginx configurations.

## License

[MIT](https://github.com/hpowernl/aws-blocker/blob/main/LICENSE)
