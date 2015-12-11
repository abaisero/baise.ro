---
title: weblog
icon: fa-book
---

# Weblog

This page is under development. The current posts are all tests.

{:.list-group}{% for post in site.posts %}
 * {:.list-group-item}
    {:.remove}
    <small>**{{ post.date | date: "%d %b %Y" }}**</small>
    <i class="fa {{ post.icon }} fa-fw"></i>
    [{{ post.title }}]({{ site.url}}{{post.url }})
    <small>~ {{ post.description }}</small>
{% endfor %}

