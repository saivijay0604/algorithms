import sys
from PIL import Image
from numpy import *
from numpy.core.tests.test_mem_overlap import *
import pytest
from range import *

im1 = Image.open(r"C:\Users\saivi\Desktop\photos\amma.jpg")
im2 = Image.open(r"C:\Users\saivi\Desktop\photos\me.JPG")
im1.show()
im2.show()


def get_concat_h(im1, im2):
    dst = Image.new('RGB', (im1.width + im2.width, im1.height))
    dst.paste(im1, (0, 0))
    dst.paste(im2, (im1.width, 0))
    return dst

def get_concat_v(im1, im2):
    dst = Image.new('RGB', (im1.width, im1.height + im2.height))
    dst.paste(im1, (0, 0))
    dst.paste(im2, (0, im1.height))
    return dst

h=get_concat_h(im1, im2).save(r"C:\Users\saivi\Desktop\photos/h.jpg")
v=get_concat_v(im2, im1).save(r"C:\Users\saivi\Desktop\photos/v.jpg")
h=Image.open(r"C:\Users\saivi\Desktop\photos/h.jpg")
v=Image.open(r"C:\Users\saivi\Desktop\photos/h.jpg")
h.show()
v.show()
