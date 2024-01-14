import speech_recognition as sr

r = sr.Recognizer()

with sr.Microphone() as source:
	r.adjust_for_ambient_noise(source, duration=0.2)

	while True:
		try:
			print("Say something...")
			audio = r.listen(source, timeout=5)

			text = r.recognize_google(audio)
			text = text.lower()

			print("Transcription:")
			print(text)

		except sr.UnknownValueError:
			print("din't get that")
		except sr.RequestError as e:
			print(f"Could not request results from Google Speech Recognition service; {e}")

