"""
example_usage.py -- Demonstrates PriceDropNotifierClient
"""
from client import PriceDropNotifierClient

def main():
    client = PriceDropNotifierClient()
    result = client.audit_price_change(
        original_price=100.0,
        new_price=80.0,
        subscribers=[{"name": "Sarah", "email": "sarah@test.com"}]
    )
    print("[Price Drop Notifier Result]")
    print(f"Drop Pct: {result['drop_percentage']}%")
    print(f"Alerts: {result['notifications']}")

if __name__ == "__main__":
    main()
