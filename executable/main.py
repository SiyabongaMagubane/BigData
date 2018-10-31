from LZW_compressionAlgorithm import *
from helpers import *

if __name__ == "__main__":

    LZW = LZW_compression()
    image = Image.open("GPS.bmp")
    ArrayImage = numpy.array(image)
    rows,cols,channel = ArrayImage.shape
    #cv2.imshow('image_original',ArrayImage)
    img_b , img_g , img_r = cv2.split(ArrayImage)
    print(img_b.shape)
    WriteOriginal("original_red.csv",img_r)
    WriteOriginal("original_green.csv",img_g)
    WriteOriginal("original_blue.csv",img_b)

    print("File sizes of matrix RGB original: ")
    print(findsize("original_red.csv"))
    print(findsize("original_green.csv"))
    print(findsize("original_blue.csv"))

    img_b = LZW.compression(img_b)
    img_g = LZW.compression(img_g)
    img_r = LZW.compression(img_r)

    print("File sizes of matrix RGB compressed: ")
    WriteToCSV(img_b,"blue.csv")
    WriteToCSV(img_g,"green.csv")
    WriteToCSV(img_r,"red.csv")

    print(findsize("red.csv"))
    print(findsize("green.csv"))
    print(findsize("blue.csv"))

    rgb = numpy.dstack((img_b,img_g,img_r))
    cv2.imwrite('encoded_img.bmp',rgb)

    img_b = LZW.decompression(img_b)
    img_g = LZW.decompression(img_g)
    img_r = LZW.decompression(img_r)

    print("File sizes of matrix RGB decompressed: ")
    WriteToCSV(img_b,"blue_decompressed.csv")
    WriteToCSV(img_g,"green_decompressed.csv")
    WriteToCSV(img_r,"red_decompressed.csv")

    print(findsize("red_decompressed.csv"))
    print(findsize("green_decompressed.csv"))
    print(findsize("blue_decompressed.csv"))

    rgb = numpy.dstack((img_b,img_g,img_r))
    cv2.imwrite('decoded_img.bmp',rgb)
	#cv2.imshow('encoded_img.bmp',rgb)
	#cv2.waitKey(0)
	#cv2.destroyAllWindows()
	#print(img_g)
	#print(img_b)
	#img = cv2.imread(Image_)
	#cv2.imshow('image_original' , img)
	#cv2.waitKey(0)
	#cv2.destroyAllWindows()
	#ArrayImage = numpy.asmatrix(ArrayImage)
	#for i in ArrayImage:
		#print(i) 