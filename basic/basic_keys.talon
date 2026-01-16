# Phonetic alphabet
{user.alphabet}: insert(alphabet)
big {user.alphabet}: insert(user.upper(alphabet))
all caps {user.alphabet}+: insert(user.upper(user.cat(alphabet_list)))

# Numbers and punctuation
(numb | number) <user.digits>: insert(digits)
{user.punctuation}: key(punctuation)
{user.punctuation_long}: key(punctuation_long)
long {user.punctuation_long}: key("space {punctuation_long} space")

# Simple keys
ace: key(space)
cutter: key(ctrl-x)
eskimo: key(escape)
ski: key(escape)
shackle: key(home shift-end)
select all: key(ctrl-a)
select every: key(ctrl-a)
finder: key(ctrl-f)
[and] save$: edit.save()
spark: edit.paste()
stoosh: edit.copy()
hug curly: key({)
hug brax: key([)
# Simple keys with repeat
(tabby | taboo) [<user.n20>]: key("tab:{n20 or 1}")
(tabby | taboo) lease [<user.n20>]: key("shift-tab:{n20 or 1}")
shock [<user.n20>]: key("enter:{n20 or 1}")
(clear | clearing) [<user.n20>]: key("backspace:{n20 or 1}")
deli [<user.n20>]: key("delete:{n20 or 1}")
page up [<user.n20>]: key("pgup:{n20 or 1}")
page down [<user.n20>]: key("pgdown:{n20 or 1}")
space [<user.n20>]: key("space:{n20 or 1}")
redo [<user.n20>]: key("ctrl-y:{n20 or 1}")
zoom in [<user.n20>]: key("ctrl-=:{n20 or 1}")
zoom out [<user.n20>]: key("ctrl--:{n20 or 1}")
^undo [<user.r20>]$:
    edit.undo()
    repeat(r20 or 0)
check [<user.r20>]:
    edit.line_insert_down()
    repeat(r20 or 0)
duple [<user.r20>]:
    edit.line_clone()
    repeat(r20 or 0)
splat [<user.r20>]:
    edit.delete_word()
    repeat(r20 or 0)
splat ross [<user.r20>]:
    user.delete_word_right()
    repeat(r20 or 0)


# Directions
{user.direction_modifiers} [<user.n20>]: key("{direction_modifiers}left:{n20 or 1}")
[{user.direction_modifiers}] {user.directions} [<user.n20>]:
    key("{direction_modifiers or ''}{directions}:{n20 or 1}")
[{user.direction_modifiers}] {user.directions_extreme} wally:
    key("{direction_modifiers or ''}{directions_extreme}")


# Text
phrase <phrase> [over]:
    insert(user.formatted_text(phrase, 7, 0))
(say | so) <phrase>$:
    insert(user.formatted_text(phrase, 7, 0))
sigma <phrase>$:
    insert(user.formatted_text(phrase, 4, 0))
({user.capitalisation} {user.spacing} | {user.capitalisation} | {user.spacing}) bow <phrase>:
    insert(user.formatted_text(phrase, capitalisation or 0, spacing or 0))
({user.capitalisation} {user.spacing} | {user.capitalisation} | {user.spacing}) burner <phrase>$:
    insert(user.formatted_text(phrase, capitalisation or 0, spacing or 0))

repeat last [<user.n20>]:
    core.repeat_phrase(n20)

{user.personal}: insert(personal)

and sleep$: user.dragon_mimic("go to sleep")
