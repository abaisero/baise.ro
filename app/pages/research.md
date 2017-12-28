name: research
icon: fas fa-flask

# Research

Full publication list [<span class="icon far fa-file"></span> here][pubs].

[pubs]: /research/publications

---

## CCIS @ Northeastern University (2017&ndash;)

;; <div class="alert alert-info" role="alert">
;;   <strong>Heads up!</strong> I will begin working at Northeastern Uni in the Fall of 2017.
;; </div>

### Active Goal Recognition

<div class="alert alert-info" role="alert">
  <strong>Uh-oh!</strong> This content is currently being updated and will be restored shortly.
</div>

;; ### Policy Search in POMDPs

---

## MLR @ University of Stuttgart (2013&ndash;2017)

;; As a research assistant at the Machine Learning and Robotics (MLR) group,
;; I worked on the following topics:

### Decoding the Geometry out of Relational Descriptions

<img src="/static/img/rfdm.png"
  class="pull-right"
  style="width:66%"/>

Human cooperation very often depends on a specific type of interaction, in
which one agent Alice defines a task via a high-level description of the goal
state, and the other agent Bob interprets the goal state and performs the task.
For this to take place, Alice has to be able to encode her desired geometric
state and compress it into a predicate-based relational description, while Bob
has to be able to take such description and decode it into a belief over the
possible wanted geometric states.

<div class="alert alert-info" role="alert">
  <strong>Uh-oh!</strong> This content is currently being updated and will be restored shortly.
</div>

### Identification of Unmodeled Objects via Relational Descriptions

Successful Human-Robot Interaction (HRI) requires advanced communication
algorithms which are able to parse instances of human language and associate
the symbolic components with perceptual representations of the environment.
The identification problem is one instance where this is required, and is
defined as the problem of correctly identifying an object out of many given
a relational description.

The description problem is alike to a standard classification
problem&mdash;each object representing a separate class&mdash;with the key
difference that the number of classes and their associated semantics are not
predefined, but rather differ in problem instance.  As a further consequence,
the output classes also have features associated with them, e.g.  a mug which
could be the object of identification could have measurable features relative
to its color, shape, or position.

<img src="/static/img/iden.png"
  style="width:100%"/>

To address the description problem, we propose a logistic-regression-like
stochastic model which outputs a likelihood over all objects.  The model
exploits contextual information by weighing the significance of each
description predicate by how much other objects in the scenario exhibit that
same property, which in turn allows the given descriptions to be flexibly given
as long as they focus in one way or another on combinations of properties which
make the referent object distinguishible from the rest of the environment.

<div class="panel panel-default">
  <div class="panel-heading">
    <h4 class="panel-title">Relevant Publications</h4>
  </div>
  <div class="panel-body">
    <ul class="list-unstyled">
      <li>
        <a class="btn btn-link btn-xs" href="/research/publications#2017_baisero_identification">
          <span class="icon fas fa-link"></span> link</a>
        <a class="btn btn-link btn-xs" href="/research/publications/2017_baisero_identification.pdf">
          <span class="icon far fa-file-pdf"></span> pdf</a>
        <a class="btn btn-link btn-xs" href="/research/publications/2017_baisero_identification.mp4">
          <span class="icon fas fa-video"></span> mp4</a>
        &mdash;
        Identification of Unmodeled Objects from Symbolic Descriptions
      </li>
    </ul>
  </div>
</div>

### Temporal Segmentation of Concurrent Asynchronous Manipulations

<img src="/static/img/tseg.png"
  class="pull-right"
  style="width:26em"/>

A general human demonstration of a complex task is typically composed of
a large number of concurrent and asynchronous interactions with the environment
which we call interaction phases.  The success of an autonomous system which
learns from human demonstrations hinges on its ability to semantically parse
such demonstrations and deconstruct them into their atomic components, thus
learning a representation for how and why they are performed.

In this work, we use a conditional random field (CRF) to model and infer
interactions between objects from their joint motions.  The model is applicable
both to hand-object pairs, in order to extract purposeful interactions with the
environment, and to object-object pairs, to extract changes of state in
assembly tasks.

