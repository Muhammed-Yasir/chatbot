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
    response(long.R_CHAT_61, ['role', 'Prime', 'Minister', 'Indian', 'government'], required_words=['Prime', 'Minister', 'Indian', 'government'])
    response(long.R_CHAT_62, ['Members', 'Parliament', 'elected', 'India'], required_words=['Members', 'Parliament', 'elected', 'India'])
    response(long.R_CHAT_63, ['significance', 'President', 'India', 'government'], required_words=['President', 'India', 'government'])
    response(long.R_CHAT_64, ['Indian', 'Parliament', 'structured'], required_words=['Indian', 'Parliament', 'structured'])
    response(long.R_CHAT_65, ['role', 'Supreme', 'Court', 'Indian', 'politics'], required_words=['Supreme', 'Court', 'Indian', 'politics'])
    response(long.R_CHAT_66, ['state', 'governments', 'formed', 'India'], required_words=['state', 'governments', 'formed', 'India'])
    response(long.R_CHAT_67, ['major', 'political', 'parties', 'India', 'ideologies'], required_words=['political', 'parties', 'India', 'ideologies'])
    response(long.R_CHAT_68, ['elections', 'conducted', 'India'], required_words=['elections', 'conducted', 'India'])
    response(long.R_CHAT_69, ['role', 'Election', 'Commission', 'India'], required_words=['role', 'Election', 'Commission', 'India'])
    response(long.R_CHAT_70, ['fundamental', 'rights', 'Indian', 'Constitution'], required_words=['fundamental', 'rights', 'Indian', 'Constitution'])
    response(long.R_CHAT_71, ['significance', 'Directive', 'Principles', 'State', 'Policy', 'Indian', 'Constitution'], required_words=['Directive', 'Principles', 'State', 'Policy', 'Indian', 'Constitution'])
    response(long.R_CHAT_72, ['Prime', 'Minister', 'India', 'appointed'], required_words=['Prime', 'Minister', 'India', 'appointed'])
    response(long.R_CHAT_73, ['procedure', 'amending', 'Indian', 'Constitution'], required_words=['procedure', 'amending', 'Indian', 'Constitution'])
    response(long.R_CHAT_74, ['role', 'Governor', 'state', 'government'], required_words=['role', 'Governor', 'state', 'government'])
    response(long.R_CHAT_75, ['Chief', 'Justice', 'India', 'appointed'], required_words=['Chief', 'Justice', 'India', 'appointed'])
    response(long.R_CHAT_76, ['role', 'Chief', 'Election', 'Commissioner', 'India'], required_words=['role', 'Chief', 'Election', 'Commissioner', 'India'])
    response(long.R_CHAT_77, ['importance', 'Preamble', 'Indian', 'Constitution'], required_words=['importance', 'Preamble', 'Indian', 'Constitution'])
    response(long.R_CHAT_78, ['procedure', 'removal', 'President', 'India'], required_words=['procedure', 'removal', 'President', 'India'])
    response(long.R_CHAT_79, ['judges', 'Supreme', 'Court', 'India', 'appointed'], required_words=['judges', 'Supreme', 'Court', 'India', 'appointed'])
    response(long.R_CHAT_80, ['role', 'Attorney', 'General', 'India'], required_words=['role', 'Attorney', 'General', 'India'])
    response(long.R_CHAT_81, ['significance', 'Union', 'Budget', 'Indian', 'governance'], required_words=['significance', 'Union', 'Budget', 'Indian', 'governance'])
    response(long.R_CHAT_82, ['Vice', 'President', 'India', 'elected'], required_words=['Vice', 'President', 'India', 'elected'])
    response(long.R_CHAT_83, ['composition', 'Rajya', 'Sabha', 'Council', 'States'], required_words=['composition', 'Rajya', 'Sabha', 'Council', 'States'])
    response(long.R_CHAT_84, ['Lok', 'Sabha', 'House', 'People', 'constituted'], required_words=['Lok', 'Sabha', 'House', 'People', 'constituted'])
    response(long.R_CHAT_85, ['role', 'Chief', 'Justice', 'India', 'judiciary'], required_words=['role', 'Chief', 'Justice', 'India', 'judiciary'])
    response(long.R_CHAT_86, ['process', 'impeachment', 'judges', 'India'], required_words=['process', 'impeachment', 'judges', 'India'])
    response(long.R_CHAT_87, ['role', 'Speaker', 'Lok', 'Sabha'], required_words=['role', 'Speaker', 'Lok', 'Sabha'])
    response(long.R_CHAT_88, ['Union', 'Territories', 'governed', 'India'], required_words=['Union', 'Territories', 'governed', 'India'])
    response(long.R_CHAT_89, ['role', 'Finance', 'Commission', 'India'], required_words=['role', 'Finance', 'Commission', 'India'])
    response(long.R_CHAT_90, ['Chief', 'Ministers', 'states', 'appointed', 'India'], required_words=['Chief', 'Ministers', 'states', 'appointed', 'India'])
    response(long.R_CHAT_91, ['procedure', 'dissolution', 'Lok', 'Sabha'], required_words=['procedure', 'dissolution', 'Lok', 'Sabha'])
    response(long.R_CHAT_92, ['role', 'Comptroller', 'Auditor', 'General', 'India'], required_words=['role', 'Comptroller', 'Auditor', 'General', 'India'])
    response(long.R_CHAT_93, ['significance', 'unity', 'diversity', 'Indian', 'politics'], required_words=['significance', 'unity', 'diversity', 'Indian', 'politics'])
    response(long.R_CHAT_94, ['ordinances', 'promulgated', 'India'], required_words=['ordinances', 'promulgated', 'India'])
    response(long.R_CHAT_95, ['procedure', 'division', 'powers', 'Union', 'states', 'India'], required_words=['procedure', 'division', 'powers', 'Union', 'states', 'India'])
    response(long.R_CHAT_96, ['role', 'Deputy', 'Chairman', 'Rajya', 'Sabha'], required_words=['role', 'Deputy', 'Chairman', 'Rajya', 'Sabha'])
    response(long.R_CHAT_97, ['High', 'Court', 'judges', 'appointed', 'India'], required_words=['High', 'Court', 'judges', 'appointed', 'India'])
    response(long.R_CHAT_98, ['significance', 'Concurrent', 'List', 'Indian', 'federalism'], required_words=['significance', 'Concurrent', 'List', 'Indian', 'federalism'])
    response(long.R_CHAT_99, ['members', 'legislative', 'assemblies', 'MLAs', 'elected', 'India'], required_words=['members', 'legislative', 'assemblies', 'MLAs', 'elected', 'India'])
    response(long.R_CHAT_100, ['role', 'Central', 'Bureau', 'Investigation', 'India'], required_words=['role', 'Central', 'Bureau', 'Investigation', 'India'])
    response(long.R_CHAT_101, ['procedure', 'adoption', 'Indian', 'Constitution'], required_words=['procedure', 'adoption', 'Indian', 'Constitution'])
    response(long.R_CHAT_102, ['significance', 'amendment', 'Indian', 'Constitution'], required_words=['significance', 'amendment', 'Indian', 'Constitution'])
    response(long.R_CHAT_103, ['role', 'Public', 'Accounts', 'Committee', 'India'], required_words=['role', 'Public', 'Accounts', 'Committee', 'India'])
    response(long.R_CHAT_104, ['procedure', 'legislation', 'Indian', 'Parliament'], required_words=['procedure', 'legislation', 'Indian', 'Parliament'])
    response(long.R_CHAT_105, ['role', 'Rajya', 'Sabha', 'India'], required_words=['role', 'Rajya', 'Sabha', 'India'])
    response(long.R_CHAT_106, ['procedure', 'financial', 'emergency', 'India'], required_words=['procedure', 'financial', 'emergency', 'India'])
    response(long.R_CHAT_107, ['significance', 'judicial', 'review', 'India'], required_words=['significance', 'judicial', 'review', 'India'])
    response(long.R_CHAT_108, ['role', 'Planning', 'Commission', 'India'], required_words=['role', 'Planning', 'Commission', 'India'])
    response(long.R_CHAT_109, ['procedure', 'appointment', 'judges', 'High', 'Courts', 'India'], required_words=['procedure', 'appointment', 'judges', 'High', 'Courts', 'India'])
    response(long.R_CHAT_110, ['role', 'Leader', 'Opposition', 'India'], required_words=['role', 'Leader', 'Opposition', 'India'])
    response(long.R_CHAT_111, ['origin', 'football', 'game'], required_words=['origin', 'football', 'game'])
    response(long.R_CHAT_112, ['FIFA', 'World', 'Cup', 'history'], required_words=['FIFA', 'World', 'Cup', 'history'])
    response(long.R_CHAT_113, ['most', 'successful', 'football', 'club'], required_words=['successful', 'football', 'club'])
    response(long.R_CHAT_114, ['Ballon', 'd\'Or', 'award', 'criteria'], required_words=['Ballon', 'd\'Or', 'award', 'criteria'])
    response(long.R_CHAT_115, ['UEFA', 'Champions', 'League', 'format'], required_words=['UEFA', 'Champions', 'League', 'format'])
    response(long.R_CHAT_116, ['major', 'football', 'tournaments'], required_words=['major', 'football', 'tournaments'])
    response(long.R_CHAT_117, ['notable', 'football', 'rivalries'], required_words=['notable', 'football', 'rivalries'])
    response(long.R_CHAT_118, ['VAR', 'use', 'football', 'matches'], required_words=['VAR', 'use', 'football', 'matches'])
    response(long.R_CHAT_119, ['different', 'football', 'positions'], required_words=['different', 'football', 'positions'])
    response(long.R_CHAT_120, ['highest', 'transfer', 'fee', 'paid', 'football', 'player'], required_words=['highest', 'transfer', 'fee', 'paid', 'football', 'player'])
    response(long.R_CHAT_121, ['football', 'clubs', 'with', 'most', 'international', 'titles'], required_words=['football', 'clubs', 'international', 'titles'])
    response(long.R_CHAT_122, ['top', 'scorer', 'FIFA', 'World', 'Cup', 'history'], required_words=['top', 'scorer', 'FIFA', 'World', 'Cup', 'history'])
    response(long.R_CHAT_123, ['UEFA', 'European', 'Championship', 'winners'], required_words=['UEFA', 'European', 'Championship', 'winners'])
    response(long.R_CHAT_124, ['football', 'players', 'with', 'most', 'Ballon', 'd\'Or', 'awards'], required_words=['football', 'players', 'Ballon', 'd\'Or', 'awards'])
    response(long.R_CHAT_125, ['role', 'football', 'manager'], required_words=['role', 'football', 'manager'])
    response(long.R_CHAT_126, ['history', 'El', 'Clasico'], required_words=['history', 'El', 'Clasico'])
    response(long.R_CHAT_127, ['significant', 'football', 'rule', 'changes'], required_words=['significant', 'football', 'rule', 'changes'])
    response(long.R_CHAT_128, ['Golden', 'Boot', 'award', 'winners', 'FIFA', 'World', 'Cup'], required_words=['Golden', 'Boot', 'award', 'winners', 'FIFA', 'World', 'Cup'])
    response(long.R_CHAT_129, ['major', 'football', 'leagues', 'world'], required_words=['major', 'football', 'leagues', 'world'])
    response(long.R_CHAT_130, ['football', 'stadium', 'with', 'largest', 'capacity'], required_words=['football', 'stadium', 'largest', 'capacity'])
    response(long.R_CHAT_131, ['most', 'expensive', 'football', 'transfers'], required_words=['expensive', 'football', 'transfers'])
    response(long.R_CHAT_132, ['football', 'clubs', 'with', 'most', 'domestic', 'titles'], required_words=['football', 'clubs', 'domestic', 'titles'])
    response(long.R_CHAT_133, ['role', 'FIFA', 'president'], required_words=['role', 'FIFA', 'president'])
    response(long.R_CHAT_134, ['football', 'players', 'with', 'highest', 'market', 'value'], required_words=['football', 'players', 'highest', 'market', 'value'])
    response(long.R_CHAT_135, ['significant', 'football', 'injuries'], required_words=['significant', 'football', 'injuries'])
    response(long.R_CHAT_136, ['football', 'clubs', 'with', 'most', 'fans'], required_words=['football', 'clubs', 'fans'])
    response(long.R_CHAT_137, ['role', 'football', 'captain'], required_words=['role', 'football', 'captain'])
    response(long.R_CHAT_138, ['football', 'clubs', 'with', 'longest', 'unbeaten', 'streaks'], required_words=['football', 'clubs', 'longest', 'unbeaten', 'streaks'])
    response(long.R_CHAT_139, ['football', 'managers', 'with', 'most', 'trophies'], required_words=['football', 'managers', 'trophies'])
    response(long.R_CHAT_140, ['football', 'clubs', 'with', 'most', 'expensive', 'squads'], required_words=['football', 'clubs', 'expensive', 'squads'])

    response(long.R_CHAT_141, ['best', 'football', 'player', 'world'], required_words=['best', 'football', 'player', 'world'])
    response(long.R_CHAT_142, ['player', 'most', 'goals', 'FIFA', 'World', 'Cup', 'tournament'], required_words=['player', 'most', 'goals', 'FIFA', 'World', 'Cup', 'tournament'])
    response(long.R_CHAT_143, ['footballer', 'King', 'Assists', 'modern', 'football'], required_words=['footballer', 'King', 'Assists', 'modern', 'football'])
    response(long.R_CHAT_144, ['player', 'most', 'Ballon', 'd\'Or', 'awards', 'history'], required_words=['player', 'most', 'Ballon', 'd\'Or', 'awards', 'history'])
    response(long.R_CHAT_145, ['footballer', 'Egyptian', 'King'], required_words=['footballer', 'Egyptian', 'King'])
    response(long.R_CHAT_146, ['player', 'incredible', 'speed', 'dribbling', 'skills', 'CR7'], required_words=['player', 'incredible', 'speed', 'dribbling', 'skills', 'CR7'])
    response(long.R_CHAT_147, ['captain', 'Argentina', 'national', 'team', 'greatest', 'players'], required_words=['captain', 'Argentina', 'national', 'team', 'greatest', 'players'])
    response(long.R_CHAT_148, ['footballer', 'nicknamed', 'Magician'], required_words=['footballer', 'nicknamed', 'Magician'])
    response(long.R_CHAT_149, ['player', 'known', 'nickname', 'Golden', 'Boy'], required_words=['player', 'known', 'nickname', 'Golden', 'Boy'])
    response(long.R_CHAT_150, ['footballer', 'called', 'Baby-faced', 'Assassin'], required_words=['footballer', 'called', 'Baby-faced', 'Assassin'])
    response(long.R_CHAT_151, ['footballer', 'recognized', 'nickname', 'Kun'], required_words=['footballer', 'recognized', 'nickname', 'Kun'])
    response(long.R_CHAT_152, ['player', 'often', 'referred', 'nickname', 'Flea'], required_words=['player', 'often', 'referred', 'nickname', 'Flea'])
    response(long.R_CHAT_153, ['footballer', 'known', 'nickname', 'Phenomenon'], required_words=['footballer', 'known', 'nickname', 'Phenomenon'])
    response(long.R_CHAT_154, ['player', 'known', 'nickname', 'Neymar'], required_words=['player', 'known', 'nickname', 'Neymar'])
    response(long.R_CHAT_155, ['footballer', 'referred', 'nickname', 'King', 'Lionel'], required_words=['footballer', 'referred', 'nickname', 'King', 'Lionel'])
    response(long.R_CHAT_156, ['player', 'recognized', 'nickname', 'G.O.A.T.'], required_words=['player', 'recognized', 'nickname', 'G.O.A.T.'])
    response(long.R_CHAT_157, ['footballer', 'nicknamed', 'Fenômeno'], required_words=['footballer', 'nicknamed', 'Fenômeno'])
    response(long.R_CHAT_158, ['player', 'known', 'nickname', 'Flash'], required_words=['player', 'known', 'nickname', 'Flash'])
    response(long.R_CHAT_159, ['footballer', 'called', 'nickname', 'Golden', 'Boy'], required_words=['footballer', 'called', 'nickname', 'Golden', 'Boy'])
    response(long.R_CHAT_160, ['player', 'referred', 'nickname', 'CR7'], required_words=['player', 'football', 'nickname', 'CR7'])


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