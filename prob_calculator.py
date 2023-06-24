from random import randint
import copy

class Hat:
    
    def __init__(self, **kwargs):
        self.contents = []
        for (key, value) in kwargs.items():
            for i in range(value):
                self.contents.append(key)

    def draw(self, num_balls):
        self.num_balls = num_balls
        self.drawn_balls = []
        num_balls_left = len(self.contents)
        if self.num_balls > num_balls_left:
            return self.contents
        else:
            for draw in range(self.num_balls):
                self.drawn_balls.append(self.contents.pop(randint(0, (num_balls_left - 1))))
                num_balls_left -= 1
            return self.drawn_balls
        
def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    probability = 0
    matches = 0
    
    hat_results_list = []
    for experiment in range(num_experiments):
        hat_copy = hat.contents.copy()
        hat_results_list.append(hat.draw(num_balls_drawn))
        hat.contents = hat_copy
    hat_results_dicts = []    
    for draw in hat_results_list:
        dict = {}
        for item in draw:
            dict[item] = dict.get(item, 0) + 1
        hat_results_dicts.append(dict)

    def draw_checker(draw, expected_balls):
        for ball in expected_balls:
            if ball not in draw:
                return False
        for ball in expected_balls:
            if expected_balls[ball] > draw[ball]:
                return False
            else:
                continue
        return True

    for draw in hat_results_dicts:
        if draw_checker(draw, expected_balls):
            matches += 1

    #print(hat_results_list)
    #print(hat_results_dicts)
    #print(expected_balls)
    #print(matches)


    return matches / num_experiments * 100       

                
            
            
                
                
        


    


hat1 = Hat(red=2, blue=1, purple=6)
#print(hat1.contents)
#print(hat1.draw(3))   
print(experiment(hat1, {'blue':1, 'purple':2}, 3, 2000))  