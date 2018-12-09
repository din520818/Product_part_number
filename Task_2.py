'''Task 2 
Write one program in any language (which you know) to generate the part number.
Assume we have one product called 'Apple Iphone', now iphone have different variant.
Color [CLR] = Red, Blue, Green
Ram [RM] = 1Gb, 2Gb
Space [SPC] = 16gb, 64gb, 128gb'''

def fun(d,j):

    #Enter the part no pattern here
    part_no_patt="IPHONE [CLR]-[RM]-[SPC]"

    part_no_patt = part_no_patt.replace('[CLR]' , d[j][0]).replace('[RM]' , d[j][1]).replace('[SPC]' , d[j][2])
    return part_no_patt

cl = ["Red", "Blue", "Green"]
ra = ["1 GB", "2 GB"]
sp = ["16 GB", "64 GB", "128 GB"]

c = [[x,y,z] for x in cl for y in ra for z in sp]

for i in range(0,18):
    print(fun(c,i))
