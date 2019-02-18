def raindrops(number):
    randrops_dict = {
    3: 'Pling',
    5: 'Plang',
    7: 'Plong',
    }
    raindrops = []
    for factor, sound in randrops_dict.items():
        if number % factor == 0:
            raindrops.append(sound)
    if len(raindrops) == 0:
        raindrops.append(str(number))
    return "".join(sound for sound in raindrops)