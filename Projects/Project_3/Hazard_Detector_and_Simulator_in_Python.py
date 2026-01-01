import itertools
import random
from typing import List, Tuple
import matplotlib.pyplot as plt

# ============================================================
# Boolean Function Engine (Hybrid SOP)
# ============================================================

class BooleanFunction:
    def __init__(self, expression: str, variables: List[str]):
        self.expression = expression.replace(" ", "")
        self.variables = variables
        self.terms = self.expression.split("|")  # SOP terms

    def eval_term(self, term: str, values: Tuple[int, ...]) -> int:
        env = dict(zip(self.variables, map(bool, values)))
        return int(eval(term, {}, env))

    def evaluate(self, values: Tuple[int, ...]) -> int:
        return int(any(self.eval_term(t, values) for t in self.terms))

    def evaluate_inverted(self, values: Tuple[int, ...]) -> int:
        return int(not self.evaluate(values))


# ============================================================
# Truth Table
# ============================================================

class TruthTable:
    def __init__(self, logic: BooleanFunction):
        self.logic = logic
        self.table = self._generate()

    def _generate(self):
        return {
            inputs: self.logic.evaluate(inputs)
            for inputs in itertools.product([0, 1], repeat=len(self.logic.variables))
        }

    def display(self):
        print("\nTruth Table")
        print(" ".join(self.logic.variables), "| F")
        print("-" * (4 * len(self.logic.variables)))
        for k, v in self.table.items():
            print(" ".join(map(str, k)), "|", v)


# ============================================================
# Transition Simulator (Hybrid Timing)
# ============================================================

class TransitionSimulator:
    def __init__(self, logic: BooleanFunction):
        self.logic = logic
        self.term_delay_range = (1, 5)

    def simulate(self, start, end):
        diff = [i for i in range(len(start)) if start[i] != end[i]]
        timelines = []

        for order in itertools.permutations(diff):
            t = 0
            state = list(start)

            # Independent delays per SOP term
            term_delays = {
                term: random.randint(*self.term_delay_range)
                for term in self.logic.terms
            }

            timeline = [(0, self.logic.evaluate(tuple(state)))]

            for idx in order:
                state[idx] = end[idx]

                events = []
                for term, d in term_delays.items():
                    val = self.logic.eval_term(term, tuple(state))
                    events.append((t + d, val))

                events.sort()
                current = timeline[-1][1]

                for time, _ in events:
                    out = int(any(v for tm, v in events if tm <= time))
                    if out != current:
                        current = out
                        timeline.append((time, current))

                t = timeline[-1][0]

            timelines.append(timeline)

        return timelines


# ============================================================
# Hazard Detector (Static-0 FIXED)
# ============================================================

