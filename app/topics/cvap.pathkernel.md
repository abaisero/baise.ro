id: pathkernel
group: CVAP
title: Implicit Feature Space Embeddings for Sequential Structures
pubkeys: 2012_baisero_encoding;2013_baisero_path;2015_baisero_family;2015_baisero_path

<div class="thumbnail pull-right" style="margin-left:1em;">
  <div>
  <img src="{{ url_for('static', filename='img/pathkernel_intuition.png') }}"
    alt="binary path matrix denoting similarity at character level"
    style="width:13em;margin:.5em;"
    />
  <img src="{{ url_for('static', filename='img/pathkernel.png') }}"
    alt="selected paths overlapped on the path matrix"
    style="width:13em;margin:.5em;"
    />
  <br/>
  <img src="{{ url_for('static', filename='img/pathkernel_stretches.png') }}"
    alt="stretches corresponding to selected paths"
    style="width:27em;margin:.5em;"
    />
  </div>
  <div class="caption">
    Similarity encoded by combinations of matching stretches.
  </div>
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
