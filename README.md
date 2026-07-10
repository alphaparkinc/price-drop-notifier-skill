# genpark-price-drop-notifier-skill

> **GenPark AI Agent Skill** -- Price drop watcher and notifier.

## Quick Start

```python
from client import PriceDropNotifierClient
client = PriceDropNotifierClient()
res = client.audit_price_change(50, 40, [{"email": "user@test.com"}])
print(res["drop_percentage"])
```
