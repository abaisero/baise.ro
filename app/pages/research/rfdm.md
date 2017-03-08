name: research
icon: fa-flask

# Decoding Relational Descriptions

Page temporarily unavailable.

; Human cooperation very often features a specific type of interaction, in which
; one agent Alice defines a task via a high-level description of the goal state,
; and the other agent Bob interprets the goal state and performs the task.  For
; this to take place, Alice has to be able to encode her desired geometric state
; and compress it into a predicate-based relational description, while Bob has to
; be able to take such description and decode it into a belief over the possible
; wanted geometric states.  We will focus on modeling this decoding process.

; Let us start by defining some notation:

; Environment $E$

; : A list of objects which exists in the current domain, e.g. Hammer,
; Hand1, Nail, Piece, etc.

; Lexicon $\Lambda = \{\sigma_i\}_i$

; : A list of labels shared by the agents, e.g. SMALL, RED, UNDER, ON, etc.

; Description / Relational State $\Sigma = \{\bar\sigma_i\}_i$

; : this is ok

; Geometry $\phi_E$

; : , e.g. $\left(\phi_\text{Hammer}^\top\right)^\top$


; ### The Inversion Problem

; We call this decoding problem the _inversion problem_ due to the fact that it
; is the opposite


; The problem of modeling this type of interaction is addresed by developing
; a discriminative probabilistic model of the environment features conditioned on
; a symbolic relational state $\operatorname{pr}(\phi_E ~|~ \Sigma)$ which we
; call Relational Feature Density Model (RFDM).

; The model exploits Bayes' theorem and mild independency assumptions to model
; the posterior $\operatorname{pr}(\phi_E ~|~ \Sigma)$ as a function of simpler
; density models on a) prior features $\operatorname{pr}(\phi_o)$ and b)
; posterior features conditioned on a single ground predicate
; $\operatorname{pr}(\phi_{\bar\sigma} ~|~ \bar\sigma)$.

; Having to model only $\operatorname{pr}(\phi_o)$ and
; $\operatorname{pr}(\phi_{\bar\sigma} ~|~ \bar\sigma)$ results in multiple
; advantages:

;  * Only positive examples are necessary for training, which avoids the
;    awkwardness of having to provide negative examples.
;  * Each model can be trained independently, because the RFDM model takes care
;    of the information propagation and generalizes well to never-seen-before
;    combinations of ground predicates in the relational state.
;  * Additionally, modeling the required densities as (mixtures of) Gaussians
;    results in a particularly efficient computation of the posterior
;    distribution parameters.

