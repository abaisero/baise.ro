name: research
icon: fa-flask

# Research

[Publications][pubs]

[pubs]: publications/

### Decoding relational descriptions

Multi-agent cooperative tasks very often feature one specific type of
interaction, in which one agent defines a task via a high-level description of
the goal state, and the other agent performs it.  

The problem of modeling this type of interaction is addresed by developing
a discriminative probabilistic model of the environment features conditioned on
a symbolic relational state $\operatorname{pr}(\phi_E ~|~ \Sigma)$ which we
call Relational Feature Density Model (RFDM).

The model exploits Bayes' theorem and mild independency assumptions to model
the posterior $\operatorname{pr}(\phi_E ~|~ \Sigma)$ as a function of simpler
density models on a) prior features $\operatorname{pr}(\phi_o)$ and b)
posterior features conditioned on a single ground predicate
$\operatorname{pr}(\phi_{\bar\sigma} ~|~ \bar\sigma)$.

Having to model only $\operatorname{pr}(\phi_o)$ and
$\operatorname{pr}(\phi_{\bar\sigma} ~|~ \bar\sigma)$ results in multiple
advantages:

 * Only positive examples are necessary for training, which avoids the
   awkwardness of having to provide negative examples.
 * Each model can be trained independently, because the RFDM model takes care
   of the information propagation and generalizes well to never-seen-before
   combinations of ground predicates in the relational state.
 * Additionally, modeling the required densities as (mixtures of) Gaussians
   results in a particularly efficient computation of the posterior
   distribution parameters.

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
