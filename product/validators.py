from django.core.exceptions import ValidationError
def validator_file_size(file):
    """This Validator Valid If file size is less than 10MB"""
    max_size = 10
    max_size_in_bytes = max_size * 1024 * 1024

    if file.size > max_size_in_bytes :
        raise ValidationError(f"File size cannot be larger than {max_size_in_bytes} MB!")

    
