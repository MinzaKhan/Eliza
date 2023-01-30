''' This is a program where Eliza plays the role of a university academic advisor, unlike the traditional Eliza program that plays the role of a psychotherapist. The code remembers a few details about the student and brings those topics up in conversation. 
The input given by the student begins with "< ".
The response given by Eliza begins with "> ".


Usage instructions: Enter your input after the "< " sign. End your input with proper punctuation marks. The Eliza code will then give a suitable response.
Example 1:
input: I am feeling stressed.
output: The academic year gets stressful sometimes, but I am sure you will be fine!
Example 2:
input: I want to study.
output: Why do you want to study.
Example 3:
input: I don't know how many credits I need to graduate.
output: Why don't you know how many credits you need to graduate?


The first thing that the program asks is the user's name, the second thing is their major. It stores both these values and then the name and major
are used later in the conversation in order to make the conversation feel more personal.
The algorithm takes the input from the user, and then it first checks whether the input is gibberish or abusive language.
In case the input is gibberish, the program tells the user to rephrase the sentence, or it tells the user not to enter gibberish statements. It gives an putput 
from a number of output choices present in the list List_gibberish, such as "That does not make sense." or "Please do not enter gibberish."
If the user uses abusive language in the input, and it is detected by the program, the program gives an output from a number of output choices present in the 
list List_abusive, such as "Please mind your language!" or "That's a very rude thing to say!".
If the input is neither abusive nor gibberish, we move on to the next part of the code, where it tries to match the input to a number of regular expressions
present in the list "List". For each regular expression, the list contains a number of suitable responses. For example, if the user says "thank you",
the code may give the response "You're welcome!" or "I am happy that I could help you!". If the user input is "I am stressed", the code may give the response
"Don't lose hope.",  "You sound discouraged." or "Why are you stressed?". 
The code begins finding a match from the beginning of the list. So the statements in the beginning of the list have a higher priority than the statements in the 
end. If the code reaches the end without finding a match, there is a regular expression "(.*)", which matches any input. If the code reaches this, there are many
generic outputs stored that the cod ecan give such as: "Go on.", "Tell me more.", "Do you enjoy your classes?", "What do you like most about %2?" (here %2 is replaced by the major
of the student, which the program had already asked and stored in the beginning.)
The program also transforms part of the input when it gives the response. For instance, if the input is "I don't know how many credits I need to graduate.",
the sentence will be matched to the regular expression ("I don't know (.*?)(\.|!|,|\?)"). The response given will be, "Why don't you know how many credits you
need to graduate?". Here in the input, the part "how many credits I need to graduate" has been changed to "how many credits you need to graduate". "I" has 
been transformed to "you" using the list of transformation, List_transformations. This list also converts myself to yourself, me to you, etc. in the matched 
part of the input before giving the output. 
In this way, the code is able to detect gibberish input, abusive language, and give clever responses. It also stores some data about the user to use in the 
conversation.
Keyword spotting is also being done. The code checks if the words stupid, idiot, and idiotic, are present anywhere in the input, and tells the user not to use 
abusive language. Similarly, if the keyword "study" is spotted anywhere in the input, Eliza gives the response "You should study hard!".
'''


'''importing the library for regular expressions.'''
import re 
import random 
'''importing the library random so that the code randomly chooses an output from a list of suitable outputs once a match is found.'''


name = "" #This variable stores the name of the student.
major = "" #This variable saves the major of the student.
pattern_1 = "(My|my) name is (\\w+)" #When the program asks the student their name, it matches the response with this regular expression and saves the name 
#in the variable "name"
pattern_2 = "(\\w+)"
pattern_3 = "(.*)"

