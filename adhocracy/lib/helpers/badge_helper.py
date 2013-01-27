from base64 import b64encode
import StringIO
from PIL import Image, ImageDraw


def generate_thumbnail_tag(badge, height="48", width="48"):
    """returns string with the badge thumbnail img tag
    """
    heigth = height
    width = width
    #TODO resize and get mimetype from PIL, joka
    #TODO cache, joka
    #TODO test, joka
    #TODO config option to set default width/height, joka
    #TODO what todo if no colour and no thumbnail?, joka
    mimetype = "image/png"
    img_template = """<img src="data:%s;base64,%s" height="%s" width="%s" />"""
    data = badge.thumbnail
    colour = badge.color or u"#ffffff"
    if not data:
        im = Image.new('RGB', (10, 10))
        draw = ImageDraw.Draw(im)
        draw.rectangle((0, 0, 10, 10), fill=colour, outline=colour)
        f = StringIO.StringIO()
        im.save(f, "PNG")
        data = f.getvalue()
        del draw, im, f
    data_enc = b64encode(data)
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
