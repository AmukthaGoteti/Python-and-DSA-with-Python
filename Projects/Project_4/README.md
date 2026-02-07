# Sampling and Aliasing Demonstration (Python)

This project demonstrates the effects of different sampling rates on a composite analog signal and visualizes how aliasing occurs when sampling below the Nyquist rate. It includes user-driven parameter selection, time-domain and frequency-domain plotting, and an automated aliasing analysis.

---

## 📚 **Overview**

Sampling is the process of converting a continuous-time signal into discrete samples. When sampling signals that contain high-frequency components, aliasing can occur if the sampling frequency is insufficient.

This tool helps you explore:

* Composite analog signal generation
* Sampling at different rates (below, at, and above Nyquist)
* FFT-based frequency spectrum analysis
* Aliasing behavior and implications
* Practical decision-making for sampling systems

---

## 🧠 **Technical Concepts**

### **Composite Signal**

A signal of the form:

```
x(t) = a₁·sin(2πf₁t) + a₂·sin(2πf₂t)
```

### **Nyquist Theorem**

To avoid aliasing:

```
f_s ≥ 2·f_max
```

where `f_max` is the highest signal frequency.

### **Aliasing**

If `f > f_s/2`, the aliased frequency is approximately:

```
f_alias = |f - round(f/f_s)·f_s|
```

Aliased frequencies appear as lower-frequency artifacts in the spectrum, corrupting reconstruction.

---

## 🏗️ **Project Structure**

The script contains five major components:

| Component                     | Description                                                                |
| ----------------------------- | -------------------------------------------------------------------------- |
| `get_user_inputs()`           | Collects frequency, amplitude, duration, and sampling rates interactively. |
| `generate_composite_signal()` | Builds the time-domain composite signal.                                   |
| `compute_fft()`               | Computes FFT magnitude spectrum for sampled signals.                       |
| `plot_results()`              | Visualizes time and frequency domains for each sampling scenario.          |
| `analyze_aliasing()`          | Prints observations and aliasing outcomes.                                 |

---

## 🚀 **How to Run**

### **Requirements**

Install dependencies:

```bash
pip install numpy matplotlib scipy
```

### **Execute the Script**

```bash
python your_script_name.py
```

During execution, you will be prompted to enter:

* Two signal frequencies (`f1`, `f2`)
* Amplitudes (`a1`, `a2`)
* Signal duration
* Sampling rates (below, at, and above Nyquist)

Defaults are provided for all values, so pressing **Enter** accepts defaults.

---

## 🎛️ **User Inputs**

Example prompts:

```
Enter first frequency (Hz): 5
Enter second frequency (Hz): 15
Enter first signal amplitude: 1
Enter second signal amplitude: 0.5
Enter signal duration (seconds): 1

Enter sampling rate BELOW Nyquist (Hz): 15.0
Enter sampling rate AT Nyquist (Hz): 30
Enter sampling rate ABOVE Nyquist (Hz): 150
```

Based on the inputs, the script computes:

* Maximum signal frequency
* Nyquist rate (`2·max_freq`)

---

## 📊 **Outputs and Visualization**

The script generates:

1. **Time-Domain Plots**

   * Original continuous signal
   * Sampled signal markers

2. **FFT-Based Frequency Spectrum**

   * Shows peaks for actual and aliased frequencies
   * Highlights Nyquist frequency

Each scenario is shown for:

* **Below Nyquist**
* **At Nyquist**
* **Above Nyquist**

---

## 🧩 **Aliasing Analysis (Printed Output)**

The following observations are generated:

* Whether each signal component aliases
* Aliased frequency calculation
* Nyquist frequency for each sampling mode
* Summary interpretation

---

## 🧪 **Example Interpretation**

If `f1 = 5 Hz` and `f2 = 15 Hz`:

* Nyquist rate = `2·15 = 30 Hz`

Sampling at:

| Sampling Rate | Expectation                               |
| ------------- | ----------------------------------------- |
| `fs = 15 Hz`  | Aliasing for 15 Hz → appears as 0 Hz (DC) |
| `fs = 30 Hz`  | Borderline sampling, phase-sensitive      |
| `fs = 150 Hz` | No aliasing, accurate reconstruction      |

---

## 🎯 **Key Takeaways**

* Sampling **below Nyquist** produces **irreversible aliasing**
* Sampling **at Nyquist** is theoretically minimum but risky
* Sampling **above Nyquist** ensures accurate spectral representation
* Anti-aliasing filters must precede real-world ADCs
* Once aliasing happens, original frequency information is lost

---

## 🛠️ **Useful Enhancements**

You can extend the project with:

* Anti-aliasing FIR filter demos
* Zero-order hold and sinc interpolation
* Frequency sweeping automation
* GUI-based parameter selection (e.g., using Tkinter or Qt)

---

## 📦 **Dependencies**

| Library    | Purpose                   |
| ---------- | ------------------------- |
| NumPy      | Signal generation, FFT    |
| Matplotlib | Plotting                  |
| SciPy      | Optional signal utilities |