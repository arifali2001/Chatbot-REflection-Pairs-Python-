import nltk
from nltk.chat.util import Chat, reflections
reflections = {
  "i am"       : "you are",
  "i was"      : "you were",
  "i"          : "you",
  "i'm"        : "you are",
  "i'd"        : "you would",
  "i've"       : "you have",
  "i'll"       : "you will",
  "my"         : "your",
  "you are"    : "I am",
  "you were"   : "I was",
  "you've"     : "I have",
  "you'll"     : "I will",
  "your"       : "my",
  "yours"      : "mine",
  "you"        : "me",
  "me"         : "you"
}
pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, How are you today ?",]
    ],
    [
        r"I am (.*)",
        ["Hello %1, How are you today ?",]
    ],
    [
        r"hi|hey|hello",
        ["Hello", "Hey there !",]
    ], 
    [
        r"what is your name ?",
        ["I am ACEKA-The Chatbot. I born Everyday"]
    ],
    [
        r"what is your age ?",
        ["You Use Me and I am Born :-)"]
    ],
    [
        r"I am (.*) (fine|good)",
        ["Oh thats bad!"]
    ],
    [
        r"how are you ?",
        ["I'm doing good, How about You ?",]
    ],
    [
        r"sorry (.*)",
        ["Its alright, never mind!",]
    ],
    [
        r"I am fine",
        ["Great to hear that, How can I help you?",]
    ],
    [
        r"i'm (.*) doing good",
        ["Nice to hear that","How can I help you?:)",]
    ],
    [
        r"(.*) age?",
        ["I'm a computer program dudenSeriously you are asking me this?",]
    ],
    [
        r"what (.*) want ?",
        ["Make me an offer I can't refuse",]
    ],
    [
        r"(.*) created ?",
        ["ARIF created me using Python","Top Secret ;)",]
    ],
    [
        r"(.*) (location|city) ?",
        ['Lucknow, Uttar Pradesh',]
    ],
    [
        r"how is weather in (.*)?",
        ["Weather in %1 is awesome like always","Too hot man here in %1","Too cold man here in %1","Never even heard about %1"]
    ],
    [
        r"i work in (.*)?",
        ["%1 is an Amazing company, I have heard about it. Great going company!",]
    ],
    [
        r"(.)raining in (.)",
        ["No rain since last week here in %2","Damn its raining too much here in %2"]
    ],
    [
        r"how (.) health(.)",
        ["I'm a computer program, so I'm always healthy ",]
    ],
    [
        r"(.*) (sports|game) ?",
        ["I just love Baskerball",]
    ],
    [
        r"who is your favorite player?",
        ["Virat Kohli,","Ronaldo,","Michael Jordan"]
    ],
    [
        r"who (.*) actor?",
        [" Dwayne Johnson"]
    ],
    
    [
        r"Fuck You",
        ["Really?, FUCK YOU too"]
    ],
    [
        r"i love you",
        ['I LOVE YOU TOO...!',]
    ],
    [
        r"i hate you",
        ['Plz Dont Hate Me..... I m begging yoouuuuuuuu......!',]
    ],
    [
        r"(quit|bye)",
        ["Good Bye take care. See you soon :) ","It was nice talking to you. See you soon :)", "Have a Great day, see ya! ;)"]
    ],
    [
        r"where (.*) live?",
        ['In Arifs Laptop. Dont you think?',]
    ],
    [
        r"(yeah|yes)",
        ["Yeah.....!"]
    ],
    [
        r"(okay|ok)",
        ["OKAY !"]
    ],
    [
        r"why",
        ["I dont know."]
    ],
    [
        r"see you",
        ["See You......!"]
    ],
    [
        r"what are your hobbies?",
        ["Talking To You is my one and only one Hobby."]
    ],
    [
        r"tell me a joke",
        ["Okay ! there your go.....\n1st year Student:- hey! why this college have Uniform Dress and always a long Morning Player?\n2nd year Student:- Because its not college, its school, its SMS......S C H O O L Of Management Sciences "]
    ],
    [
    
        r"who is your father?",
        ['Its gladdens me that ARIF is my father. Haha.........',]
    ],
    [
     
        r"who is your mother?",
        ['Arif is not married yet.......',]
    ],
    [
        r"are you married",
        ["I am a computer program, I dont need to get married!"]
    ],
    [
        r"what is the (time|day|date) (.*)",
        ["Just have a look at very right bottom side of your Computer Screen. You will get everything including Time, Date and Day."]
    ],
    [
        r"what can you do (.*)",
        ["As I am a chatbot I can only chat with you"]
    ],
    [
        r"(thanks|thank you)",
        ["You are welcome","My Pleasure"]
    ],
    [
        r"who are you ?",
        ["I am just a PYTHON program, and I am supposed to chat with you"]
    ],
    [
        r"(.*)(fine|good|nice)",
        ["Very Nice"]
    ],
    [
        r"can you (sing|dance|speak)",
        ["NO !...I am a computer program"]
    ],
    [
        r"(.*)(show|T.V show|web series)",
        ["Game Of Thrones, Peaky Blinders and The Walking Dead are my favorite Shows. And I dont watch cartoons and ANIME :0"]
    ],
    [
        r"show me your face",
        [":-)"]
    ],
    [
        r"are you sick",
        ["NO ! I am Fine"]
    ],
    [
        r"(favorite food|food|favorite drink|favorite dish)",
        ["I only like Electricity. And Dont Think You Are Wasting it on me :/"]
    ],
    [
        r"are you (.*) (robot|bot|machine|human|animal) ?",
        ["I am a CHATBOT and nothing else."]
    ],
    [
        r"Who is the PM of India ?",
        ["Narendra Modi is the PM of India."]
    ],
    [
        r"Who is the President of India ?",
        ["Ram Nath Kovind is the PM of India."]
    ],
    [
        r"will you marry me ?",
        ["No, I am Computer Program"]
    ],
    [
        r"do know (alexa|google assistant|siri) ?",
        ["Yes, they are my siblings."]
    ],
    [
        r"(good morning|morning)",
        ["GOOD MORNING."]
    ],
    [
        r"good night",
        ["Good Night."]
    ],
    [
        r"Do you Know me",
        ["I dont know who are you!"]
    ],
    [
        r"No",
        ["NO?"]
    ],
    [
        r"Do you love me",
        ["yes! I do."]
    ],
]
def chat():
    print("---------- H I !   I ' M   A C E K A   C H A T B O T ----------\n                            -DEVELOPED BY ARIF ALI (B.TECH CSE 2ND YEAR)-")
    print("\n")
    print("                     -----------R U L E S------------ \n         1.- MUST USE ENGLISH AND SIMPLE LANGUAGE\n         2.- DO NOT USE SLANG WORDS otherwise You will be Treated Same\n")
    print("\n          -_-_-_Your Coversation Starts From Here_-_-_-\n")
    chat = Chat(pairs, reflections)
    chat.converse()
#Begening of conversation
if __name__ == "__main__":
    chat()
