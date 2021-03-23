#!/bin/sh
rm -r cached_encodings/
rm -r images/testing/
rm -r images/training/
rm -r videos/testing/
rm -r videos/training/
mkdir cached_encodings/
mkdir images/testing/
mkdir images/training/
mkdir videos/testing/
mkdir videos/training/
cp pass cached_encodings/
cp pass etc/
cp pass images/testing/
cp pass images/training/
cp pass videos/testing/
cp pass videos/training/
