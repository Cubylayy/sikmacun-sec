#!/bin/bash

message="ioc list upload"

git add .
git commit -m "$message"
git push
git status
