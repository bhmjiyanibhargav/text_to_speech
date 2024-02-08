import gtts
import playsound

text =input("enter somthing here: ")

sound = gtts.gTTS(text, lang="en")

sound.save("iam.mp3")

playsound.playsound("iam.mp3")