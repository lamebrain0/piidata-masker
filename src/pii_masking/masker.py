import re
from dataclasses import dataclass
from typing import Optional

@dataclass
class MaskConfig:
    """Configuration options for PII masking"""
    email_show_chars: int = 2  # How many chars to show in email username
    phone_show_chars: int = 4  # How many chars to show at end of phone
    mask_char: str = "*"       # Character to use for masking
    mask_domains: bool = False # Whether to mask email domains too

class PIIMasker:
    """Main class for PII masking operations"""
    
    def __init__(self, config: Optional[MaskConfig] = None):
        self.config = config or MaskConfig()
    
    def mask_email(self, email: str) -> str:
        """
        Mask email addresses by hiding most of the username
        
        Args:
            email: Email address to mask
            
        Returns:
            Masked email address
            
        Examples:
            >>> masker = PIIMasker()
            >>> masker.mask_email("john.smith@company.com")
            'jo********@company.com'
        """
        try:
            username, domain = email.split('@', 1)
            
            if len(username) <= self.config.email_show_chars:
                masked_username = username[0] + self.config.mask_char
            else:
                show_chars = self.config.email_show_chars
                masked_username = (username[:show_chars] + 
                                 self.config.mask_char * (len(username) - show_chars))
            
            if self.config.mask_domains:
                domain_parts = domain.split('.')
                if len(domain_parts) > 1:
                    masked_domain = (domain_parts[0][:2] + 
                                   self.config.mask_char * (len(domain_parts[0]) - 2) +
                                   '.' + '.'.join(domain_parts[1:]))
                    domain = masked_domain
            
            return masked_username + '@' + domain
        except ValueError:
            return email  # Return original if not valid email format
    
    def mask_phone(self, phone: str) -> str:
        """
        Mask phone numbers by showing only the last N digits
        
        Args:
            phone: Phone number to mask (digits only)
            
        Returns:
            Masked phone number
            
        Examples:
            >>> masker = PIIMasker()
            >>> masker.mask_phone("5551234567")
            '******4567'
        """
        digits = re.sub(r'\D', '', phone)  # Remove non-digits
        
        if len(digits) <= self.config.phone_show_chars:
            return self.config.mask_char * len(digits)
        
        show_chars = self.config.phone_show_chars
        return (self.config.mask_char * (len(digits) - show_chars) + 
                digits[-show_chars:])
    
    def mask_text(self, text: str) -> str:
        """
        Mask all email addresses and phone numbers in text
        
        Args:
            text: Text containing potential PII
            
        Returns:
            Text with PII masked
            
        Examples:
            >>> masker = PIIMasker()
            >>> masker.mask_text("Call me at 555-123-4567 or john@example.com")
            'Call me at ******4567 or jo**@example.com'
        """
        # Mask emails
        email_pattern = r'[\w.+-]+@[\w-]+\.[\w.-]+'
        text = re.sub(email_pattern, 
                     lambda x: self.mask_email(x.group()), text)
        
        # Mask phone numbers - comprehensive pattern
        phone_pattern = (r'(?:\+\d{1,4}[-.\s]?(?:\d{1,4}[-.\s]?){1,5}\d{2,4})|'
                        r'(?:(?:\+?\d{1,3}[-.\s]?)?(?:\(?\d{3}\)?[-.\s]?)?\d{3}[-.\s]?\d{4})')
        
        def phone_replacer(match):
            phone = match.group()
            digits_only = re.sub(r'\D', '', phone)
            if len(digits_only) >= 10:  # Only mask if looks like full phone number
                return self.mask_phone(digits_only)
            return phone
        
        text = re.sub(phone_pattern, phone_replacer, text)
        return text

# Convenience functions for backward compatibility and ease of use
_default_masker = PIIMasker()

def mask_email(email: str, config: Optional[MaskConfig] = None) -> str:
    """Convenience function to mask a single email"""
    masker = PIIMasker(config) if config else _default_masker
    return masker.mask_email(email)

def mask_phone(phone: str, config: Optional[MaskConfig] = None) -> str:
    """Convenience function to mask a single phone number"""
    masker = PIIMasker(config) if config else _default_masker
    return masker.mask_phone(phone)

def mask_text(text: str, config: Optional[MaskConfig] = None) -> str:
    """Convenience function to mask PII in text"""
    masker = PIIMasker(config) if config else _default_masker
    return masker.mask_text(text)
