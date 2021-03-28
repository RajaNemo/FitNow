import random

while 1:
    areps = ("10", "15", "20", "25", "30", "35")
    areps2 = ("40", "50", "65", "75", "80", "95", "100")
    lreps = ("10", "15", "20", "25", "30", "35")
    lreps2 = ("40", "50", "65", "75", "80", "95", "100")
    breps = ("10", "15", "20", "25", "30", "35")
    breps2 = ("40", "50", "65", "75", "80", "95", "100")
    arms = ("Push ups", "Punches", "Squat+Push up combo")
    legs = ("Squats", "Squat+Sit up combo", "Squat hold", "Squat position punches")
    eabs = ("Situps", "Side leg raises", "Leg raises")
    counter = input("Are you: 1.Total Beginner, 2.Beginner, 3.Intermediate, 4.Advanced, 5.Master, 6.Fitness guru, 7.Goku")
    betweensets = ("Plank", "Jumping jacks", "Punch+Knee+Kick combo", "Knees")




    warm = random.choice(arms)
    wleg = random.choice(legs)
    wabs = random.choice(eabs)
    wpause = random.choice(betweensets)

    if counter == "1":
        l = 10
        r = 20
        s = 1
        arepsize = random.choice(areps)
        lrepsize = random.choice(lreps)
        brepsize = random.choice(breps)
    if counter == "2":
        l = 15
        r = 20
        s = 1
        arepsize = random.choice(areps)
        lrepsize = random.choice(lreps)
        brepsize = random.choice(breps)
    if counter == "3":
        l = 20
        r = 20
        arepsize = random.choice(areps)
        lrepsize = random.choice(lreps)
        brepsize = random.choice(breps)
        s = 2
    if counter == "4":
        l = 35
        r = 15
        arepsize = random.choice(areps)
        lrepsize = random.choice(lreps)
        brepsize = random.choice(breps)
        s = 3
    if counter == "4":
        l = 50
        r = 15
        arepsize = random.choice(areps)
        lrepsize = random.choice(lreps)
        brepsize = random.choice(breps)
        s = 4
    if counter == "5":
        l = 70
        r = 15
        arepsize = random.choice(areps2)
        lrepsize = random.choice(lreps2)
        brepsize = random.choice(breps2)
        s = 7
    if counter == "6":
        l = 90
        r = 10
        arepsize = random.choice(areps2)
        lrepsize = random.choice(lreps2)
        brepsize = random.choice(breps2)
        s = 14
    if counter == "7":
        l = 120
        r = 5
        arepsize = random.choice(areps2)
        lrepsize = random.choice(lreps2)
        brepsize = random.choice(breps2)
        s = 25


    print("You need to do", s , "sets of", arepsize, warm, lrepsize, wleg, brepsize, wabs, l, "seconds of", wpause, "You have", r, "seconds of rest between sets.")


