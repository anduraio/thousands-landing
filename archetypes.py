# -*- coding: utf-8 -*-
"""Copy archetypes for lite sectors.

A "lite" sector (see data6..data10) hand-writes only what makes it unique —
name, audience, a few sector-specific features and its four brands — and
borrows the rest (stats, plans, testimonials, FAQs, filler features) from one
of these archetypes, with {audience} / {name} placeholders filled in.
"""

ARCHETYPES = {
    "booking": dict(
        generic=[
            ("📅", "Instant booking for {audience}", "Live availability that books itself, day and night."),
            ("🔔", "Reminders that cut no-shows", "Confirmations and nudges that keep every slot filled."),
            ("💳", "Payments and packages", "Take payment, deposits and passes at booking time."),
            ("🗓️", "Syncs with your calendar", "Two-way sync with Google, Outlook and Apple calendars."),
            ("⭐", "Reviews that compound", "Feedback requested at the perfect moment."),
        ],
        stats=[("4,200", "operators"), ("2.9M", "bookings monthly"), ("-41%", "no-shows"), ("4.9★", "customer rating")],
        plans=[("Standard", 29, "One location, unlimited bookings for {audience}."), ("Pro", 79, "Adds packages, deposits and reporting."), ("Enterprise", "custom", "Multi-site rollouts with SSO and SLAs.")],
        testimonials=[
            ("Bookings doubled in the first month — the calendar just filled.", "Dana Whitfield", "Owner"),
            ("No-shows dropped by half with deposits and reminders.", "Marcus Webb", "Director"),
            ("Our front desk finally does the work humans should do.", "Priya Sharma", "Manager"),
            ("Set up in an afternoon and it paid for itself the same week.", "Owen Reid", "Founder"),
        ],
        faqs=[
            ("Do customers need an app?", "No — booking, payments and reminders run from any browser link."),
            ("Can we set deposits and cancellation rules?", "Yes — policies are enforced automatically at checkout."),
            ("Which calendars does it sync with?", "Google, Outlook, Apple and most booking platforms."),
            ("How fast can {name} go live?", "Most {audience} are taking bookings the same day."),
        ],
    ),
    "marketplace": dict(
        generic=[
            ("🛒", "Listings in minutes", "Create, edit and promote listings with photos and prices."),
            ("🤝", "Safe, secure payments", "Money held until both sides are happy."),
            ("⭐", "Ratings that build trust", "Verified reviews from real transactions."),
            ("🔎", "Discovery that converts", "Search and filters tuned to what buyers want."),
            ("🛡️", "Protection included", "Dispute support and guarantees on every order."),
        ],
        stats=[("180k", "sellers"), ("3.4M", "buyers"), ("$2.1B", "traded annually"), ("4.8★", "user rating")],
        plans=[("Seller", 0, "List and sell — small fee per completed order."), ("Pro", 19, "Lower fees, analytics and promoted listings."), ("Business", 59, "Shops, teams and volume selling.")],
        testimonials=[
            ("We sell out every week now — buyers trust the platform.", "Sofia Marino", "Seller"),
            ("The protection means neither side gets burned. That's the product.", "James Park", "Buyer"),
            ("Fees are fair and payouts are fast. Simple as that.", "Anika Rao", "Power seller"),
        ],
        faqs=[
            ("What does it cost to sell?", "Nothing to list — a small fee applies only when you sell."),
            ("When do I get paid?", "Payouts land 24–48 hours after the buyer confirms."),
            ("How are disputes handled?", "A specialist team reviews evidence and refunds fairly."),
            ("Can shops have multiple staff?", "Yes — roles and permissions on Business plans."),
        ],
    ),
    "fieldservice": dict(
        generic=[
            ("📸", "Quotes from photos", "Price jobs without driving to site — approve remotely."),
            ("🗺️", "Crews routed by day", "Schedules that pack more jobs into every route."),
            ("✅", "Checklists and proof", "Every job documented with photos and sign-off."),
            ("🧾", "Invoices on the spot", "Bill before the van leaves the driveway."),
            ("🔁", "Recurring work, automatic", "Maintenance plans that renew and schedule themselves."),
        ],
        stats=[("2,900", "companies"), ("1.8 hrs", "saved daily"), ("+23%", "jobs per week"), ("4.8★", "client rating")],
        plans=[("Crew", 39, "One team, unlimited jobs for {audience}."), ("Company", 99, "Multiple crews, routing and quotes."), ("Enterprise", "custom", "Multi-branch with ERP integrations.")],
        testimonials=[
            ("One extra job per crew per day. The maths is silly.", "Carlos Mendes", "Owner"),
            ("Quotes from photos close in a day instead of a week.", "Rebecca Stone", "Operations"),
            ("Customers love the photo reports on every invoice.", "Janet Wu", "Client"),
        ],
        faqs=[
            ("Does it work offline on site?", "Yes — jobs, photos and sign-offs sync when you're back online."),
            ("Can customers approve remotely?", "Yes — quotes open from a link with one-tap approval."),
            ("Does it handle recurring contracts?", "Maintenance plans schedule and bill automatically."),
            ("What hardware do crews need?", "Any phone or tablet — nothing else."),
        ],
    ),
    "b2bops": dict(
        generic=[
            ("⚙️", "Live in a day", "Import your data and invite the team — no consultants."),
            ("🔌", "Integrations included", "Connects to the tools your {audience} already run."),
            ("📊", "Dashboards, not spreadsheets", "Live metrics that replace the Friday report."),
            ("🔐", "Roles and audit trails", "The right access for every teammate, fully logged."),
            ("🤖", "Automation, built in", "Routine steps happen without anyone asking."),
        ],
        stats=[("7,400", "companies"), ("9 hrs", "saved weekly"), ("+19%", "throughput"), ("4.8★", "team rating")],
        plans=[("Team", 49, "Up to 10 seats for {audience}."), ("Business", 149, "Unlimited seats, integrations and API."), ("Enterprise", "custom", "SSO, data residency and custom SLAs.")],
        testimonials=[
            ("The Friday report now writes itself before anyone asks.", "Grace Liu", "Head of Operations"),
            ("Onboarding took a day, not a quarter of consulting.", "Jonas Weber", "COO"),
            ("We stopped duct-taping five tools together.", "Marta Nowak", "Team lead"),
        ],
        faqs=[
            ("How long is implementation?", "Most {audience} import data and go live within a day."),
            ("Which integrations are supported?", "40+ native connectors plus a full API."),
            ("Can we control permissions?", "Yes — role-based access with complete audit logs."),
            ("Is our data secure?", "SOC 2 Type II, encryption at rest and in transit."),
        ],
    ),
    "commerce": dict(
        generic=[
            ("🛍️", "A store that's fast", "Storefronts that score 95+ on mobile speed."),
            ("💳", "Checkout that converts", "One-page checkout with wallets and local methods."),
            ("📦", "Shipping, sorted", "Live rates, labels and tracking out of the box."),
            ("📈", "Merchandising that learns", "Recommendations and bundles that lift every order."),
            ("✉️", "Customers who return", "Abandoned-cart and win-back flows on autopilot."),
        ],
        stats=[("12,400", "stores"), ("+29%", "conversion"), ("4.1M", "orders monthly"), ("4.8★", "merchant rating")],
        plans=[("Launch", 29, "Everything to start selling for {audience}."), ("Grow", 79, "Adds automation, segments and reports."), ("Scale", 249, "Headless APIs, SLAs and priority support.")],
        testimonials=[
            ("Conversion up 30% the month we moved. Sales didn't change, the checkout did.", "Sofia Marino", "Store owner"),
            ("Shipping used to eat a day a week. Now it's minutes.", "James Park", "Ops lead"),
            ("The abandoned-cart emails paid for the year in a month.", "Anika Rao", "Founder"),
        ],
        faqs=[
            ("Can we migrate our existing store?", "Yes — products, customers and orders import in hours."),
            ("Are there transaction fees?", "0% on annual plans beyond payment processing."),
            ("Do you handle taxes?", "Automatic sales tax, VAT and GST calculation."),
            ("Can we customize everything?", "Themes, an editor, or full headless access."),
        ],
    ),
    "community": dict(
        generic=[
            ("👥", "Members, organized", "A directory, profiles and groups your members actually use."),
            ("📣", "Comms that land", "Announcements and digests to the right people only."),
            ("🎟️", "Events, ticketed", "Meetups and programs with RSVPs and payments."),
            ("💳", "Dues on autopilot", "Membership renewals that collect themselves."),
            ("🛡️", "Healthy spaces", "Moderation tools that keep the community kind."),
        ],
        stats=[("3,100", "communities"), ("410k", "members"), ("87%", "renewal rate"), ("4.9★", "member rating")],
        plans=[("Circle", 19, "Up to 100 members for {audience}."), ("Community", 49, "Unlimited members, events and dues."), ("Network", 149, "Chapters and federated groups.")],
        testimonials=[
            ("Renewals took care of themselves the first season.", "Grace Adeyemi", "Community lead"),
            ("Events filled up without a single group-chat argument.", "Peter Lindgren", "Organizer"),
            ("New members introduce themselves now. That's new.", "Fatima Noor", "Moderator"),
        ],
        faqs=[
            ("Do members need accounts?", "A magic link works — accounts are optional."),
            ("Can we charge dues?", "Yes — recurring memberships with autopay."),
            ("Does it support chapters?", "Network plan runs federated local groups."),
            ("Is moderation included?", "Tools plus optional AI screening on every plan."),
        ],
    ),
    "content": dict(
        generic=[
            ("✍️", "Publish, everywhere", "One draft to your site, feed and newsletter."),
            ("📈", "Honest analytics", "Know what resonates without the vanity metrics."),
            ("💰", "Monetize your way", "Subscriptions, tips and sponsor slots built in."),
            ("🗂️", "An archive that works", "Everything searchable and resurfacing for years."),
            ("👥", "An audience that grows", "Referrals and cross-promotion on autopilot."),
        ],
        stats=[("56k", "creators"), ("2.4M", "subscribers"), ("+31%", "audience growth"), ("4.9★", "creator rating")],
        plans=[("Free", 0, "Publish and grow, free forever."), ("Creator", 12, "Adds monetization and custom domains."), ("Pro", 29, "Team seats and advanced analytics.")],
        testimonials=[
            ("I post once and it's everywhere. My Sundays are mine again.", "Aiko Tanaka", "Creator"),
            ("The archive resurfacing drives half my new subscribers.", "Marcus Reid", "Writer"),
            ("First payout in week two. No thresholds, no nonsense.", "Elena Vasquez", "Podcaster"),
        ],
        faqs=[
            ("Who owns the content?", "You do — export everything, anytime."),
            ("Can I move my existing audience?", "Yes — import subscribers with one click."),
            ("What can I monetize?", "Subscriptions, one-off tips and sponsor placements."),
            ("Is there a free plan?", "Yes — publishing is free, always."),
        ],
    ),
    "care": dict(
        generic=[
            ("🤝", "Intake that feels human", "Assessments and history captured with warmth, not forms."),
            ("🗓️", "Sessions, scheduled", "Reminders and waitlists that keep care continuous."),
            ("🔒", "Private by design", "Encrypted records with access you control."),
            ("👨‍👩‍👧", "The circle, included", "Families and carers see what they should — nothing more."),
            ("📈", "Progress, visible", "Outcome tracking that shows care is working."),
        ],
        stats=[("5,600", "providers"), ("41k", "clients served"), ("96%", "show-up rate"), ("4.9★", "client rating")],
        plans=[("Solo", 39, "One practitioner, unlimited clients."), ("Practice", 99, "Teams, notes and family visibility."), ("Organization", "custom", "Multi-site with compliance packs.")],
        testimonials=[
            ("Families finally feel included instead of informed.", "Dr. Lena Vogt", "Clinician"),
            ("The intake is the first form our clients didn't dread.", "Omar Haddad", "Practice director"),
            ("Outcome data made our funding renewal easy.", "Amara Osei", "Program lead"),
        ],
        faqs=[
            ("Is client data encrypted?", "Yes — at rest and in transit, with access logs."),
            ("Can families see records?", "Only what you explicitly share, per client."),
            ("Do you sign BAAs?", "Yes — compliance agreements on every plan."),
            ("Can we migrate existing clients?", "Bulk import with mapping support included."),
        ],
    ),
    "learning": dict(
        generic=[
            ("🎓", "A curriculum that adapts", "Lessons that meet learners exactly where they are."),
            ("📊", "Progress you can see", "Mastery tracking per learner, per skill."),
            ("✅", "Assessments, graded", "Auto-marked practice with useful feedback."),
            ("📜", "Certificates that count", "Completion proof employers and boards accept."),
            ("📱", "Learn anywhere", "Full experience on phones, offline included."),
        ],
        stats=[("340k", "learners"), ("9,200", "programs"), ("82%", "completion rate"), ("4.8★", "learner rating")],
        plans=[("Start", 0, "First 30 learners free for {audience}."), ("Program", 6, "Per learner. Adds assessments and certificates."), ("Institution", "custom", "SSO, cohorts and custom content.")],
        testimonials=[
            ("Completion rates doubled — the pacing does the work.", "Rachel Simmons", "Program director"),
            ("Certificates our employers actually recognize.", "Marcus Bell", "Training manager"),
            ("Learners practice on phones during commutes. It stuck.", "Ines Duarte", "Instructor"),
        ],
        faqs=[
            ("Is there a free tier?", "Yes — 30 learners free forever, no ads."),
            ("Can we use our own content?", "Yes — upload, structure and brand everything."),
            ("Does it track certifications?", "Completion, expiry and renewals included."),
            ("Is progress visible to managers?", "Cohort and per-learner reporting on Program."),
        ],
    ),
    "fleetops": dict(
        generic=[
            ("📍", "Every vehicle, live", "Location, status and health on one map."),
            ("🔧", "Maintenance, predicted", "Service windows that prevent breakdowns."),
            ("📋", "Compliance, automatic", "Inspections, logs and certificates on file."),
            ("📱", "Driver-friendly apps", "One-screen tools crews actually use."),
            ("💰", "Costs, per vehicle", "Fuel, wear and downtime counted honestly."),
        ],
        stats=[("9,400", "operators"), ("74k", "vehicles tracked"), ("-18%", "running costs"), ("4.8★", "operator rating")],
        plans=[("Fleet", 6, "Per vehicle. Tracking and maintenance for {audience}."), ("Operations", 18, "Adds compliance, apps and routing."), ("Enterprise", "custom", "Integrations, SLAs and on-prem options.")],
        testimonials=[
            ("Breakdowns dropped by a third once maintenance went predictive.", "Sam Porter", "Fleet manager"),
            ("Compliance used to be a binder. Now it's a report.", "Nina Sokolov", "Ops director"),
            ("Drivers like the app — that never happens.", "Diego Ramos", "Dispatch lead"),
        ],
        faqs=[
            ("Do vehicles need hardware?", "Most 2016+ vehicles connect natively; dongles for the rest."),
            ("Can drivers use personal phones?", "Yes — the app is one screen, built for gloves."),
            ("Does it handle maintenance schedules?", "Mileage and hour-based service planning included."),
            ("Is there an API?", "Yes — full telemetry access on Operations."),
        ],
    ),
    "venue": dict(
        generic=[
            ("🎟️", "Bookings and capacity", "Space and session capacity managed to the seat."),
            ("🍿", "Food and drink, flowing", "Orders, stock and staff timed to the show."),
            ("🧑‍🏭", "Staffing that matches", "Rosters built from your forecast, not guesses."),
            ("📱", "Guests, self-served", "Order, find and check in from their phones."),
            ("📊", "The room, in numbers", "Spend per head and utilization per session."),
        ],
        stats=[("1,900", "venues"), ("+24%", "per-head spend"), ("-31%", "queue times"), ("4.8★", "guest rating")],
        plans=[("Venue", 99, "One site, bookings and orders."), ("Group", 249, "Multi-site with shared inventory."), ("Chain", 0, "Portfolio pricing and reporting.")],
        testimonials=[
            ("Spend per head rose a quarter — ordering is just easier.", "Sofia Marino", "Venue manager"),
            ("Staffing finally matches the forecast, not the vibes.", "James Park", "General manager"),
            ("Guests order from the table and the queue disappeared.", "Anika Rao", "Operations"),
        ],
        faqs=[
            ("Do guests need an app?", "No — QR ordering and maps run in the browser."),
            ("Does it integrate our tills?", "Square, Toast, Lightspeed and more."),
            "Can we run private events?", "Deposits, packages and run sheets included.",
            "Is there a kitchen display?", "Yes — routed orders with timing targets.",
        ],
    ),
    "finance": dict(
        generic=[
            ("📑", "Applications, streamlined", "Digital intake with document capture and checks."),
            ("🧮", "Decisions, faster", "Rules-driven scoring your team can audit."),
            ("🔐", "Compliance, provable", "KYC, AML and records kept to the letter."),
            ("💳", "Money movement", "Disbursements and collections with reconciliation."),
            ("📊", "The book, transparent", "Portfolio health by cohort, product and channel."),
        ],
        stats=[("820", "institutions"), ("$6.4B", "originated"), ("+21%", "approval accuracy"), ("4.7★", "partner rating")],
        plans=[("Desk", 249, "One team, unlimited applications."), ("Lender", 0, "Full origination with custom rules."), ("Platform", 0, "White-label and banking partners.")],
        testimonials=[
            ("Time-to-decision dropped from days to hours.", "Ruth Adebayo", "Lending director"),
            ("Auditors loved the evidence trail. That's a first.", "Robert Mensah", "Compliance officer"),
            ("Our brokers close twice as many cases a month.", "Grace Adeyemi", "Network manager"),
        ],
        faqs=[
            ("Is it regulation-ready?", "KYC/AML workflows with records kept to standard."),
            ("Can we use our own scorecards?", "Yes — your rules, fully auditable."),
            ("How are payments handled?", "Disbursement and collection rails built in."),
            ("Is there an API?", "Yes — apply, decide and settle via API."),
        ],
    ),
}

