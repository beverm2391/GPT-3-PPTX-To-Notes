import fitz
from bs4 import BeautifulSoup
from pptx import Presentation
import os
import openai
from dotenv import load_dotenv
import json
from transformers import GPT2Model, GPT2Config, GPT2Tokenizer

from PDF_text_v3_OO import PDFToText
from pptx_to_notes_v3 import getResponse, IterateOverPrompt, WriteFile

# ! GPT-3 SETUP

file_name = ""

# AI setup and settings
load_dotenv('.env')
api_key = os.environ.get('OPENAI-API-KEY')
openai.api_key = api_key

# config tokenizer
configuration = GPT2Config()
model = GPT2Model(configuration)
tokenizer = GPT2Tokenizer.from_pretrained('gpt2')


# ! Run it baby

PDF_text = PDFToText(file_name)

print("\nPDF Converted to Text")

response = IterateOverPrompt("Key points from each slide:", PDF_text, .7)

print("\nKey Points Identified \n")

WriteFile(response, f"/outputs/{file_name}.txt")
