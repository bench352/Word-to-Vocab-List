# Installation Guide

## Lite Version

An executable file (.exe) for Microsoft Windows is available for the Lite Version, so you can directly run it without any setup by double-clicking `word2VocabListLite.exe` .

## Standard Version

On the other hand, Standard Version requires complicated setup since no executable file (.exe) is available. Non-tech-savvy people may find the following steps difficult. The setup procedure can be summarized as below:

1. Set up the Python Interpreter (if you already have Python Interpreter installed on your computer, you can skip this step)
2. Install required libraries on your computer ( `PyDictionary`, `deep-translator` and `nltk`)

Note that the data for `nltk` is sized around 3.4GB. Make sure you have enough storage for it.

### 1. Set up the Python Interpreter on Microsoft Windows

1. Download Python installer from [official Python website](https://www.python.org/)

2. After downloading, run `python-3.XX.XX-amd64.exe`

3. Make sure you enable "Add Python 3.XX to PATH" at the bottom of the setup window, then click `Install Now`

   ![image-20220103195722387](Installation%20Guide.assets/image-20220103195722387.png)

4. After installation, you can click `Close` to close the installer.

   ![image-20220103200003334](Installation%20Guide.assets/image-20220103200003334.png)

### 2. Install required libraries on your computer

1. Open the Command Prompt on Windows by pressing `[Win]` on your keyboard, type `cmd`, and hit `[Enter]`

   > `[Win]` key means the Windows key on your keyboard. On most keyboards, there is a Microsoft Windows logo on that key.

2. In the Command Prompt, enter the following command to install `PyDictionary`

   ```
   pip install PyDictionary
   ```

3. In the Command Prompt, enter the following command to install `deep-translator`

   ```
   pip install deep-translator
   ```

4. In the Command Prompt, enter the following command to install `NLTK`

   ```
   pip install nltk
   ```

5. Close the Command Prompt. Open `Python 3.XX` via Start Menu (It's in the "Python 3.XX" folder). You would see an interface similar to the Command Prompt. Enter the following commands:

   ```
   import nltk
   nltk.download('all')
   ```

6. Now you can run the Standard Version by double-clicking on `word2VocabList.py`

