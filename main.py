# Do not modify these lines
__winc_id__ = '7b9401ad7f544be2a23321292dd61cb6'
__human_name__ = 'arguments'

# Add your code after this line

def greet(name, greeting="Hello, <name>!"):
    return greeting.replace("<name>",name)
    
print(greet("Edwin", "What's up, <name> !"))

planeet = {
    "sun":274,
    "jupiter":24.92,
    "neptune":11.15,
    "saturn":10.4,
    "earth":9.798,
    "uranus":8.87,
    "venus":8.87,
    "mars":3.71,
    "mercury":3.7,
    "moon":1.62,
    "pluto":0.6,
    }
def force(mass, body="earth"):
    random = (planeet[body])
    berekening = mass * random
    return round(berekening,1)
    
print(force(12,"venus"))

def pull(m1,m2, d):
    G = 6.674*10**-11
    force = (G*(m1*m2)/d**2)
    return force

print(round(pull(800,1500,3),10))