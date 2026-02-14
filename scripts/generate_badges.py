from PIL import Image, ImageDraw
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ASSETS = ROOT / "assets"

ICON = ASSETS / "icon.png"
BADGE_LIGHT = ASSETS / "badge-light.png"
BADGE_DARK = ASSETS / "badge-dark.png"

SIZE = 512
ICON_SIZE = 300
BORDER_WIDTH = 12


def generate_badge(bg_color, border_color, output_path):
    icon = Image.open(ICON).convert("RGBA")

    badge = Image.new("RGBA", (SIZE, SIZE), (0, 0, 0, 0))
    draw = ImageDraw.Draw(badge)

    draw.ellipse(
        (0, 0, SIZE, SIZE), fill=bg_color, outline=border_color, width=BORDER_WIDTH
    )

    icon = icon.resize((ICON_SIZE, ICON_SIZE))
    pos = ((SIZE - ICON_SIZE) // 2, (SIZE - ICON_SIZE) // 2)
    badge.paste(icon, pos, icon)

    badge.save(output_path)


# Light mode badge
generate_badge(
    bg_color=(245, 222, 179, 255),
    border_color=(180, 150, 110, 255),
    output_path=BADGE_LIGHT,
)

# Dark mode badge
generate_badge(
    bg_color=(32, 32, 32, 255), border_color=(90, 90, 90, 255), output_path=BADGE_DARK
)

print("Badges generated successfully.")
