

try:
    import chardet
except ImportError:
    chardet = None

if chardet:
    print("chardet is there")
else:
    print("Please import chardet")

try:
    from lxml import etree
except ImportError:
    import xml.etree.ElementTree as etree

x = 1 # no need to define variable. Its unbound variable

print("The original string is : ", end="")