class HazardDetector:
    def __init__(self, tt: TruthTable, simulator: TransitionSimulator):
        self.tt = tt.table
        self.sim = simulator
        self.logic = simulator.logic

    @staticmethod
    def hamming(a, b):
        return sum(x != y for x, y in zip(a, b))

    @staticmethod
    def toggle_count(wave):
        return sum(wave[i][1] != wave[i - 1][1] for i in range(1, len(wave)))

    @staticmethod
    def is_static_glitch(wave, expected):
        outputs = [y for _, y in wave]
        return (
            outputs[0] == expected and
            outputs[-1] == expected and
            any(o != expected for o in outputs)
        )

    def detect(self, monte_carlo_runs=20):
        hazards = []

        for s1, s2 in itertools.combinations(self.tt.keys(), 2):
            hd = self.hamming(s1, s2)
            v1, v2 = self.tt[s1], self.tt[s2]

            if hd == 1 and v1 != v2:
                continue

            glitch_runs = 0
            worst_wave = None
            max_toggles = 0

            for _ in range(monte_carlo_runs):
                waves = self.sim.simulate(s1, s2)
                run_glitch = False

                for w in waves:
                    toggles = self.toggle_count(w)

                    if hd == 1 and v1 == v2:
                        if v1 == 1:
                            if self.is_static_glitch(w, 1):
                                run_glitch = True
                        else:
                            # Static-0 via inverted logic
                            inv_wave = [(t, int(not y)) for t, y in w]
                            if self.is_static_glitch(inv_wave, 1):
                                run_glitch = True

                    elif hd >= 2 and toggles >= 2:
                        run_glitch = True

                    if run_glitch:
                        if toggles > max_toggles:
                            max_toggles = toggles
                            worst_wave = w
                        break

                if run_glitch:
                    glitch_runs += 1

            if glitch_runs == 0:
                continue

            confidence = glitch_runs / monte_carlo_runs

            if hd == 1 and v1 == v2:
                htype = "Static-1 Hazard" if v1 == 1 else "Static-0 Hazard"
            elif hd >= 2 and v1 != v2:
                htype = "Dynamic Hazard"
            elif hd >= 2 and v1 == v2:
                htype = "Essential Hazard"
            else:
                continue

            hazards.append({
                "type": htype,
                "from": s1,
                "to": s2,
                "confidence": round(confidence, 2),
                "severity": max_toggles,
                "timeline": worst_wave,
                "explanation": self._explain(htype)
            })

        return hazards

    @staticmethod
    def _explain(htype):
        return {
            "Static-1 Hazard": "OR-reconvergent path delay mismatch.",
            "Static-0 Hazard": "AND-reconvergent path delay mismatch (detected via inversion).",
            "Dynamic Hazard": "Multiple output transitions before stabilization.",
            "Essential Hazard": "Unavoidable delay dependency."
        }.get(htype, "Unknown behavior")


# ============================================================
# Consensus Generator
# ============================================================

class ConsensusGenerator:
    @staticmethod
    def suggest(a, b, vars):
        term = []
        for i, v in enumerate(vars):
            if a[i] == b[i]:
                term.append(v if a[i] else f"~{v}")
        return " & ".join(term) if term else None


# ============================================================
# Waveform Visualization
# ============================================================

def plot_waveform(wave, title):
    t = [x[0] for x in wave]
    y = [x[1] for x in wave]

    plt.figure(figsize=(8, 3))
    plt.step(t, y, where="post")
    plt.ylim(-0.2, 1.2)
    plt.xlabel("Time")
    plt.ylabel("Output")
    plt.title(title)
    plt.grid(True)
    plt.show()


# ============================================================
# User Interface
# ============================================================

def main():
    print("\nAdvanced Logic Hazard Analyzer\n")

    expr = input("Enter Boolean expression (& | ~): ")
    variables = [v.strip() for v in input("Variables (comma-separated): ").split(",")]

    show_tt = input("Show truth table? (y/n): ").lower() == "y"
    show_wave = input("Show waveform? (y/n): ").lower() == "y"

    logic = BooleanFunction(expr, variables)
    tt = TruthTable(logic)
    sim = TransitionSimulator(logic)
    detector = HazardDetector(tt, sim)

    if show_tt:
        tt.display()

    hazards = detector.detect()

    print("\n--- Hazard Analysis Report ---\n")

    if not hazards:
        print("✔ Function is logically and delay-robust under simulated conditions.")
        return

    for i, h in enumerate(hazards, 1):
        print(f"Hazard {i}: {h['type']}")
        print(f"Transition: {h['from']} → {h['to']}")
        print(f"Confidence: {h['confidence'] * 100:.0f}%")
        print(f"Severity (toggles): {h['severity']}")
        print(f"Explanation: {h['explanation']}")

        fix = ConsensusGenerator.suggest(h["from"], h["to"], variables)
        if fix:
            print(f"Suggested Consensus Term: {fix}")

        if show_wave and h["timeline"]:
            plot_waveform(h["timeline"], h["type"])

        print("-" * 60)


if __name__ == "__main__":
    main()