'''The function gibberish() is used to detect if the user has input gibberish. It checks this
by checking if the user has input the same letter more than two times(as no word in english has the same letter thrice).
It also returns true if the same digit has been input more than 2 times. If this function returns true, the program tells the student not to enter gibberish
or to try rephrasing the sentence.'''
def gibberish(user_input):
	'''The regular expression "([a-zA-Z])\\1{2,}" checks if the same letter has been input more than 2 times in a given string.'''
	pattern_gibberish1= "([a-zA-Z])\\1{2,}" 
	'''The regular expression "([0-9])\\1{2,}" checks if the same digit has been input more than 2 times in a given string.'''
	pattern_gibberish2= "([0-9])\\1{2,}"
	'''Checking if the input by the user matches the patterns for detecting gibberish.'''
	if(re.search(pattern_gibberish1, user_input) or re.search(pattern_gibberish2, user_input)): 
		return True
	return False

'''The function abusive() checks for abusive language in the input given by the student. It looks for words such as stupid, idiot, disgusting, and tells the 
student not to use such language if a match is found.'''
def abusive(user_input):
	'''The regular expression "(You are (bad|ugly|disgusting|stupid|dumb|silly|jerk))" checks if the student has called the program bad, stupid, dumb, etc. '''
	pattern_abusive1= "(You are (bad|ugly|disgusting|stupid|dumb|silly|jerk))"
	'''The regular expression "(stupid|idiot|idiotic)" checks if the words stupid, idiot, or idiotic are present in the 
	input given by the user. Keyword spotting is being done here. If these words are present anywhere in the input, the function returns true and the program tells the student not to use such language.'''
	pattern_abusive2 = "(stupid|idiot|idiotic)"
	if(re.search(pattern_abusive1, user_input) or re.search(pattern_abusive2, user_input) ):
		return True
	return False
