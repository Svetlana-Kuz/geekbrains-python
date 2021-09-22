from time import sleep
class TrafficLight:
    __color = ['красный', 'жёлтый', 'зелёный']

    def running(self):
        i = 0
        while True:
            j = i % 3
            print('Cветофор переключился на ', TrafficLight.__color[j])
            if j == 0:
                sleep(7)
            elif j == 1:
                sleep(2)
            else:
                sleep(5)
            i += 1


my_trafficlight = TrafficLight()
my_trafficlight.running()