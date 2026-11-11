"""Builds products.csv for Shopify's product importer from the KALO catalogue.

Run:  python import/build_products.py
Edit the lists below (names, prices, colours, copy), re-run, then import the CSV in
Shopify admin > Products > Import. Everything marked PLACEHOLDER is a guess: replace
it with your real products before launch (you can also edit in Shopify after import).

Tags the theme understands:
  badge:Bestseller   shows a badge on the product card
  customisable       shows a "Customise on WhatsApp" button next to Add to bag
  whatsapp-only      no Add to bag, orders go through WhatsApp only (not used right now)
  no-gift-message    hides the gift card message box
"""
import csv, itertools, os

HERE = os.path.dirname(os.path.abspath(__file__))
SIZES = ["S", "M", "L", "XL", "XXL"]

COLS = [
    "Handle", "Title", "Body (HTML)", "Vendor", "Type", "Tags", "Published",
    "Option1 Name", "Option1 Value", "Option2 Name", "Option2 Value",
    "Variant SKU", "Variant Grams", "Variant Inventory Tracker",
    "Variant Inventory Policy", "Variant Fulfillment Service", "Variant Price",
    "Variant Requires Shipping", "Variant Taxable", "Image Src", "Image Position",
    "Image Alt Text", "SEO Title", "SEO Description", "Variant Weight Unit", "Status",
]

BOTTLE_NAMES = ["It's Him", "Loud Faith", "The Manger", "Rent Free", "Let Him Reign", "Still Seek Him"]

# ---------------------------------------------------------------- oversized tees (PLACEHOLDER names/prices)
TEES = [
    ("its-him-oversized-tee", "It's Him Oversized Tee", ["White", "Black"], "badge:Bestseller"),
    ("loud-faith-oversized-tee", "Loud Faith Oversized Tee", ["Black", "Oat"], ""),
    ("merry-and-bright-oversized-tee", "Merry & Bright Oversized Tee", ["White", "Bottle green"], ""),
    ("joy-oversized-tee", "Joy Oversized Tee", ["Oat", "Red"], "badge:New"),
    ("let-it-snow-oversized-tee", "Let It Snow Oversized Tee", ["Black", "Sky blue"], ""),
]
TEE_PRICE = 799  # PLACEHOLDER


def tee(h, title, colors, badge):
    tags = ", ".join(t for t in [badge, "tee", "oversized", "apparel", "christmas", "customisable"] if t)
    return dict(
        handle=h, title=title, type="T-shirt", price=TEE_PRICE, grams=260,
        options=[("Colour", colors), ("Size", SIZES)], tags=tags,
        body="<p>Oversized fit, printed front. Soft cotton that drapes well and wears in.</p>"
             "<p>Measured flat in inches. See the size guide for chest, length and shoulder. Between sizes? Take your usual size, the fit is already relaxed.</p>"
             "<p>Want it as a gift? Add a message for the card below, or ask for it in a hamper.</p>",
        seo_title=f"{title} | Printed Oversized T-shirt India | KALO Gifts",
        seo_desc=f"{title}: printed oversized tee in soft cotton. Gift-ready with a handwritten card. Packed by hand in Chennai, delivered across India.")


# ---------------------------------------------------------------- hoodie (PLACEHOLDER)
HOODIE = dict(
    handle="cosy-season-hoodie", title="Cosy Season Hoodie", type="Hoodie", price=1299, grams=650,
    options=[("Colour", ["Bottle green", "Black", "Oat"]), ("Size", SIZES)],
    tags="badge:Most gifted, hoodie, oversized, apparel, christmas, customisable",
    body="<p>Printed oversized hoodie in brushed fleece. Cosy to wear, easy to gift.</p>"
         "<p>Measured flat in inches. See the size guide for chest, length and sleeve.</p>",
    seo_title="Printed Oversized Hoodie | Christmas Gift | KALO Gifts Chennai",
    seo_desc="Printed oversized hoodie in brushed fleece. Gift-ready with a handwritten card. Packed by hand in Chennai, delivered across India.")

