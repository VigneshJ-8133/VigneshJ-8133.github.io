"""Generates the Expendracker site pages from one template.

Fill in FACTS, then run:  python build.py
The privacy page is edited by hand; this script only swaps its header and footer.
"""
import pathlib
import re

HERE = pathlib.Path(__file__).parent

FACTS = {
    "NAME": "J Vignesh",
    "EMAIL": "vigneshj8133@gmail.com",
    "ADDRESS": "Bengaluru (Bangalore), Karnataka, India",
    "CITY": "Bengaluru",
    "PRICE": "₹99",
    "REFUND_DAYS": "7",
    "UPDATED": "24 September 2026",
}

PAGES = [
    ("index.html", "About"),
    ("privacy.html", "Privacy"),
    ("terms.html", "Terms"),
    ("refund.html", "Refunds"),
    ("contact.html", "Contact"),
]


def header(current):
    here = ' aria-current="page"'
    links = "".join(
        f'<a href="{href}"{here if href == current else ""}>{label}</a>'
        for href, label in PAGES
    )
    return (
        '<header class="site"><div class="inner">'
        '<a class="brand" href="index.html">Expendracker</a>'
        f"<nav>{links}</nav></div></header>"
    )


FOOTER = (
    '<footer class="site"><div class="inner">'
    "Expendracker is developed by {NAME}, India · "
    '<a href="mailto:{EMAIL}">{EMAIL}</a> · '
    '<a href="privacy.html">Privacy</a> · <a href="terms.html">Terms</a> · '
    '<a href="refund.html">Refunds</a> · <a href="contact.html">Contact</a>'
    "</div></footer>"
)


def page(file, title, description, body):
    html = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{description}">
<link rel="stylesheet" href="site.css">
</head>
<body>
{header(file)}
<main>
{body}
</main>
{FOOTER}
</body>
</html>
"""
    for key, value in FACTS.items():
        html = html.replace("{" + key + "}", value)
    (HERE / file).write_text(html, encoding="utf-8", newline="\n")


page("index.html", "Expendracker", "Expendracker records your spending automatically from your bank's SMS alerts. An Android app for India.", """
  <h1>Expendracker</h1>
  <p class="lead">An Android app that records your spending automatically from your bank's SMS alerts, so your month adds itself up without you typing anything.</p>

  <h2>What it does</h2>
  <ul>
    <li>Captures spending and income from bank and UPI transaction SMS alerts</li>
    <li>Imports past transactions from your inbox for any date range you choose</li>
    <li>Files each payment under a label, and learns your merchants as you go</li>
    <li>Shows where your money went this month: what you spent and what you received</li>
    <li>Lets you add cash spending and income by hand</li>
    <li>Optional backup of your records to your own Google Drive</li>
  </ul>

  <h2>Private by design</h2>
  <p>There is no Expendracker server and no account to create. Your transactions stay on your phone. Messages that are not transactions are ignored, and message text is never stored or sent anywhere. Read the full <a href="privacy.html">privacy policy</a>.</p>

  <h2>Pricing</h2>
  <table class="facts">
    <tr><th>Download and core features</th><td>Free</td></tr>
    <tr><th>Backup unlock</th><td>One-time in-app purchase of {PRICE} (inclusive of applicable taxes), made through Google Play. It enables backup of your records to your own Google Drive.</td></tr>
    <tr><th>Subscriptions</th><td>None</td></tr>
  </table>
  <p>Purchases are processed by Google Play. See the <a href="refund.html">refund and cancellation policy</a> and the <a href="terms.html">terms of use</a>.</p>

  <h2>Get the app</h2>
  <p>Expendracker is available for Android on Google Play (package <code>com.expendracker</code>), currently in testing. It works with Indian banks and UPI apps.</p>

  <h2>Developer</h2>
  <p>Expendracker is developed and sold by {NAME}, an individual developer in India. <a href="contact.html">Contact details</a>.</p>
