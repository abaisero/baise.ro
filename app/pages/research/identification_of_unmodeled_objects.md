name: research
icon: fa-flask

# Identification of Unmodeled Objects via Relational Descriptions

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
