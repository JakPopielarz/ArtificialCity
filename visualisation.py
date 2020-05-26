import pygame

# colors
blue, darkblue = (152, 203, 222, 255), (0, 77, 128)
white, black = (255, 255, 255), (0, 0, 0)
grey, darkgrey = (153, 153, 153), (77, 77, 77)
green, yellow, red = (0,255,0,255), (247,184,0, 255), (255,0,0, 255)
darkgreen = (40, 70, 65)


class Visualisation():
    def __init__(self, win, lane, cell_size, clc, zlc, tlc):
        self.win = win
        self.width, self.height = win.get_width(), win.get_height()
        self.lane = lane
        self.px = cell_size
        self.carlane_c = clc
        self.zebralane_c = zlc
        self.tramlane_c = tlc

    'main method used in every iteration to draw intersection and vehicles (including pedestrians)'
    def draw(self, CAR_LANES, PEDESTRIAN_LANES, TRAM_LANES):
        self.win.fill(darkgreen)
        self.__drawIntersection()
        self.drawLights()
        self.__drawLines()
        self.drawVehicles(CAR_LANES, PEDESTRIAN_LANES, TRAM_LANES)

    def drawVehicles(self, CAR_LANES, PEDESTRIAN_LANES, TRAM_LANES):
        for key, lane in CAR_LANES.items():
            self.drawCarOnLane(key, lane.vehicles)

        for key, lane in TRAM_LANES.items():
            self.drawTramOnLane(key, lane.vehicles)

        # for lane in PEDESTRIAN_LANES:
        self.drawPedestrianOnLane()

    'method used for drawing pedestrians on their new position on every lane'
    def drawPedestrianOnLane(self):
        x, y = self.zebralane_c.get(1)
        self.drawPedestrian(x + 0.5 * self.px, y)
        x, y = self.zebralane_c.get(2)
        self.drawPedestrian(x + 0.25 * self.px, y - 0.25 * self.px)
        x, y = self.zebralane_c.get(3)
        self.drawPedestrian(x + 0.5 * self.px, y)
        x, y = self.zebralane_c.get(4)
        self.drawPedestrian(x + 0.25 * self.px, y - 0.25 * self.px)
        x, y = self.zebralane_c.get(5)
        self.drawPedestrian(x - 0.25 * self.px, y + 0.5 * self.px)
        x, y = self.zebralane_c.get(6)
        self.drawPedestrian(x, y)
        x, y = self.zebralane_c.get(7)
        self.drawPedestrian(x - 0.25 * self.px, y + 0.5 * self.px)
        x, y = self.zebralane_c.get(8)
        self.drawPedestrian(x, y)
        x, y = self.zebralane_c.get(9)
        self.drawPedestrian(x - 0.25 * self.px, y + 0.5 * self.px)
        x, y = self.zebralane_c.get(10)
        self.drawPedestrian(x, y)
        x, y = self.zebralane_c.get(11)
        self.drawPedestrian(x - 0.25 * self.px, y + 0.5 * self.px)
        x, y = self.zebralane_c.get(12)
        self.drawPedestrian(x, y)

    'method used for drawing cars on their new position on every lane'
    def drawCarOnLane(self, lane_number, cars):
        if lane_number == 4:
            for car in cars:
                self.drawCar(self.width - car.travelled * self.px - 4 * self.px,
                             self.carlane_c.get(lane_number) + 0.25 * self.lane, 'h', car.size.get("length"),
                             car.size.get("width"))
        elif lane_number == 1:
            for car in cars:
                self.drawCar((self.width - self.lane * 6 - 26 * self.px) / 2 - 4 * self.px - car.travelled * self.px,
                             self.carlane_c.get(lane_number) + 0.25 * self.lane, 'h', car.size.get("length"),
                             car.size.get("width"))
        elif lane_number == 5:
            for car in cars:
                self.drawCar((
                                         self.width - self.lane * 6 - 26 * self.px) / 2 + 6 * self.lane + 26 * self.px + car.travelled * self.px,
                             self.carlane_c.get(lane_number) + 0.25 * self.lane, 'h', car.size.get("length"),
                             car.size.get("width"))
        elif lane_number in [2, 3]:
            for car in cars:
                self.drawCar(car.travelled * self.px, self.carlane_c.get(lane_number) + 0.25 * self.lane, 'h',
                             car.size.get("length"), car.size.get("width"))
        elif lane_number in [6, 7, 8]:
            for car in cars:
                self.drawCar(self.carlane_c.get(lane_number) + 0.25 * self.lane, car.travelled * self.px, 'v',
                             car.size.get("length"), car.size.get("width"))
        elif lane_number in [9, 10, 11]:
            for car in cars:
                self.drawCar(self.carlane_c.get(lane_number) + 0.25 * self.lane,
                             self.height - car.travelled * self.px - 4 * self.px, 'v', car.size.get("length"),
                             car.size.get("width"))

    'method used for drawing pedestrians on their new position on every lane'
    def drawTramOnLane(self, lane_number, cars):
        if lane_number == 1:
            for car in cars:
                self.drawCar(self.width - car.travelled * self.px - 4 * self.px,
                             self.tramlane_c.get(lane_number) + 0.25 * self.lane, 'h', car.size.get("length"),
                             car.size.get("width"))
        else:
            for car in cars:
                self.drawCar(car.travelled * self.px, self.tramlane_c.get(lane_number) + 0.25 * self.lane, 'h',
                             car.size.get("length"), car.size.get("width"))

    'method used for drawing a single car'
    def drawCar(self, x, y, dir, length, width):
        if dir == 'h':
            car = pygame.Surface((length * self.px, width * self.px), pygame.SRCALPHA)
        else:
            car = pygame.Surface((width * self.px, length * self.px), pygame.SRCALPHA)
        car.fill(black)
        self.win.blit(car, (x, y))

    'method used for drawing a single pedestrian'
    def drawPedestrian(self, x, y):
        p = pygame.Surface((0.5 * self.px, 0.5 * self.px), pygame.SRCALPHA)
        p.fill(black)
        self.win.blit(p, (x, y))

    'method used for drawing a single car'
    def drawGrid(self):
        for x in range(self.width // self.px):
            for y in range(self.width // self.px):
                rect = pygame.Rect(x * self.px, y * self.px, self.px, self.px)
                pygame.draw.rect(self.win, black, rect, 1)

    'method used for drawing traffic lights'
    def drawLights(self):
        vertical = pygame.Surface((0.5 * self.px, self.lane), pygame.SRCALPHA)
        horizontal = pygame.Surface((self.lane, 0.5 * self.px), pygame.SRCALPHA)

        # car lanes
        for i in [2,3,4,6,7,8,9,10,11]:
            vertical.fill(green)
            horizontal.fill(green)
            if i in [2, 3]:
                self.win.blit(vertical, (self.carlane_c.get(6) - self.px,self.carlane_c.get(i)))
            if i == 4:
                self.win.blit(vertical, (self.carlane_c.get(11) + self.lane + 0.75 * self.px, self.carlane_c.get(1)))
            if i in [6,7,8]:
                self.win.blit(horizontal, (self.carlane_c.get(i), self.carlane_c.get(1) - self.px))
            if i in [9,10,11]:
                self.win.blit(horizontal, (self.carlane_c.get(i), self.carlane_c.get(3) + 0.75 * self.px))

        # tram lanes
        vertical.fill(red)
        self.win.blit(vertical, (self.carlane_c.get(8) + self.lane + self.px, self.carlane_c.get(1) + self.lane))
        self.win.blit(vertical, (self.carlane_c.get(11) + self.lane + 0.75 * self.px, self.carlane_c.get(1) + self.lane))
        self.win.blit(vertical, (self.carlane_c.get(6) - self.px, self.carlane_c.get(1) + self.lane * 2))
        self.win.blit(vertical, (self.carlane_c.get(9) - self.px, self.carlane_c.get(1) + self.lane * 2))

    'method used for drawing the intersection'
    def __drawIntersection(self):

        # rectangles
        car_lane_v = pygame.Surface((self.lane, self.height), pygame.SRCALPHA)
        car_lane_v.fill(grey)
        car_lane_h = pygame.Surface((self.carlane_c.get(6), self.lane), pygame.SRCALPHA)
        car_lane_h.fill(grey)

        tram_lanes = pygame.Surface((self.width, self.lane), pygame.SRCALPHA)
        tram_lanes.fill(blue)

        zebra_v_long = pygame.Surface((self.lane * 0.5, self.lane * 5), pygame.SRCALPHA)
        zebra_v_short = pygame.Surface((self.lane * 0.5, self.lane * 4), pygame.SRCALPHA)
        zebra_h = pygame.Surface((self.lane * 3, self.lane * 0.5), pygame.SRCALPHA)

        zebra_v_long.fill(white)
        zebra_v_short.fill(white)
        zebra_h.fill(white)

        ' car lanes '
        # horizontal
        for i in range(0, 4):
            self.win.blit(car_lane_h, (0, self.carlane_c.get(1) + i * self.lane))
            self.win.blit(car_lane_h,
                          (self.carlane_c.get(6) + 26 * self.px + 6 * self.lane, self.carlane_c.get(1) + i * self.lane))

        self.win.blit(car_lane_h, (0, self.carlane_c.get(1) + 4 * self.lane))

        # vertical
        for i in range(0, 3):
            self.win.blit(car_lane_v, (self.carlane_c.get(6) + i * self.lane, 0))
            self.win.blit(car_lane_v, (self.carlane_c.get(6) + 26 * self.px + (3 + i) * self.lane, 0))

        ' tram lanes '
        for i in range(0, 2):
            self.win.blit(tram_lanes, (0, self.carlane_c.get(1) + self.lane + i * self.lane))

        ' zebra lanes '
        self.win.blit(zebra_v_long, (self.carlane_c.get(6) - self.lane, self.carlane_c.get(1)))
        self.win.blit(zebra_v_short,
                      (self.carlane_c.get(6) + 6 * self.lane + 26 * self.px + self.lane * 0.5, self.carlane_c.get(1)))
        self.win.blit(zebra_h, (self.carlane_c.get(6), self.carlane_c.get(1) - self.lane))
        self.win.blit(zebra_h, (self.carlane_c.get(6), self.carlane_c.get(1) + 5.5 * self.lane))
        self.win.blit(zebra_h,
                      (self.carlane_c.get(6) + 3 * self.lane + 26 * self.px, self.carlane_c.get(1) - self.lane))
        self.win.blit(zebra_h,
                      (self.carlane_c.get(6) + 3 * self.lane + 26 * self.px, self.carlane_c.get(1) + 4.5 * self.lane))


    def __drawLines(self):
        ' lines '
        for i in range(0, 5):
            pygame.draw.line(self.win, darkgrey, (0, self.carlane_c.get(1) + i * self.lane),
                             (self.carlane_c.get(6), self.carlane_c.get(1) + i * self.lane), 1)
            pygame.draw.line(self.win, darkgrey, ((self.carlane_c.get(6) + 6 * self.lane + 26 * self.px),
                                                  ((self.height - self.lane * 4) / 2 + i * self.lane)),
                             (self.width, ((self.height - self.lane * 4) / 2 + i * self.lane)), 1)

        pygame.draw.line(self.win, darkgrey, (0, self.carlane_c.get(1) + 5 * self.lane),
                         (self.carlane_c.get(6), self.carlane_c.get(1) + 5 * self.lane), 1)

        for i in range(0, 3):
            pygame.draw.line(self.win, darkgrey, (self.carlane_c.get(6) + (i + 1) * self.lane, 0),
                             (self.carlane_c.get(6) + (i + 1) * self.lane, self.height), 1)
            pygame.draw.line(self.win, darkgrey, (self.carlane_c.get(6) + (i + 3) * self.lane + 26 * self.px, 0),
                             (self.carlane_c.get(6) + (i + 3) * self.lane + 26 * self.px, self.height), 1)

        pygame.draw.line(self.win, darkgrey, (self.carlane_c.get(6), 0), (self.carlane_c.get(6), self.carlane_c.get(1)),
                         1)
        pygame.draw.line(self.win, darkgrey, (self.carlane_c.get(6) + 6 * self.lane + 26 * self.px, 0),
                         (self.carlane_c.get(6) + 6 * self.lane + 26 * self.px, self.carlane_c.get(1)), 1)
        pygame.draw.line(self.win, darkgrey, (self.carlane_c.get(6), self.carlane_c.get(1) + 5 * self.lane),
                         (self.carlane_c.get(6), self.height), 1)
        pygame.draw.line(self.win, darkgrey,
                         (self.carlane_c.get(6) + 6 * self.lane + 26 * self.px, self.carlane_c.get(1) + 4 * self.lane),
                         (self.carlane_c.get(6) + 6 * self.lane + 26 * self.px, self.height), 1)

        for i in range(1, 4):
            pygame.draw.line(self.win, darkblue, (0, self.carlane_c.get(1) + i * self.lane),
                             (self.height, self.carlane_c.get(1) + i * self.lane), 1)

        pygame.draw.line(self.win, darkgrey, (0, self.carlane_c.get(3)),
                         (self.carlane_c.get(6) + self.lane, self.carlane_c.get(3)), 1)

        # self.drawGrid()
