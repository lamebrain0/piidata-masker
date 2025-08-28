import re
from typing import Dict, List

def is_valid_email(email: str) -> bool:
    """
    Validate email format
    
    Args:
        email: Email address to validate
        
    Returns:
        bool: True if email format is valid, False otherwise
    """
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))

def is_valid_phone(phone: str) -> bool:
    """
    Validate phone number format
    
    Args:
        phone: Phone number to validate
        
    Returns:
        bool: True if phone number format is valid, False otherwise
    """
    digits = re.sub(r'\D', '', phone)  # Remove non-digits
    return 10 <= len(digits) <= 15  # Most phone numbers are 10-15 digits

def extract_pii(text: str) -> Dict[str, List[str]]:
    """
    Extract all PII found in text
    
    Args:
        text: Text to scan for PII
        
    Returns:
        Dict containing lists of found emails and phone numbers
        
    Example:
        >>> text = "Contact joe@example.com or 555-123-4567"
        >>> extract_pii(text)
        {
            'emails': ['joe@example.com'],
            'phones': ['555-123-4567'],
            'total_pii': 2
        }
    """
    email_pattern = r'[\w.+-]+@[\w-]+\.[\w.-]+'
    phone_pattern = (r'(?:\+\d{1,4}[-.\s]?(?:\d{1,4}[-.\s]?){1,5}\d{2,4})|'
                    r'(?:(?:\+?\d{1,3}[-.\s]?)?(?:\(?\d{3}\)?[-.\s]?)?\d{3}[-.\s]?\d{4})')
    
    emails = re.findall(email_pattern, text)
    phones = re.findall(phone_pattern, text)
    
    return {
        'emails': list(set(emails)),
        'phones': list(set(phones)),
        'total_pii': len(set(emails)) + len(set(phones))
    }
