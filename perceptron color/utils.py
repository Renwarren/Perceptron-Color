

#hsl = hue, saturation, luminosity
def get_luminosity(rgb):
    red = rgb[0] /255
    green = rgb[1] /255
    blue = rgb[2] /255

    Cmax = max(red,green,blue)
    Cmin = min(red,green,blue)

    return round((Cmax + Cmin)/2,1)

def isBright(luminosity):
    if luminosity >= 0.5:
        return True
    return False

