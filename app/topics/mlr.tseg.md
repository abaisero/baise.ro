id: tseg
group: MLR
title: Temporal Segmentation of Concurrent Asynchronous Demonstrations
pubkeys: 2015_baisero_temporal;2015_mollard_robot

<div class="thumbnail pull-right" style="margin-left:1em;">
  <img src="{{ url_for('static', filename='img/tseg.png') }}"
    alt="extracted instruction set for the assembly of a tool box"
    style="width:26em;"
    />
  <div class="caption">
    Sequential instruction set extracted from demonstration.
  </div>
</div>

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
