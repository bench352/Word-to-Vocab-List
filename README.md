# Words To Vocabulary List

***Words To Vocabulary List*** is a program that automatically generates a vocabulary list with *English meaning, Chinese translation, synonyms, and antonyms (if available)* from a list of words.

It supports two types of output:

- **Markdown file:** A Markdown (.md) file containing all the meanings, Chinese translation, synonyms and antonyms (if available) of each word.
- **Text file for Anki:** A plain text (.txt) file for importing to [Anki](https://apps.ankiweb.net/) for creating study flashcards.

It is written in [Python](https://www.python.org/) and has a *Command Line Interface (CLI)*. The user interacts with the program by entering plain-text commands.

## Different Version

There are two versions of Word To Vocabulary List, the standard version and the lite version. The feature difference of each version is as below:

| Feature                                               | Standard Version | Lite Version |
| ----------------------------------------------------- | ---------------- | ------------ |
| Creating Markdown file                                | ✅                | ✅            |
| Creating Anki study flashcards                        | ✅                | ✅            |
| Looking up English meaning                            | ✅                | ✅            |
| Looking up Chinese translation                        | ✅                | ✅            |
| Converting Markdown file to Word Document             | ✅                | ✅            |
| Looking up Synonyms and Antonyms                      | ✅                | ❎            |
| Normalizing Words (remove tenses, plural forms, etc.) | ✅                | ❎            |

The reason for making two different versions is that some features depend on the [Natural Language Toolkit (NLTK)](https://www.nltk.org/) library, which is enormous. Since all external library used is included for the code compilation, it makes the compiled executable file unnecessarily large (and it takes forever to open!) The Lite version removes features that depend on NLTK and makes the compiled executable file much smaller.

Therefore, the Standard Version is available as a Python Script (.py) only, but the Lite Version is available as Python Script (.py) and executable file (.exe). You may still attempt to compile the Standard Version if you want.

## Setting Up the Program

For the Lite Version, you can directly use the program by dowloading and running [word2VocabListLite.exe](word2VocabListLite.exe).

For the Standard Version, it requires some setup to make the program ready to run. Please refer to the [Installation Guide](./Documentation/Installation%20Guide.md) for more details.

Once you have the program up and ready, you can start using the program with the help of the [User Guide](./Documentation/User%20Guide.md).

## Issues?

For any issues regarding the program, please don't hesitate and write an email to [benchoy352@gmail.com](mailto:benchoy352@gmail.com).

## Acknowledgement

- Meaning of words, synonyms and antonyms from WordNet.
- Chinese translation by Google Translate.
- Normalizing text using NLTK from [Axel-Cleris Gailloty](http://agailloty.rbind.io/project/nlp_clean-text/)
- Finding synonyms and antonyms using NLTK from [tutorialspoint](https://www.tutorialspoint.com/python_text_processing/python_synonyms_and_antonyms.htm)

``

