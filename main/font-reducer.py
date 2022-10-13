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
           "ClearSans-Regular.otf","ClearSans-Thin.otf","Cocomat-Light.otf","Colo-Pro-Black.otf","Colo-Pro-Inline.otf","Comfortaa-Bold.otf","Comfortaa-Light.otf","Comfortaa-Regular.otf"]

# Loop through font_names and remove bold, italic, and condensed fonts, keeping only the main one
for font_name in font_names:
    font = font_name.lower()
    if "light" in font or "thin" in font or "italic" in font or "condensed" in font:
        font_names.remove(font_name)

print(font_names)
print(len(font_names))