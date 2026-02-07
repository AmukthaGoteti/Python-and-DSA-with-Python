import numpy as np
import matplotlib.pyplot as plt
from scipy import signal as scipy_signal

def get_user_inputs():
    """Get signal and sampling parameters from user"""
    print("=" * 60)
    print("SAMPLING AND ALIASING DEMONSTRATION")
    print("=" * 60)
    
    # Get signal parameters
    print("\n--- Signal Parameters ---")
    f1 = float(input("Enter first frequency (Hz) [default: 5]: ") or "5")
    f2 = float(input("Enter second frequency (Hz) [default: 15]: ") or "15")
    a1 = float(input("Enter first signal amplitude [default: 1]: ") or "1")
    a2 = float(input("Enter second signal amplitude [default: 0.5]: ") or "0.5")
    duration = float(input("Enter signal duration (seconds) [default: 1]: ") or "1")
    
    # Get sampling parameters
    print("\n--- Sampling Parameters ---")
    max_freq = max(f1, f2)
    nyquist_rate = 2 * max_freq
    print(f"Maximum frequency: {max_freq} Hz")
    print(f"Nyquist rate: {nyquist_rate} Hz")
    
    fs_below = float(input(f"Enter sampling rate BELOW Nyquist (Hz) [default: {nyquist_rate*0.5}]: ") 
                     or str(nyquist_rate * 0.5))
    fs_nyquist = float(input(f"Enter sampling rate AT Nyquist (Hz) [default: {nyquist_rate}]: ") 
                       or str(nyquist_rate))
    fs_above = float(input(f"Enter sampling rate ABOVE Nyquist (Hz) [default: {nyquist_rate*5}]: ") 
                     or str(nyquist_rate * 5))
    
    return {
        'f1': f1, 'f2': f2, 'a1': a1, 'a2': a2, 'duration': duration,
        'fs_below': fs_below, 'fs_nyquist': fs_nyquist, 'fs_above': fs_above,
        'nyquist_rate': nyquist_rate
    }

def generate_composite_signal(t, f1, f2, a1, a2):
    """Generate composite signal with two sinusoids"""
    return a1 * np.sin(2 * np.pi * f1 * t) + a2 * np.sin(2 * np.pi * f2 * t)

def compute_fft(signal, fs):
    """Compute FFT and return frequencies and magnitudes"""
    n = len(signal)
    fft_vals = np.fft.fft(signal)
    fft_freq = np.fft.fftfreq(n, 1/fs)
    
    # Get positive frequencies only
    pos_mask = fft_freq >= 0
    fft_freq = fft_freq[pos_mask]
    fft_mag = np.abs(fft_vals[pos_mask]) / n * 2
    
    return fft_freq, fft_mag

def plot_results(params, continuous_t, continuous_signal, 
                 sampled_signals, sampled_times, sampling_rates):
    """Plot time and frequency domain results"""
    fig = plt.figure(figsize=(16, 12))
    
    titles = ['Below Nyquist', 'At Nyquist', 'Above Nyquist']
    
    for i, (fs, title) in enumerate(zip(sampling_rates, titles)):
        # Time domain plot
        ax_time = plt.subplot(3, 2, i*2 + 1)
        ax_time.plot(continuous_t, continuous_signal, 'b-', linewidth=1.5, 
                    label='Original Signal', alpha=0.7)
        ax_time.plot(sampled_times[i], sampled_signals[i], 'ro-', 
                    markersize=6, linewidth=1, label=f'Sampled at {fs} Hz')
        ax_time.set_xlabel('Time (s)')
        ax_time.set_ylabel('Amplitude')
        ax_time.set_title(f'Time Domain - {title} (fs = {fs} Hz)')
        ax_time.grid(True, alpha=0.3)
        ax_time.legend()
        ax_time.set_xlim([0, min(0.5, params['duration'])])  # Show first 0.5s
        
        # Frequency domain plot
        ax_freq = plt.subplot(3, 2, i*2 + 2)
        fft_freq, fft_mag = compute_fft(sampled_signals[i], fs)
        
        ax_freq.stem(fft_freq, fft_mag, linefmt='r-', markerfmt='ro', 
                    basefmt='k-', label='Sampled Signal Spectrum')
        ax_freq.axvline(params['f1'], color='b', linestyle='--', 
                       label=f'f1 = {params["f1"]} Hz', alpha=0.7)
        ax_freq.axvline(params['f2'], color='g', linestyle='--', 
                       label=f'f2 = {params["f2"]} Hz', alpha=0.7)
        ax_freq.axvline(fs/2, color='m', linestyle=':', linewidth=2,
                       label=f'Nyquist freq = {fs/2} Hz')
        ax_freq.set_xlabel('Frequency (Hz)')
        ax_freq.set_ylabel('Magnitude')
        ax_freq.set_title(f'Frequency Domain - {title}')
        ax_freq.grid(True, alpha=0.3)
        ax_freq.legend()
        ax_freq.set_xlim([0, max(params['f2']*2, fs/2*1.2)])
    
    plt.tight_layout()
    plt.show()

