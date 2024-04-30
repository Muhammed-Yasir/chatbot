import re
import long_responses as long


def message_probability(user_message,recognised_words, single_response=False, required_words=[]):
    message_certainty=0
    has_required_words=True


    for word in user_message:
        if word in recognised_words:
            message_certainty+=1

    #calculate the percent of recognised words in a user message
    percentage = float(message_certainty ) / float(len(recognised_words))
    
    for word in required_words:
        if word not in user_message:
            has_required_words = False
            break

    if has_required_words or single_response:
        return int(percentage*100)
    else:
        return 0
    

def check_all_messages(message):
    highest_prob_list={}

    def response(bot_response,list_of_words,single_response=False,required_words=[]):
        nonlocal highest_prob_list
        highest_prob_list[bot_response] = message_probability(message,list_of_words,single_response,required_words)

    #Responses---------------------------------------------------------------------------
    response('Hello!',['hello','hi','sup','hey','heyo'],single_response=True)
    response('I\'m doing fine ,and you?',['how','are','you','doing'],required_words=['how'])
    response('Thank you!',['i','love','code','palace'],required_words=['code','palace'])
    response(long.R_EATING,['what','you','eat'],required_words=['you','eat'])
    response(long.R_ROBOT,['are','you','roboat'],required_words=['you','robot'])
    
    response(long.R_CHAT_1, ['how', 'are', 'you'], required_words=['you'])
    response(long.R_CHAT_2, ['tell', 'me', 'a', 'story'], required_words=['tell', 'story'])
    response(long.R_CHAT_3, ['what', 'is', 'your', 'favorite', 'color'], required_words=['favorite', 'color'])
    response(long.R_CHAT_4, ['do', 'you', 'dream'], required_words=['you', 'dream'])
    response(long.R_CHAT_5, ['what', 'is', 'the', 'meaning', 'of', 'life'], required_words=['meaning', 'life'])
    response(long.R_CHAT_6, ['can', 'you', 'sing'], required_words=['you', 'sing'])
    response(long.R_CHAT_7, ['are', 'you', 'a', 'human'], required_words=['you', 'human'])
    response(long.R_CHAT_8, ['how', 'do', 'you', 'work'], required_words=['you', 'work'])
    response(long.R_CHAT_9, ['tell', 'me', 'a', 'joke'], required_words=['tell', 'joke'])
    response(long.R_CHAT_10, ['where', 'are', 'you', 'from'], required_words=['you', 'from'])
    response(long.R_CHAT_51, ['how', 'are', 'you', 'feeling'], required_words=['you', 'feeling'])
    response(long.R_CHAT_52, ['what', 'is', 'your', 'favorite', 'movie'], required_words=['favorite', 'movie'])
    response(long.R_CHAT_53, ['can', 'you', 'tell', 'me', 'a', 'funny', 'joke'], required_words=['tell', 'funny', 'joke'])
    response(long.R_CHAT_54, ['how', 'do', 'I', 'improve', 'my', 'cooking', 'skills'], required_words=['improve', 'cooking', 'skills'])
    response(long.R_CHAT_55, ['what', 'are', 'your', 'hobbies'], required_words=['your', 'hobbies'])
    response(long.R_CHAT_56, ['what', 'do', 'you', 'like', 'to', 'do', 'for', 'fun'], required_words=['you', 'like', 'fun'])
    response(long.R_CHAT_57, ['can', 'you', 'teach', 'me', 'a', 'new', 'word'], required_words=['teach', 'new', 'word'])
    response(long.R_CHAT_58, ['what', 'is', 'the', 'meaning', 'of', 'life'], required_words=['meaning', 'life'])
    response(long.R_CHAT_59, ['do', 'you', 'believe', 'in', 'ghosts'], required_words=['believe', 'ghosts'])
    response(long.R_CHAT_60, ['what', 'is', 'your', 'favorite', 'book'], required_words=['favorite', 'book'])
    response(long.R_CHAT_11, ['where', 'do', 'you', 'live'], required_words=['you', 'live'])
    response(long.R_CHAT_12, ['what', 'is', 'your', 'opinion', 'on', 'artificial', 'intelligence'], required_words=['opinion', 'artificial', 'intelligence'])
    response(long.R_CHAT_13, ['how', 'do', 'you', 'learn', 'new', 'things'], required_words=['you', 'learn', 'new', 'things'])
    response(long.R_CHAT_14, ['can', 'you', 'tell', 'me', 'a', 'story'], required_words=['tell', 'story'])
    response(long.R_CHAT_15, ['what', 'do', 'you', 'dream', 'about'], required_words=['you', 'dream'])
    response(long.R_CHAT_16, ['how', 'do', 'you', 'stay', 'organized'], required_words=['you', 'stay', 'organized'])
    response(long.R_CHAT_17, ['what', 'do', 'you', 'like', 'to', 'eat'], required_words=['you', 'like', 'eat'])
    response(long.R_CHAT_18, ['what', 'is', 'the', 'most', 'interesting', 'fact', 'you', 'know'], required_words=['interesting', 'fact', 'you', 'know'])
    response(long.R_CHAT_19, ['can', 'you', 'play', 'a', 'game', 'with', 'me'], required_words=['play', 'game'])
    response(long.R_CHAT_20, ['what', 'is', 'your', 'favorite', 'color'], required_words=['favorite', 'color'])
    response(long.R_CHAT_21, ['how', 'do', 'you', 'deal', 'with', 'stress'], required_words=['you', 'deal', 'stress'])
    response(long.R_CHAT_22, ['what', 'is', 'your', 'favorite', 'music', 'genre'], required_words=['favorite', 'music', 'genre'])
    response(long.R_CHAT_23, ['can', 'you', 'give', 'me', 'advice', 'on', 'relationships'], required_words=['give', 'advice', 'relationships'])
    response(long.R_CHAT_24, ['what', 'is', 'your', 'favorite', 'hobby'], required_words=['favorite', 'hobby'])
    response(long.R_CHAT_25, ['do', 'you', 'have', 'any', 'siblings'], required_words=['have', 'siblings'])
    response(long.R_CHAT_26, ['what', 'is', 'the', 'meaning', 'of', 'happiness'], required_words=['meaning', 'happiness'])
    response(long.R_CHAT_27, ['how', 'do', 'you', 'handle', 'boredom'], required_words=['you', 'handle', 'boredom'])
    response(long.R_CHAT_28, ['what', 'do', 'you', 'like', 'to', 'do', 'in', 'your', 'free', 'time'], required_words=['you', 'like', 'free', 'time'])
    response(long.R_CHAT_29, ['what', 'is', 'the', 'best', 'way', 'to', 'relax'], required_words=['best', 'way', 'relax'])
    response(long.R_CHAT_30, ['can', 'you', 'give', 'me', 'some', 'motivational', 'quotes'], required_words=['give', 'motivational', 'quotes'])
    response(long.R_CHAT_31, ['what', 'is', 'your', 'favorite', 'food'], required_words=['favorite', 'food'])
    response(long.R_CHAT_32, ['what', 'is', 'the', 'best', 'way', 'to', 'start', 'a', 'day'], required_words=['best', 'way', 'start', 'day'])
    response(long.R_CHAT_33, ['what', 'do', 'you', 'think', 'about', 'philosophy'], required_words=['think', 'philosophy'])
    response(long.R_CHAT_34, ['how', 'do', 'you', 'handle', 'emotions'], required_words=['you', 'handle', 'emotions'])
    response(long.R_CHAT_35, ['what', 'is', 'the', 'most', 'memorable', 'experience', 'you', 'had'], required_words=['most', 'memorable', 'experience', 'you', 'had'])
    response(long.R_CHAT_36, ['what', 'is', 'your', 'opinion', 'on', 'love'], required_words=['opinion', 'love'])
    response(long.R_CHAT_37, ['how', 'do', 'you', 'stay', 'motivated'], required_words=['you', 'stay', 'motivated'])
    response(long.R_CHAT_38, ['what', 'is', 'your', 'favorite', 'sport'], required_words=['favorite', 'sport'])
    response(long.R_CHAT_39, ['what', 'do', 'you', 'think', 'about', 'space'], required_words=['think', 'space'])
    response(long.R_CHAT_40, ['what', 'is', 'your', 'favorite', 'animal'], required_words=['favorite', 'animal'])
    response(long.R_CHAT_41, ['what', 'is', 'the', 'meaning', 'of', 'success'], required_words=['meaning', 'success'])
    response(long.R_CHAT_42, ['how', 'do', 'you', 'make', 'decisions'], required_words=['you', 'make', 'decisions'])
    response(long.R_CHAT_43, ['what', 'is', 'the', 'best', 'way', 'to', 'handle', 'failure'], required_words=['best', 'way', 'handle', 'failure'])
    response(long.R_CHAT_44, ['what', 'do', 'you', 'like', 'to', 'do', 'in', 'your', 'spare', 'time'], required_words=['you', 'like', 'spare', 'time'])
    response(long.R_CHAT_45, ['how', 'do', 'you', 'deal', 'with', 'challenges'], required_words=['you', 'deal', 'challenges'])
    response(long.R_CHAT_46, ['what', 'is', 'your', 'opinion', 'on', 'politics'], required_words=['opinion', 'politics'])
    response(long.R_CHAT_47, ['how', 'do', 'you', 'cope', 'with', 'stress'], required_words=['you', 'cope', 'stress'])
    response(long.R_CHAT_48, ['what', 'is', 'your', 'favorite', 'place', 'to', 'visit'], required_words=['favorite', 'place', 'visit'])
    response(long.R_CHAT_49, ['what', 'do', 'you', 'think', 'about', 'technology'], required_words=['think', 'technology'])
    response(long.R_CHAT_50, ['how', 'do', 'you', 'keep', 'healthy'], required_words=['you', 'keep', 'healthy'])



    best_match=max(highest_prob_list,key=highest_prob_list.get)
    #print(highest_prob_list)

    return long.unknown() if highest_prob_list[best_match] < 1 else best_match

def get_response(user_input):
    split_message = re.split(r'\s+|[,;?!.-]\s*', user_input.lower())
    response = check_all_messages(split_message)
    return response

#Testing the response system
while True:
    print('Bot: '+get_response(input('You: ')))
