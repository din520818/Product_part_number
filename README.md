# Product_part_number

Task 2 [Check task 2 update below.]
Write one program in any language (which you know) to generate the part number.
Assume we have one product called 'Apple Iphone', now iphone have different variant.
Color [CLR] = Red, Blue, Green
Ram [RM] = 1Gb, 2Gb
Space [SPC] = 16gb, 64gb, 128gb
Now based on this it has total 18 variants like [RED,1GB,16GB], [RED,1GB, 64GB] ....so on.
You need to write program which generate the part number using the attribute code.
like i set part number pattern will be = ‘IPHONE [CLR]-[RM]-[SPC]'
Then it needs to print the 18-part number like below.
IPHONE RED-1GB-16GB
IPHONE RED-1GB-64GB
IPHONE Green-1GB-64GB
All 18 need to print.
If I set like this: '([SPC])([RM])([SPC]) APPLE'
(64GB)(1GB)(Red) APPLE
(16GB)(2GB)(Red) APPLE
(64GB)(2GB)(GREEN) APPLE
Every Attribute name have specific code and that will be identified using that under bracket. like for color we use [CLR]. And values you can put in list for now.

TASK 3 UPDATE
attribute list: [{‘CLR’: [‘RED’, ‘BLUE’, ‘GREEN’]}, {‘MEM’: [‘16GB’, ‘64GB’, ‘128GB’]}]
Pattern: ‘IPHONE [CLR]-[MEM]’
You guys need to create the one function and pass above two parameters then output like below. Order of list can be any.
IPHONE RED-16GB
IPHONE BLUE-16GB
IPHONE GREN-16GB
IPHONE RED-64GB
IPHONE BLUE-64GB
IPHONE GREN-64GB
IPHONE RED-128GB
IPHONE BLUE-128GB
IPHONE GREN-128GB
