# Holypython Examples 1
# Example 1a: Assignment operator w/ string (=)
greek_island = "Santorini"
# End of Example 1a

# Example 1b: Assignment operator w/ integer & tuple (+=)
earth_age_bln = 4.4
universe_age_bln = 14

earth_age_bln += 0.1
print (earth_age_bln)
# End of Example 1b

# Example 1c: Assignment operator w/ list (=)
asia_wishlist = [
    "Bhutan",
    "Ha Long",
    "Laos",
    "Danxia",
    "Seoul",
    "Khao Sok",
    "Cebu",
    "Chiang Mai",
    "Ho Chi Minh"
]
# End of Example 1c

# Holypython Examples 2
# Example 2a: Relational (comparison) operator (==)
msg = "life is beautiful"

if msg == "I love you":
    print ("propose")
else:
    print ("wait xP")
# End of Example 2a

# Example 2b: Relational (comparison) operator (>=)
net_earnings = 10000000 # Net earnings in some currency unit

if net_earnings >= 100000000:
    print ("Large Cap") # If net earnings are 100 million or more
else:
    print ("Small Cap") # Otherwise
# End of Example 2b

# Example 3
# Example 3a: Membership operator (in)
lst = [
    "soccer",
    "swimming",
    "running",
     "skiing"
]

if "rock climbing" not in lst:
    print ("boo")
# End of Example 3a

# Example 3b: Membership operator (not in)
web_data = ["techresearch and computervision"]

if "@" in web_data:
    print ("e-mail address")
elif "0123456789" in web_data:
    print ("phone number")
else:
    print ("not e-mail nor phone number")
# End of Example 3b

#Example 4: Arithmetic operator (+, -, *, /, //, **, %)
a = 10 + 20
b = 100 - 1
c = 50 / 7
d = 50 // 7
e = 10 % 8
f = 5 ** 2

print (a, b, c, d, e, f, sep="\n ")
#End of Example 4