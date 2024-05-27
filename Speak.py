import pyttsx3

def speak(text):
    engine = pyttsx3.init()

    # Print available voices
    voices = engine.getProperty('voices')
    for i, voice in enumerate(voices):
        print(f"Voice {i}: {voice.name} ({voice.id})")

    # Set properties
    engine.setProperty('rate', 150)  # Speed of speech
    engine.setProperty('volume', 1.0)  # Volume level (0.0 to 1.0)
    
    # Try each available voice to check if any work
    for voice in voices:
        engine.setProperty('voice', voice.id)
        print(f"Testing voice: {voice.name}")
        engine.say(text)
        engine.runAndWait()

# Example usage
text_to_speak = "Hello, this is a test message from Python!"
speak(text_to_speak)
