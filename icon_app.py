
import os
from PIL import Image, ImageFilter

imagePath = input(r'请输入原icon的文件路径').strip()
rootPath = input(r'请输入要保存的文件路径').strip()



def createSizeImage(*,image,width,height,rootPath):
    img_resize = image.resize((width, height))
    img_resize.save(rootPath+'/{width}x{height}.png'.format(width=width,height=height))
    img_resize_lanczos = image.resize((width, height), Image.LANCZOS)
    img_resize_lanczos.save(rootPath+'/{width}x{height}.png'.format(width=width,height=height))

#删除alpha通道
def remove_transparency(im, bg_colour=(255, 255, 255)):

    # Only process if image has transparency (http://stackoverflow.com/a/1963146)
    if im.mode in ('RGBA', 'LA') or (im.mode == 'P' and 'transparency' in im.info):

        # Need to convert to RGBA if LA format due to a bug in PIL (http://stackoverflow.com/a/1963146)
        alpha = im.convert('RGBA').split()[-1]

        # Create a new background image of our matt color.
        # Must be RGBA because paste requires both images have the same format
        # (http://stackoverflow.com/a/8720632  and  http://stackoverflow.com/a/9459208)
        bg = Image.new("RGBA", im.size, bg_colour + (255,))
        bg.paste(im, mask=alpha)
        return bg

    else:
        return im

img = Image.open(imagePath)
noAlphaImage = remove_transparency(img)
createSizeImage(image=noAlphaImage,width=20,height=20,rootPath=rootPath)
createSizeImage(image=noAlphaImage,width=29,height=29,rootPath=rootPath)
createSizeImage(image=noAlphaImage,width=40,height=40,rootPath=rootPath)
createSizeImage(image=noAlphaImage,width=58,height=58,rootPath=rootPath)
createSizeImage(image=noAlphaImage,width=60,height=60,rootPath=rootPath)
createSizeImage(image=noAlphaImage,width=76,height=76,rootPath=rootPath)
createSizeImage(image=noAlphaImage,width=80,height=80,rootPath=rootPath)
createSizeImage(image=noAlphaImage,width=87,height=87,rootPath=rootPath)
createSizeImage(image=noAlphaImage,width=116,height=116,rootPath=rootPath)
createSizeImage(image=noAlphaImage,width=120,height=120,rootPath=rootPath)
createSizeImage(image=noAlphaImage,width=152,height=152,rootPath=rootPath)
createSizeImage(image=noAlphaImage,width=167,height=167,rootPath=rootPath)
createSizeImage(image=noAlphaImage,width=180,height=180,rootPath=rootPath)
createSizeImage(image=noAlphaImage,width=512,height=512,rootPath=rootPath)
createSizeImage(image=noAlphaImage,width=1024,height=1024,rootPath=rootPath)
createSizeImage(image=noAlphaImage,width=2048,height=2048,rootPath=rootPath)
createSizeImage(image=noAlphaImage,width=300,height=500,rootPath=rootPath)
createSizeImage(image=noAlphaImage,width=600,height=1000,rootPath=rootPath)
createSizeImage(image=noAlphaImage,width=1800,height=3000,rootPath=rootPath)