#!/usr/bin/env python3
"""Generuje assety SVG dla profilu GitHub sighmonk (kafelki kontaktowe + baner)."""
import os
import re
import subprocess

BASE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets")
os.makedirs(BASE, exist_ok=True)

FONT = "'Segoe UI',-apple-system,BlinkMacSystemFont,'Helvetica Neue',Helvetica,Arial,sans-serif"


def icon_path(slug):
    local = f"/tmp/si-{slug}.svg"
    if not os.path.exists(local):
        subprocess.run(
            ["curl", "-sL", f"https://cdn.jsdelivr.net/npm/simple-icons@13/icons/{slug}.svg", "-o", local],
            check=True,
        )
    return re.search(r'<path d="([^"]+)"', open(local).read()).group(1)


def tile(fname, label, handle, c1, c2, slug, logo_px=26.0, logo_dx=0.0):
    W, H = 300, 76
    scale = logo_px / 24.0
    lx = 30 + logo_dx
    ly = (H - logo_px) / 2.0
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-label="{label}: {handle}">
  <defs>
    <linearGradient id="g-{label.lower()}" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="{c1}"/>
      <stop offset="1" stop-color="{c2}"/>
    </linearGradient>
    <linearGradient id="sheen-{label.lower()}" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#ffffff" stop-opacity="0.16"/>
      <stop offset="0.55" stop-color="#ffffff" stop-opacity="0"/>
    </linearGradient>
  </defs>
  <rect x="0.5" y="0.5" width="{W - 1}" height="{H - 1}" rx="14" fill="url(#g-{label.lower()})"/>
  <rect x="0.5" y="0.5" width="{W - 1}" height="{H - 1}" rx="14" fill="url(#sheen-{label.lower()})"/>
  <rect x="0.5" y="0.5" width="{W - 1}" height="{H - 1}" rx="14" fill="none" stroke="#ffffff" stroke-opacity="0.18"/>
  <circle cx="42" cy="{H / 2}" r="23" fill="#ffffff" fill-opacity="0.16"/>
  <circle cx="42" cy="{H / 2}" r="23" fill="none" stroke="#ffffff" stroke-opacity="0.22"/>
  <g transform="translate({lx},{ly}) scale({scale:.4f})" fill="#ffffff">
    <path d="{icon_path(slug)}"/>
  </g>
  <text x="78" y="32" font-family="{FONT}" font-size="10" font-weight="600" letter-spacing="1.9" fill="#ffffff" fill-opacity="0.74">{label}</text>
  <text x="78" y="55" font-family="{FONT}" font-size="14.5" font-weight="700" letter-spacing="-0.2" fill="#ffffff">{handle}</text>
</svg>
"""
    open(os.path.join(BASE, fname), "w").write(svg)


tile("btn-gmail.svg", "E-MAIL", "hi@sighmonk.com", "#F4514A", "#C5221F", "gmail")
tile("btn-linkedin.svg", "LINKEDIN", "in/sajmon-koniec", "#2E8BE6", "#0A4C93", "linkedin")
tile("btn-itch.svg", "ITCH.IO", "6ajmon.itch.io", "#FF6D5A", "#CE3A22", "itchdotio")
print("ok", sorted(os.listdir(BASE)))