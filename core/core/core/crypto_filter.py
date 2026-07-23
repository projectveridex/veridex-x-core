"""
VERIDEX X
USDT TRC20 + USDC Payment Compatibility Filter
"""

CRYPTO_KEYWORDS = [
    "usdt",
    "usdc",
    "stablecoin",
    "crypto payment",
    "web3",
    "blockchain",
    "defi",
    "dao",
    "solana",
    "ethereum"
]


def check_crypto_support(opportunity):
    text = (
        opportunity.get("title", "") +
        " " +
        opportunity.get("description", "")
    ).lower()

    for keyword in CRYPTO_KEYWORDS:
        if keyword in text:
            return True

    return False


def payment_preference(opportunity):
    if check_crypto_support(opportunity):
        return {
            "status": "CRYPTO_COMPATIBLE",
            "preferred": [
                "USDT TRC20",
                "USDC"
            ]
        }

    return {
        "status": "CRYPTO_NOT_CONFIRMED",
        "preferred": [
            "USDT TRC20",
            "USDC"
        ]
          }
