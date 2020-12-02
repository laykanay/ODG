#this script starts with:
#bg studio
#ood emb at center
#shitnicker

label ooddate:
    show ood happy at bounce, center
    o "Great!"
    show ood happy at bounce, center
    o "Ooh I'm excited!"
    o "Tell you what, lets exchange numbers, and we can meet up again soon, Okay?"
    "You exchange phone numbers with Ood."
    "Is this really happening?"
    o "There. Let's get in touch next weekend!"
    p "Sure! i look forward to it"
    hide ood
    "The rest of the recording night flies by."
    pause 1
    "and before you know it it's done."
    scene bg trans with fade
    "The next few days were a blur."
    "you had to stop yourself from texting right away, but it all worked out."
    "{i}your phone buzzes{/i}"
    "I hope thats him"
    show phone o1 at center with easeinbottom
    pause(1)
    "Yes! I am so in!"
    show phone o2 at center
    pause(3)
    show phone o3 at center
    "This is great! an actual date with my favorite host!"
    hide phone o3
    "Tomorrow can't come fast enough!"
    scene bg blank with fade
    "You spend the next few hours too excited to sleep"
    pause(2)
    "But eventually you do make it to bed"
    pause(2)
    "and eventually you make it to the theatre for 6"
    scene bg movie ext with fade
    "You see a familiar face waving to you"
    show ood at right with dissolve
    o "Hey [playername]! I'm glad you could make it."
    p "Yea! I have been looking forward to it."
    p "So what movie have you been thinking about?"
    o "You can choose. There are three left that are playing before close."
    label oodmoviechoice:
    o "we have..."
    menu:
        "12 Angry Men":
            jump oodmoviefavec
        "Texas Chainsaw Massacre":
            jump oodmoviehatec
        "The Notebook":
            jump oodmovieneutc

    label oodmoviefavec:
        o "Oh, a movie set in a single room eh?"
        o "Are you sure you want that one?"
        menu:
            "Sure!":
                jump oodmoviefave
            "On second thought...":
                jump oodmoviechoice

    label oodmoviehatec:
        o "Oh, a Horror movie eh?"
        o "Are you sure you want that one?"
        menu:
            "Sure!":
                jump oodmoviehate
            "On second thought...":
                jump oodmoviechoice

    label oodmovieneutc:
        o "Oh, a Romcom eh?"
        o "Are you sure you want that one?"
        menu:
            "Sure!":
                jump oodmovieneut
            "On second thought...":
                jump oodmoviechoice

    label oodmoviefave:
        $ ood_points = ood_points + 1

        show ood happy at bounce, right with dissolve
        o "Oh hell yes!"
        o "They actually call them shoebox movies, 'cuz they are all in one spot!"
        "Ood nearly jumped out of his shoes when I said yes"
        "So cute"
        o "Come on [playername]!!"
        p "Coming"
        scene bg blank with dissolve
        "We grab some popcorn, a few drinks, and some snacks"
        cash "That will be 69.42 please"
        o "Never gets cheaper does it"
        scene bg movie with fade
        show ood happy at right with dissolve
        o "Heres some good seats"
        p "Centre of the row, centre of the theatre. Perfect."
        "We get settled in"
        "There aren't too many people in here tonight"
        pause 2
        "It...it feels nice to sit right next to my Ood"
        "What am I thinking?"
        "This is just a friendly fan-host interaction!"
        pause 2
        "Right?"
        show bg movie dark with dissolve
        p "H...Hey Oo.."
        o "shhh! movie is starting"
        "he looks so into this."
        "Ill ask him at dinner"
        pause 3
        "The movie is awesome!"
        "Its a 1957 movie about 12 jurors deliberating over an 18 year old guy"
        "Only 3 whole minutes are shot outside of the jury room"
        "Even better, every time I look over at Ood, his eyes are glued to the screen"
        "I'm glad I picked this one"
        scene bg blank with fade
        "And hour and a half later, and we are out"
        o "Did you see it? When Juror 7 changed his vote!"
        show bg movie ext with fade
        show ood happy at right with dissolve
        o "And then Juror 11..."
        "He goes on like this for a few minutes"
        o "Wow [playername]. Good choice!"
        p "Yea, I really enjoyed it!"
        o "Hoo. Good movie like that really works up an appetite eh?"
        p "Yea, I'm starved!"
        jump oodfoodout

    label oodmoviehate:
        $ ood_points = ood_points - 1

        show ood sad at right with dissolve
        o "I guess if horror is your thing, we can do that.."
        "You see Ood drags his feet a bit as you head in to take your seats."
        scene bg blank with dissolve
        "I grab some popcorn, a drink, and some snacks"
        p "Ood, do you want anything?"
        o "nah, I'll be good"
        cash "That will be 69.42 please"
        p "Haha, Never gets cheaper does it"
        "Ood gives a half hearted smile, but quickly looks toward the theatre"
        scene bg movie with fade
        show ood sad at right with dissolve
        p "Heres some okay seats"
        p "being in the back is ok, but I wish we werent so far from the middle"
        "We get settled in"
        "The theatre is fairly packed tonight"
        pause 2
        "It...it feels nice to sit right next to my Ood"
        "but there is something off"
        "he seems absent minded"
        show bg movie dark with dissolve
        p "H...Hey Oo.."
        o "shhh! Movie is starting"
        p "s..sorry.."
        "I guess it can wait"
        pause 3
        "You don't mind the movie, but Ood looks a little sick.."
        "Its a 1974 movie about a serial killer with a chainsaw"
        "Its pretty gory"
        "A couple times I look over at Ood, and he doesn't look like he is having any fun"
        "maybe I should have picked a different movie."
        scene bg blank with fade
        "And hour and a half later, and we are out"
        o "That was all a little much.."
        show bg movie ext with fade
        show ood sad at right with dissolve
        o "I mean, we talk about this stuff on the podcast, but I don't need to see more."
        "He goes he goes quiet for a moment"
        o "well [playername], i hope you liked it."
        p "Yea, I guess."
        o "I think a little food might pick me up"
        p "Yea, lets try that."
        jump oodfoodout

    label oodmovieneut:
        show ood at right with dissolve
        o "I guess a romcom isn't too bad"
        scene bg blank with dissolve
        "We grab some popcorn, drinks, and some snacks"
        cash "That will be 69.42 please"
        o "Never gets cheaper does it"
        "Ood giggles a little bit, making you crack a smile."
        scene bg movie with fade
        show ood at right with dissolve
        p "Heres some okay seats"
        o "Middle of the theatre, but too bad we are so far off the centre."
        "We get settled in"
        "The theatre is moderately full tonight"
        pause 2
        "It...it feels nice to sit right next to my Ood"
        "No! bad [playername]. Don't think that way."
        "This is just a nice friendly movie with a Podcaster!"
        "I hope he is having a good time"
        show bg movie dark with dissolve
        p "H...Hey Oo.."
        o "shhh! Movie is starting"
        p "Oof. right. Sorry"
        "I guess it can wait"
        pause 3
        "The movie is ok."
        "Its a 2004 movie about Ryan Gosling and Rachel McAdams being pretty."
        "Its a pretty standard Romcom"
        "A couple times I look over at Ood"
        "he looks a little bored, but laughs a few times"
        "This was an okay movie."
        scene bg blank with fade
        "And two hours later, and we are out"
        o "That sure was a movie"
        show bg movie ext with fade
        show ood at right with dissolve
        o "I've seen it a couple times before."
        "He goes he goes quiet for a moment"
        o "well [playername], i hope you liked it."
        p "Yea, its was okay."
        o "About ready for dinner yet?"
        p "Yea, lets do it."
        jump oodfoodout

    label oodfoodout:
    p "Where should we go?"
    o "Ooh. I know a good place. Its right around the corner. Come on!"
    scene bg blank with fade
    "We walk about a half a block, and find ourselves outside a nice little resturaunt."
    scene bg resturaunt with fade
    show ood happy at right
    o "This place has everything!"
    p "Oh good, 'cuz I am ready for everything!"
    "We are greeted at the door by a man in a suit."
    show maitre at center with dissolve
    "The resturaunt looks packed, and the food smells awesome"
    maitre "Bienvenue to zee Tout dans un Seau."
    maitre "'Ow many of you zis evening?"
    o "Just the two of us."
    maitre "Our dining room 'as a deux 'our wait, but we 'ave a space on zee roof."
    maitre "'Ow does zat sound?"
    "Ood looks at me"
    p "That will work just fine."
    maitre "Bon. Please come zis way. {size=-10}{k=+.5}tabarnac.{/k}{/size}"
    scene bg dinner with fade
    show ood at right with dissolve
    o "This place has really big portions, so we will be sharing ours."
    o "What were you thinking of getting?"
    label oodfoodchoice
    menu:
        "Lobster tails with veggies":
            jump ood
