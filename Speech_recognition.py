import speech_recognition as sr
import webbrowser as web

def main():

    path = "admin:///usr/lib/firefox/firefox.sh"


    r = sr.Recognizer()

    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)

        print("Please say something.....")

        audio = r.listen(source)

        print("Reconizing now.....")


        try:
            test = r.recognize_google(audio)
            print("You have said : " + test)

        except Exception as e:
            print("Error " + str(e))    
            
if __name__ == "__main__":
	main()            


main()

