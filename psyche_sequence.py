# This is a PSYCHE pulse seq file
# Constants
cnst20 = 10  # Desired flip angle for PSYCHE pulse element (degree)
cnst21 = 10000  # Bandwidth of each chirp in PSYCHE pulse element (Hz)
cnst4 = 1  # Number of drop points (example value, set appropriately)

# Define delays (in seconds)
tauA = None  # Placeholder, to be calculated
tauB = None  # Placeholder, to be calculated

# Input parameters (example values, replace with actual parameters)
in0 = 1 / (2 * 5000)  # Example sampling frequency of 5000 Hz
p1 = 1e-6  # Duration of high power pulse (in seconds)
p2 = 2 * p1
p10 = 1e-3  # Duration of weak gradient during PSYCHE pulse element
p16 = 1e-3  # Duration of CTP gradients (1 ms)
p40 = 1e-3  # Duration of double-chirp PSYCHE pulse element
d16 = 1e-6  # Recovery delay for gradients (1 µs)

# Calculate tauA and tauB
tauA = in0 / 2 - p16 - d16 - 50e-6  # Convert 50µs to seconds
tauB = (1 / (2 * cnst4)) + d16 + 50e-6

# Calculate RF amplitude of double-chirp PSYCHE pulse element
cnst50 = (cnst20 / 360) * ((2 * cnst21) / (p40 * 1e-6)) ** 0.5  # Adjusted for seconds
p30 = 1000000.0 / (cnst50 * 4)  # RF pulse duration (µs)
cnst31 = (p30 / p1) ** 2
spw40 = 1e-6 / cnst31  # RF power of double-chirp PSYCHE pulse element (in seconds)

# Phase settings
ph1 = [0, 0, 0, 0, 0, 0, 0, 0]
ph2 = [0, 0, 2, 2, 0, 0, 2, 2]
ph3 = [0, 1, 0, 1, 2, 3, 2, 3]
ph31 = [0, 2, 0, 2, 0, 2, 0, 2]

# Experimental sequence (simplified)
def psyc_sequence():
    print("Begin PSYCHE Sequence")
    
    # Step 1: Delay
    print(f"Delay: {d16}")
    
    # Step 2: High power pulse
    print(f"High Power Pulse (p1): {p1}s with phase {ph1}")
    
    # Step 3: Delays and gradient application
    print(f"Delay: {tauA}")
    print("Apply 50us UNBLKGRAD")
    print(f"Gradient (gp1): {p16}s")
    
    # Step 4: Second high power pulse
    print(f"Second High Power Pulse (p2): {p2}s with phase {ph2}")
    
    # Continue the sequence...
    print(f"Final delays and gradients with phase {ph31}")

# Execute the sequence
psyc_sequence()
