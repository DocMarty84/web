---
title: "{{ replace .Name "-" " " | title }}"
date: {{ .Date }}
archives: "{{ dateFormat "2006" now }}"
author: John SMITH
---
