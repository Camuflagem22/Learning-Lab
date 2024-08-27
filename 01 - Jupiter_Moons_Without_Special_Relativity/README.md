# Jupiter Moons Without Special Relativity

This is a program made to show what would happen if Special Relativity didn't apply, and light could speed up or slow down.

This would, of course, have significant consequences in causality, that is, the order by which events happen.


## Basic Description

This program is a demonstration of a hypothetical case where light's speed is added to the speed of an object that is emitting it, therefore being able to speed up or slow down. 

In this example the light is coming from Jupiter's moon Io (let's ignore that moons reflect light, they dont emmit it). In the program's calculations the Jupiter system is spaced from the observer about 1000 time the distance from Earth to Jupiter at oposition.

When Io is on the front half of it's orbit it's depicted as light blue, as on the other half its depicted as dark blue

(insert images here)

There is also some possible flickering that I forgot how I was going to solve, so i'll likely not fix it.

The coolest thing about this project is that at one point i had to draw a variable number of moons, and the way I solved it was by making the program write it's own library and import it midway during execution. So if you see:

**orbits_module.py**
being created out of nowhere, it's part of the program and it needs it to run.


### Youtube Video

Link:    let me upload the video first

## How to Use

Scroll to lines 155 and 157, and comment **ONLY ONE** of them.
* The first line shows the normal orbit of a moon arround jupiter, as you would see it though a telescope
* The second line shows the image of the same motion but in the hypothetical case that light leaves the surface at the speed of light, but has the moon's speed added to it. In other words, depending on the moons motion, light arrives at the viewer with different speeds.

```python
normal_orbit()

orbits_module.draw_relative_moons(window, canvas, Earth_Array_front, Earth_Array_back)
```

Then just run the program with python
