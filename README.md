**Python Security & Cryptography Toolkit**

Author: Alex

Status: In development

Language: Python

Background: 

A  high school student developer from **Mexico** focusing on Pyhton automation
and cybersecurity fundamentals. 


**Overview:**

This repository documents my jounrey into cryptography and software architecture. 
It  was authored on February 2026 for the purpose of learning and experimenting freely. 

Currently the project has:


**Encryption Engines**

**Casear Cipher:** A custom Casear cipher that handles variable shifts. Includes its encryption and a "cracker" that uses brute force as a decryption tool.

**Atbash Cipher:**  Cipher includes custom made alphabet and inverts plain text. Also includes "cracker".

**Feature:** Includes an English language detection algorithm to automatically score potential decryptions.



**Security Tools**

**Password Generator:** Generates passwords with customizable character sets (Upper, Lower, Symbols, Digits).

**Password Strength Checker:** Analyzes password complexity to prevent common vulnerabilities. 



**Architecture**

This project uses a modular design to prevent code repetition:

 `text_utils.py`: Shared library that fullfills 3 objectives

 Acts as the central English word detection file
 
 Handles whitespace tokenization to safely split user input
 
 Stores the master `alphabet` string used across all cipher modules to ensure consistency.


 * **`main.py`:** The central interface for running the tools.

   -----
*Created as part of a personal portfolio. Open for collaboration and feedback.* :)


