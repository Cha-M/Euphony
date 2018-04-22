import csv
import unicodedata
import collections
import re
from collections import OrderedDict
from os import system
from random import choice
from random import shuffle
from itertools import zip_longest
from tkinter import *
from tkinter.filedialog import *
from tkinter import ttk
from tkinter.font import Font
from tkinter.scrolledtext import ScrolledText
from tkinter import messagebox
from tkinter.messagebox import showwarning
from tkinter.messagebox import showinfo
from statistics import mean

class phonemeLists:
    cfrom=[]
    vfrom=[]
    c2from=[]
    v2from=[]
    c3from=[]
    v3from=[]
####
    cdoopfrom=[]
    vdoopfrom=[]
    begvfrom=[]
    begv2from=[]
    begv3from=[]
    begcfrom=[]
    begc2from=[]
    begc3from=[]
    begcdoopfrom=[]
    begvdoopfrom=[]
    endvfrom=[]
    endv2from=[]
    endv3from=[]
    endcfrom=[]
    endc2from=[]
    endc3from=[]
    endcdoopfrom=[]
    endvdoopfrom=[]
    patterns=[]
    banned=[]
    stringpatlist=[]
    finalLegibleDictionary=OrderedDict()
    replacer={}
    words=[]
    individual=[]
    MeasuredPatterns={}
    cipher={}
    translated=[]
    averageLengths={}
    patternLengths={}
    rightLengthPatterns=[]
    rightendingpatterns=[]
    texttocipher=""
    ciphersourcewords=[]
    wordsXPatterns=[]

##class euWindow:
##    euTreeview=ttk.Treeview()

class otherVariables:
    filetitle = 'Euphony'
    integerCountdown = 0
    saveName = ''
    invisibles = []
    allConsonants = ['B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'X', 'Z', 'b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'x', 'z'] + ['Ç', 'Ð', 'Ñ', '×', 'Ý', 'Þ', 'ß', 'ç', 'ð', 'ñ', 'ý', 'þ', 'ÿ', 'Ć', 'ć', 'Ĉ', 'ĉ', 'Ċ', 'ċ', 'Č', 'č', 'Ď', 'ď', 'Đ', 'đ', 'Ĝ', 'ĝ', 'Ğ', 'ğ', 'Ġ', 'ġ', 'Ģ', 'ģ', 'Ĥ', 'ĥ', 'Ħ', 'ħ', 'Ĳ', 'ĳ', 'Ĵ', 'ĵ', 'Ķ', 'ķ', 'ĸ', 'Ĺ', 'ĺ', 'Ļ', 'ļ', 'Ľ', 'ľ', 'Ŀ', 'ŀ', 'Ł', 'ł', 'Ń', 'ń', 'Ņ', 'ņ', 'Ň', 'ň', 'ŉ', 'Ŋ', 'ŋ', 'Ŕ', 'ŕ', 'Ŗ', 'ŗ', 'Ř', 'ř', 'Ś', 'ś', 'Ŝ', 'ŝ', 'Ş', 'ş', 'Š', 'š', 'Ţ', 'ţ', 'Ť', 'ť', 'Ŧ', 'ŧ', 'Ŵ', 'ŵ', 'Ŷ', 'ŷ', 'Ÿ', 'Ź', 'ź', 'Ż', 'ż', 'Ž', 'ž', 'ſ', 'ƀ', 'Ɓ', 'Ƃ', 'ƃ', 'Ƅ', 'ƅ', 'Ɔ', 'Ƈ', 'ƈ', 'Ɖ', 'Ɗ', 'Ƌ', 'ƌ', 'ƍ', 'Ƒ', 'ƒ', 'Ɠ', 'Ɣ', 'ƕ', 'Ƙ', 'ƙ', 'ƚ', 'ƛ', 'Ɯ', 'Ɲ', 'ƞ', 'Ƣ', 'ƣ', 'Ƥ', 'ƥ', 'Ʀ', 'Ƨ', 'ƨ', 'Ʃ', 'ƪ', 'ƫ', 'Ƭ', 'ƭ', 'Ʈ', 'Ƴ', 'ƴ', 'Ƶ', 'ƶ', 'Ʒ', 'Ƹ', 'ƹ', 'ƺ', 'ƻ', 'Ƽ', 'ƽ', 'ƾ', 'ƿ', 'ǀ', 'ǁ', 'ǂ', 'ǃ', 'Ǆ', 'ǅ', 'ǆ', 'Ǉ', 'ǈ', 'ǉ', 'Ǌ', 'ǋ', 'ǌ', 'Ǥ', 'ǥ', 'Ǧ', 'ǧ', 'Ǩ', 'ǩ', 'Ǯ', 'ǯ', 'ǰ', 'Ǳ', 'ǲ', 'ǳ', 'Ǵ', 'ǵ', 'Ƕ', 'Ƿ', 'Ǹ', 'ǹ', 'Ȑ', 'ȑ', 'Ȓ', 'ȓ', 'Ș', 'ș', 'Ț', 'ț', 'Ȝ', 'ȝ', 'Ȟ', 'ȟ', 'Ƞ', 'ȡ', 'Ȥ', 'ȥ', 'Ȳ', 'ȳ', 'ȴ', 'ȵ', 'ȶ', 'ȸ', 'ȹ', 'Ȼ', 'ȼ', 'Ƚ', 'Ⱦ', 'ȿ', 'ɀ', 'Ɂ', 'ɂ', 'Ƀ', 'Ʌ', 'Ɉ', 'ɉ', 'Ɋ', 'ɋ', 'Ɍ', 'ɍ', 'Ɏ', 'ɏ']
    booleanConsonants = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1]
    allVowels = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u'] + ['Á', 'Â', 'Ã', 'Ä', 'Å', 'Æ', 'È', 'É', 'Ê', 'Ë', 'Ì', 'Í', 'Î', 'Ï', 'Ò', 'Ó', 'Ô', 'Õ', 'Ö', 'Ø', 'Ù', 'Ú', 'Û', 'Ü', 'à', 'á', 'â', 'ã', 'ä', 'å', 'æ', 'è', 'é', 'ê', 'ë', 'ì', 'í', 'î', 'ï', 'ò', 'ó', 'ô', 'õ', 'ö', 'ù', 'ú', 'û', 'ü', 'Ā', 'ā', 'Ă', 'ă', 'Ą', 'ą', 'Ē', 'ē', 'Ĕ', 'ĕ', 'Ė', 'ė', 'Ę', 'ę', 'Ě', 'ě', 'Ĩ', 'ĩ', 'Ī', 'ī', 'Ĭ', 'ĭ', 'Į', 'į', 'İ', 'ı', 'Ō', 'ō', 'Ŏ', 'ŏ', 'Ő', 'ő', 'Œ', 'œ', 'Ũ', 'ũ', 'Ū', 'ū', 'Ŭ', 'ŭ', 'Ů', 'ů', 'Ű', 'ű', 'Ų', 'ų', 'Ǝ', 'Ə', 'Ɛ', 'Ɩ', 'Ɨ', 'Ɵ', 'Ơ', 'ơ', 'Ư', 'ư', 'Ʊ', 'Ʋ', 'Ǎ', 'ǎ', 'Ǐ', 'ǐ', 'Ǒ', 'ǒ', 'Ǔ', 'ǔ', 'Ǖ', 'ǖ', 'Ǘ', 'ǘ', 'Ǚ', 'ǚ', 'Ǜ', 'ǜ', 'ǝ', 'Ǟ', 'ǟ', 'Ǡ', 'ǡ', 'Ǣ', 'ǣ', 'Ǫ', 'ǫ', 'Ǭ', 'ǭ', 'Ǻ', 'ǻ', 'Ǽ', 'ǽ', 'Ǿ', 'ǿ', 'Ȁ', 'ȁ', 'Ȃ', 'ȃ', 'Ȅ', 'ȅ', 'Ȇ', 'ȇ', 'Ȉ', 'ȉ', 'Ȋ', 'ȋ', 'Ȍ', 'ȍ', 'Ȏ', 'ȏ', 'Ȕ', 'ȕ', 'Ȗ', 'ȗ', 'Ȣ', 'ȣ', 'Ȧ', 'ȧ', 'Ȩ', 'ȩ', 'Ȫ', 'ȫ', 'Ȭ', 'ȭ', 'Ȯ', 'ȯ', 'Ȱ', 'ȱ', 'Ⱥ', 'Ʉ', 'Ɇ', 'ɇ']
    booleanVowels = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1]
    useConsonants = []
    useVowels = []
    secondChoices = {'t': ('D', 'd', 'z', '£'), 'y': ('u', 'U', '&', 'o'), 'k': ('c', 'K', 'h', '¬'), 'p': ('B', 'b', 'f', '%'), 'd': ('t', 'D', 'z', '£'), 'i': ('E', 'e', 'j', '`'), 'o': ('U', 'u', 'y', '&'), 'K': ('c', 'K', 'h', '¬'), 'c': ('K', 'k', 'h', '¬'), 'b': ('p', 'B', 'f', '%'), 'a': ('V', 'v', 'W', '$'), 'j': ('e', 'E', '`', 'i'), '&': ('y', 'u', 'U', 'o'), 'D': ('t', 'D', 'z', '£'), '`': ('j', 'e', 'E', 'i'), 'E': ('i', 'E', 'j', '`'), '£': ('z', 'd', 'D', 't'), 'e': ('i', 'E', 'j', '`'), 'V': ('a', 'V', 'W', '$'), 'z': ('d', 'D', '£', 't'), 'u': ('o', 'U', 'y', '&'), '%': ('f', 'b', 'B', 'p'), 'U': ('o', 'U', 'y', '&'), 'v': ('a', 'V', 'W', '$'), '¬': ('h', 'k', 'K', 'c'), 'f': ('b', 'B', '%', 'p'), '$': ('W', 'v', 'V', 'a'), 'h': ('k', 'K', '¬', 'c'), 'B': ('p', 'B', 'f', '%'), 'W': ('v', 'V', '$', 'a')}
    ys = ['Y','y']
    ws = ['W','w']
    filerConsonants = []
    filerVowels = []
    bla=['']
    roww=[]
    placeholder=[]
    setTester=0
    numColumn=0
    numRow=0
    originalText=''
    keyList=[]
    itemCall=False
    call=False
    call2=False
    classWord=''
    tableBuilt=0
    loopingBack=0
    windowOpen=0
    windowIgOpen=0
    transformText=''
    translateText=''
    ignores=1
    translatedWord=''
    wordRunning=""
    fileInvisibles=[]
    savedfilePath=""
    wordVecVec=[]
    vecWord=[]
    de=0

euTreeview = None
scrollbar = None
tableFrame = None
lesserFrame = None
spitButton = None
reloadButton = None


#/* Here's me converting the c++ stuff

class scan:
    n = 0
    nPlus = 1
    n2Plus = 2
    n3Plus = 3
    twoJoin4 = "AAAA"
    twoJoin3 = "AAA"
    twoJoin2 = "AA"
    oneOnly = "A"
    patternFrom = ""
    broke = ""

def advance(_steps):
    scan.n += _steps
    scan.nPlus += _steps
    scan.n2Plus += _steps
    scan.n3Plus += _steps

def doublecheckAdd(_twin, _noTwin):
    scan.twoJoin2 = scan.broke[scan.n] + scan.broke[scan.nPlus]

    if (scan.broke[scan.n] == scan.broke[scan.nPlus]):
#        phonemeLists.DictionaryKeys.push_back(_twin)
        phonemeLists.finalLegibleDictionary[_twin].append(scan.twoJoin2)
        scan.patternFrom = scan.patternFrom + _twin
    else:
#        phonemeLists.DictionaryKeys.push_back(_noTwin)
        phonemeLists.finalLegibleDictionary[_noTwin].append(scan.twoJoin2)
        scan.patternFrom = scan.patternFrom + _noTwin
    advance(2)

def fourAdd(_phon):
    scan.twoJoin4 = scan.broke[scan.n] + scan.broke[scan.nPlus] + scan.broke[scan.n2Plus] + scan.broke[scan.n3Plus]

