#    a.113---main.py---Shall we play a game?

#import statements
import turtle as trtl 
import random as rand
import functools

# idea: falling raindrops that click
# you get a score
# steal code from 1.2.2 with the leaderboard
# I have some javascript code we can convert for this
# timer?
# Idea: add different color raindrops that you don't click on
#https://www.khanacademy.org/computer-programming/snow-fall/6097804743835648

# === variables ===
raindrops = []

for i in range(10):
  tmp_turtle = trtl.Turtle()
  tmp_turtle.penup()
  tmp_turtle.size(rand.randint(0.5,3))
  tmp_turtle.speed(rand.randint(0.5,5))
  tmp_turtle.goto(rand.randint(-100,100),rand.randint(-100,100))
    

for i in range(len(raindrop_pos)):
  
# TODO: make raindrop fall
'''
var xPositions = [200];
var yPositions = [0];
var diameter = [10];
var speed = [1];
for(var g=0;g<200;g++){
    diameter.push(random(2,15));
    xPositions.push(random(0,width-10));
    yPositions.push(random(0, height+25));
    speed.push(random(0.5,1));
}
mouseClicked = function(){
    diameter.push(random(2,20));
    xPositions.push(random(0,width-10));
    yPositions.push(random(0, height+25));
    speed.push(random(0.5,1));
    playSound(getSound("rpg/hit-clop"));
};
draw = function() {
    frameRate(90);
  background(87, 160, 211);
   
    for (var i = 0; i < xPositions.length; i++) {
    
        noStroke();
        ellipse(xPositions[i],yPositions[i],diameter[i],diameter[i]);
        yPositions[i] += speed[i];
            if(yPositions[i]>height+25){
                yPositions[i] =-25;
        }
    }
'''
# TODO: make multiple fall + random location
# TODO: make them clickable
# TODO: make them disappear and count when clicked
# TODO: add timer

#Timer turtle
counter =  trtl.Turtle()
counter.penup()
counter.hideturtle()
counter.goto(-150,-150)

# TODO: implement leaderboard code from previous projects
# TODO: Add different colored raindrops
# TODO: add easter eggs 
#/\//\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/[}--<
#where code?