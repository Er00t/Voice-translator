import tkinter as tk
from tkinter import messagebox
from tkinter.ttk import Combobox
import speech_recognition as sr
from googletrans import Translator
from gtts import gTTS
from playsound import playsound
import random 
import os


root=tk.Tk() # açılış
root.geometry("700x400+500+250")
root.resizable(False,False)
root.title("voice translation by Er00t")

# ***************************  language selection sections ***********************
secim=tk.StringVar()
lst=['af : afrikaans',
    'sq : albanian', 
    'am : amharic', 
    'ar : arabic', 
    'hy : armenian', 
    'az : azerbaijani', 
    'eu : basque', 
    'be : belarusian', 
    'bn : bengali', 
    'bs : bosnian', 
    'bg : bulgarian', 
    'ca : catalan', 
    'ce:: cebuano', 
    'ny : chichewa', 
    'zhn: : chinese (simplified)', 
    'zhw: : chinese (traditional)', 
    'co : corsican', 
    'hr : croatian', 
    'cs : czech', 
    'da : danish', 
    'nl : dutch', 
    'en : english', 
    'eo : esperanto', 
    'et : estonian', 
    'tl : filipino', 
    'fi : finnish', 
    'fr : french', 
    'fy : frisian', 
    'gl : galician', 
    'ka : georgian', 
    'de : german', 
    'el : greek', 
    'gu : gujarati', 
    'ht : haitian creole', 
    'ha : hausa', 
    'ha:: hawaiian', 
    'iw : hebrew', 
    'he : hebrew', 
    'hi : hindi', 
    'hm:: hmong', 
    'hu : hungarian', 
    'is : icelandic', 
    'ig : igbo', 
    'id : indonesian', 
    'ga : irish', 
    'it : italian', 
    'ja : japanese', 
    'jw : javanese', 
    'kn : kannada', 
    'kk : kazakh', 
    'km : khmer', 
    'ko : korean', 
    'ku : kurdish (kurmanji)', 
    'ky : kyrgyz', 
    'lo : lao', 
    'la : latin', 
    'lv : latvian', 
    'lt : lithuanian', 
    'lb : luxembourgish', 
    'mk : macedonian', 
    'mg : malagasy', 
    'ms : malay', 
    'ml : malayalam', 
    'mt : maltese', 
    'mi : maori', 
    'mr : marathi', 
    'mn : mongolian', 
    'my : myanmar (burmese)', 
    'ne : nepali', 
    'no : norwegian', 
    'or : odia', 
    'ps : pashto', 
    'fa : persian',
    'pl : polish', 
    'pt : portuguese', 
    'pa : punjabi', 
    'ro : romanian', 
    'ru : russian', 
    'sm : samoan', 
    'gd : scots gaelic', 
    'sr : serbian', 
    'st : sesotho', 
    'sn : shona', 
    'sd : sindhi', 
    'si : sinhala', 
    'sk : slovak', 
    'sl : slovenian', 
    'so : somali', 
    'es : spanish', 
    'su : sundanese', 
    'sw : swahili', 
    'sv : swedish', 
    'tg : tajik', 
    'ta : tamil', 
    'te : telugu', 
    'th : thai', 
    'tr : turkish', 
    'uk : ukrainian', 
    'ur : urdu', 
    'ug : uyghur', 
    'uz : uzbek', 
    'vi : vietnamese', 
    'cy : welsh', 
    'xh : xhosa', 
    'yi : yiddish', 
    'yo : yoruba', 
    'zu : zulu']
list_=Combobox(root,values=lst,textvariable=secim)
list_.set('Choose your lenguage')
list_.pack(padx=10,pady=10)

def yazdır2():
    a=secim.get()[0:2]
    return a

secim2=tk.StringVar()
lst2=["af: Afrikaans",
  "ar: Arabic",
  "bg: Bulgarian",
  "bn: Bengali",
  "bs: Bosnian",
  "ca: Catalan",
  "cs: Czech",
  "da: Danish",
  "de: German",
  "el: Greek",
  "en: English",
  "es: Spanish",
  "et: Estonian",
  "fi: Finnish",
  "fr: French",
  "gu: Gujarati",
  "hi: Hindi",
  "hr: Croatian",
  "hu: Hungarian",
  "id: Indonesian",
  "is: Icelandic",
  "it: Italian",
  "iw: Hebrew",
  "ja: Japanese",
  "jw: Javanese",
  "km: Khmer",
  "kn: Kannada",
  "ko: Korean",
  "la: Latin",
  "lv: Latvian",
  "ml: Malayalam",
  "mr: Marathi",
  "ms: Malay",
  "my: Myanmar (Burmese)",
  "ne: Nepali",
  "nl: Dutch",
  "no: Norwegian",
  "pl: Polish",
  "pt: Portuguese",
  "ro: Romanian",
  "ru: Russian",
  "si: Sinhala",
  "sk: Slovak",
  "sq: Albanian",
  "sr: Serbian",
  "su: Sundanese",
  "sv: Swedish",
  "sw: Swahili",
  "ta: Tamil",
  "te: Telugu",
  "th: Thai",
  "tl: Filipino",
  "tr: Turkish",
  "uk: Ukrainian",
  "ur: Urdu",
  "vi: Vietnamese",
  "zh-CN: Chinese (Simplified)",
  "zh-TW: Chinese (Mandarin/Taiwan)",
  "zh: Chinese (Mandarin)"]
list2_=Combobox(root,values=lst2,textvariable=secim2)
list2_.set('Choose translate lenguage')
list2_.pack()

def yazdır1():
    b=secim2.get()[0:2]
    return b


# *************************** voiceover and translation **************************

translator=Translator()
dinle=sr.Recognizer()
def konus(string):
    yaz=yazdır1()
    tts=gTTS(string,lang=f"{yaz}")
    rand= random.randint(1,10000)
    file="audio-"+str(rand)+".mp3"
    tts.save(file)
    playsound(file)
    os.remove(file)

def translate():
    yaz2=yazdır2()
    with sr.Microphone() as  cevap:
        kayit=dinle.listen(cevap)
        ses=""
        try:
            ses=dinle.recognize_google(kayit, language=f'{yaz2}')
        except sr.UnknownValueError:
            messagebox.showinfo("UnknownValueError","your voice could not be understood")     
        except sr.RequestError:
            messagebox.showinfo("RequestError","try running the program again")   
        return ses
  

# ***************************  console outputs ************************************
def son():
    # messagebox.showinfo("pleas speak","çevirmek için konuşun")
    yaz=yazdır1()
    ses=translate()
    print(ses)
    ceviri=(translator.translate(ses,dest=f"{yaz}").text)
    print(ceviri)
    konus(ceviri)
    output_text.insert("end", f"{ses}\n")
    output_text2.insert("end", f"{ceviri}\n")

    return
  

button=tk.Button(root,text="Translate",fg="black", bg="red",command=son)
button.pack(padx=10,pady=10)
button.pack(ipadx=30,ipady=5)
uyari=tk.Label(root,text='Speak after pressing the translate button.',fg="black")
uyari.pack(pady=5)
output_text = tk.Text(root, height=5, width=100)
output_text.pack(anchor="e",padx=20)
output_text2= tk.Text(root, height=10, width=100)
output_text2.pack(anchor="w",padx=20,pady=10)


root.mainloop()  # kapanış
    