#    phonemeLists.DictionaryKeys.push_back(_phon)
    phonemeLists.finalLegibleDictionary[_phon].append(scan.twoJoin4)
    scan.patternFrom = scan.patternFrom + _phon
    advance(4)

def threeAdd(_phon):
    scan.twoJoin3 = scan.broke[scan.n] + scan.broke[scan.nPlus] + scan.broke[scan.n2Plus]

#    phonemeLists.DictionaryKeys.push_back(_phon)
    phonemeLists.finalLegibleDictionary[_phon].append(scan.twoJoin3)
    scan.patternFrom = scan.patternFrom + _phon
    advance(3)

def oneAdd(_phon):
    scan.oneOnly = scan.broke[scan.n]
#    phonemeLists.DictionaryKeys.push_back(_phon)
    phonemeLists.finalLegibleDictionary[_phon].append(scan.oneOnly)
    scan.patternFrom = scan.patternFrom + _phon
    advance(1)

def inCheckConsonant (_wordChar):
    if otherVariables.booleanConsonants[ord(_wordChar)] is 1:
        return True
    return False

def inCheckVowel (_wordChar):

    if otherVariables.booleanVowels[ord(_wordChar)] is 1:
        return True
    return False

def spitReplace():
    pattern = re.compile("|".join([re.escape(k) for k in phonemeLists.replacer.keys()]), re.M)
    otherVariables.classWord = pattern.sub(lambda x: phonemeLists.replacer[x.group(0)], otherVariables.classWord)
    
def reorderKeys():
    remake = {}
    for each in phonemeLists.finalLegibleDictionary:
        if len(phonemeLists.finalLegibleDictionary[each]) > 0:
            remake[each] = phonemeLists.finalLegibleDictionary[each]
    phonemeLists.finalLegibleDictionary = remake
#cleanup
    tempdict=OrderedDict([])
    for key in ['Pattern']:
        if key in phonemeLists.finalLegibleDictionary:
            tempdict[key]= phonemeLists.finalLegibleDictionary[key]
        else:
            pass
    for key in ['t', 'd', 'z', 'D', 'a', 'v', 'w', 'V', 'c', 'k', 'h', 'K', 'i', 'e', 'j', 'E', 'p', 'b', 'f', 'B', 'o', 'u', 'y', 'U']:
        if key in phonemeLists.finalLegibleDictionary:
            tempdict[key]= phonemeLists.finalLegibleDictionary[key]
        else:
            pass
    for key in phonemeLists.finalLegibleDictionary:
        if key not in ['Pattern', 't', 'd', 'z', 'D', 'a', 'v', 'w', 'V', 'c', 'k', 'h', 'K', 'i', 'e', 'j', 'E', 'p', 'b', 'f', 'B', 'o', 'u', 'y', 'U', 'Banned', 'Transform from', 'Transform to']:
            tempdict[key]= phonemeLists.finalLegibleDictionary[key]
        else:
            pass
    for key in ['Banned', 'Transform from', 'Transform to', 'Invisibles']:
        if key in phonemeLists.finalLegibleDictionary:
            tempdict[key]= phonemeLists.finalLegibleDictionary[key]
        else:
            pass
    for key in phonemeLists.finalLegibleDictionary:
        phonemeLists.finalLegibleDictionary[key].sort()
    phonemeLists.finalLegibleDictionary=tempdict

        
#if there is an issue w/ a key not being in this list, those need to be in between the special sections at beginning and end.

def fileResultReader():
    try:
        if len(phonemeLists.finalLegibleDictionary['Pattern'])<1:
            phonemeLists.finalLegibleDictionary=OrderedDict([])
            messagebox.showwarning("Data Failure", "Could not generate usable data. Are all the words in the source text being ignored as too short?")
            return
    except:
        phonemeLists.finalLegibleDictionary=OrderedDict([])
        messagebox.showwarning("Data Failure", "Could not generate usable data. Are all the words in the source text being ignored as too short?")
        return
    reorderKeys()
    buildTable()
##

def analyst():
    bwords=phonemeLists.words
    phonemeLists.finalLegibleDictionary = { '£' : [], 'z': [], 'D': [], 'd': [], 't': [], '$': [], 'w': [], 'V': [], 'v': [], 'a': [], 'p': [], 'o': [], 'b': [], 'B': [], 'c': [], 'i': [], 'f': [], 'K': [], 'k': [], 'y': [], 'E': [], 'e': [], '%': [], 'h': [], '&': [], 'j': [], '¬': [], '`': [], 'U': [], 'u' : [], 'Pattern' : [], 'Banned' : []}
    for word in phonemeLists.words:
        if len(word)<otherVariables.ignores:
            pass
        else:
            scan.broke = word
            #not broke but w/e.  Alternative to iterating over a changing vector is to read those chunks and change only the new vectors, which makes more sense, no?>  Actually would have to make more changes to index and stuff
            scan.n = 0
            scan.nPlus = 1
            scan.n2Plus = 2
            scan.n3Plus = 3
            scan.patternFrom = ""
            theEnd = len(scan.broke)-1
            while scan.n<=theEnd:
                if scan.n == 0:
                    if 4 <= theEnd:
                        if inCheckConsonant(scan.broke[scan.n]):        
                                if inCheckConsonant(scan.broke[scan.nPlus]):
                                    if inCheckConsonant(scan.broke[scan.n2Plus]):
                                        if inCheckConsonant(scan.broke[scan.n3Plus]):
                                            fourAdd('£')
                                        else:
                                            threeAdd('z')
                                    else:
                                        doublecheckAdd('D','d')
                                else:
                                    oneAdd('t')
                        elif inCheckVowel(scan.broke[scan.n]):
                                if inCheckVowel(scan.broke[scan.nPlus]):
                                    if inCheckVowel(scan.broke[scan.n2Plus]):
                                        if inCheckVowel(scan.broke[scan.n3Plus]):
                                            fourAdd('$')
                                        else:
                                            threeAdd('w')
                                    else:
                                        doublecheckAdd('V','v')
                                else:
                                    oneAdd('a')
                        else:
                            advance(1)
                    elif 3 <= theEnd:
                        if inCheckConsonant(scan.broke[scan.n]):
                                if inCheckConsonant(scan.broke[scan.nPlus]):
                                    if inCheckConsonant(scan.broke[scan.n2Plus]):
                                        threeAdd('z')
                                    else:
                                        doublecheckAdd('D','d')
                                else:
                                    oneAdd('t')
                        elif inCheckVowel(scan.broke[scan.n]):
                                if inCheckVowel(scan.broke[scan.nPlus]):
                                    if inCheckVowel(scan.broke[scan.n2Plus]):
                                        threeAdd('w')
                                    else:
                                        doublecheckAdd('V','v')
                                else:
                                    oneAdd('a')
                        else:
                            advance(1)
                    elif 2 <= theEnd:
                        if inCheckConsonant(scan.broke[scan.n]):
                                if inCheckConsonant(scan.broke[scan.nPlus]):
                                    doublecheckAdd('D','d')
                                else:
                                    oneAdd('t')
                        elif inCheckVowel(scan.broke[scan.n]):
                                if inCheckVowel(scan.broke[scan.nPlus]):
                                    doublecheckAdd('V','v')
                                else:
                                    oneAdd('a')
                        else:
                            advance(1)
                    else:
                        if inCheckConsonant(scan.broke[scan.n]):
                                oneAdd('t')
                        elif inCheckVowel(scan.broke[scan.n]):
                                oneAdd('a')
                        else:
                            advance(1)
                elif scan.n == theEnd:
                    if inCheckConsonant(scan.broke[scan.n]):
                            oneAdd('p')
                    elif inCheckVowel(scan.broke[scan.n]):
                            oneAdd('o')
                    else:
                        advance(1)
                elif scan.nPlus == theEnd:
                    if inCheckConsonant(scan.broke[scan.n]):
                            if inCheckConsonant(scan.broke[scan.nPlus]):
                                doublecheckAdd('B','b')
                            else:
                                oneAdd('c')
                    elif inCheckVowel(scan.broke[scan.n]):
                            if inCheckVowel(scan.broke[scan.nPlus]):
                                doublecheckAdd('U','u')
                            else:
                                oneAdd('i') 
                    else:
                        advance(1)
                elif scan.n2Plus == theEnd:
                    if inCheckConsonant(scan.broke[scan.n]):
                            if inCheckConsonant(scan.broke[scan.nPlus]):
                                if inCheckConsonant(scan.broke[scan.n2Plus]):
                                    threeAdd('f')
                                else:
                                    doublecheckAdd('K','k')
                            else:
                                oneAdd('c')
                    elif inCheckVowel(scan.broke[scan.n]):
                            if inCheckVowel(scan.broke[scan.nPlus]):
                                if inCheckVowel(scan.broke[scan.n2Plus]):
                                    threeAdd('y')
                                else:
                                    doublecheckAdd('E','e')
                            else:
                                oneAdd('i')  
                    else:
                        advance(1)
                elif scan.n3Plus == theEnd:
                    if inCheckConsonant(scan.broke[scan.n]):
                            if inCheckConsonant(scan.broke[scan.nPlus]):
                                if inCheckConsonant(scan.broke[scan.n2Plus]):
                                    if inCheckConsonant(scan.broke[scan.n3Plus]):
                                        fourAdd('%')
                                    else:
                                        threeAdd('h')
                                else:
                                    doublecheckAdd('K','k')
                            else:
                                oneAdd('c')
                    elif inCheckVowel(scan.broke[scan.n]):
                            if inCheckVowel(scan.broke[scan.nPlus]):
                                if inCheckVowel(scan.broke[scan.n2Plus]):
                                    if inCheckVowel(scan.broke[scan.n3Plus]):
                                        fourAdd('&')
                                    else:
                                        threeAdd('j')
                                else:
                                    doublecheckAdd('E','e')
                            else:
                                oneAdd('i')
                    else:
                        advance(1)
                else:
                        if inCheckConsonant(scan.broke[scan.n]):
                                if inCheckConsonant(scan.broke[scan.nPlus]):
                                    if inCheckConsonant(scan.broke[scan.n2Plus]):
                                        if inCheckConsonant(scan.broke[scan.n3Plus]):
                                            fourAdd('¬')
                                        else:
                                            threeAdd('h')
                                    else:
                                        doublecheckAdd('K','k')
                                else:
                                    oneAdd('c')
                        elif inCheckVowel(scan.broke[scan.n]):
                                if inCheckVowel(scan.broke[scan.nPlus]):
                                    if inCheckVowel(scan.broke[scan.n2Plus]):
                                        if inCheckVowel(scan.broke[scan.n3Plus]):
                                            fourAdd('`')
                                        else:
                                            threeAdd('j')
                                    else:
                                        doublecheckAdd('E','e')
                                else:
                                    oneAdd('i')
                        else:
                            advance(1)
            phonemeLists.finalLegibleDictionary["Pattern"].append("<" + scan.patternFrom + ">")
#        print(phonemeLists.finalLegibleDictionary)
#        return


def doublecheckAdd2(_twin, _noTwin):
    scan.twoJoin2 = scan.broke[scan.n] + scan.broke[scan.nPlus]

    if (scan.broke[scan.n] == scan.broke[scan.nPlus]):
#        phonemeLists.finalLegibleDictionary[_twin].append(scan.twoJoin2)
        scan.patternFrom = scan.patternFrom + _twin
    else:
#        phonemeLists.finalLegibleDictionary[_noTwin].append(scan.twoJoin2)
        scan.patternFrom = scan.patternFrom + _noTwin

    otherVariables.vecWord.append(scan.twoJoin2)
    advance(2)

def fourAdd2(_phon):
    scan.twoJoin4 = scan.broke[scan.n] + scan.broke[scan.nPlus] + scan.broke[scan.n2Plus] + scan.broke[scan.n3Plus]

#    phonemeLists.finalLegibleDictionary[_phon].append(scan.twoJoin4)
    scan.patternFrom = scan.patternFrom + _phon

    otherVariables.vecWord.append(scan.twoJoin4)
    advance(4)

def threeAdd2(_phon):
    scan.twoJoin3 = scan.broke[scan.n] + scan.broke[scan.nPlus] + scan.broke[scan.n2Plus]

