import os, sys

try:

    __import__("ALAMIN").ALAMIN()

except Exception as e:

    exit(str(e))

