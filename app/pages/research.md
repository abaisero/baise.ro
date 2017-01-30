name: research
icon: fa-flask

# Research

[Publications][pubs]

[pubs]: publications/

### Decoding relational descriptions

This work focuses on a very common type of interaction which arises in
cooperative multi-agent tasks, where one agent defines a task via a relational
description of a goal state, and another one performs it such that the goal
state is satisfied.

### Identification of unmodeled objects

Successful human-robot interaction hinges on the autonomous system’s ability to
understand abstract concepts and properties, and to ground them into its
perceptual representations of the environment.

In this work I tackle the identification problem, which is here defined as that
of mapping a description to a single object out of a set of candidates. This
differs from standard classification w.r.t. a few key aspects:  a) The number
of classes and their associated semantics are not predefined, but rather change
according to the environment;  b) there is no similar notion of an explicit
vector of input features; and  c) the output classes (i.e.  the objects
themselves) have features associated with them.

I developed a stochastic logistic-regression-like model which addresses the
identification problem, and is thus able to identify previously unseen objects
given context-dependent predicate-based descriptions. The model exploits
contextual information in that the sig- nificance of each description predicate
depends on how much other objects in the scenario exhibit that same property.
This allows the descriptions to be flexibly given, and to focus on combinations
of properties which make the referent object unique in its environment.

### Temporal segmentation of sequential manipulation

; I defined a motion-based graphical model which temporally segments human
; demonstrations into the fundamental interaction sequences which concurrently
; manifest between hand-object and object-object pairs.

; The temporal segmentation can be used to autonomously break a complex
; demonstration into its atomic components, and is also used on assembly
; demonstrations to extract a set of transferrable instructions which abstract
; the performed assembly task.



The goal of this work is to deconstruct a concurrent and sequential
manipulation demon- stration into the multiple atomic interaction phases which
arise and fall between the human and the environment. An interaction phase is
here defined as a sequence of latent binary variables which indicate whether
one of the two bodies is actuating the other.  The models define a distribution
on binary interaction sequences conditional to observations of the motion
profiles. In my model, the observation features are based on correlation and
variance measures of the bodies’ motions.


A single demonstration, especially when events happen concurrently, results in
multiple parallel temporal segmentations which represent an abstraction of the
task and how it is performed. The same model is also used to analyze
object-object interactions and, in the particular case of assembly
demonstrations, extracts a transferable representation of the assembly
instructions as demonstrated by the human.

; ### A novel path-based kernel function for sequential data

; TODO