<div class="panel panel-default">
  <div class="panel-heading">
    <h4 class="panel-title">Relevant Publications</h4>
  </div>
  <div class="panel-body">
    <ul class="list-unstyled">
      <li>
        <a class="btn btn-link btn-xs" href="/research/publications#2015_baisero_temporal">
          <span class="icon fas fa-link"></span> link</a>
        <a class="btn btn-link btn-xs" href="/research/publications/2015_baisero_temporal.pdf">
          <span class="icon far fa-file-pdf"></span> pdf</a>
        <a class="btn btn-link btn-xs" href="/research/publications/2015_baisero_temporal.mp4">
          <span class="icon fas fa-video"></span> mp4</a>
        &mdash;
        Temporal Segmentation of Pair-Wise Interaction Phases in Sequential
        Manipulation Demonstrations
      </li>
      <li>
        <a class="btn btn-link btn-xs" href="/research/publications#2015_mollard_robot">
          <span class="icon fas fa-link"></span> link</a>
        <a class="btn btn-link btn-xs" href="/research/publications/2015_mollard_robot.pdf">
          <span class="icon far fa-file-pdf"></span> pdf</a>
        <a class="btn btn-link btn-xs disabled" href="#">
        <del><span class="icon fas fa-video"></span> mp4</del></a>
        &mdash;
        Robot Programming from Demonstration, Feedback and Transfer
      </li>
    </ul>
  </div>
</div>

---

## CVAP @ KTH (2012)

### Kernels for Sequential Structures

<div class="pull-right" style="width:26em">
<img src="/static/img/pathkernel_stretches.png"
  style="width:26em;padding:.5em;"/>
<img src="/static/img/pathkernel_intuition.png"
  class="pull-left"
  style="width:13em;padding:.5em;"/>
<img src="/static/img/pathkernel.png"
  class="pull-right"
  style="width:13em;padding:.5em;"/>
</div>

At the Computer Vision and Active Perception (CVAP) lab, I worked on my MSc
thesis on the topic of kernel functions for sequential data.  The main result
of this research has been the development of a novel and theoretically sound
kernel function&mdash;the Path Kernel&mdash;for discrete and finite sequences
of arbitrary symbols.

Given a lexicon $\Sigma$ and strings $s, t \in \Sigma^+$, the Path Kernel
$k_\texttt{PATH}$ computes a general measure of similarity which is
interpretable in terms of the number of matching substrings, their length and
their location.  $k_\texttt{PATH}$ is agnostic with respect to the nature of
the lexicon, and depends numerically on a freely chosen Symbol Kernel
$k_\Sigma\colon \Sigma\times\Sigma\to\mathbb{R}$ which is valid for the lexicon
$\Sigma$, and through which context and prior knowledge about the application
domain can be embedded.

<div class="panel panel-default">
  <div class="panel-heading">
    <h4 class="panel-title">Relevant Publications</h4>
  </div>
  <div class="panel-body">
    <ul class="list-unstyled">
      <li>
        <a class="btn btn-link btn-xs" href="/research/publications#2012_baisero_encoding">
          <span class="icon fas fa-link"></span> link</a>
        <a class="btn btn-link btn-xs" href="/research/publications/2012_baisero_encoding.pdf">
          <span class="icon far fa-file-pdf"></span> pdf</a>
        <a class="btn btn-link btn-xs disabled" href="#">
          <del><span class="icon fas fa-video"></span> mp4</del></a>
        &mdash;
        Encoding Sequential Structures using Kernels
      </li>
      <li>
        <a class="btn btn-link btn-xs" href="/research/publications#2013_baisero_path">
          <span class="icon fas fa-link"></span> link</a>
        <a class="btn btn-link btn-xs" href="/research/publications/2013_baisero_path.pdf">
          <span class="icon far fa-file-pdf"></span> pdf</a>
        <a class="btn btn-link btn-xs disabled" href="#">
          <del><span class="icon fas fa-video"></span> mp4</del></a>
        &mdash;
        The Path Kernel
      </li>
      <li>
        <a class="btn btn-link btn-xs" href="/research/publications#2015_baisero_family">
          <span class="icon fas fa-link"></span> link</a>
        <a class="btn btn-link btn-xs" href="/research/publications/2015_baisero_family.pdf">
          <span class="icon far fa-file-pdf"></span> pdf</a>
        <a class="btn btn-link btn-xs disabled" href="#">
          <del><span class="icon fas fa-video"></span> mp4</del></a>
        &mdash;
        On a Family of Decomposable Kernels on Sequences
      </li>
      <li>
        <a class="btn btn-link btn-xs" href="/research/publications#2015_baisero_path">
          <span class="icon fas fa-link"></span> link</a>
        <a class="btn btn-link btn-xs" href="/research/publications/2015_baisero_path.pdf"><span class="icon far fa-file-pdf"></span> pdf</a>
        <a class="btn btn-link btn-xs disabled" href="#">
          <del><span class="icon fas fa-video"></span> mp4</del></a>
        &mdash;
        The Path Kernel:  A Novel Kernel for Sequential Data
      </li>
    </ul>
  </div>
</div>


*[CCIS]: College of Computer and Information Science
*[MLR]: Machine Learning and Robotics
*[CVAP]: Computer Vision and Active Perception
*[KTH]: Royal Institute of Technology
