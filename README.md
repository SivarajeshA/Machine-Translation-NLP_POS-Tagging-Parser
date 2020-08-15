# Machine-Translation-NLP_POS-Tagging-Parser
Bottom UP Parser<br/>
Look at input, then try to find rules in grammar that apply to input • Stack keeps track of what has been found so far and still needs to be integrated in parse tree.

<br/>
Given the following grammar:<br/>
S → NP VP<br/>
NP → ART N | ART N PP | PRON | N<br/>
VP → V NP PP | V NP<br/>
PP → P NP<br/>
ART → a | an | the<br/>
N → boy | telescope | football | jam | book | saw | play<br/>
PRON → I | we | you | they<br/>
V → saw | play | eat | study | jam<br/>
P → with | for<br/>
<br/>Parser shows whether the sentences are parsable or not, and if it is parsable then output the parsing of each sentences be in bracketed parse (tree) format in a text file (output.txt) as shown below. If there are multiple parses for a sentence it shows at least two parses.<br/>

Example:<br/>
The sentence “I saw a boy with a telescope” has two possible parses:<br/>
 ( S ( NP ( PRON “I” ) ) ( VP ( V “saw” )( NP ( ART “a”) ( N “boy”)) ( PP ( P “with”) ( NP ( ART “a” ) ( N “telescope”)))))<br/>
 ( S ( NP ( PRON “I” ) ) ( VP ( V “saw” ) ( NP ( ART “a”) ( N “boy”) ( PP ( P “with”) ( NP ( ART “a” ) ( N “telescope”))))))<br/>