#    phonemeLists.finalLegibleDictionary[_phon].append(scan.twoJoin3)
    scan.patternFrom = scan.patternFrom + _phon
    otherVariables.vecWord.append(scan.twoJoin3)
    advance(3)

def oneAdd2(_phon):
    scan.oneOnly = scan.broke[scan.n]

#    phonemeLists.finalLegibleDictionary[_phon].append(scan.oneOnly)
    scan.patternFrom = scan.patternFrom + _phon
    otherVariables.vecWord.append(scan.oneOnly)
    advance(1)

def analyst2():
    #otherVariables.wordVecVec
    #vecWord
    bwords=phonemeLists.words
    #wordsXPatterns
    phonemeLists.wordsXPatterns=[]
    phonemeLists.finalLegibleDictionary = { '£' : [], 'z': [], 'D': [], 'd': [], 't': [], '$': [], 'w': [], 'V': [], 'v': [], 'a': [], 'p': [], 'o': [], 'b': [], 'B': [], 'c': [], 'i': [], 'f': [], 'K': [], 'k': [], 'y': [], 'E': [], 'e': [], '%': [], 'h': [], '&': [], 'j': [], '¬': [], '`': [], 'U': [], 'u' : [], 'Pattern' : [], 'Banned' : []}
    #patternFrom corresponding to each vecWord?
    otherVariables.vecWord = []
    for word in phonemeLists.words:
        if len(word)<otherVariables.ignores:
            pass
        else:
            scan.broke = word
            #not broke but w/e.  Alternative to iterating over a changing vector is to read those chunks and change only the new vectors, which makes more sense, no?>  Actually would have to make more changes to index and stuff
            scan.n = 0
            scan.nPlus = 1
            scan.n2Plus = 2
            scan.n3Plus = 3
            scan.patternFrom = ""
            theEnd = len(scan.broke)-1
            while scan.n<=theEnd:
                if scan.n == 0:
                    if 4 <= theEnd:
                        if inCheckConsonant(scan.broke[scan.n]):        
                                if inCheckConsonant(scan.broke[scan.nPlus]):
                                    if inCheckConsonant(scan.broke[scan.n2Plus]):
                                        if inCheckConsonant(scan.broke[scan.n3Plus]):
                                            fourAdd2('£')
                                        else:
                                            threeAdd2('z')
                                    else:
                                        doublecheckAdd2('D','d')
                                else:
                                    oneAdd2('t')
                        elif inCheckVowel(scan.broke[scan.n]):
                                if inCheckVowel(scan.broke[scan.nPlus]):
                                    if inCheckVowel(scan.broke[scan.n2Plus]):
                                        if inCheckVowel(scan.broke[scan.n3Plus]):
                                            fourAdd2('$')
                                        else:
                                            threeAdd2('w')
                                    else:
                                        doublecheckAdd2('V','v')
                                else:
                                    oneAdd2('a')
                        else:
                            advance(1)
                    elif 3 <= theEnd:
                        if inCheckConsonant(scan.broke[scan.n]):
                                if inCheckConsonant(scan.broke[scan.nPlus]):
                                    if inCheckConsonant(scan.broke[scan.n2Plus]):
                                        threeAdd2('z')
                                    else:
                                        doublecheckAdd2('D','d')
                                else:
                                    oneAdd2('t')
                        elif inCheckVowel(scan.broke[scan.n]):
                                if inCheckVowel(scan.broke[scan.nPlus]):
                                    if inCheckVowel(scan.broke[scan.n2Plus]):
                                        threeAdd2('w')
                                    else:
                                        doublecheckAdd2('V','v')
                                else:
                                    oneAdd2('a')
                        else:
                            advance(1)
                    elif 2 <= theEnd:
                        if inCheckConsonant(scan.broke[scan.n]):
                                if inCheckConsonant(scan.broke[scan.nPlus]):
                                    doublecheckAdd2('D','d')
                                else:
                                    oneAdd2('t')
                        elif inCheckVowel(scan.broke[scan.n]):
                                if inCheckVowel(scan.broke[scan.nPlus]):
                                    doublecheckAdd2('V','v')
                                else:
                                    oneAdd2('a')
                        else:
                            advance(1)
                    else:
                        if inCheckConsonant(scan.broke[scan.n]):
                                oneAdd2('t')
                        elif inCheckVowel(scan.broke[scan.n]):
                                oneAdd2('a')
                        else:
                            advance(1)
                elif scan.n == theEnd:
                    if inCheckConsonant(scan.broke[scan.n]):
                            oneAdd2('p')
                    elif inCheckVowel(scan.broke[scan.n]):
                            oneAdd2('o')
                    else:
                        advance(1)
                elif scan.nPlus == theEnd:
                    if inCheckConsonant(scan.broke[scan.n]):
                            if inCheckConsonant(scan.broke[scan.nPlus]):
                                doublecheckAdd2('B','b')
                            else:
                                oneAdd2('c')
                    elif inCheckVowel(scan.broke[scan.n]):
                            if inCheckVowel(scan.broke[scan.nPlus]):
                                doublecheckAdd2('U','u')
                            else:
                                oneAdd2('i') 
                    else:
                        advance(1)
                elif scan.n2Plus == theEnd:
                    if inCheckConsonant(scan.broke[scan.n]):
                            if inCheckConsonant(scan.broke[scan.nPlus]):
                                if inCheckConsonant(scan.broke[scan.n2Plus]):
                                    threeAdd2('f')
                                else:
                                    doublecheckAdd2('K','k')
                            else:
                                oneAdd2('c')
                    elif inCheckVowel(scan.broke[scan.n]):
                            if inCheckVowel(scan.broke[scan.nPlus]):
                                if inCheckVowel(scan.broke[scan.n2Plus]):
                                    threeAdd2('y')
                                else:
                                    doublecheckAdd2('E','e')
                            else:
                                oneAdd2('i')  
                    else:
                        advance(1)
                elif scan.n3Plus == theEnd:
                    if inCheckConsonant(scan.broke[scan.n]):
                            if inCheckConsonant(scan.broke[scan.nPlus]):
                                if inCheckConsonant(scan.broke[scan.n2Plus]):
                                    if inCheckConsonant(scan.broke[scan.n3Plus]):
                                        fourAdd2('%')
                                    else:
                                        threeAdd2('h')
                                else:
                                    doublecheckAdd2('K','k')
                            else:
                                oneAdd2('c')
                    elif inCheckVowel(scan.broke[scan.n]):
                            if inCheckVowel(scan.broke[scan.nPlus]):
                                if inCheckVowel(scan.broke[scan.n2Plus]):
                                    if inCheckVowel(scan.broke[scan.n3Plus]):
                                        fourAdd2('&')
                                    else:
                                        threeAdd2('j')
                                else:
                                    doublecheckAdd2('E','e')
                            else:
                                oneAdd2('i')
                    else:
                        advance(1)
                else:
                        if inCheckConsonant(scan.broke[scan.n]):
                                if inCheckConsonant(scan.broke[scan.nPlus]):
                                    if inCheckConsonant(scan.broke[scan.n2Plus]):
                                        if inCheckConsonant(scan.broke[scan.n3Plus]):
                                            fourAdd2('¬')
                                        else:
                                            threeAdd2('h')
                                    else:
                                        doublecheckAdd2('K','k')
                                else:
                                    oneAdd2('c')
                        elif inCheckVowel(scan.broke[scan.n]):
                                if inCheckVowel(scan.broke[scan.nPlus]):
                                    if inCheckVowel(scan.broke[scan.n2Plus]):
                                        if inCheckVowel(scan.broke[scan.n3Plus]):
                                            fourAdd2('`')
                                        else:
                                            threeAdd2('j')
                                    else:
                                        doublecheckAdd2('E','e')
                                else:
                                    oneAdd2('i')
                        else:
                            advance(1)
            otherVariables.wordVecVec.append(otherVariables.vecWord)
            phonemeLists.wordsXPatterns.append((otherVariables.vecWord, patternFrom))
#            phonemeLists.finalLegibleDictionary["Pattern"].append("<" + scan.patternFrom + ">")
#        return

def csvFiler():
    otherVariables.fileInvisibles=[]
    filePath = pathBoxtext.get()
#    csvFilerdelimiter=";"
#    if checkdig is False:
#        pass
    try:
        with open(filePath) as csvfile:
            reading = csv.reader(csvfile, delimiter=";")
            columns = zip_longest(*reading)
            columns_list = []
##
            for n in columns:
                ind = len(n) - 1
                nlist = list(n)
                filout = filter(None, nlist)
                filist = list(filout)
                phonemeLists.finalLegibleDictionary[nlist[0]] = filist[1:ind]
            if len(phonemeLists.finalLegibleDictionary['Pattern'])<1:
                phonemeLists.finalLegibleDictionary=OrderedDict([])
                messagebox.showwarning("No patterns found", "The Pattern section of this CSV is empty.")
                euTreeview.destroy()
                scrollbar.destroy()
                tableFrame.destroy()
                lesserFrame.destroy()
                pathBoxtext.set("")
                reloadButton.config(state=DISABLED)
                spitButton.config(state=DISABLED)
                otherVariables.savedfilePath=""
                euWindow.title('Euphony')
                #dialogue
                return
    except:
        messagebox.showwarning("Could not load", "Could not load this CSV.")
        euTreeview.destroy()
        scrollbar.destroy()
        tableFrame.destroy()
        lesserFrame.destroy()
        pathBoxtext.set("")
        reloadButton.config(state=DISABLED)
        spitButton.config(state=DISABLED)
        otherVariables.savedfilePath=""
        euWindow.title('Euphony')
        return
    otherVariables.savedfilePath=filePath
    if 'Transform from' and 'Transform to' in phonemeLists.finalLegibleDictionary.keys():
        phonemeLists.replacer=dict(zip(phonemeLists.finalLegibleDictionary['Transform from'], phonemeLists.finalLegibleDictionary['Transform to']))
    else:
#        print('Not there')
        phonemeLists.replacer={}
##    print('\n')
##    print(phonemeLists.finalLegibleDictionary)
##    print('Replacer', phonemeLists.replacer)
##    print("Loaded CSV")
    if 'Invisibles' in phonemeLists.finalLegibleDictionary.keys():
        otherVariables.fileInvisibles=phonemeLists.finalLegibleDictionary['Invisibles']
    reorderKeys()
    buildTable()
    spitButton.config(state=NORMAL)
    reloadButton.config(state=NORMAL)
    return
#

def setVowelConsonant():
    if yVowel.get() is 1:
        #ord(_wordChar)
        otherVariables.booleanVowels[89] = 1
        otherVariables.booleanVowels[121] = 1
        otherVariables.booleanConsonants[89] = 0
        otherVariables.booleanConsonants[121] = 0
        otherVariables.filerVowels.extend(otherVariables.ys)
    ## not working properly currently
    else:
        otherVariables.booleanVowels[89] = 0
        otherVariables.booleanVowels[121] = 0
        otherVariables.booleanConsonants[89] = 1
        otherVariables.booleanConsonants[121] = 1
        otherVariables.filerConsonants.extend(otherVariables.ys)
    if wVowel.get() is 1:
        otherVariables.booleanVowels[87] = 1
        otherVariables.booleanVowels[119] = 1
        otherVariables.booleanConsonants[87] = 0
        otherVariables.booleanConsonants[119] = 0
        otherVariables.filerVowels.extend(otherVariables.ws)
    else:
        otherVariables.booleanVowels[87] = 0
        otherVariables.booleanVowels[119] = 0
        otherVariables.booleanConsonants[87] = 1
        otherVariables.booleanConsonants[119] = 1
        otherVariables.filerConsonants.extend(otherVariables.ws)
    return

