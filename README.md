This Eliza program plays the role of a university academic advisor, unlike the traditional Eliza program that plays the role of a psychotherapist. The code remembers a few details about the student and brings those topics up in conversation. 
The input given by the student begins with "< ".
The response given by Eliza begins with "> ".


Usage instructions: Enter your input after the "< " sign. End your input with proper punctuation marks. The Eliza code will then give a suitable response.

Example 1:
input: I am feeling stressed.
output: The academic year gets stressful sometimes, but I am sure you will be fine!

Example 2:
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
generic outputs stored that the cod ecan give such as: "Go on.", "Tell me more.", "Do you enjoy your classes?", "What do you like most about %2?" (here %2 is replaced by the major of the student, which the program had already asked and stored in the beginning.)

The program also transforms part of the input when it gives the response. For instance, if the input is "I don't know how many credits I need to graduate.",
the sentence will be matched to the regular expression ("I don't know (.*?)(\.|!|,|\?)"). The response given will be, "Why don't you know how many credits you
need to graduate?". Here in the input, the part "how many credits I need to graduate" has been changed to "how many credits you need to graduate". "I" has 
been transformed to "you" using the list of transformation, List_transformations. This list also converts myself to yourself, me to you, etc. in the matched 
part of the input before giving the output. 

In this way, the code is able to detect gibberish input, abusive language, and give clever responses. It also stores some data about the user to use in the 
conversation. Keyword spotting is also being done. The code checks if the words stupid, idiot, and idiotic, are present anywhere in the input, and tells the user not to use abusive language. Similarly, if the keyword "study" is spotted anywhere in the input, Eliza gives the response "You should study hard!".
