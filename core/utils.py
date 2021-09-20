import random
import string

from django.utils.text import slugify

source_string = string.ascii.ascii_lowercase + string.digits
string_length = 6

def generate_unique_slug(slug, string=source_string, length=string_length):
    slug = "{}-{}".format(slug, random.choice(string) for _ in range(length))
    return "{}".format(slug)
