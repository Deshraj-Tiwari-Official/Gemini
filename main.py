import platform
import webbrowser
import speech_recognition as sr
import os
from gtts import gTTS
import tempfile

recognizer = sr.Recognizer()


def response(prompt):
    if "gemini deactivate" in prompt:
        speak("Ok, If you want to call me again, say Gemini.")

    elif "show cheatsheet" in prompt:
        webbrowser.open("https://github.com/Deshraj-Tiwari-Official/Gemini/blob/main/cheatsheet.md")

    elif "google search for " in prompt:
        search_term = prompt.replace("google search for ", "")
        webbrowser.open(f"https://google.com/search?q={search_term}")
    else:
        speak("I didn't get that. Try again by saying Gemini.")
        play("./audios/gemini_start.mp3")


def play(filename):
    system = platform.system()
    if system == 'Linux':
        os.system(f"mpg123 {filename} > /dev/null 2>&1")
    elif system == 'Darwin':
        os.system(f"afplay {filename} > /dev/null 2>&1")
    elif system == 'Windows':
        os.system(f"start {filename} > nul 2>&1")
    else:
        raise Exception(f"Unsupported OS: {system}")


def speak(text):
    tts = gTTS(text=text, lang="en", slow=False, tld="us")
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as temp_file:
        tts.save(temp_file.name)
        play(temp_file.name)
    os.remove(temp_file.name)


def listen_for_wake_word():
    while True:
        try:
            with sr.Microphone() as src:
                print("Listening for wake word...")
                recognizer.adjust_for_ambient_noise(src)

                call_audio = recognizer.listen(src, timeout=2.0)
                call_command = recognizer.recognize_google(call_audio)
                call_command = call_command.lower()
                print(call_command)

                if "hey gemini" in call_command:
                    return True
        except sr.UnknownValueError:
            print("Sorry, I didn't understand that.")
        except sr.RequestError:
            print("Sorry, my speech service is down.")
        except sr.WaitTimeoutError:
            print("Timeout: No speech detected.")
        except Exception as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    speak("Say Hey Gemini anytime to call for me. Enjoy your time.")
    play("./audios/gemini_start.mp3")

    while True:
        if listen_for_wake_word():
            speak("Yes, how can I help you?")
            play("./audios/gemini_start.mp3")
            try:
                with sr.Microphone() as source:
                    print("Listening...")
                    recognizer.adjust_for_ambient_noise(source)

                    try:
                        audio = recognizer.listen(source, 2.0)
                        command = recognizer.recognize_google(audio)
                        command = command.lower()
                        print(">>", command)
                        response(command)
                    except sr.UnknownValueError or sr.WaitTimeoutError:
                        speak("Speech not detected. Please try again.")
                    except sr.RequestError:
                        speak("Sorry, I'm currently facing some technical issue.")
            except Exception as e:
                print(f"Error: {e}")