# ---------------------------------------------------------------- water bottles
BOTTLES = [
    ("its-him-bottle", "It's Him", "The reason for the season? It's Him.", "Isaiah 9:6", "Hot pink", "badge:Bestseller"),
    ("loud-faith-bottle", "Loud Faith", "Silent night, loud faith. No off season.", "John 1:5", "Black", ""),
    ("the-manger-bottle", "The Manger", "The King of kings picked a manger.", "Luke 2:7", "Purple", ""),
    ("rent-free-bottle", "Rent Free", "Jesus lives rent free in my heart.", "Ephesians 3:17", "Blush pink", "badge:New"),
    ("let-him-reign-bottle", "Let Him Reign", "Let it snow, let Him reign.", "Revelation 11:15", "Sky blue", ""),
    ("still-seek-him-bottle", "Still Seek Him", "Wise men still seek Him.", "Matthew 2:2", "Navy", ""),
]


def bottle(h, name, line, verse, colour, badge):
    tags = ", ".join(t for t in [badge, "bottle", "water-bottle", "christmas"] if t)
    return dict(
        handle=h, title=f"{name} Steel Water Bottle", type="Bottle", price=599, grams=420, options=None, tags=tags,
        body=f"<p><em>“{line}”</em></p><p>{verse} (ESV). Printed steel water bottle in {colour.lower()}.</p>",
        seo_title=f"{name} Printed Steel Water Bottle | KALO Gifts",
        seo_desc=f"Printed steel water bottle in {colour.lower()} with the line “{line}” and {verse}. Delivered across India with a gift card.")


# ---------------------------------------------------------------- tote bags (PLACEHOLDER)
TOTES = [
    ("merry-and-bright-tote", "Merry & Bright Tote Bag"),
    ("loud-faith-tote", "Loud Faith Tote Bag"),
]


def tote(h, title):
    return dict(
        handle=h, title=title, type="Tote bag", price=349, grams=150,
        options=[("Colour", ["Natural", "Black"])], tags="tote, bag, christmas, customisable",
        body="<p>Printed canvas tote bag. Roomy for daily use, light enough to gift.</p>",
        seo_title=f"{title} | Printed Canvas Tote | KALO Gifts",
        seo_desc=f"{title}: printed canvas tote bag. Gift-ready with a handwritten card. Packed in Chennai, delivered across India.")


# ---------------------------------------------------------------- gift hampers (PLACEHOLDER contents/prices)
HAMPERS = [
    dict(handle="the-christmas-hamper", title="The Christmas Hamper", price=1699, grams=900,
         options=[("Tee size", SIZES), ("Bottle", BOTTLE_NAMES)],
         tags="badge:Gift set, hamper, gift-hamper, christmas, customisable",
         body="<p>A ready-to-gift box with an oversized printed tee, a printed steel water bottle and a handwritten card in your words.</p>"
              "<p>Pick the tee size and the bottle. Want a different tee, extra items or a photo frame in the box? Tap <b>Customise on WhatsApp</b>.</p>"),
    dict(handle="the-cosy-hamper", title="The Cosy Hamper", price=2299, grams=1300,
         options=[("Hoodie size", SIZES), ("Bottle", BOTTLE_NAMES)],
         tags="hamper, gift-hamper, christmas, customisable",
         body="<p>A ready-to-gift box with our printed oversized hoodie, a printed steel water bottle and a handwritten card in your words.</p>"
              "<p>Pick the hoodie size and the bottle. Want to add a tote bag or a photo frame? Tap <b>Customise on WhatsApp</b>.</p>"),
]


def hamper(d):
    d = dict(d, type="Hamper")
    d["seo_title"] = f"{d['title']} | Christmas Gift Hamper India | KALO Gifts"
    d["seo_desc"] = f"{d['title']}: a gift-ready box with printed apparel, a steel bottle and a handwritten card. Packed in Chennai, delivered across India."
    return d


