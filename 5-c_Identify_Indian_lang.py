#Identify the Indian language of a text

#!pip install torch==1.3.1+cpu -f https://download.pytorch.org/whl/torch_stable.html
#!pip install inltk
#!pip install tornado==4.5.3
from inltk.inltk import setup
setup('gu')
from inltk.inltk import identify_language
#Identify the language of given text
identify_language('બીના કાપડિયા')


#Output:
#gujarati