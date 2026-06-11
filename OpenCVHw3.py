import cv2

image1 = cv2.imread("Images/Anatomy_Of_Human.jpg", 1)
#Loads the image
cv2.imshow("First Image", image1)
#shows the image with a window title

cv2.waitKey(0)

LineStartingPoint = (215, 76)
EndingPoint = (285, 76)
#This gives the starting point and ending point of the line which will be drawn
Colour = (0, 0, 255)
#the colour of the line
Thickness = 5
#how thick the line is

Font = cv2.FONT_HERSHEY_COMPLEX
#this decides the font of the letters. I don't know what font this is.
TextStartingPoint = (290, 76)
FontScale = 1
#it is 100% of the size of the font. 
Colour = (0, 0, 255)
Thickness = 1
image1 = cv2.putText(image1, "Eye", TextStartingPoint, Font, FontScale, Colour, Thickness)

image1 = cv2.line(image1, LineStartingPoint, EndingPoint, Colour, Thickness)
#This creates the line on the image.

cv2.imshow("Label anatomy", image1)

cv2.waitKey(0)
#it will hold the window until the user presses a key
cv2.destroyAllWindows()
#it will destroy all windows