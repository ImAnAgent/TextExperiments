from PIL import Image, ImageDraw,ImageFont
import os
import random
import numpy as np
from skimage.util import random_noise

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

W,H=(200,200)

colourdict = {
  "white":[255,255,255],
  "grey":[225,225,225],
"light_blue":[171,255,245],
"green":[0,255,0],
"blue":[0,0,255],
#  "yellow":[255,255,0]
# "red":[255,0,0],
}

tracked = 0
image_saved=0

for letter in alphabet:
    for font_name in font_names:

        tracked += 1
        
        new=Image.new('RGB',(200,200),(255,255,255))

        unicode_font = ImageFont.truetype(os.path.join("fonts",font_name), 40) 

        d=ImageDraw.Draw(new)
        w,h=d.textsize(letter,font=unicode_font)
        d.text(((W-w)/2,(H-h)/2),letter,font=unicode_font,fill=(0,0,0))
        if letter.isupper():
            path = f"smallresults/{letter}-capital/{letter}-{font_name}.png"
        else:
            path = f"smallresults/{letter}/{letter}-{font_name}.png"

        try:
            new.save(path)
        except:
            if letter.isupper():
                os.makedirs(f"smallresults/{letter}-capital")
            else:
                os.makedirs(f"smallresults/{letter}")
            new.save(path)
        image_saved+=1
        
        if tracked % 3 == 0:
            
            if tracked % 6 == 0:
                d.line([W/2,0,W/2,H], fill=128)
                d.line([W/4,0,W/4,H], fill=128)
                d.line([3*W/4,0,3*W/4,H], fill=128)
                d.line((0, H/2, W, H/2), fill=128)
                d.line((0, H/4, W, H/4), fill=128)
                d.line((0, 3*H/4, W, 3*H/4), fill=128)
                d.line((0, H, W, 0), fill=128)
                d.line((0, 0, W, H), fill=128)
            else:
                d.line([random.randrange(0, W),random.randrange(0, H),W/2,H/2,W,H,random.randrange(0, W),random.randrange(0, H),random.randrange(0, W),random.randrange(0, H),W/2,H/2,random.randrange(0, W),random.randrange(0, H),random.randrange(0, W),random.randrange(0, H)], fill=128)
            new.save(path)
            image_saved+=1
        else:
            new.save(path)
            image_saved+=1
            new = Image.open(path)
            # convert to ndarray
            img_array = np.array(new)
            
            modes=['poisson','gaussian','speckle']
            strengths={400,500}

            for i in range(0,len(modes)):
                for strength in strengths:
                    noise_img = random_noise(img_array, mode=modes[i])
                    noise_img = np.array(strength*noise_img, dtype = 'uint8')
                    extra=f"--{modes[i]}--noise_multiplier_{strength}.jpg"
                    Image.fromarray(noise_img).save(path+extra)
                    image_saved+=1
