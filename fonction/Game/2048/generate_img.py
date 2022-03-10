from PIL import Image, ImageDraw, ImageFont

def generate(ls,size):
    #INIT
    space=int(size/4)
    mode="RGB"
    size=(size,size)
    color=(33,33,33)
    img = Image.new(mode, size, color)
    
    #Cube
    color=200
    y=0
    for line in ls:
        x=0
        for nbo in line:
            if nbo != 0:
                nb=color-int(nbo)*13
                if nb<0:
                    nb=0
                __draw_rectangle(img,x,y,space,space,(251, nb, 0))
                __draw_text(img,str(2**nbo),x,y,space,80)
            x+=space
        y+=space
    
    img.save("fonction/Game/2048/image.png")

def __draw_rectangle(img,x,y,width,height,bg):
    #shape = ((x1,y2) , (x2,y2))
    """
         (x1,y1
            +------------
            |           |
            |           |
            |           |
            ------------+ (x2,y2)
    """
    shape=((x,y),(x+width,y+height))
    img1 = ImageDraw.Draw(img)
    img1.rectangle(shape,fill=bg)

def __draw_text(img,text,x,y,space,size):
    img1 = ImageDraw.Draw(img)
    font = ImageFont.truetype("arial.ttf", size)
    d=font.getsize(text)
    img1.text((x+((space-d[0])/2),((y+(space-d[1])/2))),text,align="left",font=font)

#generate([[1,2,0,0]],1000)