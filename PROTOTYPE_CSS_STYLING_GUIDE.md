# Prototype CSS & Times New Roman - Styling Guide

## 🎨 Visual Design System

### Font Family
```
Font: Times New Roman, Times, serif
Applied to: ALL text elements globally
Benefits:
  ✓ Professional, classic appearance
  ✓ Serif font improves readability in long text
  ✓ Academic/educational feel
  ✓ Better for printing
  ✓ Universal compatibility
```

---

## 🎨 Color Palette

### Primary Colors
```
Background:        #f0f0f0 (Light Gray)
Card/Surface:      #ffffff (White)
Text:              #333333 (Dark Gray)
Border:            #999999 (Medium Gray)
```

### Accent Colors
```
Primary/Blue:      #0066cc (Action buttons, links, highlights)
Danger/Red:        #cc0000 (Delete, end call, warnings)
Success/Green:     #009900 (Confirm, active features)
Gray:              #666666 (Secondary text, muted info)
Light Gray:        #eeeeee (Hover states, subtle backgrounds)
```

---

## 🧩 Component Styles

### Buttons

#### Primary Button (Blue)
```
Background:   #0066cc
Text Color:   White (inverted)
Border:       2px solid #0066cc
Padding:      10px 16px
Font:         Times New Roman, bold, 14px
Border Radius: 4px
Hover:        Background #0052a3 + shadow
Cursor:       pointer
```

#### Secondary Button (Gray)
```
Background:   #ffffff (white)
Text Color:   #333333 (dark)
Border:       2px solid #999999
Padding:      10px 16px
Font:         Times New Roman, bold, 14px
Border Radius: 4px
Hover:        Background #eeeeee + shadow
Cursor:       pointer
```

#### Control Bar Buttons

**Inactive (Gray)**
```
Background:   #555555
Border:       2px solid #999999
Hover:        #777777 with shadow
```

**Active - Mic/Camera Off (Red)**
```
Background:   #cc0000
Border:       2px solid #990000
Hover:        #ff0000 with shadow
Text:         White
```

**Active - Whiteboard/Screen Share (Green)**
```
Background:   #009900
Border:       2px solid #006600
Hover:        #00cc00 with shadow
Text:         White
```

---

## 🏗️ Layout Elements

### Cards
```
Background:     White (#ffffff)
Border:         1-2px solid #999999
Border-Radius:  6px
Padding:        16px
Shadow:         0 2px 4px rgba(0, 0, 0, 0.1)
Transition:     All 0.2-0.3s ease
```

### Input Fields
```
Background:     White (#ffffff)
Border:         2px solid #999999
Border-Radius:  4px
Padding:        10px 12px
Font:           Times New Roman, 14px
Focus:          Border changes to #0066cc
Focus Shadow:   0 0 0 3px rgba(0, 102, 204, 0.1)
Transition:     All 0.2s ease
```

### Labels
```
Font:           Times New Roman, bold, 14px
Color:          #333333
Margin Bottom:  6px
Display:        Block
```

---

## 🎬 Video Conferencing Styles

### Video Main Area
```
Background:     #1a1a1a (Black - simulates video feed)
Border:         2px solid #999999
Width:          100%
Height:         Fill available space
Color Mode:     Dark text on dark background
```

### Avatar (Large - Main Feed)
```
Width/Height:   120px
Background:     Linear gradient (blue to green)
Border-Radius:  50% (perfect circle)
Border:         3px solid #999999
Font Size:      48px
Font Weight:    Bold
Color:          White
Initials:       User's first and last name initials
```

### Avatar (Small - Participant Cards)
```
Width/Height:   48px
Background:     Linear gradient (blue to red)
Border-Radius:  50% (perfect circle)
Border:         2px solid #999999
Font Weight:    Bold
Color:          White
Initial:        First letter of name
```

### Control Bar
```
Background:     #2a2a2a (Dark gray)
Border-Top:     2px solid #999999
Padding:        16px 24px
Display:        Flex, center aligned
Gap:            16px between elements
Min Height:     70px
Flex-Wrap:      Yes (wraps on small screens)
```

### Whiteboard Modal
```
Background:     White (#ffffff)
Border:         3px solid #999999
Border-Radius:  8px
Padding:        16px (separate areas)
Box-Shadow:     0 8px 16px rgba(0, 0, 0, 0.3)
Z-Index:        100 (above all content)
Overlay:        Semi-transparent black rgba(0,0,0,0.7)
```

### Whiteboard Canvas
```
Background:     White
Border:         2px solid #999999
Border-Radius:  4px
Cursor:         Crosshair
Width:          800px (max)
Height:         600px
Drawing Color:  Black (#000000)
Pen Width:      2px
```

### Participant Sidebar
```
Position:       Absolute right, full height
Width:          300px
Background:     White (#ffffff)
Border-Left:    2px solid #999999
Z-Index:        50
Box-Shadow:     -4px 0 8px rgba(0, 0, 0, 0.1)
Overflow-Y:     Auto (scrollable)
```

### Participant List Item
```
Background:     #eeeeee (light gray)
Border:         1px solid #999999
Border-Radius:  6px
Padding:        12px
Margin:         12px between items
Transition:     All 0.2s
Hover:          Background #e8e8e8 + shadow
```

---

## 📐 Spacing System

### Consistent Spacing Values
```
8px   - Small gaps, margins within components
16px  - Medium gaps, standard padding
24px  - Large gaps, section spacing
32px  - Extra large gaps between major sections
```

