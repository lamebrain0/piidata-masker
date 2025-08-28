"""
PII Masking - A library for masking Personally Identifiable Information in text
"""

__version__ = "0.1.0"

from .masker import PIIMasker, MaskConfig, mask_text, mask_email, mask_phone
from .utils import is_valid_email, is_valid_phone, extract_pii

__all__ = [
    "PIIMasker",
    "MaskConfig",
    "mask_text",
    "mask_email",
    "mask_phone",
    "is_valid_email",
    "is_valid_phone",
    "extract_pii",
]