def textfiler():
    otherVariables.fileInvisibles=[]
    filePath = pathBoxtext.get()
    if len(filePath) < 4:
        return
    try:
        c=open(filePath, "r", encoding='utf-8')
        d=c.read()
    except:
        stringPut="Cannot open this file:\n" + filePath + "\nIs this a working UTF-8 text file?"
        messagebox.showwarning("Cannot open file", stringPut)
        spitButton.config(state=DISABLED)
        euTreeview.destroy()
        scrollbar.destroy()
        tableFrame.destroy()
        lesserFrame.destroy()
        pathBoxtext.set("")
        reloadButton.config(state=DISABLED)
        spitButton.config(state=DISABLED)
        otherVariables.savedfilePath=""
        return
    otherVariables.savedfilePath=filePath
    
    otherVariables.filerConsonants = []
    otherVariables.filerVowels = []
    otherVariables.useConsonants = otherVariables.allConsonants
    otherVariables.useVowels = otherVariables.allVowels

    setVowelConsonant()
    

    if aPostCon.get() is 1:
        otherVariables.booleanConsonants[39] = 1

    elif aPostCon.get() is 0:
        d=d.replace("’","")
        d=d.replace("'","")
        otherVariables.booleanConsonants[39] = 0
        
    for bo in d:      
        if bo in otherVariables.allConsonants and bo not in otherVariables.filerConsonants and bo not in otherVariables.filerVowels:
            otherVariables.filerConsonants.append(bo)
        elif bo in otherVariables.allVowels and bo not in otherVariables.filerVowels and bo not in otherVariables.filerConsonants:
            otherVariables.filerVowels.append(bo)
    for n in d:
        if n in otherVariables.filerVowels:
            pass
        elif n in otherVariables.filerConsonants:
            pass
        else:
            d=d.replace(n, " ")
                
    phonemeLists.words=d.split()
    iterWord()
    analyst()
    fileResultReader()
    spitButton.config(state=NORMAL)
    reloadButton.config(state=NORMAL)
    return


def boxFiler():
    phonemeLists.finalLegibleDictionary=OrderedDict()
    otherVariables.d = printBox.get('1.0', END+'-1c')
    readerFiler()
    return

def readerFiler():
    otherVariables.fileInvisibles=[]
    otherVariables.filerConsonants = []
    otherVariables.filerVowels = []
    otherVariables.useConsonants = otherVariables.allConsonants
    otherVariables.useVowels = otherVariables.allVowels

    setVowelConsonant()
    if aPostCon.get() is 1:
        otherVariables.booleanConsonants[39] = 1
        otherVariables.filerConsonants.append("'")
    elif aPostCon.get() is 0:
        otherVariables.d=otherVariables.d.replace("’","")
        otherVariables.d=otherVariables.d.replace("'","")
        otherVariables.booleanConsonants[39] = 0
#        ["’", "'"]
#allConsonants not working right yet
        #this is joining together every apostrophe'd word
        #so odd behaviour after.  need different settings for cipher reader to get identical words.  These don't need to worry about apostrophes polluting the language data (as the .words won't be used for that _phonological stuff) but length is an issue.
    for bo in otherVariables.d:
        if bo in otherVariables.allConsonants and bo not in otherVariables.filerConsonants and bo not in otherVariables.filerVowels:
            otherVariables.filerConsonants.append(bo)
        elif bo in otherVariables.allVowels and bo not in otherVariables.filerVowels and bo not in otherVariables.filerConsonants:
            otherVariables.filerVowels.append(bo)
    for n in otherVariables.d:
        if n in otherVariables.filerVowels:
            pass
        elif n in otherVariables.filerConsonants:
            pass
        else:
            otherVariables.d=otherVariables.d.replace(n, " ")
        #so atm it's just replacing anything outside those two with a space
        #need a new reader fun for genning texttocipher and .words  --> individual.
                
    phonemeLists.words=otherVariables.d.split()
    for x in phonemeLists.words:
        print(x)
    iterWord()
    fileResultReader()
    global spitButton
    global reloadButton
    spitButton.config(state=NORMAL)
    reloadButton.config(state=NORMAL)
    return

def iterWord():
    phonemeLists.patterns=[]
    phonemeLists.banned=[]
    phonemeLists.stringpatlist=[]
    analyst()

def numbered():
    numberedDict = OrderedDict([])
    for ke in phonemeLists.finalLegibleDictionary:    
#        print("Iterating for " + ke)
        numberedDict[ke] = []
        lE = len(phonemeLists.finalLegibleDictionary[ke])
        li = phonemeLists.finalLegibleDictionary[ke]

        emptyDict = OrderedDict([])
        #these loops repeat for each final key.
        for x in li:
            if x not in emptyDict.keys():
                emptyDict[x] = 0
        for x in emptyDict:
            for y in li:
                if y == x:
                    emptyDict[x] = emptyDict[x] + 1
        #emptyDict= OrderedDict(sorted(emptyDict.items(), key=lambda t: t[0]))
        
        for b in emptyDict.items():
            a = b[0]
            s = b[0]+ " (" + str(b[1]) +")"
            numberedDict[ke].append(s)


    #print(numberedDict)
    #phonemeLists.finalLegibleDictionary = numberedDict
    #buildTable()
    return

def spitterSetup():
#    print(phonemeLists.finalLegibleDictionary)
    try:
        if 'Pattern' not in phonemeLists.finalLegibleDictionary.keys():
            return
    #    print('\n')
        if otherVariables.loopingBack is 0:
            howManyFirst = int(numBoxtext.get())
            howMany = ''
        #shd record reduction of no of words gen.
            if howManyFirst>1000:
                howMany = 1000
                numBoxtext.set('1000')
            else:
                howMany = howManyFirst
        #    howMany = howManyFirst
        #    checkdig = howMany.isdigit()
            otherVariables.integerCountdown = int(howMany)
        else:
            pass
    except:
        return
    spitter2()

def spitter2():
    invisibles = otherVariables.invisibles+['<','>','∅','|']+otherVariables.fileInvisibles
    if 'Banned' in phonemeLists.finalLegibleDictionary:
        banList = phonemeLists.finalLegibleDictionary['Banned']
    else:
        banListCheck.set(0)
    while otherVariables.integerCountdown > 0:
##
        wordshape = choice(phonemeLists.finalLegibleDictionary['Pattern'])
        broken = list(wordshape)
        listWord = []
#don't wanna set this again the command on the button should set invis
#*+get* from box
        for eac in broken:
            if eac not in phonemeLists.finalLegibleDictionary:
                listWord.append(eac)
            elif eac in invisibles or len(phonemeLists.finalLegibleDictionary[eac]) is 0:
                listWord.append(eac)
            else:
                rands = choice(phonemeLists.finalLegibleDictionary[eac])
                if '#RHYME' in rands:
#and usingrhymes is 1
                    rhymeDig=rands.lstrip('#RHYME')
                    if rhymeDig.isdigit:
                        rhymeInt=int(rhymeDig)-1
                        if rhymeInt<=len(listWord) and rhymeInt>0:
                            listWord.append(listWord[rhymeInt])
                elif '#BLANK' in rands:
#and usingrhymes is 1
                    pass
                else:
                    listWord.append(rands)
        otherVariables.classWord = ''.join(listWord)
    ########
        endChar = endCheck.get()
        showPattern = patternCheck.get()
        useBan = banListCheck.get()
        unt = showUnt.get()
        untWord=""
        listUnt=[]
#        word=''
    #        print('Before altered: ', word)
        if 'Transform from' and 'Transform to' in phonemeLists.finalLegibleDictionary:
            if len(phonemeLists.finalLegibleDictionary['Transform from'])>0:
                untWord=otherVariables.classWord
                listUnt=list(otherVariables.classWord)
                spitReplace()
                listWord=list(otherVariables.classWord)
                word=otherVariables.classWord
        else:
            word=otherVariables.classWord
            pass
        #
        if useBan is 1:
            for n in banList:
#                print("Iterating:", 'is', n, 'in word', word+'?')
                if n in word:
#                    print('Word generated was illegal,', n, 'in', word, 'found\n')
                    otherVariables.loopingBack = 1
                    spitter2()
                    return
            else:
                listWord[:] = (value for value in listWord if value not in invisibles)
                freshWord = ''.join(listWord)
                caseWord=freshWord
#
                if unt is 1 and len(listUnt)>0:
                    listUnt[:] = (value for value in listUnt if value not in invisibles)
                    untWord=''.join(listUnt)
    ##                if untWord is not caseWord:
    ##                    printBox.insert(INSERT, '['+untWord+'] = ')
                    printBox.insert(INSERT, '['+untWord+'] = ')
                    
                if wCapitalise.get() is 1:
                    caseWord = freshWord.capitalize()
                
                if showPattern is 1:
                    printBox.insert(INSERT, '['+wordshape+' : '+caseWord+']')
        #
                    if endChar is 1:
                        printBox.insert(INSERT, '\n')
                    elif endChar is 0:
                        printBox.insert(INSERT, ' ')
                    
        #
                elif showPattern is 0:
                    printBox.insert(INSERT, caseWord)
        #
                    if endChar is 1:
                        printBox.insert(INSERT, '\n')
                    elif endChar is 0:
                        printBox.insert(INSERT, ' ')
        #
                otherVariables.integerCountdown = otherVariables.integerCountdown - 1
        elif useBan is 0:
            listWord[:] = (value for value in listWord if value not in invisibles)
            freshWord = ''.join(listWord)
            caseWord=freshWord

            if unt is 1 and len(listUnt)>0:
                listUnt[:] = (value for value in listUnt if value not in invisibles)
                untWord=''.join(listUnt)
##                if untWord is not caseWord:
##                    printBox.insert(INSERT, '['+untWord+'] = ')
                printBox.insert(INSERT, '['+untWord+'] = ')
    
            if wCapitalise.get() is 1:
                caseWord = freshWord.capitalize()

            if showPattern is 1:
                printBox.insert(INSERT, '['+wordshape+' : '+caseWord+']')
        #                        
                if endChar is 1:
                    printBox.insert(INSERT, '\n')
                elif endChar is 0:
                    printBox.insert(INSERT, ' ')
        #
            elif showPattern is 0:
                printBox.insert(INSERT, caseWord)
        #                        
                if endChar is 1:
                    printBox.insert(INSERT, '\n')
                elif endChar is 0:
                    printBox.insert(INSERT, ' ')
            otherVariables.integerCountdown = otherVariables.integerCountdown - 1
        #
        printBox.yview(END)
    else:
        otherVariables.loopingBack = 0
        return
        #
#    print(phonemeLists.words)
    return

def fromTextSaver():
#    print('\n')
#    print('Begin')
    if 'Pattern' in phonemeLists.finalLegibleDictionary:
        otherVariables.saveName = asksaveasfilename(defaultextension = '.csv', filetypes = [('Comma Separated Values', '.csv')])
        try:
            with open(otherVariables.saveName, 'w', newline='') as f:
                writer = csv.writer(f, delimiter=';')
        #        longestLength = len(phonemeLists.finalLegibleDictionary['Pattern'])
                longestLength = 0
#                print('ll:', longestLength)
                for keyList in phonemeLists.finalLegibleDictionary:
#                    print("iterated")
                    if len(keyList)>longestLength:
                        longestLength = len(phonemeLists.finalLegibleDictionary.get(keyList))
        #                print(longestLength)
#                print(longestLength," final")
                rngThing=list(range(longestLength-1))
        #minus 1 for end
#                print(rngThing)
                rowList=[]
        ######################
                testJoin=[]
                keyList=[]
                for allKeys in phonemeLists.finalLegibleDictionary:
                    keyList.append(str(allKeys))
                writer.writerow(keyList)
                for each1 in rngThing:
                    for allKeys in phonemeLists.finalLegibleDictionary:
        #                print('allKeys:', allKeys)
        #                print('each1:', each1)
                        listFrom=phonemeLists.finalLegibleDictionary[allKeys]
                        if len(listFrom)>each1:
                            listitem=listFrom[each1]
        #                    print('Listitem:', listitem)
                            rowList.append(listitem)
                        else:
                            rowList.append("")
#                    print("Length of rowList: ", len(rowList))
#                    print(rowList)
                    writer.writerow(rowList)
        #            testJoin.append(rowList)
                    rowList=[]
        #        print(testJoin)
        #        print(rowList)
        #        writer.writerows(rowList)
        #        writer.writerows(testJoin)
#                print('each1:')
        except:
            return
    else:
        pass
#    print('End')
    return

###This happens when you click
def boxxFile():
    original=pathBoxtext.get()
