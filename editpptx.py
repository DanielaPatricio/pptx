from pptx import Presentation
from pptx.util import Cm

prs = Presentation('testprs.pptx')

for slide in prs.slides:
     for shape in slide.shapes:
         shape.height = Cm(15)
         shape.width = Cm(15)
         shape.left = round((prs.slide_width - shape.width) / 2)
         shape.top = round((prs.slide_height - shape.height) / 2)

         print(prs.slide_height - shape.width /2)

prs.save('testprs.pptx')




