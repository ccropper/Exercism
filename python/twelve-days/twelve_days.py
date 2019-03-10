DAYS = {
    1: "first",
    2: "second",
    3: "third",
    4: "fourth",
    5: "fifth",
    6: "sixth",
    7: "seventh",
    8: "eighth",
    9: "ninth",
    10: "tenth",
    11: "eleventh",
    12: "twelfth"
    }

GIFT_LYRICS = {
    1: "a Partridge in a Pear Tree.",
    2: "two Turtle Doves, ",
    3: "three French Hens, ",
    4: "four Calling Birds, ",
    5: "five Gold Rings, ",
    6: "six Geese-a-Laying, ",
    7: "seven Swans-a-Swimming, ",
    8: "eight Maids-a-Milking, ",
    9: "nine Ladies Dancing, ",
    10: "ten Lords-a-Leaping, ",
    11: "eleven Pipers Piping, ",
    12: "twelve Drummers Drumming, "
}


def generate_date_lyrics(day):
    return f"On the {DAYS[day]} day of Christmas my true love gave to me: "

def generate_gift_lyrics(day):
    gift_lyrics = ""
    for line in range(1, day + 1):
        if line == 1 and day != 1:
            gift_lyrics = "and " + GIFT_LYRICS[line] + gift_lyrics
        else: 
            gift_lyrics = GIFT_LYRICS[line] + gift_lyrics
    return gift_lyrics

def recite(start_verse, end_verse):
    requested_lyrics = []
    for day in range(start_verse, end_verse + 1):
        requested_lyrics.append(generate_date_lyrics(day) + generate_gift_lyrics(day))
    return requested_lyrics