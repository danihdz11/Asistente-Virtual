# Virtual Assistant

A virtual assistant developed in Python that uses voice recognition and text-to-speech synthesis to interact with the user. It can perform various tasks such as searching Wikipedia, playing music on YouTube, providing the date and time, telling jokes, opening websites, and much more.

## Features
- **Voice Recognition:** Listens to spoken commands from the user.
- **Text-to-Speech Synthesis:** Responds audibly using a text-to-speech engine.
- **Integration with Popular Services:** 
  - Playing videos on YouTube.
  - Searching Google and Wikipedia.
  - Retrieving stock prices via Yahoo Finance.
- **Multilingual Support:** Configurable for Spanish and English.
- **Utility Functions:** Telling jokes, providing the date and time, opening web applications, among others.

## Requirements
- Python
- Required packages (installable with `pip`):
  - `pyttsx3`
  - `speechrecognition`
  - `pywhatkit`
  - `yfinance`
  - `pyjokes`
  - `wikipedia`

## Usage
Run the script and speak when prompted. Some supported commands are:
- "Open YouTube"
- "What day is it today"
- "Search Wikipedia for [topic]"
- "Play [song name]"

## Customization
You can adjust the assistant's voice by modifying the configuration options in the code (id1 for Spanish and id2 for English). Additionally, you can add custom commands by editing the `pedir_cosas()` function.

### To Change the Language or Voice:
1. Open the `asistente.py` file.
2. Locate the voice configuration section, where IDs for Spanish and English (id1 and id2) are defined.
3. Modify the ID according to your preferred language or voice.
