import pdfminer
from pdfminer.layout import LTImage, LTContainer
from pdfminer.image import ImageWriter
from pdfminer.high_level import extract_pages

pages = list(extract_pages('samplei.pdf'))
page = pages[0]


def get_image(layout_object):
    if isinstance(layout_object, pdfminer.layout.LTImage):
        return layout_object
    if isinstance(layout_object, pdfminer.layout.LTContainer):
        for child in layout_object:
            return get_image(child)
    else:
        return None


def save_images_from_page(page: pdfminer.layout.LTPage):
    images = list(filter(bool, map(get_image, page)))
    iw = ImageWriter('C:\Users\HP\OneDrive\Desktop\project')
    for image in images:
        iw.export_image(image)


save_images_from_page(page)