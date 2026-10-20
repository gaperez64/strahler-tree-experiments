#!/bin/sh
# Keep source copies from inheriting an enclosing checkout's version.
GIT_CEILING_DIRECTORIES=$(dirname "$1")
export GIT_CEILING_DIRECTORIES
exec git -C "$1" describe --tags --always --dirty