""")

page("terms.html", "Expendracker Terms of Use", "Terms of use for the Expendracker Android app.", """
  <h1>Terms of Use</h1>
  <p class="meta">Last updated {UPDATED}</p>

  <p>These terms apply to the Expendracker app for Android (<code>com.expendracker</code>), provided by {NAME}, an individual developer in India ("we", "us"). By installing or using the app you agree to them. If you do not agree, please do not use the app.</p>

  <h2>1. The app</h2>
  <p>Expendracker helps you keep a record of your own spending by reading transaction alerts from your bank and UPI apps on your phone. We grant you a personal, non-exclusive, non-transferable licence to use the app on devices you own or control, for your own personal, non-commercial use.</p>

  <h2>2. Your responsibilities</h2>
  <ul>
    <li>You must be 18 or older to use the app.</li>
    <li>You choose whether to give the app permission to read SMS. It only works with messages on your own phone.</li>
    <li>You are responsible for keeping your phone and Google account secure.</li>
    <li>You must not reverse engineer, resell or misuse the app, or use it for any unlawful purpose.</li>
  </ul>

  <h2>3. Not financial advice</h2>
  <p>Expendracker is a record-keeping tool. It does not provide financial, tax, investment or legal advice, and it does not move, hold, lend or invest money.</p>

  <h2>4. Accuracy</h2>
  <p>The app reads amounts, merchants and dates from messages written by your bank. Banks change their message formats, and some messages may be read incorrectly or missed. Always rely on your bank statements for official figures. You can correct or delete any entry in the app.</p>

  <h2>5. Purchases</h2>
  <ul>
    <li>The app is free. The optional backup unlock is a one-time in-app purchase of {PRICE}, inclusive of applicable taxes, sold through Google Play.</li>
    <li>Payment is processed by Google Play under Google's terms. We never receive your card, UPI or bank details.</li>
    <li>The unlock is a digital feature delivered immediately after purchase. It is tied to the Google Play account that bought it and is restored automatically when you reinstall the app with that account.</li>
    <li>Refunds and cancellations are covered by our <a href="refund.html">refund and cancellation policy</a>.</li>
  </ul>

  <h2>6. Backup</h2>
  <p>If you turn on backup, a copy of your records is stored in your own Google Drive, under your Google account and Google's terms. You can delete it at any time. We do not have access to it.</p>

  <h2>7. Privacy</h2>
  <p>How the app handles your information is described in the <a href="privacy.html">privacy policy</a>, which forms part of these terms.</p>

  <h2>8. Changes and availability</h2>
  <p>We may update the app, add or remove features, or stop providing it. If we stop providing a paid feature within 12 months of your purchase, you may ask us for a refund as described in the refund policy.</p>

  <h2>9. Disclaimer and limitation of liability</h2>
  <p>The app is provided "as is", without warranties of any kind, to the extent permitted by law. We are not liable for any indirect or consequential loss, or for decisions you make based on the app's records. Our total liability to you for any claim is limited to the amount you paid for the app in the 12 months before the claim.</p>

  <h2>10. Governing law</h2>
  <p>These terms are governed by the laws of India. Any dispute is subject to the exclusive jurisdiction of the courts at {CITY}, India.</p>

  <h2>11. Changes to these terms</h2>
  <p>We may update these terms. The date at the top shows the latest version. Continuing to use the app after a change means you accept the updated terms.</p>

  <h2>12. Contact</h2>
  <p>{NAME} · <a href="mailto:{EMAIL}">{EMAIL}</a> · <a href="contact.html">all contact details</a></p>
