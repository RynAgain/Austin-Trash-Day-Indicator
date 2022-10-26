# Austin Trash Day Indicator
 A raspberry pi project that will webscrape the Austin city website for what trash bins go out that week.  Then it will light up with different colors.

## Finished Project

## Dev Log

### 9/24/22
Starting development.  Focusing on the webscraping aspect first.

### 10/5/22
Using Selenium was a more complex than it was worth for this particular task.  Thankfully the youtube algo provided me the perfect video that brought me to a new solution to my problem.  https://youtu.be/DqtlR0y0suo

With the variables easy to obtain, i can now work on the raspberry pi portion of the project!

### 10/6/22
Made a new main file, removing the old one and putting into a a legacy folder.  I want to keep the code for future reference. 

I think i finished the code?  I gotta build the electronics and test it... I'll add photos of all that.


### 10/22/22
#### 1
Small gap in updates.  A few days after my last update, I discovered that the api i was using was unstable after a few days.  Additionally, this project lead to a breakthrough on a very important work project so I switched my focus to that for a bit.  Today I fixed the api error so this project should be fully stable now.

#### 2
Tested it on my Rpi.  It works! now i just have to finish wiring it, adjust the timing and make it fun.  But the functional code is written

#### 3
- need to add an error mode to signal loss of connection. 
- Ordered the parts today. 
- Add e-ink display and an RGB LED ring, I'll map the colors to the outputs.  
- Main body is 3d printed
- servo to lift the lid?
- Delayed the activation of thread 2 by 10 seconds to allow the boolean values to be set by T1.


### 10/26/22

I worked on the LED wiring and code today.  I'll be uploading more on that soon.  But I decided to go with the NeoPixel rings because they have a good Light output and they are easy to program.  Rushing to have this done by my Halloween party.  I think it'll make a great conversation piece, lmao.