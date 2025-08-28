# PII Data Masker

A Python library for masking Personally Identifiable Information (PII) in text data.

## Installation

```bash
pip install piidata-masker
```

## Basic Usage

```python
from piidata_masker import PIIMasker

# Create a masker
masker = PIIMasker()

# Mask email
email = masker.mask_email("john.doe@example.com")
print(email)  # jo******@example.com

# Mask phone
phone = masker.mask_phone("555-123-4567")
print(phone)  # ******4567

# Mask text with multiple PII
text = "Hello, this is John Smith from ABC Corporation. You can reach me at john.smith@company.com or call me at 555-123-4567. For urgent matters, try my mobile at +1-800-555-9876 or send an email to j.s@corp.co. Our customer service team can be contacted at support@helpdesk.example.org or by calling 1234567890. If you need to reach our international office, dial +44-207-123-4567 or email london.office@global-company.co.uk. For quick questions, you might also try reaching out to sarah.johnson123@marketing.dept.com at 9876543210, or our CEO directly at ceo@company.net (phone: +33-1-23-45-67-89). Emergency contact: a@b.c at 5551234567. Don't forget to CC operations@facility.management.co on important emails, and their direct line is 555.987.6543.
"
masked = masker.mask_text(text)
print(masked)  
# Hello, this is John Smith from ABC Corporation. You can reach me at joh#######@co#####.com or call me at #####34567. For urgent matters, try my mobile at ######59876 or send an email to j#@co##.co. Our customer service team can be contacted at sup####@he######.example.org or by calling #####67890. If you need to reach our international office, dial #######34567 or email lon##########@gl############.co.uk. For quick questions, you might also try reaching out to sar#############@ma#######.dept.com at #####43210, or our CEO directly at c#@co#####.net (phone: ######56789). Emergency contact: a#@b.c at #####34567. Don't forget to CC ope#######@fa######.management.co on important emails, and their direct line is #####76543.
```

## Custom Configuration

```python
from piidata_masker import MaskConfig

config = MaskConfig(
    email_show_chars=3,    # Show first 3 chars of email
    phone_show_chars=4,    # Show last 4 digits
    mask_char="#",         # Use # for masking
    mask_domains=True      # Also mask domains
)

masker = PIIMasker(config)
print(masker.mask_email("john.doe@example.com"))
# Output: joh#####@ex#####.com

print(masker.mask_phone("555-123-4567"))
#output: ******4567

print(masker.mask_text("Hello, this is John Smith from ABC Corporation. You can reach me at john.smith@company.com or call me at 555-123-4567. For urgent matters, try my mobile at +1-800-555-9876 or send an email to j.s@corp.co."))
#output:Hello, this is John Smith from ABC Corporation. You can reach me at joh#######@co#####.com or call me at #####34567. For urgent matters, try my mobile at ######59876 or send an email to j#@co##.co
```

## Features

1. Email Masking:
   - Configurable visible characters
   - Optional domain masking
   - Preserves email format

2. Phone Number Masking:
   - Multiple formats supported
   - Configurable visible digits
   - Handles international formats

3. Text Processing:
   - Masks multiple PII types
   - Preserves text structure
   - Non-destructive processing

## License

MIT License - See LICENSE file for details.
