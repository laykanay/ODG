# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define o = Character("Ood", color="#06a94d")
define l = Character("Leon", color="#f05e23")
define s = Character("Sage", color="#6699cc")
define r = Character("Richard", color="#200080")
define p = Character("[playername]", color="#80007e")
define v = Character("Valhella", color = "#000000")
define security = Character("Security", color="#6d9100")
define cash = Character("Cashier", color="#008b8b")
define maitre = Character("Maître d'", color="#f403fc")

define audio.applause = "audio/applause.mp3"
# favorite foods by name+ff, least fave name+lf. fave movie name+fm, least fave movie name+lm
define oodff = "lobster"
define oodlf = "lasagna"
define oodfm = "12 Angry Men"
define oodlm = "Texas Chainsaw Massacre"
define sageff = "mac and 4"
define sagelf = "sweet relish"
define sagefm = "Texas Chainsaw Massacre"
define sagelm = "The Notebook"
define leonff = "sausage and rice in tomato sauce"
define leonlf = "sauerkraut"
define leonfm = "John Wick"
define leonlm = "Les Demoiselles de Rochefort"
define richardff = "vermicelli noddle bowl"
define richardlf = "dill pikle vodka"
define richardfm = "sci-fi"
define richardlm = "The Last Airbender"
define valff = ""
define vallf = ""
define valfm = ""
define vallm = ""

transform bounce:
    pause .15
    yoffset 0
    easein .175 yoffset -10
    easeout .175 yoffset 0
    easein .175 yoffset -4
    easeout .175 yoffset 0
    yoffset 0
    repeat 2

init python:
    ood_points = 0
    sage_points = 0
    richard_points = 0
    leon_points = 0
    val_points = 0

# The game starts here.

label start:

    scene bg stage with fade

    play sound applause fadein .5 noloop

    show ood happy at right with dissolve

    o "... And for Occultae Veritatus Podcast, I'm Ood Gallifrey, and Live in Studio with me is.."

    hide ood happy
    show sage happy at left with dissolve

    s "Sage Murray!"

    hide sage happy
    show leon happy at right with dissolve

    l "Leon Filger"

    hide leon
    show richard happy at left with dissolve

    r "And I'm Richard Bigly"

    show ood happy at right
    show sage happy at center:
        xoffset 150
    show leon happy at center:
        xoffset -150
    r "Good night!"
    l "Later!"
    o "I love you all!"
    s "BYYEE!!!"

    stop sound fadeout 1.0
    hide ood happy
    hide sage happy
    hide leon happy
    hide richard happy
    show bg backstage with fade

    show ood at right with dissolve
    o "Wow. That was harder than I thought"

    show sage at left with dissolve
    s "Yea, I know! Takes a lot out of ya."

    hide sage
    show richard at left with dissolve
    r "Just have to meet that VIP fan now."

    hide ood
    show leon at right with dissolve
    l "What was their name again?"

    "{i}shuffles papers{/i}"
    r "it says their name is..."


    python:
        playername = renpy.input("What is your name?")
        playername = playername.strip()
        playername = playername.capitalize()
        if not playername:
            playername = "Cultist"

    r "[playername]. That is a good name."

    l "Lets head back to the dressing room and wait for them."


    jump secguard

label secguard:

    scene bg stage with fade

    p "I am so excited! I have been listening to OVPod since it came out, now I get to meet the hosts!"
    p "Just gotta head backstage. God I'm nervous."

    "You walk toward the backstage entrance, and are met by a mountain of a man."

    show security at center with dissolve
    security "Who are you kid?"

    menu:
        "Uhh, I should be on the List!":
            jump rude

        "{i}Shows VIP badge{/i} \n I have a backstage pass to meet the hosts.":
            jump polite

    label rude:
         security "I don't have a list you rude shit. Show me a badge or I'll show you out."

         "You show the beef mountain your VIP badge"

         security "See? That wasn't so hard."
    jump backstage

    label polite:
        "The nice security man looks at your pass"
        security "Thanks.. [playername]. Head on in."
        "The beef mountain smiles at you."
    jump backstage

    label backstage:
         "He moves out of your way, and lets you through."