# ---------------------------------------------------------------- printed photo frames (PLACEHOLDER designs/prices)
FRAME_DESIGNS = [
    ("its-him-frame", "It's Him Frame", "The reason for the season? It's Him.", "badge:New"),
    ("manger-frame", "The Manger Frame", "The King of kings picked a manger.", ""),
    ("let-him-reign-frame", "Let Him Reign Frame", "Let it snow, let Him reign.", ""),
]
FRAME_PRICES = {"A5": 599, "A4": 899}  # PLACEHOLDER


def frame(h, title, line, badge):
    tags = ", ".join(t for t in [badge, "frame", "photo-frame", "christmas"] if t)
    return dict(
        handle=h, title=title, type="Frame", price=FRAME_PRICES["A5"], grams=500,
        options=[("Size", ["A5", "A4"])], tags=tags,
        body=f"<p>A printed photo frame with the line <em>“{line}”</em>. Ready to hang or stand, ready to gift.</p>",
        seo_title=f"{title} | Printed Photo Frame Gift India | KALO Gifts",
        seo_desc=f"{title}: printed photo frame with a Christmas message. Gift-ready with a handwritten card. Packed in Chennai, delivered across India.")


# gift wrap add-on
WRAP = dict(handle="gift-wrap", title="Gift Wrap", type="Add-on", price=49, grams=20, options=None,
            tags="no-gift-message, add-on",
            body="<p>Hand-wrapped in KALO paper with a ribbon. Add one per gift.</p>",
            seo_title="Gift Wrap Add-on | KALO Gifts", seo_desc="Add hand gift wrapping to any KALO gift for Rs. 49.")


def rows_for(p):
    base = {
        "Vendor": "KALO Gifts", "Type": p["type"],
        "Tags": p["tags"] + (", gifts" if p["type"] not in ("Add-on",) else ""),
        "Published": "TRUE", "Status": "active",
        "Variant Inventory Tracker": "", "Variant Inventory Policy": "continue",
        "Variant Fulfillment Service": "manual", "Variant Taxable": "TRUE",
        "Variant Weight Unit": "g", "Variant Grams": p["grams"], "Variant Requires Shipping": "TRUE",
    }
    opts = p.get("options")
    if opts:
        combos = list(itertools.product(*[vals for _, vals in opts]))
    else:
        combos = [("Default Title",)]
    out = []
    for i, combo in enumerate(combos):
        r = {k: "" for k in COLS}
        r.update(base)
        r["Handle"] = p["handle"]
        price = p["price"]
        if p["type"] == "Frame":
            price = FRAME_PRICES[combo[0]]
        r["Variant Price"] = f"{price:.2f}"
        if opts:
            for n, ((oname, _), val) in enumerate(zip(opts, combo), start=1):
                r[f"Option{n} Name"] = oname if i == 0 else ""
                r[f"Option{n} Value"] = val
        else:
            r["Option1 Name"] = "Title" if i == 0 else ""
            r["Option1 Value"] = "Default Title"
        parts = [p["handle"].upper().replace("-", "")[:10]] + [c.upper().replace(" ", "")[:5] for c in combo if c != "Default Title"]
        r["Variant SKU"] = "-".join(parts)
        if i == 0:
            r["Title"], r["Body (HTML)"] = p["title"], p["body"]
            r["SEO Title"], r["SEO Description"] = p["seo_title"], p["seo_desc"]
        else:
            for k in ("Vendor", "Type", "Tags", "Published", "Status"):
                r[k] = ""
        out.append(r)
    return out


def catalogue():
    items = [tee(*t) for t in TEES] + [HOODIE] + [bottle(*b) for b in BOTTLES]
    items += [tote(*t) for t in TOTES] + [hamper(h) for h in HAMPERS] + [frame(*f) for f in FRAME_DESIGNS] + [WRAP]
    return items


if __name__ == "__main__":
    items = catalogue()
    path = os.path.join(HERE, "products.csv")
    seen = set()
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=COLS)
        w.writeheader()
        n = 0
        for p in items:
            for r in rows_for(p):
                assert r["Variant SKU"] not in seen, r["Variant SKU"]
                seen.add(r["Variant SKU"])
                w.writerow(r)
                n += 1
    print(f"{len(items)} products, {n} variants -> {path}")