# Generic company names sliced as per-sector "Trusted by" logo strips.
LOGO_POOL = [
    "Northwind", "Brightlabs", "Fernwood", "Loopwell", "Kite & Co", "Cedarline", "Harborview",
    "The Stone Yard", "Bluepeak", "Fern & Fable", "Meridian", "Aperture", "Saltgrass", "Ironvale",
    "The Orchard", "Riverton", "Old Quarter", "Goldenhour", "Willow Street", "Copperfield",
    "The Junction", "Sunfield", "Longmeadow", "Fairview", "Stonebridge", "Windmill Row",
    "The Anchor", "Hollybrook", "Driftwood", "Redgate", "Milltown", "Kingsway", "Larkspur",
    "The Granary", "Ashford", "Bellweather", "Copperleaf", "Dunmore", "Eastvale", "Fernhill",
    "Glenarm", "Hollowell", "Ivywood", "Juniper & Co", "Kingsland", "Larkfield", "Maplewood",
    "Nightjar", "Oakhurst", "Pinewood", "Quarry Lane", "Rivergate", "Silvermine", "Thornbury",
    "Underhill", "Vine Street", "Westfold", "Yarrow & Sons", "Zephyr Works", "Bramblewick",
    "Casterly", "Dunhaven", "Elmsworth", "Fallowfield", "Greyhaven", "Hartsop", "Inglewood",
    "Jessamine", "Kelbrook", "Lorimer", "Marlowe", "Nettlebed", "Ockham", "Pemberley",
    "Quincey", "Rosewall", "Sallow", "Thistlewood", "Umberleigh", "Verlaine", "Wychwood",
]

# Normalize any copy banks written as bare strings into proper tuples.
def _fixa(seq, arity):
    out, i = [], 0
    while i < len(seq):
        if isinstance(seq[i], str):
            out.append(tuple(seq[i:i + arity])); i += arity
        else:
            out.append(seq[i]); i += 1
    return out

for _a in ARCHETYPES.values():
    _a["generic"] = _fixa(_a["generic"], 3)
    _a["stats"] = _fixa(_a["stats"], 2)
    _a["plans"] = _fixa(_a["plans"], 3)
    _a["testimonials"] = _fixa(_a["testimonials"], 3)
    _a["faqs"] = _fixa(_a["faqs"], 2)
