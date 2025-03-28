# 🚢 Panama Canal Lock Water Usage Calculator

An interactive modeling tool for estimating water usage and cost during ship transits through the Panama Canal. The tool calculates water displaced, water lost, and economic cost based on ship tonnage and lock type, using realistic engineering assumptions and physical approximations.

## Overview

This project allows users to compare water use and cost across the two major Panama Canal lock systems: **Panamax** and **Neopanamax**. By entering a ship's tonnage, users can see:

- Gallons of water displaced by the ship
- Additional water needed to fill each lock chamber
- Water lost due to non-recycled drainage
- Estimated water cost per lock and per full transit (6 locks)

It is available both as a **web application** (Flask-based) and a **command-line tool**.

## Key Features

- Accepts user-defined ship size (tonnage)
- Calculates water displacement and cost for both lock types
- Supports per-lock and full-transit output views
- Includes descriptive tooltips and formatting in the web UI
- Highlights the engineering impact of ship design on water efficiency

## Purpose

Developed as part of a DoD-sponsored project focused on defense-related engineering challenges, this tool was used to support stakeholder communication around freshwater conservation in the Panama Canal. It translates physical relationships into clear outputs, helping engineers, decision-makers, and other stakeholders understand the tradeoffs between ship size, lock type, and water consumption.

## Technologies

- Python (core calculations)
- Flask (interactive web interface)
- HTML/Jinja templates for UI
