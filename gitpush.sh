#!/bin/bash

message="weekly ioc-list"

git add .
git commit -m "$message"
git push
git status
