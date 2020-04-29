from random import choice

computerResponses = [] # list of all computer's questions
humanResponses = []  # list of all the person's responses

def relationship_wellheard():
    """
        simulate a listner for relationship stress and problems
        this function asks the user questions
        based on the answer to the previous question
    """
    userComment = input("Computer >> My name is relationship wellheard and I am here to listen to your relationship stress and problems. What is happening right now? \nThe User >> ")

    flag = False
    while userComment not in ["goodbye","bye","quit","exit"]:
        humanResponses.append(userComment)

        if not flag:
            flag = True
            suicidal_attempt()
        else:
            response = respond(userComment)
            if response in computerResponses:
                response = "Again, "+response
            computerResponses.append(response)
            print("Computer >> "+response)

        userComment = input("The User >> ")

    print("bye")

def suicidal_attempt():
    userComment = input("Computer >> Do you have a suicidal tendency? \nThe User >> ")
    comments = userComment.lower().split()
    if 'yes' in comments:
        for response in hotline:
            print("Computer >> "+response)
    else:
        userComment = input("Computer >> Have you attempted to harm yourself? \nThe User >> ")
        comments = userComment.lower().split()
        if 'yes' in comments:
            for response in counsel:
                print("Computer >> "+response)

    response = 'Sincerely hope it could help you.'
    print("Computer >> "+response)


def respond(comment):
    """ generate a computer response to the user's comment"""
    wordsInSentence = contains(comment,singleWords)
    if len(wordsInSentence) >= 1:
        string = "you said you are feeling " + wordsInSentence[0] + '\n' 
        return string + choice(singleResponses)

    wordsInSentence = contains(comment,problemWords)
    if len(wordsInSentence) >= 1:
        string = "you said you are feeling " + wordsInSentence[0] + '\n' 
        return string + choice(singleResponses)

    if len(comment.split()) <= 7:  # respond to short answers...
        return choice(nothingResponses)

    return choice(generalResponses)

def contains(sentence,words):
    """ true if one of the words is in the sentence
        where sentence is a string and
        words is a list of strings
    """
    wordsInSentence = [word for word in words if word in sentence]
    return wordsInSentence

def contains2(sentence,words):
    """
    a more efficient test to see if a word in the list words
    is also in the string sentence. Note, this will return
    True for contains2("lovely day",["el"])
    which might not be what you wanted. We could first split
    sentence into words, which might be better!
    """
    for w in words:
        if w in sentence:
            return True
    return False

# Here are the keywords and responses to comments made by someone who is currently single
singleWords = "single alone lonely nobody pressure everyone want wants like attract confidence low self esteem date dating".split()
singleResponses=[
"How often do you feel lonely?",
"Do you want to be single?",
"Do you want to find new partners or dates?",
"What is your ideal partner like?",
"Do you want some love from me?",
"are you satisfied with your current state?",
"cheer up cutie!",
"if no one wants you, I do!",
    
]


# Here are the keywords and response to comments containing a potential problem or breakup with a partner keyword
problemWords = "mad angry upset hate anger angry why problem fight sad breakup cheat cry hurt heartbreak broken abuse violent yell scream selfish argue trust issue cold conflic".split()
problemResponses = [
  "calm down...",
  "what about the good times you guys had?",
  "How long have you been feeling this way?",
  "what is your next step in this relationship?",
  "i am listening, what makes your relationship problematic?",
  "what will your partner change to make your relationship better?",
  "How are you and your partner communicating?",
  "what ways can your communication with each other be better?",
  "How does your partner usually treat you?",
  "no worries, I got your back!"
]

# these are the possible responses to comments like "nothing, good, ok, okay, why, what"
nothingResponses = [
    "it seems like you are fine, feel free to enter 'bye' to exit our chat",
    "tell me other things you would like to talk about",
    "what are other ways you would like to get help from me?",
    "if you are still feeling down, feel free to tell me more",
    "sorry I can't solve your problems, I am only here to listen",
    "feel free to leave anytime by entering 'bye'!",
    "Could you please elaborate?",
    "Would you mind elaborating?",
    "What else?",
    "Anything more to say?",
    "everything will be okay soon",
    "Tell me more cutie",
    "Tell me more about your feelings right now",
    "I can't help you unless you tell me more!",
    "what do you mean?",
    "why?",
    "I am not sure I understand",
    "really? how?",
    "what are your way of coping?",
    "im sorry",
    "how can I help?",
    "how can I do better?",
    "what do you plan to do now?"
    
]


# We give these responses if there is nothing else to say!
generalResponses = [
  "Tell me more.",
  "Do you have a lot of these thoughts?",
  "Why do you feel or think this way?",
  "Why do you act this way?",
  "How was your relationship in the past?",
  "How do you feel or think about that?",
  "How often do you feel or think this way?",
  "What do you think are some ways that can improve your relationship?",
  "How do you think you can change your current situition?",
  "Are you planning to meet someone new soon?",
  "Are you satisfied with your current relationship status?",
  "How do you think your relationships in the past have affected the way you are now?",
  "Do you want to get this problem solved or are you just seeking for a listener?"
]

hotline = [
    'If you think someone might be suicidal, ask them directly "Are you thinking about suicide?"',
    'Don’t be afraid to do this, it shows you care and will actually decrease their risk because it shows someone is willing to talk about it.',
    'Make sure you ask directly and unambiguously.',
    'National Suicide Prevention Lifeline Call 1-800-273-8255 Available 24 hours everyday',
    'https://www.dadabhagwan.org/path-to-happiness/self-help/suicide-prevention/what-happens-after-suicide',
]
counsel = [
    'The Brandeis Counseling Center (BCC) provides counseling for students in times of stress and encourages them to ask for help with their most immediate concerns.',
    'The BCC is available to provide urgent consultations by phone 24 hours a day.',
    'Psychotherapy groups are suspended until further notice.',
    'Teletherapy appointments are available to students who are in treatment with the BCC, and are residing within Massachusetts.',
    'If you are seeking routine care, or a referral in your local area, please contact us at the above phone number. We will recommend individualized resources and referrals.',
    'https://www.brandeis.edu/counseling/',
    'https://www.brandeis.edu/romance-studies/pdfs/counseling-center-information.pdf'
]


if __name__=="__main__":
    relationship_wellheard()  # call wellheard when run as a script
             # but not when imported



