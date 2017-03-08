name: research
icon: fa-flask

# Temporal Segmentation of Sequential Manipulations

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
