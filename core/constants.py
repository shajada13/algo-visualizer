# =============================================================================
# core/constants.py
# -----------------
# এই file এ সব constant value রাখা আছে।
# Window size, color, panel size — সব কিছু এখানে define করা।
# যেকোনো value change করতে চাইলে এখান থেকেই করতে হবে।
# =============================================================================

import pygame

# --- Window auto-detect (laptop screen এ fit করার জন্য) ----------------------
# pygame init না করলে display info পাওয়া যায় না, তাই আলাদাভাবে init করছি
pygame.init()
_info = pygame.display.Info()

# Screen এর ৯৫% ব্যবহার করব যাতে taskbar overlap না হয়
SCREEN_W = _info.current_w
SCREEN_H = _info.current_h

# Window size — screen এর 95% নেব, minimum 1024x640
WIDTH  = max(1024, int(SCREEN_W * 0.95))
HEIGHT = max(640,  int(SCREEN_H * 0.90))

FPS   = 60                              # Frames per second
TITLE = "AlgoViz Desktop"              # Window title

# --- Panel Layout (Web version এর মতো 3 column) ------------------------------
TOP_PANEL_H    = 100    # উপরের control bar এর height
BOTTOM_PANEL_H = 32     # নিচের status bar এর height
CANVAS_TOP     = TOP_PANEL_H
CANVAS_H       = HEIGHT - TOP_PANEL_H - BOTTOM_PANEL_H

# তিনটি column এর width ভাগ করা
CODE_W = int(WIDTH * 0.22)             # বাম: Python code panel
EXPL_W = int(WIDTH * 0.22)             # ডান: Explanation panel
VIZ_W  = WIDTH - CODE_W - EXPL_W      # মাঝে: Visualization panel

CODE_X = 0                             # বাম panel এর শুরু
VIZ_X  = CODE_W                        # মাঝের panel এর শুরু
EXPL_X = CODE_W + VIZ_W               # ডান panel এর শুরু

# --- রঙের সংজ্ঞা (Color Definitions) ----------------------------------------
# Background / UI রঙ
C_BG            = (10,  14,  22)       # গাঢ় navy — main background
C_PANEL         = (16,  22,  36)       # panel background
C_PANEL2        = (13,  18,  30)       # secondary panel (code/expl)
C_BORDER        = (30,  45,  70)       # border line
C_BORDER_BRIGHT = (42,  64, 112)       # উজ্জ্বল border

# Text রঙ
C_TEXT          = (232, 240, 254)      # সাদা text
C_TEXT_DIM      = (136, 153, 187)      # মাঝারি text
C_TEXT_MUTED    = (68,   85, 119)      # ম্লান text (label, hint)

# Accent রঙ
C_CYAN          = (  0, 229, 255)      # প্রধান accent রঙ
C_GREEN         = ( 57, 255,  20)      # সবুজ (sorted / done)
C_ORANGE        = (255, 107,  43)      # কমলা (end node / swap)
C_PURPLE        = (191,  90, 242)      # বেগুনি (pivot / path)
C_YELLOW        = (255, 214,  10)      # হলুদ (comparison)
C_RED           = (255,  69,  58)      # লাল (swap / worst)
C_BLUE          = ( 30, 144, 255)      # নীল (visited)
C_PINK          = (255,  45, 130)      # গোলাপী

# --- Bar রঙ (Sorting Visualizer) --------------------------------------------
C_BAR_DEFAULT  = ( 30,  58,  90)       # default অবস্থায় bar এর রঙ
C_BAR_ACTIVE   = C_CYAN               # যে bar compare হচ্ছে (1st)
C_BAR_COMPARED = C_YELLOW             # যে bar compare হচ্ছে (2nd)
C_BAR_SWAP     = C_RED               # swap হচ্ছে এমন bar
C_BAR_SORTED   = C_GREEN             # final position এ বসে গেছে
C_BAR_PIVOT    = C_PURPLE            # pivot element

# --- Grid রঙ (Pathfinding Visualizer) ----------------------------------------
C_CELL_DEFAULT  = ( 18,  26,  42)     # খালি cell
C_CELL_WALL     = ( 55,  65,  85)     # wall (obstacle)
C_CELL_START    = C_GREEN            # শুরুর cell
C_CELL_END      = C_ORANGE           # শেষের cell (লক্ষ্য)
C_CELL_VISITED  = ( 30,  90, 200)    # visit করা হয়েছে
C_CELL_FRONTIER = ( 80, 160, 255)    # queue তে আছে
C_CELL_PATH     = C_PURPLE           # final shortest path

# --- Button রঙ ---------------------------------------------------------------
C_BTN_NORMAL   = ( 22,  34,  58)     # সাধারণ button
C_BTN_HOVER    = ( 32,  50,  88)     # mouse hover করলে
C_BTN_DISABLED = ( 20,  28,  44)     # disabled button
C_BTN_TEXT     = C_TEXT
C_BTN_TEXT_DIM = C_TEXT_MUTED

# --- Sorting Visualizer Config -----------------------------------------------
BAR_COUNT_DEFAULT = 35               # default bar সংখ্যা
BAR_PADDING       = 3                # bar এর মাঝে gap (pixel)
BAR_AREA_MARGIN   = 24               # panel এর দুই পাশে margin

# --- Grid Config (Pathfinding) -----------------------------------------------
GRID_COLS = 36                       # grid এর column সংখ্যা
GRID_ROWS = 26                       # grid এর row সংখ্যা
CELL_SIZE = VIZ_W // GRID_COLS       # প্রতিটি cell এর size

# --- Speed Config ------------------------------------------------------------
SPEED_MIN     = 1                    # সর্বনিম্ন speed
SPEED_MAX     = 10                   # সর্বোচ্চ speed
SPEED_DEFAULT = 5                    # শুরুতে speed
