# Snowy Road :snowflake:

## Problem Description
The weather is especially bad this winter in Berland. A heavy snowstorm passed last night over the city of Bertown and covered some road with snow of variable thickness and completely destroyed other roads.

Bertown road network consists of *n*  intersections, connected by bidirectional roads. For each road a municipal weather services reported the thickness of snow covering this road in millimeters.

Gilbert wants to ride an e-bike from his house, located at intersection number *s*, to his work at intersection *t*. He doesn't feel particularly adventurous today, so he would like to avoid the roads with a lot of snow. In particular, he would like to find a route from his house to work such that the maximum amount of snow on a road on this route is minimal. However, since he doesn't want to be terribly late, he also wants to find the shortest among all of these routes.

This is why he is asking you to help him.

## Input

The first line of the input contains four integers:  1≤*n*≤30000, 0≤*m*≤30000,  1≤*s*,*t*≤*n*, which are the number of intersections and the number of intact roads in Bertown, as well as the locations of Gilberts' house and work.

Next *m* lines contain the description of Bertown's road network. Line *i* contains four integers:  1≤a<sub>i</sub>,b<sub>i</sub>≤*n*,1≤*w<sub>i</sub>*, *c<sub>i</sub>* ≤10<sup>9</sup>  where  *a<sub>i</sub>,b<sub>i</sub>* are the road's endpoints,  *w<sub>i</sub>* is the length of the road and  *c<sub>i</sub>*  is the high of snow on the road in millimeters. It is guaranteed that  *a<sub>i</sub> != b<sub>i</sub>*, and any two intersections are connected by at most one road,

## Output

If there is no possible path connecting *s* to *t*, output "Impossible" (case sensitive).

Otherwise output two integers: the minimum value *c* such that there exists a path between *s* and *t* going only on roads with snow height at most *c*, and the minimum length of such path.

If *s=t*, both numbers should be *0*.