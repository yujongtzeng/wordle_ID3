# wordle_ID3

This project implements the ID3 algorithm to suggest the best guesses to play [wordle](https://www.nytimes.com/games/wordle/index.html).

The idea is motivated by the following two vidoes by 3Blue1Brown but the code was written independently:

* [Solving Wordle using information theory](https://www.youtube.com/watch?v=v68zYyaEmEA)
* [Oh, wait, actually the best Wordle opener is not “crane”…](https://www.youtube.com/watch?v=fRed0Xmc2Wg)


## Clarification and Note
The first video by 3Blue1Brown made a mistake in computing the matching patterns if words has repeated letters (for example 'grebe' with 'crane'). 
The second 'e' in 'grebe' shoould not be counted as yellow, it's a black. As a result, the numbers in the first video might be incorrect. 

The entropy in the videos is exactly the information gain in ID3 algorithm, since initially and after filtered we assume each words appears uniformly random. 

A confusing part is the entropy in the first part of the first video is computed by guessable words v.s. guessable words. In the first video it's computed by guessable words v.s. possible answers. Some of the entropy around 5'20" are still incorrect though.

In the test part of this project, I run their code and my code and compare the entropy of each words. All results match. 

## To-do
* other strategy?
* write a game simulator
* write game helper
