from PIL import Image, ImageDraw, ImageFont

def generate(ls,size,name):
    #INIT
    space=int(size/3)
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
                nb=color-int(nbo)*24
                if nb<0:
                    nb=0
                __draw_rectangle(img,x,y,space,space,(251, nb, 0))
                __draw_text(img,str(2**nbo),x,y,space,50)
            x+=space
        y+=space
    
    img.save(f"fonction/Game/2038/{str(name)}.png")

def __draw_rectangle(img,x,y,width,height,bg):
    #shape = ((x1,y2) , (x2,y2))
    """
         (x1,y1)
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

#generate([[1,6,5]],400,"ok.png")