""")

page("refund.html", "Expendracker Refund and Cancellation Policy", "Refund and cancellation policy for purchases in the Expendracker Android app.", """
  <h1>Refund and Cancellation Policy</h1>
  <p class="meta">Last updated {UPDATED}</p>

  <h2>What you can buy</h2>
  <p>Expendracker is free to download and use. The only paid item is the <strong>backup unlock</strong>: a one-time in-app purchase of {PRICE} (inclusive of applicable taxes) that enables backup to your own Google Drive. It is a digital feature, delivered immediately. There are no subscriptions or recurring charges.</p>

  <h2>Cancellation</h2>
  <p>Because there is no subscription, there is nothing to cancel after purchase. You can cancel a purchase before completing it by closing the Google Play payment screen. If a payment is still pending, it is cancelled automatically by Google Play if it does not complete.</p>

  <h2>Refunds</h2>
  <ol>
    <li><strong>Within 48 hours of purchase:</strong> request a refund directly from Google Play at <a href="https://play.google.com/store/account/orderhistory">play.google.com/store/account/orderhistory</a>, choose the order, then <em>Request a refund</em>. Google decides these requests under its own policy.</li>
    <li><strong>Within {REFUND_DAYS} days of purchase:</strong> email us at <a href="mailto:{EMAIL}">{EMAIL}</a> with your Google Play order number (it starts with <code>GPA.</code>) and the reason. If the backup does not work for you and we cannot fix it, we refund the full amount.</li>
    <li><strong>If we discontinue the backup feature</strong> within 12 months of your purchase, we refund the full amount on request.</li>
  </ol>
  <p>Approved refunds are issued through Google Play to your original payment method. Google Play usually processes them within 3 to 5 business days, although your bank may take longer to show the credit. Once refunded, the backup unlock is removed from your account. Your records on your phone and any backup file already in your Drive are not affected.</p>

  <h2>Contact</h2>
  <p>{NAME} · <a href="mailto:{EMAIL}">{EMAIL}</a></p>
""")

page("contact.html", "Contact Expendracker", "Contact details for Expendracker and its developer.", """
  <h1>Contact</h1>
  <p class="lead">Questions, support, refunds or privacy requests: we usually reply within 2 business days.</p>

  <table class="facts">
    <tr><th>Developer</th><td>{NAME} (individual developer)</td></tr>
    <tr><th>Email</th><td><a href="mailto:{EMAIL}">{EMAIL}</a></td></tr>
    <tr><th>Location</th><td>{ADDRESS}</td></tr>
    <tr><th>App</th><td>Expendracker for Android, <code>com.expendracker</code></td></tr>
  </table>

  <h2>Common requests</h2>
  <ul>
    <li><strong>Refunds:</strong> see the <a href="refund.html">refund and cancellation policy</a>.</li>
    <li><strong>Deleting your data:</strong> see <a href="privacy.html#delete-data">how to delete your Expendracker data</a>. We hold none of your data ourselves.</li>
    <li><strong>Terms:</strong> see the <a href="terms.html">terms of use</a>.</li>
  </ul>
""")

# Privacy: shared stylesheet, header and footer; body untouched apart from the
# developer's name and contact email.
privacy = (HERE / "privacy.html").read_text(encoding="utf-8")
privacy = re.sub(r"<style>.*?</style>", '<link rel="stylesheet" href="site.css">', privacy, flags=re.S)
privacy = re.sub(r"<header class=\"site\">.*?</header>\n", "", privacy, flags=re.S)
privacy = re.sub(r"<footer class=\"site\">.*?</footer>\n", "", privacy, flags=re.S)
privacy = privacy.replace("<body>\n<main>", "<body>\n" + header("privacy.html") + "\n<main>")
privacy = privacy.replace("</main>\n</body>", "</main>\n" + FOOTER + "\n</body>")
privacy = privacy.replace("developed by Vignesh J, an individual", "developed by {NAME}, an individual")
privacy = re.sub(r'<a href="mailto:[^"]+">[^<]+</a></p>\n</main>', '<a href="mailto:{EMAIL}">{EMAIL}</a></p>\n</main>', privacy)
for key, value in FACTS.items():
    privacy = privacy.replace("{" + key + "}", value)
(HERE / "privacy.html").write_text(privacy, encoding="utf-8", newline="\n")
print("built", ", ".join(p for p, _ in PAGES))
