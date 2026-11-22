"""Reproduce the CHH–GVH synthetic orbital video. Requires NumPy, SciPy, Pillow and FFmpeg."""
from pathlib import Path
import subprocess

import numpy as np
from PIL import Image, ImageDraw, ImageFont
from scipy.integrate import solve_ivp

OUT = Path(__file__).resolve().parent
G = 4 * np.pi**2
EARTH = 3.003e-6
JUPITER = 9.5459e-4
AU_KM = 149_597_870.7
YEAR_S = 31_557_600
SIZE = (1080, 1920)
FPS = 24
DURATION = 20

def simulate(with_jupiter):
    earth_r = .9833
    earth_v = np.sqrt(G * (1 + EARTH) * (2 / earth_r - 1))
    jupiter_v = np.sqrt(G * (1 + JUPITER) / 5.2)

    def inverse_cube(position):
        return position / np.linalg.norm(position)**3

    def derivatives(_, state):
        r, v, R, V = state.reshape(4, 2)
        earth_field = inverse_cube(r)
        radial = -G * (1 + EARTH) * earth_field
        if not with_jupiter:
            return np.r_[v, radial, 0, 0, 0, 0]
        jupiter_field = inverse_cube(R)
        mutual = inverse_cube(R - r)
        radial += G * JUPITER * (mutual - jupiter_field)
        outer = -G * ((1 + JUPITER) * jupiter_field + EARTH * (mutual + earth_field))
        return np.r_[v, radial, V, outer]

    def crossing(_, state):
        return state[1]

    crossing.direction = 1
    result = solve_ivp(
        derivatives, (0, 12.2), [earth_r, 0, 0, earth_v, 5.2, 0, 0, jupiter_v],
        method="DOP853", rtol=1e-12, atol=1e-14, max_step=.0125,
        dense_output=True, events=crossing,
    )
    returns = result.t_events[0][1:]
    states = result.y_events[0][1:]
    assert result.success and len(returns) == 12 and np.all(states[:, 0] > 0)
    return result.sol, returns, np.linalg.norm(states[:, :2], axis=1)

def font(size, bold=False):
    face = "DejaVuSans-Bold.ttf" if bold else "DejaVuSans.ttf"
    return ImageFont.truetype(face, size)

def render():
    baseline, baseline_returns, baseline_radii = simulate(False)
    perturbed, perturbed_returns, perturbed_radii = simulate(True)
    delta_t = (perturbed_returns - baseline_returns) * YEAR_S
    delta_r = (perturbed_radii - baseline_radii) * AU_KM
    assert abs(delta_t[-1] + 5125.53) < .02 and abs(delta_r[-1] - 18.33) < .02
    print("12e retour, différence (s et km):", delta_t[-1], delta_r[-1], flush=True)

    centers = [(540, 640), (540, 1130)]
    labels = ["Soleil–Terre", "Soleil–Terre–Jupiter"]
    colors = ["#65dffa", "#8ce6ae"]
    bg = Image.new("RGB", SIZE, "#071222")
    d = ImageDraw.Draw(bg)
    def text(canvas, xy, label, size, color="#eef6ff", bold=False, anchor=None):
        canvas.text(xy, label, font=font(size, bold), fill=color, anchor=anchor)
    text(d, (78, 92), "CHH → GVH  /  CONTRÔLE NEWTONIEN", 24, "#85b5ce", True)
    text(d, (77, 148), "Jupiter change-t-elle", 69, bold=True)
    text(d, (77, 232), "le retour de la Terre ?", 68, bold=True)
    text(d, (80, 329), "Deux modèles, des conditions initiales communes", 29, "#a8bed3")
    for j, (cx, cy) in enumerate(centers):
        d.rounded_rectangle((72, cy-210, 1008, cy+216), 31, fill="#102238", outline="#273e57", width=2)
        text(d, (102, cy-182), labels[j], 33, bold=True)
        d.line((cx-170, cy, cx+225, cy), fill="#334c62", width=2)
        d.ellipse((cx-14, cy-14, cx+14, cy+14), fill="#ffce64")
        phases = np.linspace(0, 1, 320)
        orbit = (baseline if j == 0 else perturbed)(phases)[:2].T
        d.line([(cx+135*x, cy-135*y) for x,y in orbit], fill=colors[j], width=3)
        text(d, (102, cy+146), "Terre", 23, colors[j], True)
        text(d, (102, cy+177), "Trace du premier tour", 21, "#a8bed3")
        text(d, (728, cy+35), "Direction du retour", 20, "#a8bed3")
    text(d, (78, 1425), "12ᵉ RETOUR · EFFET DE JUPITER", 28, "#85b5ce", True)
    text(d, (76, 1503), "1 h 25 min plus tôt", 64, "#8ce6ae", True)
    text(d, (79, 1590), "+18 km à ce passage", 48, bold=True)
    d.line((78, 1700, 1002, 1700), fill="#273e57", width=2)
    text(d, (78, 1744), "Simulation synthétique · vue dans le plan orbital", 28, "#a8bed3")
    text(d, (78, 1790), "Jupiter : direction indiquée, distance hors cadre", 25, "#a8bed3")
    text(d, (78, 1833), "GitHub / col38470682 / Univers", 26, "#85b5ce", True)

    def frame(t):
        image = bg.copy()
        draw = ImageDraw.Draw(image)
        for j, (solution, times) in enumerate(((baseline, baseline_returns), (perturbed, perturbed_returns))):
            state = solution(t)
            cx, cy = centers[j]
            x, y = cx + 135*state[0], cy - 135*state[1]
            draw.ellipse((x-13, y-13, x+13, y+13), fill=colors[j], outline="#ffffff", width=2)
            count = min(int(np.searchsorted(times, t, side="right")), 12)
            text(draw, (975, cy-166), f"Tour {count:02d} / 12", 24, "#eef6ff", True, "rm")
            if j:
                n = state[4:6] / np.linalg.norm(state[4:6])
                px, py = cx + 180*n[0], cy - 180*n[1]
                draw.ellipse((px-7, py-7, px+7, py+7), fill="#ffce64")
                text(draw, (770, cy+172), "● Direction Jupiter", 20, "#ffce64")
        if t < baseline_returns[-1]:
            draw.rectangle((72, 1490, 1008, 1665), fill="#071222")
            text(draw, (78, 1515), f"{t:.1f} années simulées".replace(".", ","), 37, bold=True)
            draw.rounded_rectangle((78, 1590, 1000, 1602), 6, fill="#273e57")
            end = 78 + 922*t/baseline_returns[-1]
            if end > 79:
                draw.rounded_rectangle((78, 1590, end, 1602), 6, fill="#8ce6ae")
        return image

    last = float(baseline_returns[-1])
    frame(last).save(OUT / "Couverture_Terre_Jupiter.png")
    command = [
        "ffmpeg", "-loglevel", "error", "-y", "-f", "rawvideo", "-pix_fmt", "rgb24",
        "-s", "1080x1920", "-r", str(FPS), "-i", "-", "-an", "-c:v", "libx264",
        "-preset", "fast", "-crf", "19", "-pix_fmt", "yuv420p", "-movflags", "+faststart",
        str(OUT / "Simulation_Terre_Jupiter.mp4"),
    ]
    with subprocess.Popen(command, stdin=subprocess.PIPE) as video:
        assert video.stdin is not None
        for index in range(DURATION * FPS):
            t = last * min(index / (16 * FPS - 1), 1)
            video.stdin.write(frame(t).tobytes())
        video.stdin.close()
        if video.wait():
            raise RuntimeError("FFmpeg could not encode the video.")

if __name__ == "__main__":
    render()
