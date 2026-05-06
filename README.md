# Image Steganography using Python

## Overview

This project implements an Image Steganography system using Python.  
It hides a secret image inside a cover image and later extracts the hidden image with minimal visual distortion.

The project demonstrates concepts of:
- Image Processing
- Data Hiding
- Pixel Manipulation
- Security using Steganography

---

## Features

- Hide a secret image inside another image
- Extract hidden image from stego image
- Structural Similarity (SSIM) calculation
- Peak Signal-to-Noise Ratio (PSNR) analysis
- Grayscale image processing
- Simple and beginner-friendly implementation

---

## Technologies Used

- Python 3
- NumPy
- Pillow (PIL)
- scikit-image

---

## Project Structure

```text
image-stegnography/
│
├── new4.py
├── cover1.png
├── secret1.png
├── stego.png
├── extracted.png
├── requirements.txt
├── README.md
└── .gitignore