label meeting:

    scene bg greenroom door

    "You steel yourself. You have been listening to OVPod since the beginning."
    "You have been a part of their Patreon since they posted the link."
    "You have been chatting with the hosts on their Discord server."
    "Now you get to meet them in..."
    "3"
    "2"
    "1"
    "You enter the door..."

    scene bg greenroom
    with dissolve
    show ood at right
    with dissolve
    show sage at left
    with dissolve
    show leon at center:
        xoffset 150
    with dissolve
    show richard at center:
        xoffset -150
    with dissolve

    "And you see your four favourite people."

    show ood happy at right
    with dissolve
    o "There they are!"
    show leon happy at center:
        xoffset 150
    with dissolve
    l "Glad you could make it!"
    show sage happy at left
    with dissolve
    s "[playername] right? Glad to meet you!"
    show richard happy at center:
        xoffset -150
    with dissolve
    r "We have been looking forward to meeting you all night!"

    "They are all looking at you happily."
    $ renpy.pause(2.0)
    show ood with dissolve
    show sage with dissolve
    show richard with dissolve
    show leon with dissolve

    "You should say something"
    menu:
        ".....Hi... Im... [playername]...":
            jump meetingshy
        "Wow! I am so glad to finally meet you all! I'm [playername]!":
            jump meetingloud

    label meetingshy:
        show richard happy
        r "You don't have to be shy, we dont bite"
        show leon happy
        l   "I mean, Sage might, but only if you want her to"
        show sage happy
        s "That's not true!  ... ok its a little true but not with our top fan!"
        show ood happy
        o "So what did you think of the show?"
    jump invite

    label meetingloud:
        show ood happy
        o "Yea! We're excited too!"
        show sage happy
        s "After our last talk on Discord, I've been so pumped to meet you!"
        s "Even Richard has been excited"
        show richard happy
        r "Yea, Were all happy to see you"
        show leon happy
        l "A pleasure to meet you [playername]!"
    jump invite

label invite:
    scene bg blank with fade
    "You ended up talking to he hosts for a good hour."
    "They were really nice, and just like their personas..."
    "If not a little more tired."
    "And, the most exciting part is,"
    "They invited you to their studio to be a guest!"
    p "I..."
    menu:
        "Played it cool":
            jump cooldood
        "Totally freaked out":
            jump freakout
    label cooldood:
        p "I played it cool."
        p "Richard and Leon both just nodded approvingly when I accepted."
        jump meetingend
    label freakout:
        p "I totally freaked out"
        p "Ood and Sage joined me in my excited freak out!"
        jump meetingend

label meetingend:
    p "In one week's time, I will get to hangout out with my Hosts again"
    p "This time with a microphone and everything!"

    jump recording

label recording:
    scene bg trans with fade
    "One week later..."
    scene bg studio with fade
    "You arrived and the hosts met you at the door and invited you in."
    "You headed into the studio, and were shown a couch and a chair with a microphone."
    show ood at center with dissolve
    o "You can take your pick, if you want to be a guest, have a seat in the recording chair."
    o "You can also just hang out on that couch over there, and be in the audience."
    o "It's up to you."

    menu:
        "I think I will take the couch. I am a little too nervous":
            jump recordingshy
        "I think I can hop in and be a guest!":
            jump recordingloud

label recordingshy:
    $ richard_points = richard_points + 1
    $ leon_points = leon_points + 1

    hide ood
    show richard at left with dissolve
    r "Thats ok [playername]. Everyone has to start somewhere"

    hide richard
    "You sit through all four episodes."
    "Ood did an episode on some sort of paranormal mystery"
    "Sage talked about another serial killer."
    "Richard had an episode about a hacking event."
    "Leon talked about a space incident."

    label noshy:
    show bg studio with fade
    show leon at left with dissolve
    show ood at right with dissolve
    show sage at center with dissolve:
        xoffset -150
    show richard at center with dissolve:
        xoffset 150

    o "So [playername], what did you think?"
    s "Yea, who did your favorite episode of the night?"

