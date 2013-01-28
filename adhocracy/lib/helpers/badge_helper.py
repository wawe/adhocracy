from base64 import b64encode
import StringIO
from PIL import Image, ImageDraw


def generate_thumbnail_tag(badge, height="48", width="48"):
    """returns string with the badge thumbnail img tag
    """
    heigth = height
    width = width
    #TODO cache, joka
    #TODO config option to set default width/height, joka
    #TODO Generated image is not Working with IE < 8, joka

    img_template = """<img src="data:%s;base64,%s" height="%s" width="%s" />"""
    imagefile = StringIO.StringIO(badge.thumbnail)
    mimetype = "image/png"
    try:
        im = Image.open(imagefile)
        mimetype = "image/" + im.format.lower()
        im.thumbnail((width, heigth), Image.ANTIALIAS)
    except  IOError:
        colour = badge.color or u"#ffffff"
        im = Image.new('RGB', (10, 10))
        draw = ImageDraw.Draw(im)
        draw.rectangle((0, 0, 10, 10), fill=colour, outline=colour)
        f = StringIO.StringIO()
        im.save(f, "PNG")
        imagefile = f
        del draw, im
    data_enc = b64encode(imagefile.getvalue())
    del imagefile
    return (img_template % (mimetype, data_enc, heigth, width))


def get_parent_badges(badge):
    """Returns a generator with all parent badges
       in hierachical order (root last)
    """
    if hasattr(badge, "parent") and badge.parent:
        parent = badge.parent
        yield parent
        for p in get_parent_badges(parent):
            yield p
