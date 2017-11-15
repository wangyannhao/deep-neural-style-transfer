from PIL import Image

if __name__=='__main__':

	for i in range(1,61):
		pic_name = 'in'+str(i)+'.png'
		im = Image.open(pic_name)
		width, height = im.size
		im = im.resize((width/2, height/2), Image.ANTIALIAS)
		im.save(pic_name)