menu:
    "Ood. I love a mystery.":
        jump ooddateshy
    "Sage. I am facinated by serial killers":
        jump sagedateshy
    "Richard. Tech stuff is so interesting!":
        jump richarddateshy
    "Leon. Space is Great!":
        jump leondateshy

        label ooddateshy:
            hide sage
            hide richard
            hide leon
            show ood blush at center with dissolve
            o "Really? My episode?"
            show ood happy
            o "You have great taste!"
            show ood emb
            o "Say... would you maybe want to talk more about mysteries with me?"
            o "Maybe somewhere with just the two of us?"
            menu:
                "Yes! i'd love to!":
                    jump ooddate
                "Nah, i'm not really interested":
                    jump oodnoshy
            label oodnoshy:
            show ood sad at center with dissolve
            o "Oh, thats too bad. Maybe you had a different favorite episode?"
            o "You could tell one of the other hosts"
            menu:
                "Yea, that sounds alright":
                    jump noshy
                "No. This is lame":
                    jump losershy

        label sagedateshy:
            hide ood
            hide leon
            hide richard
            show sage blush at center with dissolve
            s "Really? My episode?"
            show sage happy
            s "I'm so flattered!"
            show sage emb
            s "Say... would you maybe want to talk more about serial killers with me?"
            s "Maybe somewhere with just the two of us?"
            menu:
                "Yes! i'd love to!":
                    jump sagedate
                "Nah, i'm not really interested":
                    jump sagenoshy
            label sagenoshy:
                show sage sad at center with dissolve
                s "Oh, thats too bad. Maybe you had a different favorite episode?"
                s "You could tell one of the other hosts"
                menu:
                    "Yea, that sounds alright":
                        jump noshy
                    "No. This is lame":
                        jump losershy

        label richarddateshy:
            hide sage
            hide ood
            hide leon
            show richard blush at center with dissolve
            r "Really? My episode?"
            show richard happy
            r "I knew you were a nerd!"
            show richard emb
            r "Say... would you maybe want to talk more about tech shit with me?"
            r "Maybe somewhere with just the two of us?"
            menu:
                "Yes! i'd love to!":
                    jump richarddate
                "Nah, i'm not really interested":
                    jump richardnoshy
            label richardnoshy:
                show richard sad at center with dissolve
                r "Oh, thats too bad. Maybe you had a different favorite episode?"
                r "You could tell one of the other hosts"
                menu:
                    "Yea, that sounds alright":
                        jump noshy
                    "No. This is lame":
                        jump losershy

        label leondateshy:
            hide ood
            hide sage
            hide richard
            show leon blush at center with dissolve
            l "Really? My episode?"
            show leon happy
            l "I knew you were into space just like me!"
            show leon emb
            l "Say... would you maybe want to talk more about tech shit with me?"
            l "Maybe somewhere with just the two of us?"
            menu:
                "Yes! i'd love to!":
                    jump leondate
                "Nah, i'm not really interested":
                    jump leonnoshy
            label leonnoshy:
                show leon sad at center with dissolve
                l "Oh, thats too bad. Maybe you had a different favorite episode?"
                l "You could tell one of the other hosts"
                menu:
                    "Yea, that sounds alright":
                        jump noshy
                    "No. This is lame":
                        jump losershy



label recordingloud:
    $ ood_points = ood_points + 1
    $ sage_points = sage_points + 1

    o "Cool! Have a seat there, and speak right into the mic."
    pause 1.0
    o "So whose episode do you want to guest on?"
    o "I'm talking about a paranormal mystery"
    hide ood with dissolve
    show sage at center with dissolve
    s "I've got another serial killer"
    hide sage with dissolve
    show richard at center with dissolve
    r "There was a hacking event that I'll be talking about"
    hide richard with dissolve
    show leon at center with dissolve
    l "And I am continuing my topic of space flight missions"
    hide leon with dissolve
    pause 1
