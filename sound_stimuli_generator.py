# -*- coding: utf8 -*

## Text-to-Speech Initialization
import pyttsx3 as py3
engine = py3.init()

## Settings
engine.setProperty('voice', 'com.apple.voice.enhanced.fr-FR.Aurelie')
engine.setProperty('rate', 180)
engine.setProperty('pitch', 1.0)

## Stimuli texts

test1 = "Paris est une ville dans îles-de France. Paul vient de Paris. Il est?  un, parisien,  deux, parisois,  trois, parisais,  quatre, pariséen"
test2 = "L'Europe est un territoire conventionnellement. Clara vient de l'Europe. Elle est?  un, europienne,  deux, europoise,  trois, europaise,  quatre, européenne"

m1 = "Musième est une ville. Paul vient de Musième. Il est?  un,  musièmien,  deux,  musièmois,  trois,  musièmais,  quatre,  musièméen"
p1 = "Musièpe est une ville. Clara vient de Musièpe. Elle est?  un,  musiépienne,  deux,  musiépoise,  trois,  musiépaise,  quatre,  musiépéenne"
b1 = "Musièbe est une ville. Jean vient de Musièbe. Il est?  un,  musiébien,  deux,  musiébois,  trois,  musiébais,  quatre,  musiébéen"
f1 = "Musièfe est une ville. Marie vient de Musièfe. Elle est?  un,  musiéfienne,  deux,  musiéfoise,  trois,  musiéfaise,  quatre,  musiéféenne"
v1 = "Musiève est une ville. Pierre vient de Musiève. Il est?  un,  musiévien,  deux,  musiévois,  trois,  musiévais,  quatre,  musiévéen"
n1 = "Musiène est une ville. Claire vient de Musiène. Elle est?  un,  musiénienne,  deux,  musiénoise,  trois,  musiénaise,  quatre,  musiénéenne"
t1 = "Musiète est une ville. Thomas vient de Musiète. Il est?  un,  musiétien,  deux,  musiétois,  trois,  musiétais,  quatre,  musiétéen"
d1 = "Musiède est une ville. Sophie vient de Musiède. Elle est?  un,  musiédienne,  deux,  musiédoise,  trois,  musiédaise,  quatre,  musiédéenne"
s1 = "Musièse est une ville. David vient de Musièsse. Il est?  un,  musiéssien,  deux,  musiéssois,  trois,  musiéssais,  quatre,  musiésséen"
z1 = "Musièse est une ville. Zoé vient de Musièse. Elle est?  un,  musiésienne,  deux,  musiéssoise,  trois,  musiésaise,  quatre,  musiéséenne"
l1 = "Musièle est une ville. Gocé vient de Musièle. Il est?  un,  musiélien,  deux,  musiélois,  trois,  musiélais,  quatre,  musiéléen"
S1 = "Musièche est une ville. Léa vient de Musièche. Elle est?  un,  musiéchienne,  deux,  musiéchoise,  trois,  musiéchaise,  quatre,  musiéchéenne."
Z1 = "Musiège est une ville. Benjamin vient de Musiège. Il est?  un,  musiégien,  deux,  musiégeois,  trois,  musiégeais,  quatre,  musiégéen."
j1 = "Musièye est une ville. Gabrielle vient de Musièye. Elle est?  un,  musiéyinne,  deux,  musiéyoise,  trois,  musiéyaisse,  quatre,  musiéyéenne."
k1 = "Musièque est une ville. Léon vient de Musique. Il est?  un,  musiéquien,  deux,  musiéquois,  trois,  musiéquais,  quatre,  musiéquéen."
g1 = "Musiègue est une ville. Julie vient de Musiègue. Elle est?  un,  musiéguienne,  deux,  musiégoise,  trois,  musiégaise,  quatre,  musiéguéenne."
R1 = "Musière est une ville. Antoine vient de Musière. Il est?  un,  musiérien,  deux,  musiérois,  trois,  musiérais,  quatre,  musiéréen."

# Save stimuli as WAV files
engine.save_to_file(m1, 'stimulus1.wav')
engine.save_to_file(p1, 'stimulus2.wav')
engine.save_to_file(b1, 'stimulus3.wav')
engine.save_to_file(f1, 'stimulus4.wav')
engine.save_to_file(v1, 'stimulus5.wav')
engine.save_to_file(n1, 'stimulus6.wav')
engine.save_to_file(t1, 'stimulus7.wav')
engine.save_to_file(d1, 'stimulus8.wav')
engine.save_to_file(s1, 'stimulus9.wav')
engine.save_to_file(z1, 'stimulus10.wav')
engine.save_to_file(l1, 'stimulus11.wav')
engine.save_to_file(S1, 'stimulus12.wav')
engine.save_to_file(Z1, 'stimulus13.wav')
engine.save_to_file(j1, 'stimulus14.wav')
engine.save_to_file(k1, 'stimulus15.wav')
engine.save_to_file(g1, 'stimulus16.wav')
engine.save_to_file(R1, 'stimulus17.wav')

engine.save_to_file(test1, 'paris.wav')
engine.save_to_file(test2, 'europe.wav')


## To run the speech synthesis
engine.runAndWait()