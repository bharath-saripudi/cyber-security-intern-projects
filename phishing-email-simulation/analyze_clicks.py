import json
from collections import Counter
from datetime import datetime

LOG_FILE = "click_log.json"

def load_log():
    try:
        with open(LOG_FILE) as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def analyze_clicks(log):
    if not log:
        print("No click data found.")
        return

    total_clicks = len(log)
    print(f"Total clicks: {total_clicks}")

    # Clicks per campaign
    campaign_counter = Counter(entry.get('campaign', 'unknown') for entry in log)
    print("\nClicks per campaign:")
    for campaign, count in campaign_counter.most_common():
        print(f"  {campaign}: {count}")

    # Unique IPs
    ips = [entry.get('ip') for entry in log if entry.get('ip')]
    unique_ips = set(ips)
    print(f"\nUnique IP addresses: {len(unique_ips)}")
    if len(unique_ips) <= 10:
        for ip in unique_ips:
            print(f"  {ip}")

    # Timestamps analysis
    timestamps = []
    for entry in log:
        ts = entry.get('timestamp')
        if ts:
            try:
                dt = datetime.fromisoformat(ts.replace('Z', '+00:00'))
                timestamps.append(dt)
            except:
                pass
    if timestamps:
        print(f"\nFirst click: {min(timestamps)}")
        print(f"Last click: {max(timestamps)}")

    # Campaign names
    campaign_names = [entry.get('campaign_name') for entry in log if entry.get('campaign_name')]
    if campaign_names:
        name_counter = Counter(campaign_names)
        print("\nClicks per campaign name:")
        for name, count in name_counter.most_common():
            print(f"  {name}: {count}")

if __name__ == "__main__":
    log = load_log()
    analyze_clicks(log)