'''The following list, "List", contains all the regular expressions that the program tries to match with the input given by the user. 
The items mentioned first in the list have a higher priority than the items mentioned later, as the program stops as soon as it finds a match.
If no match is found and the program reaches the end of the list, it matches the sentence to the regular expression ".*?", as this
regular expression can match with any sentence. It then gives a list of generic responses as it has found no match, such as 
"Go on.", "Do you enjoy your classes?", "That's interesting.", etc. It also brings up topics from the past conversation by asking specifically about the 
major of the student, and mentioning their name in the conversation.
"%1" has been used in the sample outputs to show that the user input will be transformed and given as the output there. For example,
if the input "I want to know how I can get good marks" is given by the student, it will match the regular expression "I want to know (.*?)(\.|!|,)".
The output chosen may then be "Why do you want to know %1?". The code will then replace %1 with "how I can get good marks" after transforming it and changing it
to "how you can get good marks". So the final response given by the program will be "Why do you want to know how you can get good marks?"
If "%2" is present in the list of possible responses, it will be replaced by the student's major when the program uses it as a response. 
If "%3" is present in the list of possible responses, it will be replaced by the student's name when the program uses it as a response.  
'''
List= [["I am feeling (depressed|anxious|stressed|tired)(.*?)", 
["Why are you feeling %1?", "The academic year gets stressful sometimes, but I am sure you will be fine!", "Everything will be fine %3.", "Don't lose hope."]], 
["I am very (depressed|anxious|stressed|tired)(.*?)", ["Why are you %1?", "You sound discouraged.", "Everything will be fine %3.", "Don't lose hope."]],
["I feel (depressed|anxious|stressed|tired)(.*?)", ["Why are you %1?", "You sound discouraged.", "Everything will be fine %3.", "Don't lose hope."]],
["I feel very (depressed|anxious|stressed|tired)(.*?)", ["Why are you %1?", "You sound discouraged.", "Everything will be fine %3.", "Don't lose hope."]],
["(Thanks|thanks|thank you|Thank you)",["You're welcome!", "I am happy that I could help you!", "My pleasure!"]],
["Sorry|sorry|i apologize|I apologize",["That's alright.", "Don't worry about it!", "I hope you have learnt from your mistakes.", "You don't need to apologize."]],
["I am (depressed|anxious|stressed|tired)(.*?)", ["Why are you %1?", "You sound discouraged.", "Everything will be fine %3.", "Don't lose hope."]],
["I love (.*?)(\.|!|,)", ["What do you love about %1?","I am happy to hear that! Tell me more about %1.", "What do you love most about %1?"]],
["I like (.*?)(\.|!|,)", ["What do you like about %1?","I am happy to hear that! Tell me more about %1.", "What do you like most about %1?"]],
["I am very (happy|excited)(.*?)", ["I am glad to hear that you are %1!", "That is good to know."]],
["I feel very (happy|excited)(.*?)", ["I am glad to hear that you are %1!", "That is good to know."]],
["I feel (happy|excited)(.*?)", ["I am glad to hear that you are %1!", "That is good to know."]],
["I am (happy|excited)(.*?)", ["I am glad to hear that you are %1!", "That is good to know."]],
["You are (.*?)(\.|!|,)", ["What makes you think I am %1?", "Why do you think so?"]],
["I want to know (.*?)(\.|!|,)", ["Why do you want to know %1?", "You should already know %1 if you are serious about your studies."]],
["\\bYes|yes|yeah|Yeah\\b", ["You sound certain.", "You seem quite positive.", "You are sure."]],
["\\bNo|no\\b", ["Why not?", "You sound discouraged."]],
["Not|not", ["Why not?", "You are being negative."]],
["I hate (.*?)(\.|!|,)", ["You are being very negative.", "Why do you hate %1?", "It is very sad that you hate %1."]],
["I think (.*?)(\.|!|,)", ["Why do you think so?", "What makes you think %1?"]],
["I can't (.*?)(\.|!|,)", ["Why do you think you can't %1 ?", "You sound demotivated", "Try harder!", "Why can't you %1?"]],
["How should|can I (.*?)(\.|!|,|\?)", ["How do you think you should %1?", "You should know how to %1."]],
["I don't know how to (.*?)(\.|!|,|\?)", ["Why don't you know how to %1?", "Try to find out how that can be done.", "You should know how to %1"]],
["I don't know (.*?)(\.|!|,|\?)", ["I am concerned that you don't know %1.","That is irresponsible.", "Why don't you know %1?"]],
["I don't want to (.*?)(\.|!|,)", ["Why don't you want to %1?", "Why so?", "Why not?"]],
["I don't think (.*?)(\.|!|,)", ["Why do you think so?", "Why so?", "Why not?", "Don't be negative."]],
["I am (.*?)(\.|!|,|\?)",["Why do you think you are %1?"]],
["I (.*?) question|Question|ask|Ask", ["Sure, what do you want to ask me?", "Sure, how can I help you?"]],
["I want (.*?)(\.|!|,)", ["Why do you want %1?"]],
["\\bstudy\\b",["You should study hard!"]],
["\\bgraduate\\b", ["Have you thought about what you will do after you graduate?"]],
["(.*)", ["Tell me more.", "Go on.", "Do you enjoy your classes?", "That's interesting.", "How often do you study?", "What do you like most about %2?", "Do you enjoy studying %2?", "Please go on."]]]
 
'''The list "List_gibberish" contains a set of responses that the program chooses from randomly if a gibberish input is detected.'''
List_gibberish = ["I cannot understand what you are saying.", "That does not make sense.", "Please do not enter gibberish.", "Can you please rephrase that?"]
'''The list "List_abusive" contains a set of responses that the program chooses from randomly if abusive language is detected in the input.'''
List_abusive = ["Please mind your language!", "That's a very rude thing to say!"]
'''The list "List_transformations" is used to transform the input given by the user so that the program can give the correct output. For example,
for the input "I don't know how many credits I need to graduate", the output will be "Why don't you know how many credits you need to graduate?".
Here, the part "how many credits I need to graduate" has been transformed to "how many credits you need to graduate" using the transformation list.'''
List_transformations = [["I", "you"], ["my", "your"], ["myself", "yourself"], ["am", "are"], ["you", "I"], ["myself", "yourself"], ["are", "am"]]
'''The program starts by identifying that this is the program Eliza.'''
print("This is Eliza The Academic Advisor, programmed by Minza Nadeem Khan.")
'''The conversation begins by the program asking the name of the student.'''
print("> Hi! I am Eliza, an academic advisor. What is your name?") 
user_input = input("< ")
if(re.search(pattern_1,user_input)):
	if(gibberish(user_input)):
		print("> "+random.choice(List_gibberish))
	elif(abusive(user_input)):
		print("> "+random.choice(List_abusive))
	else:
		x= re.search(pattern_1,user_input)
		name = x.group(2) #The name has been saved and will be brought up in the conversation.
		'''The program then asks the student's major'''
		print("> Nice to meet you "+x.group(2) +"! What is your major?")
