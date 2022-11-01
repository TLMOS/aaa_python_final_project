"""Utils for testing."""


def remove_digits(text: str) -> str:
    """Remove digits from text."""
    return ''.join([i for i in text if not i.isdigit()])