def analyze_aliasing(params, sampling_rates):
    """Print analysis of aliasing effects"""
    print("\n" + "=" * 60)
    print("ANALYSIS AND OBSERVATIONS")
    print("=" * 60)
    
    print(f"\nOriginal Signal Frequencies: f1 = {params['f1']} Hz, f2 = {params['f2']} Hz")
    print(f"Nyquist Rate: {params['nyquist_rate']} Hz")
    
    for i, (fs, title) in enumerate(zip(sampling_rates, 
                                        ['Below Nyquist', 'At Nyquist', 'Above Nyquist'])):
        print(f"\n--- {title} Sampling (fs = {fs} Hz) ---")
        print(f"Nyquist frequency (fs/2): {fs/2} Hz")
        
        # Check aliasing for each frequency
        for freq, name in [(params['f1'], 'f1'), (params['f2'], 'f2')]:
            if freq > fs/2:
                alias_freq = abs(freq - round(freq/fs) * fs)
                print(f"  {name} = {freq} Hz > {fs/2} Hz: ALIASED to ~{alias_freq:.2f} Hz")
            elif freq == fs/2:
                print(f"  {name} = {freq} Hz = {fs/2} Hz: AT Nyquist frequency")
            else:
                print(f"  {name} = {freq} Hz < {fs/2} Hz: No aliasing")
    
    print("\n" + "=" * 60)
    print("IMPLICATIONS OF ALIASING")
    print("=" * 60)
    print("""
1. BELOW NYQUIST RATE:
   - High frequencies appear as lower frequencies (aliasing)
   - Original signal cannot be reconstructed
   - Spectral components fold back into lower frequency range
   
2. AT NYQUIST RATE:
   - Theoretical minimum for perfect reconstruction
   - In practice, slightly above Nyquist is recommended
   - Phase sensitivity can cause issues
   
3. ABOVE NYQUIST RATE:
   - All frequency components correctly preserved
   - Perfect reconstruction possible with ideal interpolation
   - Oversampling provides better quality and reduces noise
   
KEY TAKEAWAYS:
   - Always sample at >2x the highest frequency component
   - Anti-aliasing filters needed before sampling
   - Aliasing creates false low-frequency components
   - Once aliased, original signal is lost (irreversible)
    """)

def main():
    # Get user inputs
    params = get_user_inputs()
    
    # Generate continuous signal (high resolution for reference)
    fs_continuous = params['nyquist_rate'] * 50  # Very high sampling
    continuous_t = np.linspace(0, params['duration'], 
                               int(fs_continuous * params['duration']))
    continuous_signal = generate_composite_signal(continuous_t, params['f1'], 
                                                   params['f2'], params['a1'], params['a2'])
    
    # Sample at different rates
    sampling_rates = [params['fs_below'], params['fs_nyquist'], params['fs_above']]
    sampled_signals = []
    sampled_times = []
    
    for fs in sampling_rates:
        t_sampled = np.arange(0, params['duration'], 1/fs)
        sig_sampled = generate_composite_signal(t_sampled, params['f1'], 
                                                params['f2'], params['a1'], params['a2'])
        sampled_signals.append(sig_sampled)
        sampled_times.append(t_sampled)
    
    # Plot results
    plot_results(params, continuous_t, continuous_signal, 
                sampled_signals, sampled_times, sampling_rates)
    
    # Analyze aliasing
    analyze_aliasing(params, sampling_rates)

if __name__ == "__main__":
    main()