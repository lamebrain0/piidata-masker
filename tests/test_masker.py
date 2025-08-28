import unittest
from pii_masking import PIIMasker, MaskConfig, mask_text, mask_email, mask_phone
from pii_masking.utils import is_valid_email, is_valid_phone, extract_pii

class TestPIIMasking(unittest.TestCase):
    def setUp(self):
        self.masker = PIIMasker()
        self.config = MaskConfig(
            email_show_chars=3,
            phone_show_chars=4,
            mask_char="#",
            mask_domains=True
        )
        self.custom_masker = PIIMasker(self.config)

    def test_mask_email(self):
        # Test default masking
        self.assertEqual(
            self.masker.mask_email("john.doe@example.com"),
            "jo******@example.com"
        )
        
        # Test custom masking
        self.assertEqual(
            self.custom_masker.mask_email("john.doe@example.com"),
            "joh#####@ex#####.com"
        )
        
        # Test short username
        self.assertEqual(
            self.masker.mask_email("jo@example.com"),
            "j*@example.com"
        )

    def test_mask_phone(self):
        # Test default masking
        self.assertEqual(
            self.masker.mask_phone("5551234567"),
            "******4567"
        )
        
        # Test custom masking
        self.assertEqual(
            self.custom_masker.mask_phone("5551234567"),
            "######4567"
        )
        
        # Test with formatting
        self.assertEqual(
            self.masker.mask_phone("555-123-4567"),
            "******4567"
        )

    def test_mask_text(self):
        text = "Contact john.doe@example.com or 555-123-4567"
        expected = "Contact jo******@example.com or ******4567"
        self.assertEqual(self.masker.mask_text(text), expected)

    def test_validation(self):
        # Test email validation
        self.assertTrue(is_valid_email("john.doe@example.com"))
        self.assertFalse(is_valid_email("invalid.email"))
        
        # Test phone validation
        self.assertTrue(is_valid_phone("5551234567"))
        self.assertTrue(is_valid_phone("555-123-4567"))
        self.assertFalse(is_valid_phone("123"))

    def test_extract_pii(self):
        text = "Contact john.doe@example.com or 555-123-4567"
        result = extract_pii(text)
        
        self.assertIn("john.doe@example.com", result["emails"])
        self.assertIn("555-123-4567", result["phones"])
        self.assertEqual(result["total_pii"], 2)

if __name__ == '__main__':
    unittest.main()