#   euWindow.config(cursor="wait")
    menuResult = askopenfilename(defaultextension = '.txt', filetypes = [('Comma Separated Values', '.csv'), ('UTF-8 Text File to Iterate Over', '.txt')])
    pathBoxtext.set(menuResult)
    if menuResult.endswith('.txt'):
        phonemeLists.finalLegibleDictionary=OrderedDict()
        otherVariables.filetitle = menuResult+' - Euphony'
        euWindow.title(otherVariables.filetitle)
        textfiler()
    elif menuResult.endswith('.csv'):
        phonemeLists.finalLegibleDictionary=OrderedDict()
        otherVariables.filetitle = menuResult+' - Euphony'
        euWindow.title(otherVariables.filetitle)
        csvFiler()
    else:
#        otherVariables.filetitle = original+' - Euphony'
        pathBoxtext.set(original)
#        euWindow.title(otherVariables.filetitle)
        euWindow.title('Euphony')
    return

def reloadFile():
#   euWindow.config(cursor="wait")
    menuResult = otherVariables.savedfilePath
    phonemeLists.finalLegibleDictionary=OrderedDict()
    if menuResult.endswith('.txt'):
        otherVariables.filetitle = menuResult+' - Euphony'
        euWindow.title(otherVariables.filetitle)
        textfiler()
    elif menuResult.endswith('.csv'):
        otherVariables.filetitle = menuResult+' - Euphony'
        euWindow.title(otherVariables.filetitle)
        csvFiler()
    else:
        euWindow.title('Euphony')
    return

##def boxxFile_preset():
##    phonemeLists.finalLegibleDictionary=OrderedDict()
##    menuResult=pathBoxtext.get()
##    if menuResult.endswith('.txt'):
##        otherVariables.filetitle = menuResult+' - Euphony'
##        euWindow.title(otherVariables.filetitle)
##        textfiler()
##    elif menuResult.endswith('.csv'):
##        otherVariables.filetitle = menuResult+' - Euphony'
##        euWindow.title(otherVariables.filetitle)
##        csvFiler()
##    else:
##        euWindow.title('Euphony')
##    return

def boxxFileSetupForC():
    menuResult = askopenfilename(defaultextension = '.txt', filetypes = [('Comma Separated Values', '.csv'), ('UTF-8 Text File to Iterate Over', '.txt')])
    pathBoxtext.set(menuResult)
    global cipherWindow
    cipherWindow.lift()
    return

def boxxFileCipherSourceSetup():
    menuResult = askopenfilename(defaultextension = '.txt', filetypes = [('UTF-8 Text File to Iterate Over', '.txt')])
    pathBoxtext_ciphersource.set(menuResult)
    global cipherWindow
    cipherWindow.lift()
    return

def meanLength():
    phonemeLists.averageLengths={}
    for everyKey in phonemeLists.finalLegibleDictionary:
        if everyKey not in ['Pattern','Banned','Transform from','Transform to']:
            lengthListForKey=[]
            for n in phonemeLists.finalLegibleDictionary[everyKey]:
                lengthListForKey.append(len(n))
            averagePLength=mean(lengthListForKey)
            phonemeLists.averageLengths[everyKey]=averagePLength
#    print(phonemeLists.averageLengths)
    return

def patternLength():
    phonemeLists.patternLengths={}
    for eachPattern in phonemeLists.finalLegibleDictionary['Pattern']:
        listPattern=list(eachPattern)
        lengthCounter=0
        for n in listPattern:
            if n not in ['<','>','∅','|']+otherVariables.invisibles+otherVariables.fileInvisibles:
                lengthCounter=lengthCounter+phonemeLists.averageLengths[n]
        phonemeLists.patternLengths[eachPattern]=lengthCounter
#    print(phonemeLists.patternLengths)
    return

def cipherSpitter():
    invisibles = otherVariables.invisibles+['<','>','∅','|']+otherVariables.fileInvisibles
    if 'Banned' in phonemeLists.finalLegibleDictionary:
        banList = phonemeLists.finalLegibleDictionary['Banned']
    else:
        banListCheck.set(0)
##
#########nb this changes the options        
##
    wordshape = choice(phonemeLists.rightLengthPatterns)
    broken = list(wordshape)
    listWord = []
#don't wanna set this again the command on the button should set invis
#*+get* from box
    for eac in broken:
        if eac not in phonemeLists.finalLegibleDictionary:
            listWord.append(eac)
        elif eac in invisibles or len(phonemeLists.finalLegibleDictionary[eac]) is 0:
            listWord.append(eac)
        else:
            rands = choice(phonemeLists.finalLegibleDictionary[eac])
            if '#RHYME' in rands:
                rhymeDig=rands.lstrip('#RHYME')
                if rhymeDig.isdigit:
                    rhymeInt=int(rhymeDig)-1
                    if rhymeInt<=len(listWord) and rhymeInt>0:
                        listWord.append(listWord[rhymeInt])
            elif '#BLANK' in rands:
                pass
            else:
                listWord.append(rands)
    otherVariables.classWord = ''.join(listWord)
########
    endChar = endCheck.get()
    showPattern = patternCheck.get()
    useBan = banListCheck.get()
#    word=''
    if 'Transform from' and 'Transform to' in phonemeLists.finalLegibleDictionary:
        if len(phonemeLists.finalLegibleDictionary['Transform from'])>0:
            spitReplace()
            listWord=list(otherVariables.classWord)
            word=otherVariables.classWord
    else:
        word=otherVariables.classWord
        pass
    #
    if useBan is 1:
        for n in banList:
            if n in word:
#
                otherVariables.loopingBack = 1
                cipherSpitter()
                return
        else:
            listWord[:] = (value for value in listWord if value not in invisibles)
            freshWord = ''.join(listWord)
            caseWord=freshWord
            otherVariables.translated=caseWord
#            print('Randomly generated translation:', otherVariables.translated,'\n')
#
    elif useBan is 0:
        listWord[:] = (value for value in listWord if value not in invisibles)
        freshWord = ''.join(listWord)
        caseWord=freshWord
        otherVariables.translated=caseWord
#        print('Randomly generated translation:', otherVariables.translated,'\n')
    return

def cipherAct():
##    pattern = re.compile("|".join([re.escape(k) for k in phonemeLists.cipher.keys()]), re.M)
##    phonemeLists.texttocipher = pattern.sub(lambda x: phonemeLists.cipher[x.group(0)], phonemeLists.texttocipher)
##    print(phonemeLists.texttocipher)
    pattern = re.compile("|".join([re.escape(k) for k in phonemeLists.cipher.keys()]), re.M)
    ciphered = pattern.sub(lambda x: phonemeLists.cipher[x.group(0)], phonemeLists.texttocipher)
#    print(blop)
    printBox.insert(INSERT, phonemeLists.texttocipher+"\n\n")
    printBox.insert(INSERT, ciphered+"\n")
    return
    

##def cipher_display():
##    return

def preCipher():
    phonemeLists.finalLegibleDictionary=OrderedDict()
    menuResult=pathBoxtext.get()
    if menuResult.endswith('.txt'):
        otherVariables.filetitle = menuResult+' - Euphony'
        euWindow.title(otherVariables.filetitle)
        textfiler()
    elif menuResult.endswith('.csv'):
        otherVariables.filetitle = menuResult+' - Euphony'
        euWindow.title(otherVariables.filetitle)
        csvFiler()
    else:
        euWindow.title('Euphony')
    filePath = pathBoxtext_ciphersource.get()
    if len(filePath) < 4:
        return
    else:
        pass
    try:
        c=open(filePath, "r", encoding='utf-8')
        d=c.read()
        #
        phonemeLists.texttocipher=d
        #
    except:
        stringPut="Cannot open this file:\n" + filePath + "\nIs this a working UTF-8 text file?"
        messagebox.showwarning("Cannot open file", stringPut)
        return
# need a new variable for this
    for x in d:
        if x not in otherVariables.allConsonants and x not in otherVariables.allVowels and x not in ["'"] and x not in otherVariables.ys and x not in otherVariables.ws:
            d=d.replace(x," ")
        pass
##    if aPostCon.get() is 1:
##        if x not in otherVariables.allConsonants and x not in otherVariables.allVowels and x is not "'":
##            d=d.replace(x," ")
##        pass
##    elif aPostCon.get() is 0:
##        for x in d:
##            if x not in otherVariables.allConsonants and x not in otherVariables.allVowels:
##                d=d.replace(x," ")
            
    phonemeLists.ciphersourcewords=d.split()
    cipherSetup()
    return

def cipherSetup():
###@@@@@@@
    try:
        if 'Pattern' not in phonemeLists.finalLegibleDictionary.keys():
            return
        else:
            pass
    except:
        return
    phonemeLists.individual=[]
    phonemeLists.cipher={}
#PL words(cipher ver) and PL individual(cipher ver) need to be separate and come from a different file.
#need a menu to determine how much length difference to allow.
    for u in phonemeLists.ciphersourcewords:
        if u not in phonemeLists.individual:
            phonemeLists.individual.append(u)
#    print(phonemeLists.individual)
    meanLength()
    #make
    patternLength()
    ########################################
    #++++++++
    maxBiggerLEndIf = longerLimit.get()
    maxSmallerLEndIf = shorterLimit.get()
    #++++++++
    for e in phonemeLists.individual:
#        print('Generating a pattern for', e)
        otherVariables.wordRunning=e
        lengthOfWord = len(e)
        phonemeLists.rightLengthPatterns = []
        for l in phonemeLists.patternLengths:
            if phonemeLists.patternLengths[l] <= lengthOfWord + maxBiggerLEndIf and phonemeLists.patternLengths[l] >= lengthOfWord - maxSmallerLEndIf:
                phonemeLists.rightLengthPatterns.append(l)
#        print(phonemeLists.rightLengthPatterns)
################################
        if len(phonemeLists.rightLengthPatterns)>0:
            cipherSpitter()
            translatedWord=otherVariables.translated
            phonemeLists.cipher[e]=translatedWord
        else:
#the alternative has to be to broaden the search
#            print('Broaden the search')
            phonemeLists.rightLengthPatterns = []
            for increasingnumber in range(1,10):
                if len(phonemeLists.rightLengthPatterns) is 0:
#                    print('Broaden: ',increasingnumber)
                    for l in phonemeLists.patternLengths:
                        if phonemeLists.patternLengths[l] <= lengthOfWord + maxBiggerLEndIf + increasingnumber and phonemeLists.patternLengths[l] >= lengthOfWord - maxSmallerLEndIf - increasingnumber:
                            phonemeLists.rightLengthPatterns.append(l)
                else:
#                    print('Got at least one, passing. Broaden: ',increasingnumber)
                    pass
#            print(phonemeLists.rightLengthPatterns)
            cipherSpitter()
            translatedWord=otherVariables.translated
            phonemeLists.cipher[e]=translatedWord
################################
    #genning ciphered text
##    phonemeLists.translated=[]
##    #
##    if cipherread is 1:
##        for eachword in phonemeLists.words:
##            if eachword in phonemeLists.cipher:
##                phonemeLists.translated.append(phonemeLists.cipher[eachword])
##        print(phonemeLists.translated)
    listKeys=list(phonemeLists.cipher.keys())
#    tidyup
    for n in listKeys:
        phonemeLists.cipher[n.title()]=phonemeLists.cipher[n].title()
        phonemeLists.cipher[n.lower()]=phonemeLists.cipher[n].lower()
#    print("The Cipher:", phonemeLists.cipher)
    #add for re-use
##    phonemeLists.finalLegibleDictionary=OrderedDict()
##    phonemeLists.finalLegibleDictionary['Pattern']=['#']
    if 'Translate from' not in phonemeLists.finalLegibleDictionary.keys():
        phonemeLists.finalLegibleDictionary['Translate from']=[]
    if 'Translate to' not in phonemeLists.finalLegibleDictionary.keys():
        phonemeLists.finalLegibleDictionary['Translate to']=[]
#
##    for z in phonemeLists.cipher.keys():
##        phonemeLists.finalLegibleDictionary['Transform from'].append(z)
##        phonemeLists.finalLegibleDictionary['Transform to'].append(phonemeLists.cipher[z])
##
    listToOrder=[]
    for z in phonemeLists.cipher.keys():
        aLittleTuple=(z,phonemeLists.cipher[z])
        listToOrder.append(aLittleTuple)
    listToOrder.sort()
