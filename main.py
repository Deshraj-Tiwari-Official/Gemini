import platform
import speech_recognition as sr
import os
from gtts import gTTS
import tempfile

recognizer = sr.Recognizer()


def response(prompt):
    if prompt == "hello gemini":
        return speak("Hello, how are you?")


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
                recognizer.adjust_for_ambient_noise(src, duration=1.0)

                call_audio = recognizer.listen(src, timeout=3.0)
                call_command = recognizer.recognize_google(call_audio)
                call_command = call_command.lower()

                if "hey gemini" in call_command:
                    play("./audios/gemini_start.mp3")
                    return True
        except sr.UnknownValueError:
            pass
        except sr.RequestError:
            speak("Sorry, my speech service is down.")
        except Exception as err:
            speak("Some error occurred. Please try again.")
            print(err)


if __name__ == "__main__":
    speak("Initializing Gemini...")

    while True:
        if listen_for_wake_word():
            try:
                with sr.Microphone() as source:
                    print("Listening...")
                    recognizer.adjust_for_ambient_noise(source, duration=1.0)

                    try:
                        audio = recognizer.listen(source, timeout=5.0)
                        command = recognizer.recognize_google(audio)
                        command = command.lower()
                        print(command)
                        response(command)
                    except sr.WaitTimeoutError:
                        print("Timeout: No speech detected.")
                    except sr.UnknownValueError:
                        print("Sorry, I didn't understand that.")
                    except sr.RequestError:
                        print("Sorry, my speech service is down.")
            except Exception as e:
                print(f"Error: {e}")
