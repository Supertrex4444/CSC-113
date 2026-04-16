# PRD: GummyWorm.js (MVP)

**Project Lead:** Travis Cayton
**Date:** April 16, 2026
**Status:** Draft / MVP Definition  

---

## 1. Problem Statement
The classic "Snake" game is a staple of computer science education, but most implementations are visually sterile (static blocks/pixels). There is a lack of polished, themed versions that utilize modern CSS/Canvas capabilities to create a "juicy" feel. **GummyWorm.js** aims to provide a nostalgic, satisfying arcade experience by applying a "gummy candy" aesthetic to the classic snake mechanic.

## 2. Target User
- **Casual Web Users:** People looking for a 60-second distraction.
- **Retro Game Enthusiasts:** Players who enjoy classic mechanics with a modern visual twist.
- **CS Portfolio Reviewers:** Potential employers looking for clean, well-documented code with a focus on "game feel."

## 3. Must-Have Features (MVP)

### A. Fluid Gummy Movement & Growth
- **The Snake:** Instead of blocks, the snake is rendered as a series of connected, rounded segments with 80% opacity to mimic gummy candy.
- **Growth:** When the head collides with a "Sugar Crystal" (food), a new segment is added to the tail.
- **Input:** Grid-based movement controlled by Arrow keys or WASD.

### B. Collision & Game State Logic
- **Self-Collision:** Game over if the head hits any part of the body.
- **Boundary Collision:** Game over if the head hits the canvas edge.
- **Score Tracking:** A simple HUD showing current length and "Highest Sugar Rush" (High Score).

### C. Themed Visuals ("The Sugar High")
- **The Food:** "Sugar Crystals" that pulse or glow.
- **The "Squish":** When the worm moves, the segments should have a slight lag or easing effect to feel less like a rigid robot and more like a gelatinous worm.
- **Color Palette:** Neon translucent colors (Pink, Lime Green, or Electric Blue).

## 4. User Interaction Flow
1.  **Entry:** User loads the URL. A "Press Space to Start" overlay appears over the game board.
2.  **Start:** User presses space. The Gummy Worm begins moving from the center.
3.  **Active Play:** 
    - User steers using WASD/Arrows.
    - Worm consumes Sugar Crystals.
    - Speed increases slightly every 5 items consumed.
4.  **Death:** Upon collision, the worm "dissolves" (simple opacity fade). A "Game Over" screen appears showing the final score.
5.  **Restart:** User presses "R" or clicks a button to reset the state.

## 5. What to Exclude (v1 / Out of Scope)
- **Multiplayer:** No local or network-based co-op.
- **Global Leaderboards:** No backend or database integration; local storage only for high scores.
- **Skins/Customization:** No shop or worm selection.
- **Touch Controls:** No mobile-specific d-pads (v1 is Desktop-only).
- **Power-ups:** No speed boosts or invincibility frames.

---

## 6. Technical Stack Suggestions (Mental Note for Dev)
- **Frontend:** HTML5 Canvas, Vanilla JavaScript (or TypeScript for better state management).
- **Styling:** CSS3 for "glassmorphism" UI effects and canvas container.
- **Deployment:** Vercel, Netlify, or GitHub Pages.

---

### Prompt for Code Generation (Copy/Paste this):
> "I am building a web-based Snake game themed around a gummy worm based on a PRD. Please create a single-file MVP using HTML5 Canvas, CSS, and Vanilla JavaScript. The snake should look like translucent gummy segments (rounded) and move on a grid. Include a 'Sugar Crystal' as food, collision detection for walls/self, and a high-score system using LocalStorage. Ensure the code is modular and includes a 'Game Over' overlay."
