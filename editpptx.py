from pptx import Presentation
from pptx.util import Cm

prs = Presentation('testprs.pptx')

for slide in prs.slides:
     for shape in slide.shapes:
         shape.height = Cm(15)
         shape.width = Cm(15)

prs.save('testprs.pptx')