label noloud:
    p "I think I'll go with..."
    menu:
        "Ood. I love a mystery.":
            jump ooddateloud
        "Sage. I am facinated by serial killers":
            jump sagedateloud
        "Richard. Tech stuff is so interesting!":
            jump richarddateloud
        "Leon. Space is Great!":
            jump leondateloud

    label ooddateloud:
        "I do love a mystery, and Ood is usually my favorite Host"
        p "I'll be a guest on Ood's episode!"
        hide sage
        hide leon
        hide richard
        show ood at right with dissolve
        "Not only do you listen intently to Ood's episode,"
        "you get to chime in!"
        show ood happy
        "When you add little jokes, and good points, Ood's smile gets bigger and bigger as he speaks"
        "You think you can actually hear it in the recording."
        pause 3
        show ood
        o "... and thats where this story leaves off."
        o "It's not solved yet, but who knows what the future holds."
        o "And thanks to my guest, [playername]!."
        o "Thats it for me. I'm Ood Gallifrey,"
        hide ood with dissolve
        "As the hosts sign off one by one, you almost feel a connection to Ood"
        pause 1
        "It felt good to be on an episode, especially with him"
        show ood at center with dissolve
        o "I think that went really well [playername]!"
        o "You're a natural."
        show ood emb with dissolve
        o "Say [playername], would you want to hang out some time and talk more mystery with me?"
        o "Maybe just with the two of us?"
        menu:
            "Yes! i'd love to!":
                jump ooddate
            "Nah, i'm not really interested":
                jump oodnoloud
        label oodnoloud:
            show ood sad at center with dissolve
            l "Oh, thats too bad. Maybe you would like to record with a different host?"
            l "You could jump in with one of them."
            menu:
                "Yea, that sounds alright":
                    jump noloud
                "No. This is lame":
                    jump loserloud

    label sagedateloud:
        "I do love a story about a serial killer, and Sage is usually my favorite Host"
        p "I'll be a guest on Sage's episode!"
        hide ood
        hide leon
        hide richard
        show sage at right with dissolve
        "Not only do you listen intently to Sage's episode,"
        "you get to chime in!"
        show sage happy
        "When you add little jokes, and good points, Sage's smile gets bigger and bigger as she speaks"
        "You think you can actually hear it in the recording."
        pause 3
        show sage
        s "... and thats Seri Al. Crazy? Maybe. A killer? Definately"
        s "He is behind bars for now, but parole happens."
        s "Oh, and thanks to my guest, [playername]!."
        s "Thats it for me. I'm Sage Murray,"
        hide sage with dissolve
        "As the hosts sign off one by one, you almost feel a connection to Sage"
        pause 1
        "It felt good to be on an episode, especially with her"
        show sage at center with dissolve
        s "I think that went really well [playername]!"
        s "You're a natural."
        show sage emb with dissolve
        s "Say [playername], would you want to hang out some time and talk more killer stuff with me?"
        s "Maybe just with the two of us?"
        menu:
            "Yes! i'd love to!":
                jump sagedate
            "Nah, i'm not really interested":
                jump sagenoloud
        label sagenoloud:
            show sage sad at center with dissolve
            s "Oh, thats too bad. Maybe you would like to record with a different host?"
            s "You could jump in with one of them."
            menu:
                "Yea, that sounds alright":
                    jump noloud
                "No. This is lame":
                    jump loserloud


    label richarddateloud:
        "I do love a good hacker story, and Richard is usually my favorite Host"
        p "I'll be a guest on Richard's episode!"
        hide sage
        hide leon
        hide ood
        show richard at right with dissolve
        "Not only do you listen intently to Richard's episode,"
        "you get to chime in!"
        show richard happy
        "When you add little jokes, and good points, Richard's smile gets bigger and bigger as he speaks"
        "You think you can actually hear it in the recording."
        pause 3
        show richard
        r "... and thats how one man hacked the Pentagon, White house, and American Airlines all at once."
        r "We have his username, but no idea who he is. If he IS a he..."
        r "But for now, thats where we will leave it."
        r "Big thanks to my guest, [playername]!."
        r "Thats it for me. I'm Richard Bigly,"
        hide richard with dissolve
        "As the hosts sign off one by one, you almost feel a connection to Richard"
        pause 1
        "It felt good to be on an episode, especially with him"
        show richard at center with dissolve
        r "I think that went really well [playername]!"
        r "You're a natural."
        show richard emb with dissolve
        r "Say [playername], would you want to hang out some time and talk more techie things with me?"
        r "Maybe just with the two of us?"
        menu:
            "Yes! i'd love to!":
                jump richarddate
            "Nah, i'm not really interested":
                jump richardnoloud
        label richardnoloud:
            show richard sad at center with dissolve
            r "Oh, thats too bad. Maybe you would like to record with a different host?"
            r "You could jump in with one of them."
            menu:
                "Yea, that sounds alright":
                    jump noloud
                "No. This is lame":
                    jump loserloud



    label leondateloud:
        "I do love a space story, and Leon is usually my favorite Host"
        p "I'll be a guest on Leon's episode!"
        hide sage
        hide richard
        hide ood
        show leon at right with dissolve
        "Not only do you listen intently to Leon's episode,"
        "you get to chime in!"
        show leon happy
        "When you add little jokes, and good points, Leon's smile gets bigger and bigger as he speaks"
        "You think you can actually hear it in the recording."
        pause 3
        show leon
        l "... and thats how a few brave people stopped the worst space accident in its tracks!"
        l "We did it this time, but how long will it last?"
        l "But for now, thats where we will leave it."
        l "Big thanks to my guest, [playername]!."
        l "Thats it for me. I'm Leon Filger,"
        hide leon with dissolve
        "As the hosts sign off one by one, you almost feel a connection to Richard"
        pause 1
        "It felt good to be on an episode, especially with him"
        show leon at center with dissolve
        l "I think that went really well [playername]!"
        l "You're a natural."
        show leon emb with dissolve
        l "Say [playername], would you want to hang out some time and talk more techie things with me?"
        l "Maybe just with the two of us?"
        menu:
            "Yes! i'd love to!":
                jump leondate
            "Nah, i'm not really interested":
                jump leonnoloud
        label leonnoloud:
            show leon sad at center with dissolve
            r "Oh, thats too bad. Maybe you would like to record with a different host?"
            r "You could jump in with one of them."
            menu:
                "Yea, that sounds alright":
                    jump noloud
                "No. This is lame":
                    jump loserloud

