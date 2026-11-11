# KALO Gifts: Shopify setup

What's in this folder

| Path | What it is |
|---|---|
| `theme/` | The Shopify theme (Online Store 2.0). Same look as the current page: night green, gold, Bodoni + Manrope. |
| `dist/kalo-theme.zip` | The theme zipped, ready to upload. |
| `import/products.csv` | 20 products, 142 variants (5 oversized tees, 1 hoodie, 6 bottles, 2 totes, 2 hampers, 3 printed photo frames, gift wrap), with SEO titles and descriptions. Names, prices and colours are placeholders. |
| `import/build_products.py` | Edit prices, colours or copy here and re-run to regenerate the CSV. |
| `source/` | The original page, kept for reference. |

## 1. Create the store (you do this)
1. Sign up at shopify.com. Choose the **Basic** plan. Use the free trial while you set up.
2. **Settings > Store details:** country India, currency INR, time zone Kolkata.
3. **Settings > General > Store currency > Change formatting:** set "HTML without currency" to `₹{{amount_no_decimals}}`.
4. Keep the store **password protected** until step 8.

## 2. Upload the theme
Online Store > Themes > Add theme > Upload zip file > `dist/kalo-theme.zip`, then **Publish**.

## 3. Import the products
Products > Import > `import/products.csv`. Then:
- Add photos to each product (Products > open one > Media). Until then the site shows an icon placeholder.
- Check the weights (`Variant Grams`). They are estimates, and shipping rates depend on them.
- Inventory is not tracked. Turn tracking on per product if you hold stock.
- **Replace the placeholders** in `import/build_products.py` first: the five tee names and colours, prices (tee ₹799, tote ₹349, hampers ₹1,699 and ₹2,299, frames ₹599/₹899), hamper contents, and the size-guide measurements for your oversized fit.

## 4. Collections (Products > Collections > Create, type "Automated")
| Title | Handle | Condition |
|---|---|---|
| Gift hampers | `gift-hampers` | Type is equal to `Hamper` |
| Oversized wear | `apparel` | Tag is equal to `apparel` |
| Water bottles | `water-bottles` | Type is equal to `Bottle` |
| Tote bags | `tote-bags` | Type is equal to `Tote bag` |
| Photo frames | `photo-frames` | Type is equal to `Frame` |

Check each handle after you create the collection (it shows under "Search engine listing"). The homepage links to these exact handles.

## 5. Pages and menus
- **Page:** Online Store > Pages > Add page, title "Size guide", set template to `page.size-guide`. The handle must be `size-guide`.
- **Menu `main-menu`:** Gift hampers (`/collections/gift-hampers`), Oversized wear, Bottles, Photo frames, Size guide, FAQ (`/#faq`).
- **Menu `footer`:** the links you want in the footer's Shop column.
- **Menu `collection-chips`:** Gift hampers, Oversized wear, Water bottles, Tote bags, Photo frames. These become the filter chips on collection pages.

## 5b. How WhatsApp customising works
- Tag `customisable` on a product shows a **Customise on WhatsApp** button beside Add to bag. It opens WhatsApp with the product name, the chosen size/colour and the link already typed in.
- Tag `whatsapp-only` removes Add to bag so a product is ordered through WhatsApp only. No product uses it right now.
- The WhatsApp number comes from Theme settings > Contact and social. Without it the button shows a reminder instead.
- You take payment for WhatsApp orders yourself (UPI link) or create a draft order in Shopify admin and send the invoice link.

## 6. Theme settings (Customise)
- Theme settings > Contact and social: your real WhatsApp number (digits with country code, e.g. `919876543210`), email, Instagram handle.
- Home page: add your photos to the hero, then check each section's text.
- Upload a favicon and a social sharing image.

## 7. Money and shipping (Settings)
- **Payments:** turn on Shopify Payments if offered for your account, or add Razorpay / PayU. Enable UPI. Cash on delivery is optional.
- **Taxes and duties:** India, **include tax in prices** (your prices include GST). Enter your GSTIN.
- **Shipping and delivery:** create a shipping profile with rates:
  - Chennai (PIN codes 600001 to 600130): ₹40
  - Rest of India: ₹79
  - Free over ₹999 (add a "free over ₹999" condition to both rates).
  Add a local pickup location for Chennai collection.
- **Customer accounts:** set to **Disabled** (you said no accounts).
- **Checkout:** require phone number so you can reach buyers on WhatsApp.

## 8. Bulk discounts (Discounts > Create > Automatic)
Create three "Amount off products" automatic discounts, each as a percentage off the products in the Gifts collection:
- 10% off, minimum quantity 10
- 15% off, minimum quantity 25
- 20% off, minimum quantity 50

For 100+ pieces, customers use the WhatsApp quote button. Shopify applies the best single automatic discount, so the tiers don't stack.

## 9. Before you launch
- Place a test order (Settings > Payments > test mode, or a ₹1 test product) and check it end to end: product page, name field, cart, checkout, confirmation email.
- Check that the gift message appears on a test order, and print the packing slip to see it.
- Connect your domain (Settings > Domains), then remove the storefront password.
- Add the Google & YouTube channel and the Facebook & Instagram channel (Sales channels) to list your products for free.
- Set up your Google Business Profile for Chennai.

## Known limits of this first version
- **Gift card message** is an optional text box on each product page (up to 200 characters), saved on the order as "Gift message". You'll see it on the order in Shopify admin. Gift wrap has no message box.
- Customers pay at checkout, as normal for Shopify. There is no mockup step any more.
- No search page, customer accounts or product reviews yet.
- Fonts load from Google Fonts. Fine to start, and you can self-host them later for speed.