##
    #now the tupless are in alphabetical order
    alpKeys=[]
    for z in listToOrder:
        alpKeys.append(z[0])
    alpKeys.sort(key=len, reverse=True)
#    print(alpKeys)
##
    #now we have a list of the keys in the right order
    tupleListOrdered=[]
    for z in alpKeys:
        aLittleTuple=(z,phonemeLists.cipher[z])
        tupleListOrdered.append(aLittleTuple)
#
    for z in tupleListOrdered:
        phonemeLists.finalLegibleDictionary['Translate from'].append(z[0])
        phonemeLists.finalLegibleDictionary['Translate to'].append(z[1])   
#   reload
    phonemeLists.cipher=OrderedDict(zip(phonemeLists.finalLegibleDictionary['Translate from'], phonemeLists.finalLegibleDictionary['Translate to']))
    arrowDict=OrderedDict()
    for n in phonemeLists.cipher.keys():
##        k="<"+n+">"
##        v="<"+phonemeLists.cipher[n]+">"
        arrowDict["<"+n+">"]="<"+phonemeLists.cipher[n]+">"
    phonemeLists.cipher.update(arrowDict)
    buildTable()
#    print(phonemeLists.texttocipher, '\n')
    cipherAct()
#test to read
        ### right now if you cipher one text and then do another, while it does take the text it only refilters
######??>:I worx
    otherVariables.cipherwinopen=0
    pathBoxtext.set("")
    euWindow.title('Euphony')
    cipherWindow.destroy()
    return
        

def boxEnter(a):
    menuResult = pathBoxtext.get()
    if menuResult.endswith('.txt'):
        otherVariables.filetitle = menuResult+' - Euphony'
        euWindow.title(otherVariables.filetitle)
        textfiler()
    elif menuResult.endswith('.csv'):
        otherVariables.filetitle = menuResult+' - Euphony'
        euWindow.title(otherVariables.filetitle)
        csvFiler()
    else:
        euWindow.title('Euphony')
    return

def editcsv():
    try:
        selected = pathBoxtext.get()
        os.system(selected)
        return
    except:
        return


def fourAdd2(_phon):
    scan.twoJoin4 = scan.broke[scan.n] + scan.broke[scan.nPlus] + scan.broke[scan.n2Plus] + scan.broke[scan.n3Plus]

#    phonemeLists.finalLegibleDictionary[_phon].append(scan.twoJoin4)
    scan.patternFrom = scan.patternFrom + _phon

    otherVariables.vecWord.append(scan.twoJoin4)
    advance(4)

def threeAdd2(_phon):
    scan.twoJoin3 = scan.broke[scan.n] + scan.broke[scan.nPlus] + scan.broke[scan.n2Plus]

#    phonemeLists.finalLegibleDictionary[_phon].append(scan.twoJoin3)
    scan.patternFrom = scan.patternFrom + _phon
    otherVariables.vecWord.append(scan.twoJoin3)
    advance(3)

def oneAdd2(_phon):
    scan.oneOnly = scan.broke[scan.n]

#    phonemeLists.finalLegibleDictionary[_phon].append(scan.oneOnly)
    scan.patternFrom = scan.patternFrom + _phon
    otherVariables.vecWord.append(scan.oneOnly)
    advance(1)


dicter = [(['Ch', 'a', 'rl', 'o', 'tt', 'e'], '<dikiKo>'), (['Ch', 'a', 'rl', 'o', 'tt', 'e'], '<dikiKo>')]
#needs to be generated by analyst2

def analyst2():
    #otherVariables.wordVecVec
    #vecWord
    # note Ll is d not D
    phonemeLists.words = ["Charlotte", "Charlotte"]
    #needs to be generated by analyst2
    bwords=phonemeLists.words
    #phonemeLists.finalLegibleDictionary = { '£' : [], 'z': [], 'D': [], 'd': [], 't': [], '$': [], 'w': [], 'V': [], 'v': [], 'a': [], 'p': [], 'o': [], 'b': [], 'B': [], 'c': [], 'i': [], 'f': [], 'K': [], 'k': [], 'y': [], 'E': [], 'e': [], '%': [], 'h': [], '&': [], 'j': [], '¬': [], '`': [], 'U': [], 'u' : [], 'Pattern' : [], 'Banned' : []}
    #patternFrom corresponding to each vecWord?
    for word in phonemeLists.words:
        otherVariables.vecWord = []
        if len(word)<otherVariables.ignores:
            pass
        else:
            scan.broke = word
            #not broke but w/e.  Alternative to iterating over a changing vector is to read those chunks and change only the new vectors, which makes more sense, no?>  Actually would have to make more changes to index and stuff
            scan.n = 0
            scan.nPlus = 1
            scan.n2Plus = 2
            scan.n3Plus = 3
            scan.patternFrom = ""
            theEnd = len(scan.broke)-1
            while scan.n<=theEnd:
                if scan.n == 0:
                    if 4 <= theEnd:
                        if inCheckConsonant(scan.broke[scan.n]):        
                                if inCheckConsonant(scan.broke[scan.nPlus]):
                                    if inCheckConsonant(scan.broke[scan.n2Plus]):
                                        if inCheckConsonant(scan.broke[scan.n3Plus]):
                                            fourAdd2('£')
                                        else:
                                            threeAdd2('z')
                                    else:
                                        doublecheckAdd2('D','d')
                                else:
                                    oneAdd2('t')
                        elif inCheckVowel(scan.broke[scan.n]):
                                if inCheckVowel(scan.broke[scan.nPlus]):
                                    if inCheckVowel(scan.broke[scan.n2Plus]):
                                        if inCheckVowel(scan.broke[scan.n3Plus]):
                                            fourAdd2('$')
                                        else:
                                            threeAdd2('w')
                                    else:
                                        doublecheckAdd2('V','v')
                                else:
                                    oneAdd2('a')
                        else:
                            advance(1)
                    elif 3 <= theEnd:
                        if inCheckConsonant(scan.broke[scan.n]):
                                if inCheckConsonant(scan.broke[scan.nPlus]):
                                    if inCheckConsonant(scan.broke[scan.n2Plus]):
                                        threeAdd2('z')
                                    else:
                                        doublecheckAdd2('D','d')
                                else:
                                    oneAdd2('t')
                        elif inCheckVowel(scan.broke[scan.n]):
                                if inCheckVowel(scan.broke[scan.nPlus]):
                                    if inCheckVowel(scan.broke[scan.n2Plus]):
                                        threeAdd2('w')
                                    else:
                                        doublecheckAdd2('V','v')
                                else:
                                    oneAdd2('a')
                        else:
                            advance(1)
                    elif 2 <= theEnd:
                        if inCheckConsonant(scan.broke[scan.n]):
                                if inCheckConsonant(scan.broke[scan.nPlus]):
                                    doublecheckAdd2('D','d')
                                else:
                                    oneAdd2('t')
                        elif inCheckVowel(scan.broke[scan.n]):
                                if inCheckVowel(scan.broke[scan.nPlus]):
                                    doublecheckAdd2('V','v')
                                else:
                                    oneAdd2('a')
                        else:
                            advance(1)
                    else:
                        if inCheckConsonant(scan.broke[scan.n]):
                                oneAdd2('t')
                        elif inCheckVowel(scan.broke[scan.n]):
                                oneAdd2('a')
                        else:
                            advance(1)
                elif scan.n == theEnd:
                    if inCheckConsonant(scan.broke[scan.n]):
                            oneAdd2('p')
                    elif inCheckVowel(scan.broke[scan.n]):
                            oneAdd2('o')
                    else:
                        advance(1)
                elif scan.nPlus == theEnd:
                    if inCheckConsonant(scan.broke[scan.n]):
                            if inCheckConsonant(scan.broke[scan.nPlus]):
                                doublecheckAdd2('B','b')
                            else:
                                oneAdd2('c')
                    elif inCheckVowel(scan.broke[scan.n]):
                            if inCheckVowel(scan.broke[scan.nPlus]):
                                doublecheckAdd2('U','u')
                            else:
                                oneAdd2('i') 
                    else:
                        advance(1)
                elif scan.n2Plus == theEnd:
                    if inCheckConsonant(scan.broke[scan.n]):
                            if inCheckConsonant(scan.broke[scan.nPlus]):
                                if inCheckConsonant(scan.broke[scan.n2Plus]):
                                    threeAdd2('f')
                                else:
                                    doublecheckAdd2('K','k')
                            else:
                                oneAdd2('c')
                    elif inCheckVowel(scan.broke[scan.n]):
                            if inCheckVowel(scan.broke[scan.nPlus]):
                                if inCheckVowel(scan.broke[scan.n2Plus]):
                                    threeAdd2('y')
                                else:
                                    doublecheckAdd2('E','e')
                            else:
                                oneAdd2('i')  
                    else:
                        advance(1)
                elif scan.n3Plus == theEnd:
                    if inCheckConsonant(scan.broke[scan.n]):
                            if inCheckConsonant(scan.broke[scan.nPlus]):
                                if inCheckConsonant(scan.broke[scan.n2Plus]):
                                    if inCheckConsonant(scan.broke[scan.n3Plus]):
                                        fourAdd2('%')
                                    else:
                                        threeAdd2('h')
                                else:
                                    doublecheckAdd2('K','k')
                            else:
                                oneAdd2('c')
                    elif inCheckVowel(scan.broke[scan.n]):
                            if inCheckVowel(scan.broke[scan.nPlus]):
                                if inCheckVowel(scan.broke[scan.n2Plus]):
                                    if inCheckVowel(scan.broke[scan.n3Plus]):
                                        fourAdd2('&')
                                    else:
                                        threeAdd2('j')
                                else:
                                    doublecheckAdd2('E','e')
                            else:
                                oneAdd2('i')
                    else:
                        advance(1)
                else:
                        if inCheckConsonant(scan.broke[scan.n]):
                                if inCheckConsonant(scan.broke[scan.nPlus]):
                                    if inCheckConsonant(scan.broke[scan.n2Plus]):
                                        if inCheckConsonant(scan.broke[scan.n3Plus]):
                                            fourAdd2('¬')
                                        else:
                                            threeAdd2('h')
                                    else:
                                        doublecheckAdd2('K','k')
                                else:
                                    oneAdd2('c')
                        elif inCheckVowel(scan.broke[scan.n]):
                                if inCheckVowel(scan.broke[scan.nPlus]):
                                    if inCheckVowel(scan.broke[scan.n2Plus]):
                                        if inCheckVowel(scan.broke[scan.n3Plus]):
                                            fourAdd2('`')
                                        else:
                                            threeAdd2('j')
                                    else:
                                        doublecheckAdd2('E','e')
                                else:
                                    oneAdd2('i')
                        else:
                            advance(1)
                otherVariables.wordVecVec.append(otherVariables.vecWord)
                phonemeLists.wordsXPatterns.append((otherVariables.vecWord, scan.patternFrom))


def warper():
    analyst2()
    warpChange()
    n = 0
    for pair in phonemeLists.wordsXPatterns:
        print("go pair")
        wWord = ""
        nn = -1
        patternFrom = pair[1].strip('<>')
        print(patternFrom)
        print("is patternFrom")
        for h in pair[0]:

            q = 0
            b = patternFrom[nn]
            patternDictEntry = phonemeLists.finalLegibleDictionary[b]
            #print(b, patternDictEntry)
            for x in patternDictEntry:
                if h == x:
                    q = 1
            if q == 0:
                for x in patternDictEntry:
                    print("h is ",h)
                    print("x is ",x)
                    if h[0] == x[0]:
                        h = x
                        q = 1
            if q == 0:
                #print(h, " not found")

                wWord += choice(patternDictEntry)
            else:
                #print(h, " found")
                wWord += h

            nn += 1
            q = 0
        #print(wWord)
        #printBox.insert(INSERT, '['+wordshape+' : '+caseWord+']')
        printBox.insert(INSERT, wWord + ' ')

