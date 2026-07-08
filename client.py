"""
price-drop-notifier-skill: Client SDK
Tracks pricing drops and drafts personalized customer discount alerts.
"""
from __future__ import annotations
from typing import Optional


class PriceDropNotifierClient:
    """
    SDK for discount and alert routing.
    """

    def audit_price_change(
        self,
        original_price: float,
        new_price: float,
        subscribers: list[dict],
    ) -> dict:
        diff = original_price - new_price
        drop_pct = round((diff / original_price) * 100, 1) if original_price > 0 else 0.0

        notifications = []
        # Only notify if there is a significant price drop (> 5%)
        if drop_pct >= 5.0:
            for sub in subscribers:
                name = sub.get("name", "there")
                email = sub.get("email", "")
                notifications.append({
                    "email": email,
                    "subject": f"Price drop alert! Save {drop_pct}%",
                    "body": f"Hi {name},\n\nGood news! An item on your wishlist just dropped from ${original_price} to ${new_price}. Click here to shop now."
                })

        return {
            "drop_percentage": drop_pct,
            "notifications": notifications,
            "alerts_generated": len(notifications)
        }
