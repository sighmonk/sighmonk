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


def banner(fname, dark=True):
    W, H = 1000, 250
    if dark:
        bg1, bg2 = "#0A1020", "#121C33"
        ink, sub = "#F2F6FC", "#93A1B5"
        ring = "#ffffff"
        ring_op = "0.08"
        dot_op = "0.10"
        glow1, glow2 = "0.42", "0.34"
    else:
        bg1, bg2 = "#FFFFFF", "#EDF2FA"
        ink, sub = "#161B22", "#525C6B"
        ring = "#0d1117"
        ring_op = "0.08"
        dot_op = "0.10"
        glow1, glow2 = "0.20", "0.16"

    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-label="Sajmon Koniec — game developer">
  <defs>
    <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="{bg1}"/>
      <stop offset="1" stop-color="{bg2}"/>
    </linearGradient>
    <linearGradient id="accent" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0" stop-color="#478CBF"/>
      <stop offset="0.55" stop-color="#7C5CFF"/>
      <stop offset="1" stop-color="#22D3A6"/>
    </linearGradient>
    <radialGradient id="glow-a" cx="0.5" cy="0.5" r="0.5">
      <stop offset="0" stop-color="#478CBF" stop-opacity="{glow1}"/>
      <stop offset="1" stop-color="#478CBF" stop-opacity="0"/>
    </radialGradient>
    <radialGradient id="glow-b" cx="0.5" cy="0.5" r="0.5">
      <stop offset="0" stop-color="#7C5CFF" stop-opacity="{glow2}"/>
      <stop offset="1" stop-color="#7C5CFF" stop-opacity="0"/>
    </radialGradient>
    <pattern id="dots" width="22" height="22" patternUnits="userSpaceOnUse">
      <circle cx="1.5" cy="1.5" r="1.5" fill="{ink}" fill-opacity="{dot_op}"/>
    </pattern>
  </defs>

  <rect width="{W}" height="{H}" fill="url(#bg)"/>
  <rect width="{W}" height="{H}" fill="url(#dots)" opacity="0.55"/>
  <ellipse cx="905" cy="20" rx="290" ry="230" fill="url(#glow-a)"/>
  <ellipse cx="700" cy="260" rx="260" ry="200" fill="url(#glow-b)"/>

  <g stroke="{ring}" stroke-opacity="{ring_op}" fill="none">
    <circle cx="872" cy="125" r="76"/>
    <circle cx="872" cy="125" r="110"/>
    <circle cx="872" cy="125" r="144"/>
  </g>
  <circle cx="872" cy="15" r="5" fill="#22D3A6" fill-opacity="0.9"/>
  <circle cx="986" cy="196" r="4" fill="#7C5CFF" fill-opacity="0.9"/>
  <rect x="818" y="71" width="108" height="108" rx="26" fill="url(#bg)" fill-opacity="0.85" stroke="url(#accent)" stroke-width="2.5"/>
  <text x="872" y="142" text-anchor="middle" font-family="{FONT}" font-size="46" font-weight="800" letter-spacing="-1" fill="{ink}">SK</text>

  <text x="62" y="112" font-family="{FONT}" font-size="62" font-weight="800" letter-spacing="-1.6" fill="{ink}">Sajmon Koniec</text>
  <rect x="64" y="132" width="120" height="5" rx="2.5" fill="url(#accent)"/>
  <text x="64" y="176" font-family="{FONT}" font-size="22" font-weight="500" letter-spacing="0.2" fill="{sub}">Game developer · Godot 4 &amp; C# · AI-driven gameplay</text>
  <text x="64" y="208" font-family="{FONT}" font-size="15" font-weight="600" letter-spacing="2.4" fill="{sub}" fill-opacity="0.85">M.SC. CS · UMK TORUŃ · KNI UMK</text>
</svg>
"""
    open(os.path.join(BASE, fname), "w").write(svg)


tile("btn-gmail.svg", "E-MAIL", "sajmonskkoniec@gmail.com", "#F4514A", "#C5221F", "gmail")
tile("btn-linkedin.svg", "LINKEDIN", "in/sajmon-koniec", "#2E8BE6", "#0A4C93", "linkedin")
tile("btn-itch.svg", "ITCH.IO", "6ajmon.itch.io", "#FF6D5A", "#CE3A22", "itchdotio")
banner("banner-dark.svg", dark=True)
banner("banner-light.svg", dark=False)
print("ok", sorted(os.listdir(BASE)))