def warpChange():
    #this changes the patterns of the words to warp to accepted ones
    legalPatterns = phonemeLists.finalLegibleDictionary["Pattern"]
    shuffle(legalPatterns)
    #phonemeLists.wordsXPatterns = [(['Ch', 'a', 'rl', 'o', 'tt', 'e'], '<dikiKo>'), (['Ch','a','r'], '<dip>')]
    n=1
    tuplematches = []
    for x in phonemeLists.wordsXPatterns:
        thispat = x[1]
        if thispat in legalPatterns:
            #print("y")
            tuplematches.append(x)
        else:
            #print("n")
            size = len(thispat) - 1
            #MyString[a:b]
            alike = ""
            while size > 0 and otherVariables.de is 0:
                otherVariables.de = 0
                for g in legalPatterns:
                    if thispat[0:size] in g and otherVariables.de is 0:
                        alike = g
                        #print(thispat[0:size], alike)
                        a = len(alike)
                        d = len(thispat)
                        if a>d:
                            x[0].extend(list(range(a-d)))
                        elif a is d:
                            pass
                        else:
                            pass
                        #x[0].append
                        tuplematches.append((x[0], alike))
                        otherVariables.de = 1
                size -= 1
            otherVariables.de = 0
        n+=1
    phonemeLists.wordsXPatterns = tuplematches



#frame = Frame(root, width=100, height=100)


euWindow = Tk()
ignoreWindow=Toplevel()
ignoreWindow.withdraw()
invisibleWindow=Toplevel()
invisibleWindow.withdraw()
#ttk.Style().configure("Treeview", background="#ccc", borderwidth=10)

pathBoxtext = StringVar()
pathBoxtext_ciphersource = StringVar()
numBoxtext = IntVar()
numBoxtext.set(10)
banListCheck = IntVar()
banListCheck.set(1)
patternCheck = IntVar()
endCheck = IntVar()
aPostCon = IntVar()
wCapitalise = IntVar()
#this is not being read correctly
wCapitalise.set(1)
showUnt = IntVar()
showUnt.set(0)
##tableyes = IntVar()
##tableyes.set(1)
invisiblePatternText = StringVar()
#invisiblePatternText.set
invisibleLabelText = StringVar()
invisibleSpitterText = ''
ignoreLength = IntVar()
ignoreLength.set(1)
#placehold = IntVar()
yVowel = IntVar()
yVowel.set(1)
wVowel = IntVar()
longerLimit = IntVar()
shorterLimit = IntVar()
longerLimit.set(1)
shorterLimit.set(1)

euTreeview=ttk.Treeview()

def buildTable():
    global euTreeview
    global scrollbar
    global tableFrame
    global lesserFrame
    if otherVariables.tableBuilt is 1:
        euTreeview.destroy()
        scrollbar.destroy()
        tableFrame.destroy()
        lesserFrame.destroy()
    else:
        pass
    keysTuple = tuple(phonemeLists.finalLegibleDictionary.keys())
    tableFrame = Frame(mainTopFrame)
    lesserFrame = Frame(tableFrame)
    scrollbar = Scrollbar(lesserFrame)
    euTreeview = ttk.Treeview(lesserFrame, height = 10, selectmode='browse', columns=keysTuple, displaycolumns=keysTuple, yscrollcommand=scrollbar.set)

    for nom in keysTuple:
#        euTreeview.heading(nom, text=nom, command=listclicker)
        euTreeview.heading(nom, text=nom)
        euTreeview.column(nom, width=Font().measure(nom), stretch=NO)
        
    for lengthTester in keysTuple:
        if len(phonemeLists.finalLegibleDictionary[lengthTester])>otherVariables.setTester:
           otherVariables.setTester=len(phonemeLists.finalLegibleDictionary[lengthTester])
    longestrange=range(0, otherVariables.setTester)
    for t in longestrange:
        for n in keysTuple:
            otherVariables.placeholder=phonemeLists.finalLegibleDictionary[n]
    #        if this end of the dictionary exists else append a blank to fill gap
    #       otherwise it will fail at the first hurdle with an empty banList!
            if len(otherVariables.placeholder)>=t+1:
                otherVariables.roww.append(otherVariables.placeholder[t])
            else:
                otherVariables.roww.append('')
        euTreeview.insert('', 'end', values=otherVariables.roww)
    #    print(otherVariables.roww)
        otherVariables.roww=[]

    for eac in phonemeLists.finalLegibleDictionary:
        thekey=eac
        thelist=phonemeLists.finalLegibleDictionary.get(eac)
        z=eac
        for eac2 in thelist:
            if Font().measure(eac2)>Font().measure(z):
                z=eac2
            if Font().measure(eac2)>Font().measure('AAAAAAAAAAAAAAA'):
                z = 'AAAAAAAAAAAAAAA'
        euTreeview.column(thekey, width=Font().measure(z)+10, stretch=NO, minwidth=1)
    #banned needs wider than 0. nd set to title width if that's longest
    #    euTreeview.column(thekey, width=z)
#        print(thekey, 'Should now have a width of', z)
    euTreeview.column('#0', width=0, stretch=NO, minwidth=0)
    euTreeview.grid(row = 0, column = 0)
    scrollbar.grid(row = 0, column = 1, sticky=N+S)
    scrollbar.config(command=euTreeview.yview)
    tableFrame.grid(row = 1, column = 0, columnspan = 3, pady = 6, sticky=W+E)
#    lesserFrame.place(relx=.5, rely=.5, anchor="c")
    lesserFrame.pack(expand=1)
#    euTreeview.bind('<Button-1>',listclicker)
    otherVariables.tableBuilt = 1
#    print('otherVariables.tableBuilt=',otherVariables.tableBuilt)
    return

def rclicktextarea(posevent):
    boxRCMenu.post(posevent.x_root, posevent.y_root)
    return

def rccut():
    global printBox
    printBox.focus_set()
    printBox.event_generate("<<Cut>>")
    return
def rccopy():
    global printBox
    printBox.focus_set()
    printBox.event_generate("<<Copy>>")
    return
def rcsall():
    global printBox
    printBox.focus_set()
    printBox.tag_add(SEL, "1.0", END)
    printBox.mark_set(INSERT, "1.0")
    printBox.see(INSERT)
    return
def rcpaste():
    global printBox
    printBox.focus_set()
    printBox.event_generate("<<Paste>>")
    return

##def spitReplace():
##    pattern = re.compile("|".join([re.escape(k) for k in phonemeLists.replacer.keys()]), re.M)
##    otherVariables.classWord = pattern.sub(lambda x: phonemeLists.replacer[x.group(0)], otherVariables.classWord)
##fix this!###
def rcTransform():
    global printBox
    printBox.focus_set()
    otherVariables.transformText=printBox.selection_get()
    pattern = re.compile("|".join([re.escape(k) for k in phonemeLists.replacer.keys()]), re.M)
    otherVariables.transformText = pattern.sub(lambda x: phonemeLists.replacer[x.group(0)], otherVariables.transformText)
    printBox.event_generate("<Delete>")
    printBox.insert(INSERT, otherVariables.transformText)
    return

def rcTranslate():
    global printBox
    printBox.focus_set()
    otherVariables.translateText=printBox.selection_get()
    otherVariables.translateText=otherVariables.translateText.replace(' ',"> <")
    otherVariables.translateText="<"+otherVariables.translateText+">"
    for n in [".",",","?","!",";",":","-"]:
##############need list of all things normally considered to separate words- eg. not apostrophes
        otherVariables.translateText=otherVariables.translateText.replace(n, ">"+n+"<")  
    pattern = re.compile("|".join([re.escape(k) for k in phonemeLists.cipher.keys()]), re.M)
    otherVariables.translateText = pattern.sub(lambda x: phonemeLists.cipher[x.group(0)], otherVariables.translateText)
    otherVariables.translateText=otherVariables.translateText.replace('<','')
    otherVariables.translateText=otherVariables.translateText.replace('>','')
    printBox.event_generate("<Delete>")
    printBox.insert(INSERT, otherVariables.translateText)
    return

def setCipherWindow():
#this is still opening when it's open, shouldn't
    try:
        if otherVariables.cipherwinopen is 1:
            return
        else:
            openupCipher()
            otherVariables.cipherwinopen=1
    except:
        openupCipher()
        otherVariables.cipherwinopen=1
    return

def cipherSetBack():
    cipherWindow.destroy()
    otherVariables.cipherwinopen=0
    pathBoxtext.set("")
    return

def openupCipher():
    global cipherWindow
    cipherWindow = Toplevel()
    cipherWindow.title("Cipher settings")
    cipherWindow.resizable(0, 0)
    cipherframe = Frame(cipherWindow, padx = 4, pady = 4)
#
    pathBoxLabel_source = Label(cipherframe, text ='Text to cipher:')
    pathBox_source = Entry(cipherframe, width = 30, textvariable = pathBoxtext_ciphersource)
#####################    pathBox_source.bind('<Return>', boxEnter_ciphersource)
    pathButton_source = Button(cipherframe, text = 'browse...', command = boxxFileCipherSourceSetup)
    pathBoxLabel_source.grid(row = 0, column = 0, sticky = W, padx = 2, pady = 2)
    pathBox_source.grid(row = 0, column = 1, sticky = W)
    #pathButton.grid(row = 0, column = 2, sticky = W, padx = -50)
    pathButton_source.grid(row = 0, column = 2, sticky = W)
#
    pathBoxLabel_rules = Label(cipherframe, text ='Word rules:')
    pathBox_rules = Entry(cipherframe, width = 30, textvariable = pathBoxtext)
    pathButton_rules = Button(cipherframe, text = 'browse...', command = boxxFileSetupForC)
    pathBoxLabel_rules.grid(row = 1, column = 0, sticky = W, padx = 2, pady = 2)
    pathBox_rules.grid(row = 1, column = 1, sticky = W)
    #pathButton.grid(row = 0, column = 2, sticky = W, padx = -50)
    pathButton_rules.grid(row = 1, column = 2, sticky = W)
    startbutton = Button(cipherframe, text = 'Cipher text', command = preCipher)
    startbutton.grid(row =  4, columnspan = 3, padx = 4, pady = 18)
    longerboxlabel=Label(cipherframe, text = 'Permitted upper length difference:')
    shorterboxlabel=Label(cipherframe, text = 'Permitted lower length difference:')
    longerbox=Spinbox(cipherframe, textvariable = longerLimit, from_= 0, to= 1000, width = 5)
    shorterbox=Spinbox(cipherframe, textvariable = shorterLimit, from_= 0, to= 1000, width = 5)
    longerboxlabel.grid(row = 2, column = 0, sticky=W, padx = 2, pady = 2)
    shorterboxlabel.grid(row = 3, column = 0, sticky=W, padx = 2, pady = 2)
    longerbox.grid(row = 2, column = 1, sticky=W)
    shorterbox.grid(row = 3, column = 1, sticky=W)
#    checktransformappend=Checkbutton(cipherframe, text="Add cipher data to",variable =
#
    cipherframe.grid(row = 0, column = 0)
#
    big=str(euWindow.geometry())
    bigw=big.replace('+','x')
    t4Numbers=bigw.split(sep='x')
#    print('geometry ripped', t4Numbers)

    theX=str(int(int(t4Numbers[0])/2)+int(t4Numbers[2])-220)
    theY=str(int(int(t4Numbers[1])/2)+int(t4Numbers[3])-85)
    pluses='+'+theX+'+'+theY
#    print(pluses)
    cipherWindow.geometry(pluses)
    otherVariables.cipherwinopen=1
    cipherWindow.protocol("WM_DELETE_WINDOW", cipherSetBack)
    return

def rcdelete():
    global printBox
    printBox.focus_set()
    printBox.event_generate("<Delete>")
    return
def rcclearall():
    global printBox
    printBox.focus_set()
    printBox.tag_add(SEL, "1.0", END)
    printBox.mark_set(INSERT, "1.0")
    printBox.see(INSERT)
    printBox.event_generate("<Delete>")
    return

