import os, sys
from PIL import Image, ImageDraw, ImageFont
args = sys.argv[1:]

#Outputs a twitter thumbnail (High res)

if len(args) > 1:
    titlesize = 130
    titlefont = ImageFont.truetype("Tests/fonts/NotoSans-Regular.ttf", titlesize)
    #Adjust title font size to accommodate its length
    while (titlefont.getsize(args[1])[0] > 1000):
        titlesize -= 1
        if (titlesize < 10):
            print("Title too long!")
            sys.exit()
        titlefont = ImageFont.truetype("Tests/fonts/NotoSans-Regular.ttf", titlesize)

    tagsize = 80
    tagfont = ImageFont.truetype("Tests/fonts/NotoSans-Regular.ttf", tagsize)
    #Adjust tag font size to accommodate the length of the longest tag
    #First find the longest tag
    longestarg = args[2]
    for i in args[3:]:
        if len(i) > len(longestarg):
            longestarg = i
    #Then do the same thing as for the title
    while (tagfont.getsize(longestarg)[0] > 1000):
        tagsize -= 1
        if (tagsize < 10):
            print("Tag too long!")
            sys.exit()
        tagfont = ImageFont.truetype("Tests/fonts/NotoSans-Regular.ttf", tagsize)

    infile = args[0]
    outfile = args[1] + "_thumbnail_twitter.png"
    if infile != outfile:
        try:
            with Image.open(infile) as im:
                #print(im.format, im.size, im.mode) #for debug
                im = im.resize((1080,1080)) #resize if necessary
                layer = Image.new("RGB", (1080,1080), (255,255,255)) #create a pure white layer
                im = Image.blend(im, layer, 0.85) #blend them to make image slightly faded
                if len(args) > 2: #if there's tags
                    tagstring = ""
                    for i in args[2:]:
                        tagstring += i + "\n" #cook a big ol' string of them
                    #print(tagstring) #for debug
                    d = ImageDraw.Draw(im) #draw title and tags
                    d.text((540,164), args[1], fill="black",anchor="ms", font=titlefont)
                    d.multiline_text((540,300), tagstring, fill = "black", anchor = "ms",spacing = 4, font=tagfont) 

                else:
                    #draw just title
                    d = ImageDraw.Draw(im)
                    d.text((432,432), args[1], fill="black",anchor="ms", font=titlefont)
                im.save(outfile, "PNG")
        except OSError:
            print("ERROR: cannot create thumbnail for", infile)

#output an FA thumbnail (low res)

if len(args) > 1:
    titlesize = 30
    titlefont = ImageFont.truetype("Tests/fonts/NotoSans-Regular.ttf", titlesize)
    #Adjust title font size to accommodate its length
    while (titlefont.getsize(args[1])[0] > 230):
        titlesize -= 1
        if (titlesize < 10):
            print("Title too long!")
            sys.exit()
        titlefont = ImageFont.truetype("Tests/fonts/NotoSans-Regular.ttf", titlesize)

    tagsize = 25
    tagfont = ImageFont.truetype("Tests/fonts/NotoSans-Regular.ttf", 25)
    #Adjust tag font size to accommodate the length of the longest tag
    #First find the longest tag
    longestarg = args[2]
    for i in args[3:]:
        if len(i) > len(longestarg):
            longestarg = i
    #Then do the same thing as for the title
    while (tagfont.getsize(longestarg)[0] > 230):
        tagsize -= 1
        if (tagsize < 10):
            print("Tag too long!")
            sys.exit()
        tagfont = ImageFont.truetype("Tests/fonts/NotoSans-Regular.ttf", tagsize)

    infile = args[0]
    outfile = args[1] + "_thumbnail.png"
    if infile != outfile:
        try:
            with Image.open(infile) as im:
                #print(im.format, im.size, im.mode) #for debug
                im = im.resize((250,250)) #resize if necessary
                layer = Image.new("RGB", (250,250), (255,255,255)) #create a pure white layer
                im = Image.blend(im, layer, 0.9) #blend them to make image slightly faded
                if len(args) > 2: #if there's tags
                    tagstring = ""
                    for i in args[2:]:
                        tagstring += i + "\n" #cook a big ol' string of them
                    #print(tagstring) #for debug
                    d = ImageDraw.Draw(im) #draw title and tags
                    d.text((125,38), args[1], fill="black",anchor="ms", font=titlefont)
                    d.multiline_text((125, 75), tagstring, fill = "black", anchor = "ms",spacing = 4, font=tagfont) 

                else:
                    #draw just title
                    d = ImageDraw.Draw(im)
                    d.text((100,100), args[1], fill="black",anchor="ms", font=titlefont)
                im.save(outfile, "PNG")
        except OSError:
            print("ERROR: cannot create thumbnail for", infile)

else:
    print("Usage: thumbnailer2.py <image> <title> <tags (optional)>")


    