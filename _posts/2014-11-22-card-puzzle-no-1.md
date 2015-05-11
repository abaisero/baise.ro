---
title: Card Puzzle No. 1
description: Find optimal policy and expected value of playing the game.
icon: fa-puzzle-piece
---

Let's play a game[^game]; here are the rules:

* Take a standard shuffled deck of 52 cards, of which 26 are red and 26 black, and initialize the score to zero.
* Every turn, draw a card. Increase the score by one if the card is red, and decrease it otherwise.
* If there are cards left in the deck, you can choose to continue the game and go back to the drawing phase.
* Otherwise, the game ends and you win/lose your score in your local currency.

Given the setup, which is the best policy to play the game? and how much would
you be willing to pay to play it?  I.e. what is the expected value of playing?

The state of the game is described concisely by the number of red and black
cards remaining in the deck, respectively `nred` and `nblack`.  The number of
remaining cards is trivially `ncards = nred + nblack`, while the current score
is obtained as `score = nblack - nred`.

Overall, this problem can be trivially solved using dynamic programming.

can be described by the current score, and the number of
remaining red and black cards in the deck, i.e. `st = (s, nr, nb, n = nr +
nb)`.  Obviously, the value of ending the game at any step is precisely $$Q(st)
= s$$.  On the other hand, the value of continuing the game is $$Q(st) =
\frac{nr}{n} (s+1) + \frac{nb}{n} (s-1) = 1 + \frac{nr -  nb}{n}$$.

***

[LINK](../../Untitled0.html)

<div class="include" url="../../Untitled0.html"></div>

***

### Footnotes

[^game]: This puzzle was taken from [Data Genetics](http://datagenetics.com/blog/october42014/index.html); I read the problem statement and liked enough that I wanted to solve it myself before reading their analysis.
