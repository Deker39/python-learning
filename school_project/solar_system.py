import turtle
import random
import math

t = turtle.Pen()

turtle.title("My Solar System")
turtle.Screen().bgcolor("black")

solar_system = {"Sun": 30,"Mercury":4.87,"Venus":12.10,
                "Earth":12.72,"Mars":6.77,"Jupiter":139.82,
                "Saturn":116.46,"Uranus":50.72,"Neptune":49.24}

# solar_system_1 = [30,4.87,12.10,12.72,6.77,139.82,116.46,50.72,49.24]

solar_system_distance= [0,20,36,50,76,150,269,400,475,0]
solar_system_colors= ["#ffcc00","#8585ad","#ff6600","#6699ff",
                      "#804000","#ff9933","#ff9966","#ff8000",
                      "#1a53ff"]
# for x in solar_system:
#     print("{0} - {1}".format(x,solar_system[x]))

turtle.pencolor("yellow")

i = 0

for x in solar_system:
    r = solar_system_distance[i+1]
    rand = random.randrange(0,360)
    kek1 = int(r*math.cos(rand))
    #x = r*cos()
    #y = r*sin()
    kek2 = int(r*math.sin(rand))
    print(kek1,kek2)

    coordinates = (solar_system_distance[i],0)
    turtle.dot(solar_system[x],str(solar_system_colors[i]))
    turtle.goto(coordinates)
    i += 1
    turtle.up()
    turtle.goto(0, (solar_system_distance[i]*(-1)))
    turtle.down()
    turtle.circle(solar_system_distance[i])
    turtle.up()
    # turtle.goto(solar_system_distance[i],0)
    turtle.goto(kek1,kek2)


turtle.mainloop()




