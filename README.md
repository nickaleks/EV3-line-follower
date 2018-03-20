# EV3 Line Follower

This repository contains source code for simple EV3 line follower using PID controller.

## Demo

Video of robot is available at:
https://www.youtube.com/watch?v=kuj4zojKGlo

## Robot Design

Design of a robot follows the standard instructions provided with EV3 set. Changes to design:

1. Added second color sensor

2. Sensors are placed closer to the central axis of the robot

3. Sensors are turned backwards, so they are located closer to vehicle

Second color sensor improves precision of calculations, simplifies error calculation and allows arbitrary placement of a robot.

Placing sensors closer to the body allows for smoother response since there is less difference between robot location of the wheels and sensors.

## Code Design

Code of the robot is quite simple and straightforward. Main loop performs following actions:

1. Read values from sensors and calculate error

2. Apply controller to adjust speeds of the wheels

Speeds are adjusted using simple PID controller.


## Working Process

Initially, robot was intended to have one color sensor. Such design works, however robot must be always placed in the same position relatively to the line. Also error calculations are hard, since we need to approximate value of a sensor between line and the floor, which leads to imprecise results.

Two sensor design allows to place robot more freely and error calculation is simpler.

After robot was done, the part that remained is to tune PID controller. This was done using trial and error approach.

## PID Tuning

Initially proportional coefficient was found, which allows robot to move along straight line and take non-sharp turns without losing stability. After that integral coefficient was found. This coefficient allowed robot to take sharper turns, however stability suffered. To improve stability, derivative coefficient was adjusted so that robot moves more smoothly.

As a result, on a given speed robot moves smoothly and can take rather sharp turns. Of course, if we increase speed, or change sampling time (by introducing arbitrary sleep in the main loop) PID coefficients will have to be adjusted.

If we further increase one of the coefficients, either robot oscillates on straight lines (Pk and Pd), or loses track on turns because of too much of a turn (Pi).
