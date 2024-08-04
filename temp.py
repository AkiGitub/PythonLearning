from fpdf import FPDF
from PIL import Image

class clsShirticate:
    def __init__(self,imgName):
         self._imageName = imgName
         self._pdf = FPDF(orientation="P", unit="mm", format="A4")
         self._pdf.add_page()
    
    def putTextinPDF(self,text,fontSize,tupleColor,locY):
        self._pdf.set_font("Helvetica", "B" ,size=fontSize)
        self._pdf.set_text_color(tupleColor)
        widthText = self._pdf.get_string_width(text)
        xloc = self._pdf.w/2 -  (widthText/2)
        self._pdf.set_xy(xloc,locY)
        self._pdf.cell(widthText,text=text,border=0,align='C')

#put image in the center of pdf---------
    def putImageinCenter(self):
        #get pdf width
        widthPDF =  self._pdf.w

        #get image w,h
        w_img ,h_img =self.getImageDimensions_mm()

        locXimg = (widthPDF - w_img) / 2

        self._pdf.image(self._imageName,x=locXimg,y=80,w=w_img)
       


#read and get image dim in (mm)----------
    def getImageDimensions_mm(self):
        with Image.open(self._imageName) as img:
            wImg, hImg = img.size

        widthImg_mm, heighImg_mm =wImg * 25.4 / 96, hImg * 25.4 / 96

        return widthImg_mm, heighImg_mm

    @classmethod
    def readName(self):
        return input('Name:')

def main():
    ss= r'D:\Learning Docs\EDX\Code\Lecture1\PythonLeaning\Standard_Package\pdf'

    objShirtCase = clsShirticate(ss+'\\shirtificate.png')

    objShirtCase.putImageinCenter()

    objShirtCase.putTextinPDF('CS50 Shirtificate',fontSize=50,tupleColor=(0,0,0),locY=30)

    objShirtCase.putTextinPDF(clsShirticate.readName()+ ' took CS50',fontSize=30,tupleColor=(255,255,255),locY=120)

    objShirtCase._pdf.output('D:\\temp\\out.pdf')
    
if __name__== '__main__':
    main()