### Padding/Margin Examples
```
Small:  8px 12px (buttons)
Medium: 16px (cards, sections)
Large:  24px (major sections)
Extra:  32px (page margins)
```

---

## 🎯 Typography Scale

```
H1: 28px, bold, Times New Roman
H2: 24px, bold, Times New Roman
H3: 20px, bold, Times New Roman
H4: 18px, bold, Times New Roman
H5: 16px, bold, Times New Roman
H6: 14px, bold, Times New Roman
P:  14px, normal weight, Times New Roman
Label: 14px, bold, Times New Roman
Small: 12px, normal weight, Times New Roman
(All with serif font)
```

---

## 🌈 Interactive States

### Button States
```
REST:       Standard appearance as described
HOVER:      Darker shade + subtle shadow
ACTIVE:     Slightly inset appearance
DISABLED:   Grayed out (opacity: 0.5)
FOCUS:      Blue outline for keyboard navigation
```

### Input States
```
DEFAULT:    White background, gray border
FOCUS:      Blue border, blue shadow
ERROR:      Red border (when needed)
DISABLED:   Gray background, gray text
```

---

## 📱 Responsive Breakpoints

### Desktop (1024px+)
- Full control bar with all elements
- Participant cards visible
- Sidebar visible
- All buttons visible

### Tablet (768px - 1023px)
- Control bar adapts
- Reduced gaps (12px instead of 16px)
- Smaller buttons

### Mobile (480px - 767px)
- Compact control bar
- Stacked layout where needed
- Session code hidden
- Buttons smaller (padding reduces to 8px 10px)

### Extra Small (< 480px)
- Minimal spacing (8px gaps)
- Smallest buttons
- Two-line control bar possible
- Essential features only

---

## 🎨 CSS Class Examples

### Using Prototype CSS Classes

#### Layout
```jsx
<div className="prototypeFlexCol">        {/* Flex column */}
  <div className="prototypeFlexCenter">  {/* Centered flex */}
    <button className="prototypeButton">Button</button>
  </div>
</div>
```

#### Components
```jsx
<div className="prototypeCard">           {/* Card styling */}
  <h3 className="prototypeText">Title</h3>
  <input className="prototypeInput" />
  <label className="prototypeLabel">Label</label>
</div>
```

#### Video Conferencing
```jsx
<div className="prototypeVideoArea">     {/* Video container */}
  <div className="prototypeAvatarLarge">JD</div>
  <p className="prototypeVideoName">John Doe</p>
</div>

<div className="prototypeControlBar">    {/* Control bar */}
  <button className="prototypeControlButton prototypeButtonGray">
    Mic
  </button>
</div>
```

---

## ✨ Special Effects

### Shadows
```
Standard:  0 2px 4px rgba(0, 0, 0, 0.1)
Elevated:  0 4px 12px rgba(0, 0, 0, 0.15)
Large:     0 8px 16px rgba(0, 0, 0, 0.3) (modals)
```

### Hover Shadow
```
Applied:   var(--prototype-shadow) on hover
Effect:    Subtle lift and depth
Duration:  Instant (no transition needed)
```

### Transitions
```
Standard:  0.2s ease (inputs, buttons)
Moderate:  0.3s ease (larger components)
Modal:     0.3s ease-out (animations)
```

### Animations
```
Fade In:   Opacity 0 → 1 over 0.3s
Slide In:  TranslateX 100% → 0 over 0.3s
Both:      Applied to modals and sidebars
```

---

## 📋 Design Tokens Summary

```
Colors:
  --prototype-bg:           #f0f0f0
  --prototype-card:         #ffffff
  --prototype-text:         #333333
  --prototype-border:       #999999
  --prototype-blue:         #0066cc
  --prototype-red:          #cc0000
  --prototype-green:        #009900
  --prototype-gray:         #666666
  --prototype-light-gray:   #eeeeee

Sizing:
  Small Gap:                8px
  Medium Gap:               16px
  Large Gap:                24px
  Button Padding (large):   10px 16px
  Button Padding (small):   8px 12px

Shadows:
  Standard:                 0 2px 4px rgba(0, 0, 0, 0.1)
  Elevated:                 0 4px 12px rgba(0, 0, 0, 0.15)

Typography:
  Font Family:              Times New Roman, Times, serif
  Base Size:                14px
  Line Height:              1.6
```

---

## 🎯 Design Principles

1. **Clarity**: Clean borders and clear visual hierarchy
2. **Simplicity**: Minimal ornamentation, focus on content
3. **Professional**: Serif font for academic credibility
4. **Accessibility**: High contrast ratios, readable sizes
5. **Consistency**: Same styling applied throughout
6. **Responsiveness**: Adapts to all screen sizes
7. **Usability**: Clear button states and feedback
8. **Educational**: Formal appearance suitable for learning

---

## 📖 Reference

- **Primary Font**: Times New Roman (serif)
- **Font Size**: 14px base
- **Color Mode**: Light theme (dark backgrounds for video areas)
- **Border Style**: Solid, 1-3px thickness
- **Border Radius**: 4-8px (minimal for prototype feel)
- **Shadow Amount**: Subtle (0.1 opacity maximum)

---

**Prototype CSS Version**: 1.0  
**Times New Roman**: Global  
**Components Styled**: 40+  
**Color Palette Items**: 11  
**Responsive Breakpoints**: 4
