
# !pip install works for new installations
import datetime as dt # This script should contain all the basics from the structure.md file.

# The following expression uses an f-String, that means the string is formatted and contains an replacement field in curly brackets {}
# If an variable is not a string a conversion is necessary, this can be done via:
# !s - calls str() method, !r - calls repr() method, !a calls ascii() method

world = "World"
print(f"Hello {world}")
print(f"Hello {world!s}")
print(f"Hello {world!r}")
print(f"Hello {world!a}")

# there are also date specifier:
today = dt.datetime(year=2023, month=4, day=14)
print(f" Today is the {today:%B %d, %Y}")