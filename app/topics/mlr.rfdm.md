id: rfdm
group: MLR
title: Decoding the Geometry out of Relational Descriptions of the Environment

Human cooperation very often depends on a specific type of interaction, in
which one agent Alice defines a task via a high-level description of the goal
state, and the other agent Bob interprets the goal state and performs the task.
For this to take place, Alice has to be able to encode her desired geometric
state and compress it into a predicate-based relational description, while Bob
has to be able to take such description and decode it into a belief over the
possible wanted geometric states.

<div class="thumbnail">
  <img src="{{ url_for('static', filename='img/rfdm.png') }}"
    alt="application of relational feature density model to a room domain"
    />
  <div class="caption">
    The relational description of a scene is converted into a joint
    distribution of object geometric properties (position, size, etc).
  </div>
</div>
