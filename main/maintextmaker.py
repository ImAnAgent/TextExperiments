from PIL import Image, ImageDraw,ImageFont
import os
import random
import cv2
import numpy as np
from skimage.util import random_noise

alphabet=[u"A",u"a",u"B",u"b",u"C",u"c",u"Ç",u"ç",u"D",u"d",u"E",u"e",u"Ə",u"ə",u"F",u"f",
          u"G",u"g",u"Ğ",u"ğ",u"H",u"h",u"X",u"x",u"I",u"ı",u"İ",u"i",u"J",u"j",u"K",u"k",u"Q",u"q",u"L",u"l",u"M",u"m",u"N",u"n",u"O",u"o",u"Ö",u"ö",u"P",u"p",u"R",u"r",u"S",u"s",u"Ş",u"ş",u"T",u"t",u"U",u"u",u"Ü",u"ü",u"V",u"v",u"Y",u"y",u"Z",u"z"]
#alphabet=[u"a"]
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
#Remember to comment out the colours that you do not need!
tracked = 0

def random_boolean():
    true_or_false = random.getrandbits(1)
    return bool(true_or_false)

for letter in alphabet:
    for font_name in font_names:
        for color_name, rgb in colourdict.items():
            tracked += 1
            
            #These are the specifications of the image.
            new=Image.new('RGB',(200,200),color=(rgb[0],rgb[1],rgb[2]))

            #This is here because pillow's default fonts only work for ascii characters. This is why we must use a unicode font.
            unicode_font = ImageFont.truetype(os.path.join("fonts",font_name), 40) 

            d=ImageDraw.Draw(new)
            w,h=d.textsize(letter,font=unicode_font)
            d.text(((W-w)/2,(H-h)/2),letter,font=unicode_font,fill=(0,0,0))
            
            if tracked % 2 == 0:
                #This next bit that is commented out is here as an option for the random squiggles.
                #for times in range(0,random.randrange(0,5)):
                    #d.line([random.randrange(0, W),random.randrange(0, H),W/2,H/2], fill=128)
                
                order = random_boolean()
                if order==True:
                    d.line([W/2,0,W/2,H], fill=128) #This part is for drawing orderly grid lines with a cross. Maybe I could make some sort of loop to generate it, but I think that might end up being a bit confusing.
                    d.line([W/4,0,W/4,H], fill=128)
                    d.line([3*W/4,0,3*W/4,H], fill=128)
                    d.line((0, H/2, W, H/2), fill=128)
                    d.line((0, H/4, W, H/4), fill=128)
                    d.line((0, 3*H/4, W, 3*H/4), fill=128)
                    d.line((0, H, W, 0), fill=128)
                    d.line((0, 0, W, H), fill=128)
                else:
                    d.line([random.randrange(0, W),random.randrange(0, H),W/2,H/2,W,H,random.randrange(0, W),random.randrange(0, H),random.randrange(0, W),random.randrange(0, H),W/2,H/2,random.randrange(0, W),random.randrange(0, H),random.randrange(0, W),random.randrange(0, H)], fill=128) # I can make random squiggles like this and make sure that they pass through the origin
                new.save(os.path.join("results", f" {letter}-{color_name}-{font_name}.png"))
            else:
                path=os.path.join("results", f" {letter}-{color_name}-{font_name}.png")
                new.save(path)
                new = cv2.imread(path)
                noise=random_boolean()
                if noise==True:
                    modes=['s&p','poisson','gaussian','speckle']
                    strengths={400,500}
                    salt_pepper_ratios={0.8,0.2,0.5,0.3}


                    for i in range(0,len(modes)): # I am looping through all of the changeable characteristics of the noise.
                        if modes[i]=='s&p':
                            
                            for ratio in salt_pepper_ratios:#These features are only available for the salt and pepper.
                                strength=400
                                amount1=random.uniform(0.2, 0.4)
                                noise_img = random_noise(new, mode=modes[i],amount=amount1,salt_vs_pepper=ratio,seed=random.randint(100,200))
                                noise_img = np.array(strength*noise_img, dtype = 'uint8')
                                extra=f"--ratio_{ratio}--amount_{round(amount,2)}.jpg" #because in the name there is now a randomly generated variable, I recommend deleting the results folder and remaking it each time the program is run.
                                Image.fromarray(noise_img).save(os.path.join("results", f" {letter}-{color_name}-{font_name}--{modes[i]}"+extra))#This is saving the files using pillow.
                        else:
                            extra=".jpg" #This is for the other noise types
                            for strength in strengths:
                                noise_img = random_noise(new, mode=modes[i])
                                noise_img = np.array(strength*noise_img, dtype = 'uint8')#I know this line is repeating, but I do not know whether it is worth making a separate function for it.
                                Image.fromarray(noise_img).save(os.path.join("results", f" {letter}-{color_name}-{font_name}--{modes[i]}--noise_multiplier_{strength}"+extra))
                
                
