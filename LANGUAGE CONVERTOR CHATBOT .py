#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install googletrans==4.0.0-rc1


# In[ ]:


from googletrans import Translator

# Define language codes and their corresponding names
languages = {
    "en": "English",
    "te": "Telugu",
    "hi": "Hindi",
    "as": "Assamese",
    "bn": "Bengali",
    "gu": "Gujarati",
    "kn": "Kannada",
    "ks": "Kashmiri",
    "kok": "Konkani",
    "ml": "Malayalam",
    "mni": "Manipuri",
    "mr": "Marathi",
    "ne": "Nepali",
    "or": "Oriya",
    "pa": "Punjabi",
    "sa": "Sanskrit",
    "sd": "Sindhi",
    "ta": "Tamil",
    "ur": "Urdu",
    "brx": "Bodo",
    "sat": "Santali",
    "mai": "Maithili",
    "doi": "Dogri"
}

def translate_text(text, dest_lang='en'):
    translator = Translator()
    translated = translator.translate(text, dest=dest_lang)
    return translated.text

def main():
    print("Welcome to the Language Translator Chatbot!")
    print("Supported languages:")
    for code, name in languages.items():
        print(f"{code}: {name}")
    print("Type 'exit' to quit.")

    while True:
        dest_lang = input("Enter the language code you want to translate to: ")
        
        if dest_lang.lower() == 'exit':
            print("Exiting...")
            break
        
        if dest_lang not in languages:
            print("Invalid language code. Please try again.")
            continue
        
        while True:
            user_input = input(f"Enter text to translate to {languages[dest_lang]}: ")
            
            if user_input.lower() == 'exit':
                print("Exiting...")
                return
            
            print(f"Translating to {languages[dest_lang]}...")
            translated_text = translate_text(user_input, dest_lang)
            print(f"Translated text: {translated_text}\n")
            break

if __name__ == "__main__":
    main()


# In[ ]:




