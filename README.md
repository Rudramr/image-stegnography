# Image Steganography using Reversible Logic Gates

## Overview

This project presents a secure image steganography system inspired by **Reversible Logic Gates**, particularly the **Feynman (CNOT) Gate** and concepts related to **Toffoli Gates** and **Quantum Dot Cellular Automata (QCA)**.

Unlike conventional steganography systems that use irreversible logic and consume higher computational energy, this project applies reversible XOR-based embedding logic to achieve:

- Lossless secret image extraction
- Minimal visual distortion
- Improved theoretical energy efficiency
- Future compatibility with nano-scale hardware systems

The project is implemented using Python and demonstrates how reversible computing principles can be integrated into digital image security.

---

## Key Concepts

### Steganography
Steganography is the technique of hiding secret information inside another medium such as an image without revealing the existence of hidden data.

### Reversible Logic
Reversible logic gates preserve information during computation, reducing theoretical energy dissipation according to Landauer’s Principle.

### Feynman Gate (CNOT)
The embedding and extraction process is inspired by the XOR behavior of the Feynman Gate:

- P = A
- Q = A ⊕ B

This reversible mapping allows accurate recovery of hidden data.

### Toffoli Gate Concept
The project also relates to reversible computing architectures such as the Toffoli gate, which plays a major role in quantum and reversible computation systems.

### Quantum Dot Cellular Automata (QCA)
The reversible logic model used in this project is conceptually aligned with QCA-based nano-scale hardware implementation for ultra-low-power secure communication systems.

---

## Features

- Reversible XOR-based image embedding
- Secret image extraction with no logical information loss
- High PSNR and SSIM values
- Low visual distortion
- Grayscale image steganography
- Pixel-level reversible embedding
- QCA-oriented reversible logic approach
- Simple Python implementation

---

## Technologies Used

- Python 3
- NumPy
- Pillow (PIL)
- Matplotlib
- Scikit-Image
- Visual Studio Code

---

## Working Principle

1. Convert cover and secret images into grayscale format.
2. Extract the two most significant bits from the secret image.
3. Embed them into the least significant bits of the cover image using reversible XOR mapping.
4. Generate the stego image.
5. Apply the same reversible logic during extraction to recover the secret image perfectly.

The process mimics the functionality of reversible Feynman gate operations.

---

## Quality Evaluation Metrics

The project evaluates image quality using:

- MSE (Mean Squared Error)
- PSNR (Peak Signal-to-Noise Ratio)
- SSIM (Structural Similarity Index)

High PSNR and SSIM values indicate that the stego image remains visually almost identical to the original cover image.

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
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/Rudramr/image-stegnography.git
```

Move into the project directory:

```bash
cd image-stegnography
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Run the Project

```bash
python new4.py
```

---

## Output

The system generates:

- Stego Image
- Extracted Secret Image
- PSNR, SSIM, and MSE evaluation metrics

The stego image visually appears almost identical to the original image while securely hiding the secret data.

---

## Advantages

- Lossless secret data recovery
- Low computational complexity
- Reduced theoretical power dissipation
- Future compatibility with QCA hardware
- Improved imperceptibility
- Suitable for secure communication systems

---

## Future Scope

- Hardware implementation using QCA
- FPGA/VLSI realization
- Color image steganography
- Encryption integration
- Real-time secure communication systems
- Quantum-inspired reversible security systems

---

## Research Inspiration

This work is inspired by:
- Reversible Computing
- Feynman Gate Logic
- Toffoli Gate Architectures
- Quantum Dot Cellular Automata (QCA)
- Low-power nano-scale computation

---

## Authors

- M RRUDRAMOORTHY

Department of Electronics and Communication Engineering  
RGUKT RK Valley

---

## License

This project is developed for academic and educational purposes.
