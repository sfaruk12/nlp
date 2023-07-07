
#Import NLP Libraries for Indian Languages and perform:
#Note: Execute this practical in https://colab.research.google.com/

#pip install torch==1.13.1+cpu -f https://download.pytorch.org/whl/torch_stable.html
#pip install inltk
#pip install tornado==4.5.3

from inltk.inltk import setup
setup('hi')
from inltk.inltk import tokenize
hindi_text = """प्राकृ तिक भाषा सीखना बहुि तिलचस्प है।"""
# tokenize(input text, language code)
tokenize(hindi_text, "hi")

#output
#['▁प्राकृ तिक', '▁भाषा', '▁सीखना', '▁बहुि', '▁तिलचस्प', '▁है', '।']