class helpWriteup():
    helpwrote="The generator selects randomly from strings of characters shown in the lettered columns and sticks them together according to a randomly selected pattern shown in the Patterns column.\n\nYou can make your own CSV files, like for your own cultures or languages, that follow the same format.  In each column which has a single letter as a title, the strings included can be any characters, strings of characters or words you want.\n\nThe reader reads the patterns of words and elements of those words from text files to get usable data to generate words (or phrases).\n\nThose words should sound similar to the words from the source file, because theY arrange the same sounds in the same patterns.  There are some examples included with the exe.\n\nStraight off, the data might not be enough to get the kind of words you want.  But you can always fiddle with the CSV if you save the data.\n\nStrings in the Banned column won't appear in any words you generate.  Strings in the Transform from column will be changed to the strings in the Transform to column.\n\nRight now the reader only works for Latin characters.\n\n'Invisibles' means characters that are read when constructing words but do not have a value.  theY are used when banning and transforming words, but do not select a value to output.  <, >, ∅ and | are always invisibles."
    
def showHelp(a):
    messagebox.showinfo("Some help", helpWriteup.helpwrote)
    return
def showHelp2():
    messagebox.showinfo("Some help", helpWriteup.helpwrote)
    return

euWindow.geometry('+628+169')
euWindow.title(otherVariables.filetitle)
euWindow.resizable(0, 0)

menuBar = Menu(euWindow)

def fileMenuUpdate():
    if len(phonemeLists.finalLegibleDictionary)>0:
        fileMenu.entryconfig(2, state=NORMAL)
    else:
        fileMenu.entryconfig(2, state=DISABLED)
    if len(phonemeLists.finalLegibleDictionary)>0 and len(pathBoxtext.get())>2:
        fileMenu.entryconfig(1, state=NORMAL)
    else:
        fileMenu.entryconfig(5, state=DISABLED)
    if len(phonemeLists.finalLegibleDictionary)>0:# and len(pathBoxtext.get())>2:
        fileMenu.entryconfig(5, state=NORMAL)
    else:
        fileMenu.entryconfig(1, state=DISABLED)
    global printBox
    if len(printBox.get('1.0', END+'-1c'))>0:
        fileMenu.entryconfig(3, state=NORMAL)
    else:
        fileMenu.entryconfig(3, state=DISABLED)
    return

fileMenu = Menu(menuBar, tearoff = 0, postcommand=fileMenuUpdate)
fileMenu.add_command(label = 'Load File', command = boxxFile)
fileMenu.add_command(label = 'Edit Loaded File', command = editcsv)
fileMenu.add_command(label = 'Save Loaded Data as CSV', command = fromTextSaver)
fileMenu.add_command(label = 'Load Text From Box', command = boxFiler)
fileMenu.add_command(label = 'Cipher Text', command = setCipherWindow)
fileMenu.add_command(label = 'Warp', command = warper)
fileMenu.add_command(label = 'Exit', command = euWindow.destroy)
menuBar.add_cascade(label = 'File', menu = fileMenu)

optionsMenu = Menu(menuBar, tearoff = 0)
readerMenu = Menu(optionsMenu, tearoff = 0)
generatorMenu = Menu(optionsMenu, tearoff = 0)
optionsMenu.add_cascade(label = 'Reader', menu = readerMenu)
readerMenu.add_checkbutton(label = 'Count apostrophes as consonants when reading text files', variable = aPostCon)
readerMenu.add_checkbutton(label = 'Count Y as a vowel when reading text files', variable = yVowel)
readerMenu.add_checkbutton(label = 'Count W as a vowel when reading text files', variable = wVowel)
optionsMenu.add_cascade(label = 'Generator', menu = generatorMenu)
generatorMenu.add_checkbutton(label = 'Use a ban list', variable = banListCheck)
generatorMenu.add_checkbutton(label = 'Show the pattern used for each word', variable = patternCheck)
generatorMenu.add_checkbutton(label = 'Show each word before transformation', variable = showUnt)
generatorMenu.add_checkbutton(label = 'New line for each word', variable = endCheck)
generatorMenu.add_checkbutton(label = 'Regular case for words', variable = wCapitalise)

def invisibleSetback():
    invisibleWindow.destroy()
    otherVariables.windowOpen=0
    return

def openup():
    global invisibleWindow
    invisibleWindow = Toplevel()
    invisibleWindow.title("")
    invisibleWindow.resizable(0, 0)
    invisible_frame = Frame(invisibleWindow, padx = 12, pady = 12)
    invisible_frame.pack()
##    invisibleWindow.geometry('+800+300')
##    invisibleWindow.resizable(0, 0)
    invisible_label = Label(invisible_frame, text = 'Extra invisibles:')
    invisible_label.grid(row = 0, column = 0, sticky = W)
    invisible_box = Entry(invisible_frame, textvariable = invisiblePatternText, width = 5)
    invisible_box.bind('<Return>', invisibleSetKey)
    invisible_box.grid(row = 0, column = 1, sticky = W)
    invisible_button = Button(invisible_frame, text = 'set', command = invisibleSet)
    invisible_button.grid(row = 0, column = 2, sticky = W)
    invisibleWindow.protocol("WM_DELETE_WINDOW", invisibleSetback)
#
    big=str(euWindow.geometry())
    bigw=big.replace('+','x')
    t4Numbers=bigw.split(sep='x')
#    print('geometry ripped', t4Numbers)
    theX=str(int(int(t4Numbers[0])/2)+int(t4Numbers[2])-85)
    theY=str(int(int(t4Numbers[1])/2)+int(t4Numbers[3])-26)
    pluses='+'+theX+'+'+theY
#    print(pluses)
    invisibleWindow.geometry(pluses)
    otherVariables.windowOpen=1
    return
    
def setinwindow():
#this is still opening when it's open, shouldn't
    try:
        if otherVariables.windowOpen is 1:
            return
        else:
            openup()
            otherVariables.windowOpen=1
    except:
        openup()
        otherVariables.windowOpen=1
    return

def igsetback():
    ignoreWindow.destroy()
    otherVariables.windowIgOpen=0
    return

def openupig():
    global ignoreWindow
    ignoreWindow = Toplevel()
    ignoreWindow.title("")
    ignoreWindow.resizable(0, 0)
    ignoreFrame = Frame(ignoreWindow, padx = 12, pady = 12)
    ignoreFrame.pack()
##    ignoreWindow.geometry('+800+300')
##    ignoreWindow.resizable(0, 0)
    ignoreLabel = Label(ignoreFrame, text = 'Ignore words shorter than:')
    ignoreLabel.grid(row = 0, column = 0, sticky = W)
    ignoreBox = Spinbox(ignoreFrame, textvariable = ignoreLength, from_= 1, to= 1000, width = 5)
    ignoreBox.bind('<Return>', ignoreSetKey)
    ignoreBox.grid(row = 0, column = 1, sticky = W)
    ignoreBoxButton = Button(ignoreFrame, text = 'set', command = ignoreSet)
    ignoreBoxButton.grid(row = 0, column = 2, sticky = W)
    ignoreWindow.protocol("WM_DELETE_WINDOW", igsetback)
#
    big=str(euWindow.geometry())
    bigw=big.replace('+','x')
    t4Numbers=bigw.split(sep='x')
#    print('geometry ripped', t4Numbers)
    theX=str(int(int(t4Numbers[0])/2)+int(t4Numbers[2])-121)
    theY=str(int(int(t4Numbers[1])/2)+int(t4Numbers[3])-26)
    pluses='+'+theX+'+'+theY
#    print(pluses)
    ignoreWindow.geometry(pluses)
    otherVariables.windowIgOpen=1
    return
    
def setIgnoreWindow():
    try:
        if otherVariables.windowIgOpen is 1:
            return
        else:
            openupig()
            otherVariables.windowIgOpen=1
    except:
        openupig()
        otherVariables.windowIgOpen=1
    return

def invisibleSetKey(a):
    invisibleSet()
    
def invisibleSet():
    global invisibleWindow
    if invisiblePatternText.get() is '':
        otherVariables.invisibles = []
        messagebox.showwarning("Extra invisibles emptied", "Not using any extra invisibles.")
##need to restore deleted ones or show a record somewhere else
## or spitter could just call the box text and set from there
        pass
    else:
        otherVariables.invisibles = list(invisiblePatternText.get())
        readout= 'Extra invisibles set to:\n'
        for noo in otherVariables.invisibles:
            readout = readout+noo+', '
        readout= readout.strip(', ')
        messagebox.showinfo("Invisibles set", readout)
    otherVariables.windowOpen=0
    invisibleWindow.destroy()
    return
#
#
def ignoreSetKey(a):
    ignoreSet()
    
def ignoreSet():
    global ignoreWindow
    otherVariables.ignores = int(ignoreLength.get())
    if otherVariables.ignores>1 or otherVariables.ignores is 0:   
        readout="Will ignore words less than "+str(otherVariables.ignores)+" characters long."
    else:
       readout="Will ignore words less than "+str(otherVariables.ignores)+" character long." 
    messagebox.showinfo("Reader ignoring words", readout)
    otherVariables.windowIgOpen=0
    ignoreWindow.destroy()
    return
    
generatorMenu.add_command(label = 'Pattern settings...', command = setinwindow)
readerMenu.add_command(label = 'Ignore words...', command = setIgnoreWindow)

menuBar.add_cascade(label = 'Options', menu = optionsMenu)

aboutmenu = Menu(menuBar, tearoff = 0)
aboutmenu.add_command(label = "By Cha-M, 2018")
aboutmenu.add_command(label = "Help", command=showHelp2)
menuBar.add_cascade(label = 'Help', menu = aboutmenu)

euWindow.bind("<F1>", showHelp)

euWindow.config(menu = menuBar)

def rcupdate():
    if len(phonemeLists.replacer)>0:
        boxRCMenu.entryconfig(5, state=NORMAL)
    else:
        boxRCMenu.entryconfig(5, state=DISABLED)
    if len(phonemeLists.cipher)>0:
        boxRCMenu.entryconfig(6, state=NORMAL)
    else:
        boxRCMenu.entryconfig(6, state=DISABLED)
    return

boxRCMenu = Menu(euWindow, tearoff=0, postcommand=rcupdate)
boxRCMenu.add_command(label="Cut", command=rccut)
boxRCMenu.add_command(label="Copy", command=rccopy)
boxRCMenu.add_command(label="Paste", command=rcpaste)
boxRCMenu.add_command(label="Delete", command=rcdelete)
boxRCMenu.add_command(label="Select All", command=rcsall)
boxRCMenu.add_command(label="Transform selection", command=rcTransform, state=DISABLED)
boxRCMenu.add_command(label="Translate selection", command=rcTranslate, state=DISABLED)
boxRCMenu.add_command(label="Clear All", command=rcclearall)

mainTopFrame = Frame(euWindow, pady = 2)
pathFrame = Frame(mainTopFrame)
numBoxLabel = Label(mainTopFrame, text ='Words to generate:', padx = 2)

pathBoxLabel = Label(mainTopFrame, text ='File path:')
pathBox = Entry(pathFrame, width = 30, textvariable = pathBoxtext)
pathBox.bind('<Return>', boxEnter)

pathButton = Button(pathFrame, text = 'browse...', command = boxxFile)
reloadButton = Button(pathFrame, text = 'Reload', command = reloadFile, state=DISABLED)

pathBoxLabel.grid(row = 0, column = 0, padx = 2, pady = 2)
pathBox.grid(row = 0, column = 1, sticky = W)

pathButton.grid(row = 0, column = 2, sticky = W)
reloadButton.grid(row = 0, column = 3, sticky = W)
#
numBox = Spinbox(mainTopFrame, textvariable = numBoxtext, from_= 1, to= 1000, width = 5)

def spitterSetupKey(a):
    spitterSetup()
    return

numBox.bind('<Return>', spitterSetupKey)
spitButton = Button(mainTopFrame, text = 'Generate some words!', command = spitterSetup, state=DISABLED)

printBox = ScrolledText(height = 30)
printBox.bind("<Button-3>", rclicktextarea)

pathBoxLabel.grid(row = 0, column = 0, pady = 2, sticky = W)
pathFrame.grid(row = 0, column = 1, sticky = W+E)
numBoxLabel.grid(row = 2, column = 0, pady = 2, sticky = W)
numBox.grid(row = 2, column = 1, sticky = W)

printBox.grid(row = 13, columnspan = 4, sticky = W+E)

spitButton.grid(row = 9, column = 0, columnspan = 4, pady = 18)
mainTopFrame.grid(row = 0, columnspan = 4)

euWindow.mainloop()
