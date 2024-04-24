import torch
from transformers import pipeline,AutoTokenizer,AutoModelForSeq2SeqLM
import textacy
from textacy import preprocessing as prep
import re
import contractions


class PreprocessingPipeline:
    # defining regex function for the pipeline
    #removing html tags
    def remove_html(self,text):
        text = re.sub(r"<[^>]+>"," ",text)
        return re.sub(r"&[\S]+"," ",text) #removes &nbsp
    #removing emails
    def remove_email(self,text):
        return re.sub(r"\S*@\S*.com","",text)

    #removing hashtags
    def remove_hash(self,text):
        return re.sub(r"\#*","",text)

    #removing special symbols except () '' "" ? ! - .
    def remove_special(self,text):
        return re.sub(r"[^\w\s()\'\"\?\!\-\.]","",text)

    #replacing _ with space
    def replace_(self,text):
        return re.sub(r"[_]"," ",text)

    #Expand Contracions
    def expand(self,text):
        expanded = []
        for word in text.split():
            expanded.append(contractions.fix(word))
        txt = ' '.join(expanded)
        return txt

    #Lowering word
    def low(self,text):
        return text.lower()

    def preprocess_pipeline(self,text):
        pipe = prep.make_pipeline(
            self.remove_email,
            prep.replace.emojis,
            prep.replace.urls,
            prep.replace.phone_numbers,
            self.remove_hash,
            prep.replace.currency_symbols,
            self.remove_html,
            self.low,
            prep.normalize.hyphenated_words, # sentences that have been split by a '-' is split and joined together
            prep.normalize.quotation_marks, # normalize all singal and double quotes in the text to ASCII representation,
            prep.normalize.unicode,
            prep.normalize.bullet_points,
            self.replace_,
            self.remove_special,
            prep.normalize.whitespace
        )

        return pipe(text)

class Model:
    def __init__(self,model_name):
        self.model_name = model_name
        self.model_path = "t5_20k/results/t5_cnn_model"
        self.gen_kwargs = {'length_penalty':0.8,'num_beams':8,'max_length':125}

        if self.model_name == 'tf-base':
            self.model_path = 't5_20k/results/t5_cnn_model'
        elif self.model_name == 'bart-base':
            self.model_path = 'bart_20k/results/bart_cnn_model'

        self.model = AutoModelForSeq2SeqLM.from_pretrained(self.model_path)
        self.tokenizer = AutoTokenizer.from_pretrained(self.model_path)
        self.pipe = pipeline('summarization',model = self.model, tokenizer = self.tokenizer)
    
    def predict(self,text):
        if self.model_name == 'bart-base':
            generated = self.pipe(' '.join(text.split()[:810]),**self.gen_kwargs)
        else:
            generated = self.pipe(text,**self.gen_kwargs)
        return generated[0]['summary_text']