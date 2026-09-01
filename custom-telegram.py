#!/usr/bin/env python3

import sys
import json
import requests

# IMPORTANT:
# Replace these placeholders only on your Wazuh server.
TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"
CHAT_ID = "YOUR_TELEGRAM_CHAT_ID"


def main():
    try:
        alert_file = sys.argv[1]

        with open(alert_file, "r", encoding="utf-8") as f:
            alert = json.load(f)

        agent_name = alert.get("agent", {}).get("name", "Unknown Agent")
        rule_id = alert.get("rule", {}).get("id", "N/A")
        rule_level = alert.get("rule", {}).get("level", "N/A")
        rule_description = alert.get("rule", {}).get("description", "No description")
        location = alert.get("location", "Unknown location")

        message = (
            "🔔 *WAZUH ALERT*\n"
            "━━━━━━━━━━━━━━━\n"
            f"📍 *Agent:* {agent_name}\n"
            f"⚠️ *Level:* {rule_level}\n"
            f"📝 *Rule ID:* {rule_id}\n"
            f"📄 *Description:* {rule_description}\n"
            f"📂 *Location:* {location}"
        )

        url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

        requests.post(
            url,
            data={
                "chat_id": CHAT_ID,
                "text": message,
                "parse_mode": "Markdown",
            },
            timeout=10,
        )

    except Exception as e:
        print(f"Telegram integration error: {e}")


if __name__ == "__main__":
    main()
