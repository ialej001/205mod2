def simplePic():
  pic = makePicture(pickAFile())
    
  newPic = shrink(pic)

  show(newPic)
  
# shrinks image by half
def shrink(pic):
  picWidth = getWidth(pic)
  picHeight = getHeight(pic)
  x2 = 0
  y2 = 0
  
  shrunkPic = makeEmptyPicture(picWidth/2, picHeight/2)
  
  for x in range (0, picWidth, 2):
    for y in range (0, picHeight, 2):
      currentPixel = getPixel(pic, x, y)
      newPixel = getPixel(shrunkPic, x2, y2)
      pixelColor = getColor(currentPixel)
      setColor(newPixel, pixelColor)
      y2 = y2 + 1
    x2 = x2 + 1

  
  return shrunkPic
