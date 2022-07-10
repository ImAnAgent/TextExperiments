from PIL import Image, ImageDraw,ImageFont
alphabet=[u"A",u"a",u"B",u"b",u"C",u"c",u"Ç",u"ç",u"D",u"d",u"E",u"e",u"Ə",u"ə",u"F",u"f",
          u"G",u"g",u"Ğ",u"ğ",u"H",u"h",u"X",u"x",u"I",u"ı",u"İ",u"i",u"J",u"j",u"K",u"k",u"Q",u"q",u"L",u"l",u"M",u"m",u"N",u"n",u"O",u"o",u"Ö",u"ö",u"P",u"p",u"R",u"r",u"S",u"s",u"Ş",u"ş",u"T",u"t",u"U",u"u",u"Ü",u"ü",u"V",u"v",u"Y",u"y",u"Z",u"z"]

font_names=["DejaVuSans.ttf","DejaVuSans-Oblique.ttf","dejavu-sans.condensed-bold-oblique.ttf","dejavu-sans.condensed-bold.ttf","UKIJTuzBold.ttf","TruetypewriterPolyglott-mELa.ttf","UKIJMoyQ.ttf","FreeSansBold.ttf","Abel-Bold.otf",
            "Abel-Regular.otf","Acidic.otf","Agency-Bold.ttf","Agency-Regular.ttf","Alboroto.otf","Aldo.ttf","Algerian.otf","Amydor.otf","Ambassadore-Bold-Italic.otf","Ambassadore-Bold.otf","Ambassadore-Italic.otf","Ambassadore-Regular.otf"
           ,"Antonio-Bold.otf","Antonio-Light.otf","Antonio-Regular.otf","Arch-Bold-Condensed.otf","Arch-Bold.otf","Arch-Condensed.otf","Arch-Light-Condensed.otf","Arch-Light.otf","Arch-Regular.otf",
           "ArialNU.otf","Arkitextura.otf","Arrus-Black.ttf","Arrus-Bold-Italic.ttf","Arrus-Bold.ttf","Arrus-Italic.ttf","Arrus.ttf","ArtfulBeauty.otf"
           ,"AllegroScript.otf","AlwaysRadio.ttf","AmericanCaptain.otf","AnabelleScript.otf","Anglecia-Pro-Display.otf","AphroditeSlimPro.otf","ArgoHvy-Bold-Italic.otf","ArgoHvy-Bold.otf","ArgoHvy-Italic.otf","ArgoHvy.otf",
           "Banjax-Bold-Italic.otf","Banjax-Bold.otf","Banjax-ExtraBold-Italic.otf","Banjax-ExtraBold.otf","Banjax-ExtraLight-Italic.otf","Banjax-ExtraLight.otf","Banjax-Italic.otf","Banjax-Light-Italic.otf","Banjax-Light.otf","Banjax-Medium-Italic.otf",
           "Banjax-Medium.otf","Banjax-Regular.otf","Banjax-UltraBlack-Italic.otf","Banjax-UltraBlack.otf","Barmeno-ExtraBold.otf","Barmeno-Medium.otf","Baskerville-Bold-Italic.otf","Baskerville-Bold.otf","Baskerville-Italic.otf","Baskerville.otf",
           "BebasNeue-Bold.otf","BebasNeue-Book.otf","BebasNeue-Light.otf","BebasNeue-Thin.otf","Belwe-Bold.otf","Belwe-Condensed-Bold.otf","Belwe-Light.otf","Belwe-Medium.otf","Beradon-Script.otf","BickhamScriptPro-Bold.otf","BickhamScriptPro-Regular.otf"
           ,"BickhamScriptPro-Semibold.otf","Bifur.otf","Brandon-Black.otf","Brandon-Bold.otf","Brandon-Double.otf","Brandon-Inline.otf","Brandon-Medium.otf","Brandon-One.otf","Brandon-OneShadow.otf","Brandon-Regular.otf","Brandon-Shadow.otf","Brandon-TextBlack.otf"
           , "Brandon-TextBold.otf","Brandon-TextMedium.otf","Brandon-TextRegular.otf","Brandon-Two.otf","Brandon-TwoShadow.otf","Break-Fill-Bold.otf","Break-Fill-Extralight.otf","Break-Fill-Light.otf","Break-Fill-Regular.otf","Break-Fill-Semibold.otf"
           ,"Callista.otf","Cambalache-Bold.otf","Cambalache-Light.otf","Cambalache.otf","Cambria-Lite-Bold-Italic.ttf","Cambria-Lite-Bold.ttf","Cambria-Lite-Italic.ttf","Cambria-Lite.ttf","Canter-Bold.otf","Canter-Light.otf","Carrington.ttf",
           "Centurion.otf","Cera-Stencil-Bold.otf","Cera-Stencil-Medium.otf","Chelsea.otf","Cicek.otf","Cinzel-Black.otf","Cinzel-Bold.otf","Cinzel-Regular.otf","CinzelDecorative-Black.otf","CinzelDecorative-Bold.otf","CinzelDecorative-Regular.otf",
           "CirceRounded-Alt-Bold.otf","CirceRounded-Alt-ExtraBold.otf","CirceRounded-Bold.otf","CirceRounded-ExtraBold.otf","CirceRounded-ExtraLight.otf","CirceRounded-Light.otf","CirceRounded-Regular.otf","CirceRounded-Thin.otf","Co-Headline-Regular.otf",
           "Co-text.otf","Coal-Hand-Luke.ttf","ClearSans-Bold.otf","ClearSans-BoldItalic.otf","ClearSans-Italic.otf","ClearSans-Italic.otf","ClearSans-Light.otf","Cooper.otf","Copperplate.otf","Cormac-Black.otf","Cormac-ExtraLight.otf","CQ-Mono.otf","ClearSans-MediumItalic.otf",
           "ClearSans-Regular.otf","ClearSans-Thin.otf","Cocomat-Light.otf","Colo-Pro-Black.otf","Colo-Pro-Inline.otf","Comfortaa-Bold.otf","Comfortaa-Light.otf","Comfortaa-Regular.otf"]#153 font types
#print(len(font_names))

#alphabet=["a","b","c"]
#alphabet=[u"Ə"]
W,H=(200,200)

colourdict = {
    "white":[255,255,255],
    "grey":[225,225,225],
  "light_blue":[171,255,245],
   "red":[255,0,0],
  "green":[0,255,0],
    "blue":[0,0,255],
    "yellow":[255,255,0]
}
#This dictionary is how I am dealing with the background colours 

#And this is a dictionary that I am using for now for testing if the font types work:
colourdict = {
    "white":[255,255,255]}
import os

for i in range(0,len(alphabet)): #Here I am creating a loop in which I take all of the letters of the alphabet and use them in pillow
    for my_font in range(0,len(font_names)):
        for colour_name, the_colour in colourdict.items():
            #print(the_colour)
            #text=input("enter text here... ")
            text=alphabet[i]
            
            
            new=Image.new('RGB',(200,200),color=(the_colour[0],the_colour[1],the_colour[2]))#These are the specifications of the image.
 
            unicode_font = ImageFont.truetype(os.path.join("fonts",font_names[my_font]), 40) #This is here because pillow's default fonts only work for ascii characters. This is why we must use a unicode font.

            d=ImageDraw.Draw(new)
            w,h=d.textsize(text,font=unicode_font)
            d.text(((W-w)/2,(H-h)/2),text,font=unicode_font,fill=(0,0,0))#putting the text on the screen.



            new.save(os.path.join("results", alphabet[i]+font_names[my_font]+colour_name+".png"))#saving the files
            #new.show()