label losershy:
    scene bg blank
    "Well, this is awkward."
    "I guess you dont want to date the hosts?"
    "Maybe try a different game then"
    pause 1
    "Last chance. Wanna try again?"
    menu:
        "{i}sigh{/i} fine, ok":
            jump noshy
        "nope":
            jump loser

label loserloud:
    scene bg blank
    "Well, this is awkward."
    "I guess you dont want to date the hosts?"
    "Maybe try a different game then"
    pause 1
    "Last chance. Wanna try again?"
    menu:
        "{i}sigh{/i} fine, ok.":
            jump noloud
        "nope":
            jump loser

label loser:
    "Well screw you too then buddy"
    "I'm telling the hosts."
    show bird at truecenter
    "Bugger off then"
    pause 3
    "I still love you <3"
    jump credits

label credits:
    $ credits_speed = 25 #scrolling speed in seconds
    scene bg blank #replace this with a fancy background
    with dissolve
    show theend:
        yanchor 0.5 ypos 0.5
        xanchor 0.5 xpos 0.5
    with dissolve
    with Pause(1)
    hide theend
    show cred at Move((0.5, 5.0), (0.5, 0.0), credits_speed, repeat=False, bounce=False, xanchor="center", yanchor="bottom")
    with Pause(credits_speed)
    show thanks:
        yanchor 0.5 ypos 0.5
        xanchor 0.5 xpos 0.5
    with dissolve
    with Pause(2)
    hide thanks
    return

init python:
    credits = ('Backgrounds', 'SgtSquishy'), ('Sprites and CG', 'SgtSquishy'), ('Writing', 'Arthur Talis'), ('Programming', 'Arthur Talis'), ('Music', 'by Kevin MacLeod\n'), ('Music', 'Song Title 1 \n by Kevin MacLeod (incompetech.com) \n Licensed under the Creative Commons 3.0: By Attribution license.\n'), ('Music', 'Song Title 2 \n by Kevin MacLeod (incompetech.com) \n Licensed under the Creative Commons 3.0: By Attribution license.\n'), ('Credit scroll code', 'Dafool, and'), ("Credit scroll code", "leon"), ("Credit scroll code", 'from Lemmasoft.renai.us')
    credits_s = "{size=80}Credits\n\n"
    c1 = ''
    for c in credits:
        if not c1==c[0]:
            credits_s += "\n{size=40}" + c[0] + "\n"
        credits_s += "{size=45}" + c[1] + "\n"
        c1=c[0]
    credits_s += "\n{size=40}Built with\n{size=60}" + renpy.version()

init:
#    image cred = Text(credits_s, font="myfont.ttf", text_align=0.5) #use this if you want to use special fonts
    image cred = Text(credits_s, text_align=0.5)
    image theend = Text("{size=80}The end", text_align=0.5)
    image thanks = Text("{size=80}Thanks for Playing!", text_align=0.5)