else:
	if(gibberish(user_input)):
		print("> "+random.choice(List_gibberish))
	elif(abusive(user_input)):
		print("> "+random.choice(List_abusive))
	else:
		x = re.search(pattern_2,user_input)
		name = x.group(1)
		print("> Nice to meet you "+x.group(1)+"! What is your major?")
	

user_input = input("< ")
x= re.search(pattern_3,user_input)
major = x.group(1) #The student's major has been saved and will be brought up in the conversation later.
print("> That sounds interesting!")

j=""
'''If "%1" is present in the response chosen by the program, the program tranforms the part of the student input
that matches the regular expression and gives a response based on that.'''
x ="%1" 
'''If "%2" is present in the response chosen by the program, it is replaced by the name of the student.'''
y ="%2"
'''If "%3" is present in the response chosen by the program, it is replaced by the major of the student.'''
a ="%3"

'''The following while loop keeps taking input from the student and gives responses based on the student input.'''

while(1):
	user_input = input("< ")
	'''Each time the student gives an input, the program first checks whether the input is gibberish. If it is, the program
	gives an appropriate response for that and the student enters another input.'''
	if(gibberish(user_input)):
		print("> "+random.choice(List_gibberish))
	elif(abusive(user_input)):
		'''If the input is not gibberish, the program checks if has any abusive language. If the input has abusive language,
	a response is given based on that and the student is prompted to give an input again.'''
		print("> "+random.choice(List_abusive))
		'''If the user inputs bye or goodbye, the program gives the response "Bye!" and then ends.'''
	elif(re.search("(bye|Bye|goodbye|Goodbye)", user_input)):
		print("> Bye!")
		break

	else:
		'''If the input is neither gibberish nor abusive, it is matched with the list "List" to check if the input matches any regular expressions there.'''
		for i, n in List:
			if(re.search(i,user_input)):
				'''If a match is found, a response is chosen randomly from a set of possible responses.'''
				j = random.choice(n)
				'''Checking if "%1" is present in the response chosen. '''
				index = j.find(x)
				'''Checking if "%2" is present in the response chosen. '''
				index1 = j.find(y)
				'''Checking if "%3" is present in the response chosen. '''
				index2 = j.find(a)
				'''The variable z stores the output of matching the regular expression with the usrr input.'''
				z = re.search(i,user_input)
				if(index != -1):
					num = 0
					new_output = ""
					'''Transforming the part of the input that matched so that it can be used in the response given by the program.'''
					original_input = z.group(1)
					new_word = ""
					for word in original_input:
						for k, l in List_transformations:
							if word==k:
								num = 1
								new_word = l
								break
						if (num == 1):
							new_output = new_output + new_word
						else:
							new_output = new_output + word
						num = 0
						new_word = ""
					index_1 = index+2
					print("> "+j[:index] +new_output+j[index_1:])
				
				elif(index1!=-1):
					'''Replacing "%2" with the major of the student in the response.'''
					index_1 = index1+2
					print("> "+j[:index1] +major+j[index_1:])
				
				elif(index2!=-1):
					'''Replacing "%3" with the name of the student in the response.'''
					index_1 = index2+2
					print("> "+j[:index2] +name+j[index_1:])
				
				else:
					'''If "%1", "%2", and "%3" are not present in the output chosen, the program just gives the chosen response as the output with no modifications.'''
					print("> "+j)
				'''the loop ends once a match is found so that it does not give multiple responses.'''
				break

