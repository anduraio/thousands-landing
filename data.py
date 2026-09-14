# -*- coding: utf-8 -*-
"""Content banks for 100 landing pages.

SECTORS  — per-sector copy banks (features, stats, plans, testimonials, faqs, logos).
BRANDS   — 100 products: (name, sector_key, headline, subhead).
"""

SECTORS = {
    "Fintech": dict(
        icon="💳", accent="#6d5dfc", accent2="#22c1dc", audience="finance teams",
        features=[
            ("💳", "Instant virtual cards", "Spin up unlimited virtual cards with per-merchant limits in two clicks."),
            ("🔄", "Automated reconciliation", "Every transaction matches itself against your ledger, nightly."),
            ("📊", "Real-time burn", "Runway recalculates the moment money moves — no spreadsheets."),
            ("🔐", "Role-based approvals", "Route any spend over a threshold to the right approver, automatically."),
            ("🧾", "Receipt capture", "Snap a receipt; OCR files it against the right transaction."),
            ("🌍", "Multi-currency", "Hold, convert and spend in 30+ currencies at mid-market rates."),
            ("📈", "Cashflow forecast", "A 13-week rolling forecast that updates itself every night."),
        ],
        stats=[("99.99%", "uptime SLA"), ("$4.2B", "processed annually"), ("11k+", "finance teams"), ("3 days", "to go live")],
        plans=[("Seed", 0, "For founders doing the books themselves."), ("Growth", 29, "Unlimited cards, approvals and integrations."), ("Scale", 89, "Multi-entity, ERP sync and a dedicated CSM.")],
        testimonials=[
            ("We closed the books in four days for the first time ever.", "Maya Chen", "Controller, Brightlabs"),
            ("Approvals used to live in Slack threads. Now they live in one place.", "Daniel Okafor", "CFO, Fernwood"),
            ("Our burn report updates before standup. It changed how we make decisions.", "Priya Raman", "Founder, Loopwell"),
            ("Reconciliation went from a Friday ritual to a complete non-event.", "Tom Alvarez", "Head of Finance, Kite & Co"),
        ],
        faqs=[
            ("How long does implementation take?", "Most teams connect their bank and card accounts in under an hour and run their first automated close within a week."),
            ("Is my financial data secure?", "Yes — SOC 2 Type II certified, AES-256 encryption at rest, and bank connections are strictly read-only until you approve an action."),
            ("Do you replace my accountant?", "No. We do the tedious matching and filing so your accountant can do the actual thinking."),
            ("Which tools do you integrate with?", "QuickBooks, Xero, NetSuite, Brex, Slack and 40+ others. API access is included on every plan."),
        ],
        logos=["Northwind", "Brightlabs", "Fernwood", "Loopwell", "Kite & Co"],
    ),
    "Healthcare": dict(
        icon="🩺", accent="#0ea5a4", accent2="#3b82f6", audience="care teams",
        features=[
            ("📅", "Smart scheduling", "Waitlists auto-fill cancellations the second they happen."),
            ("🔒", "HIPAA-compliant by default", "Encryption, audit logs and BAAs included on every plan."),
            ("🩺", "Intake before arrival", "Patients complete forms at home; your front desk stops shuffling paper."),
            ("💬", "Two-way reminders", "Text reminders that patients can actually reply to."),
            ("📋", "One shared chart", "Labs, notes and imaging in a single timeline per patient."),
            ("🧑‍⚕️", "e-Prescribe", "Renewals routed to the pharmacy in seconds, with interaction checks."),
            ("📈", "Panel insights", "Spot no-show patterns and chronic-care gaps across your panel."),
        ],
        stats=[("2.4M", "patients managed"), ("38%", "fewer no-shows"), ("9 min", "saved per visit"), ("HIPAA", "compliant")],
        plans=[("Solo practice", 49, "One provider, unlimited patients."), ("Clinic", 129, "Up to 10 providers with shared calendars."), ("Health system", 0, "Multi-site rollouts, SSO and custom SLAs.")],
        testimonials=[
            ("Our no-show rate dropped by half in the first quarter.", "Dr. Amara Osei", "Family Medicine, Cedar Clinic"),
            ("Intake used to eat 20 minutes per patient. Now it eats zero.", "Jonas Feld", "Practice Manager, Northbay Health"),
            ("The shared chart finally ended our 'where is the file' era.", "Dr. Lena Vogt", "Internist, Altstadt Praxis"),
        ],
        faqs=[
            ("Are you actually HIPAA compliant?", "Yes — we sign BAAs with every customer, encrypt PHI at rest and in transit, and log every access."),
            ("Does it work with my EHR?", "We integrate with Epic, Cerner, Athenahealth and DrChrono via HL7/FHIR."),
            ("Do patients need to download an app?", "No. Everything patients see works over SMS and a browser link."),
            ("How long is onboarding?", "Solo practices go live in a day; multi-site clinics typically in two weeks with our migration team."),
        ],
        logos=["Cedar Clinic", "Northbay Health", "Altstadt Praxis", "Riverton Med", "Bluepeak Care"],
    ),
    "Education": dict(
        icon="🎓", accent="#f59e0b", accent2="#8b5cf6", audience="teachers & learners",
        features=[
            ("🧠", "Adaptive practice", "Questions get harder as students improve — never boring, never crushing."),
            ("📝", "Auto-graded assignments", "Build once; every attempt grades itself with feedback."),
            ("📊", "Mastery dashboards", "See exactly which concept each student is stuck on."),
            ("🎮", "Game modes", "Turn any lesson set into a race, a quest or a review battle."),
            ("🏫", "LMS sync", "Rosters and grades flow to Canvas, Google Classroom or Moodle."),
            ("♿", "Accessibility built in", "Read-aloud, dyslexia fonts and translations on every item."),
            ("👨‍👩‍👧", "Parent digests", "A weekly progress email families actually read."),
        ],
        stats=[("640k", "students learning"), ("94%", "teacher retention"), ("12 min", "avg. daily practice"), ("40+", "languages supported")],
        plans=[("Teacher", 0, "Free for one teacher and up to 60 students."), ("School", 4, "Per student, per month. Admin tools included."), ("District", 0, "Custom pricing, SSO and priority support.")],
        testimonials=[
            ("My struggling readers ask to practice now. That has never happened.", "Rachel Simmons", "5th grade, Maple Elementary"),
            ("I got back six hours a week I used to spend grading.", "Marcus Bell", "HS Chemistry, Westfield High"),
            ("The mastery view means I walk into class already knowing who needs me.", "Ines Duarte", "Math Lead, Colégio Horizonte"),
        ],
        faqs=[
            ("Is it really free for teachers?", "Yes — one teacher with up to 60 students is free forever, with no ads."),
            ("Does it align to standards?", "Every item is tagged to Common Core, TEKS and Cambridge frameworks."),
            ("Can students use it on phones?", "Yes — full experience on iOS, Android and any browser."),
            ("How does student data privacy work?", "We're COPPA and FERPA compliant, and student data is never sold or used for ads."),
        ],
        logos=["Maple Elementary", "Westfield High", "Colégio Horizonte", "Lakeside Prep", "Nordic Academy"],
    ),
    "E-commerce": dict(
        icon="🛍️", accent="#ec4899", accent2="#f97316", audience="online stores",
        features=[
            ("🛒", "One-click checkout", "Cut checkout steps and watch conversion climb the same week."),
            ("✉️", "Abandoned cart rescue", "Timed emails and SMS that recover carts while you sleep."),
            ("📦", "Live shipping rates", "Real carrier rates and delivery dates at checkout."),
            ("🔎", "Smart search", "Typo-tolerant search that learns what shoppers actually want."),
            ("🧾", "Post-purchase upsells", "The thank-you page becomes your highest-margin shelf."),
            ("🌍", "Global selling", "Local currencies, duties and languages handled for you."),
            ("📲", "Mobile-first storefront", "Storefronts that score 95+ on mobile speed tests."),
        ],
        stats=[("+31%", "avg. conversion lift"), ("12M", "orders per month"), ("99.98%", "checkout uptime"), ("180+", "countries served")],
        plans=[("Starter", 19, "Everything to launch your first store."), ("Pro", 59, "Advanced merchandising and automation."), ("Enterprise", 249, "Headless APIs, SLAs and a launch engineer.")],
        testimonials=[
            ("Abandoned carts paid for the subscription a hundred times over.", "Sofia Marino", "Founder, Terra Ceramics"),
            ("We migrated 40,000 SKUs over a weekend with zero downtime.", "James Park", "CTO, Urban Trail Co."),
            ("Checkout speed alone lifted our mobile revenue 28%.", "Anika Rao", "Head of Digital, Bloom & Bough"),
        ],
        faqs=[
            ("Can I migrate from Shopify or WooCommerce?", "Yes — our importer moves products, orders and customers in a few hours, and redirects keep your SEO intact."),
            ("Are there transaction fees?", "0% on annual plans. You keep every cent of your margin beyond payment processing."),
            ("Do you handle taxes?", "Automatic sales tax, VAT and GST calculation and filing for 40+ countries."),
            ("Can I customize the storefront?", "Fully — themes, a drag-and-drop editor, or headless via our APIs."),
        ],
        logos=["Terra Ceramics", "Urban Trail Co.", "Bloom & Bough", "Fern + Fable", "Halo Goods"],
    ),
    "AI & Automation": dict(
        icon="🤖", accent="#8b5cf6", accent2="#06b6d4", audience="product teams",
        features=[
            ("⚡", "Ship in an afternoon", "Wrap any model behind a production API without an ML team."),
            ("🧩", "Bring your own model", "GPT, Claude, Llama or your fine-tune — swap anytime."),
            ("🛡️", "Guardrails included", "PII redaction, jailbreak shields and output validation out of the box."),
            ("📉", "Cost autopilot", "Routes simple calls to small models; cuts spend ~60% on average."),
            ("🔍", "Full traceability", "Every prompt, token and tool call logged and replayable."),
            ("🧪", "Eval suite", "Regression-test prompts like code before they ship."),
            ("🔌", "100+ tool connectors", "Let the agent read your docs, tickets and data — with permissions."),
        ],
        stats=[("60%", "lower inference spend"), ("9B+", "tokens served monthly"), ("3.5k", "teams building"), ("p95", "latency under 400ms")],
        plans=[("Hobby", 0, "10k requests/month, community support."), ("Team", 79, "Guardrails, evals and unlimited seats."), ("Enterprise", 0, "VPC deployment, SSO and custom models.")],
        testimonials=[
            ("We shipped our copilot in two weeks. Our old vendor quoted six months.", "Nikhil Shah", "VP Engineering, Draftline"),
            ("The routing autopilot cut our AI bill from $8k to $3k a month.", "Emma Laurent", "CTO, Quill & Query"),
            ("Replayable traces turned 'AI is random' into 'here's the failing step'.", "Ben Ortiz", "Staff Engineer, Relay Systems"),
        ],
        faqs=[
            ("Do I need ML experience?", "No. If you can write a prompt, you can ship a production endpoint."),
            ("Which models are supported?", "OpenAI, Anthropic, Google, Mistral, Llama and any OpenAI-compatible endpoint."),
            ("How do guardrails work?", "Every request passes configurable filters for PII, toxicity and prompt injection before and after the model."),
            ("Can it run in our own cloud?", "Enterprise plans deploy into your VPC on AWS, GCP or Azure."),
        ],
        logos=["Draftline", "Quill & Query", "Relay Systems", "Aperture Labs", "Nimbus AI"],
    ),
    "Cybersecurity": dict(
        icon="🛡️", accent="#0f766e", accent2="#22d3ee", audience="security teams",
        features=[
            ("🚨", "24/7 threat monitoring", "Analyst-reviewed alerts in minutes, not morning-after emails."),
            ("🔑", "Passwordless access", "Hardware keys and passkeys with device trust built in."),
            ("🧪", "Continuous pentesting", "Always-on researchers plus automated scans between engagements."),
            ("🎣", "Phishing simulations", "Realistic drills that train without shaming."),
            ("📋", "Compliance autopilot", "SOC 2 and ISO 27001 evidence collected as you work."),
            ("🕶️", "Dark web watch", "Get pinged the moment your credentials surface for sale."),
            ("🧯", "One-click response", "Isolate a laptop, rotate a secret or kill a session from your phone."),
        ],
        stats=[("4 min", "median response"), ("99.2%", "phish caught"), ("500+", "signals ingested"), ("0", "agents required")],
        plans=[("Essential", 12, "Per employee. Monitoring and training."), ("Advanced", 29, "Adds pentesting and response automation."), ("Enterprise", 0, "Dedicated analysts and custom SLAs.")],
        testimonials=[
            ("A compromised vendor credential surfaced in our dark-web feed at 2am. Rotated by 2:15.", "Grace Kim", "CISO, Harborline"),
            ("We passed SOC 2 with evidence that basically collected itself.", "Victor Hugo", "Head of IT, Stackmoor"),
            ("Our last phishing failure rate: 0.4%. Before: 19%.", "Aisha Bello", "Security Lead, Kernow Bank"),
        ],
        faqs=[
            ("Do agents slow down employee machines?", "There are no heavyweight agents — we read the signals your existing stack already produces."),
            ("Is pentesting really continuous?", "A standing research team probes your external surface weekly, with automated scans daily."),
            ("What does the response actually do?", "Isolate devices, revoke sessions, rotate secrets and open a timestamped incident record."),
            ("Which compliance frameworks are covered?", "SOC 2, ISO 27001, HIPAA, PCI-DSS and GDPR evidence workflows."),
        ],
        logos=["Harborline", "Stackmoor", "Kernow Bank", "Ironvale", "Cobalt Health"],
    ),
    "Real Estate": dict(
        icon="🏠", accent="#7c3aed", accent2="#f59e0b", audience="property owners",
        features=[
            ("🏦", "Rent on autopilot", "Tenants pay by ACH or card; late fees enforce themselves."),
            ("📸", "3D virtual tours", "Shoot once with your phone; every listing gets a walkthrough."),
            ("🔧", "Maintenance triage", "Tenants report issues with photos; vendors bid and get dispatched."),
            ("✍️", "E-sign leases", "State-compliant lease templates signed in minutes."),
            ("📊", "Portfolio analytics", "Cap rate, cash-on-cash and vacancy across every door."),
            ("🧾", "Expense tagging", "Snap receipts; Schedule E basically fills itself."),
            ("🔎", "Tenant screening", "Credit, income and eviction checks returned in minutes."),
        ],
        stats=[("220k", "units managed"), ("$1.9B", "rent collected"), ("-45%", "vacancy days"), ("4.8★", "tenant app rating")],
        plans=[("Landlord", 1, "Per unit, per month. Unlimited tenants."), ("Professional", 3, "Per unit. Adds vendor dispatch and analytics."), ("Enterprise", 0, "Institutional reporting and API access.")],
        testimonials=[
            ("I manage 60 doors from one screen, and I travel full-time.", "Derek Holmes", "Owner, Holmes Properties"),
            ("Tour-to-lease time dropped from 12 days to 4.", "Nadia Petrov", "Leasing Director, Skyline Residential"),
            ("Maintenance used to be 40 texts a day. Now it's a tidy queue.", "Luis Ferrer", "Property Manager, Costa Verde"),
        ],
        faqs=[
            ("Do tenants need an account?", "No — payments, maintenance requests and leases all work from a simple link."),
            ("Is screening fair-housing compliant?", "Yes, we use the same criteria for every applicant and provide the adverse-action letters."),
            ("Can I migrate from spreadsheets?", "Yes — upload a spreadsheet and we map units, leases and balances automatically."),
            ("When do I get paid?", "Rent hits your bank in 1–2 business days; Express payouts are same-day."),
        ],
        logos=["Holmes Properties", "Skyline Residential", "Costa Verde", "Oakline Group", "Haven Estates"],
    ),
    "Food & Beverage": dict(
        icon="🍜", accent="#ef4444", accent2="#f59e0b", audience="restaurants",
        features=[
            ("📱", "QR ordering", "Guests order and pay at the table; tickets hit your kitchen instantly."),
            ("🔥", "Kitchen display", "Course timing, allergy flags and prep counts on one screen."),
            ("🛵", "Delivery dispatch", "Your drivers or couriers — one queue, optimal routing."),
            ("🧾", "Menu engineering", "See which dishes make money and which just take up space."),
            ("⭐", "Review recovery", "Unhappy guests reach you privately before they reach Yelp."),
            ("📦", "Inventory countdown", "86 items auto-hide from the menu when stock runs out."),
            ("🎁", "Loyalty that returns", "Points, punch cards and birthday offers run themselves."),
        ],
        stats=[("8.5k", "restaurants"), ("+22%", "average ticket"), ("2 min", "table turnaround"), ("12%", "food waste cut")],
        plans=[("Café", 39, "One location, unlimited orders."), ("Restaurant", 89, "Adds kitchen display and delivery dispatch."), ("Group", 199, "Multi-location menus, pricing and reports.")],
        testimonials=[
            ("Average ticket went up $7 because the app suggests dessert every time.", "Marco Bianchi", "Owner, Trattoria Sole"),
            ("We stopped losing tickets during the Friday rush entirely.", "Keiko Tanaka", "GM, Sakura Ramen"),
            ("Third-party fees used to be 30%. Our own channel is now 55% of orders.", "Priya Nair", "Director, Chai & Chaat"),
        ],
        faqs=[
            ("Do I need special hardware?", "No — QR menus run on any phone, and the kitchen display runs on any tablet."),
            ("Does it work with my POS?", "We integrate with Square, Toast, Clover and Lightspeed."),
            ("What about menus in multiple languages?", "Yes — automatic translation with per-dish photo and pricing control."),
            ("How fast can we launch?", "Most restaurants go live the same day they sign up."),
        ],
        logos=["Trattoria Sole", "Sakura Ramen", "Chai & Chaat", "Grüner Table", "Solstice Café"],
    ),
    "Travel": dict(
        icon="✈️", accent="#0284c7", accent2="#f59e0b", audience="travelers",
        features=[
            ("🧭", "Itineraries in one prompt", "Say where and when; get a day-by-day plan with bookings."),
            ("💸", "Fare drops, refunded", "We watch prices and claim the difference automatically."),
            ("🗺️", "Offline everything", "Maps, tickets and translations work with zero bars."),
            ("🏨", "One-tap rebooking", "Delayed flight? Nearby hotels with rooms appear instantly."),
            ("👥", "Group planning", "Votes, budgets and shared lists end the group-chat chaos."),
            ("🛂", "Visa & entry checks", "Know the documents you need before you book, not at the gate."),
            ("🎒", "Local hidden gems", "Recommendations from people who live there, not ad budgets."),
        ],
        stats=[("1.2M", "trips planned"), ("$180", "avg. saved per trip"), ("96%", "on-time check-in"), ("190+", "countries covered")],
        plans=[("Explorer", 0, "Plan and share unlimited trips."), ("Frequent Flyer", 8, "Per month. Fare refunds and rebooking."), ("Pro", 19, "Per month. Expense reports and priority concierge.")],
        testimonials=[
            ("It rebooked me through Lisbon before the airline even announced the delay.", "Chloe Martin", "Product Designer"),
            ("Group trip to Kyoto with zero arguments. Historic.", "Ahmed Karim", "Software Engineer"),
            ("The fare refund feature has literally paid for my flights twice.", "Isabel Ortiz", "Sales Director"),
        ],
        faqs=[
            ("Does it book flights and hotels?", "Yes — flights, hotels, trains and activities are bookable inside the app, with price watching after."),
            ("How do fare refunds work?", "If the price of a watched flight drops before departure, we claim the difference with the airline or OTA on your behalf."),
            ("Can I use it offline?", "Yes — itineraries, maps and confirmations are cached for offline use."),
            ("Is there a web version?", "Yes, and everything syncs between devices instantly."),
        ],
        logos=["Nomad Atlas", "Trailpost", "Wander Weekly", "Skyteam Blog", "Roam & Co"],
    ),
    "Fitness & Wellness": dict(
        icon="🏋️", accent="#16a34a", accent2="#84cc16", audience="active people",
        features=[
            ("🏃", "Plans that adapt", "Missed a workout? The plan reshuffles instead of guilt-tripping."),
            ("🎧", "Audio coaching", "A coach in your earbuds pacing every interval."),
            ("📸", "Photo food logging", "Point, shoot, logged — macros estimated in seconds."),
            ("😴", "Recovery scoring", "Sleep and HRV decide whether today is PR day or stroll day."),
            ("🧘", "Five-minute resets", "Breathwork and mobility sessions that fit between meetings."),
            ("👥", "Accountability pods", "Small groups with streaks, nudges and zero shame."),
            ("⌚", "Watch native", "Apple Watch and Garmin apps that work phone-free."),
        ],
        stats=[("1.8M", "workouts logged weekly"), ("82%", "still active at 6 months"), ("4.9★", "app store rating"), ("150+", "pro coaches")],
        plans=[("Basic", 0, "Tracking and starter plans, free forever."), ("Athlete", 12, "Per month. Adaptive plans and audio coaching."), ("Studio", 29, "Per month. Live classes and 1:1 coach check-ins.")],
        testimonials=[
            ("Six months in and I've never had an app keep me honest like this.", "Jordan Lee", "Marathoner"),
            ("The recovery score stopped me from overtraining into injury again.", "Marta Kowalski", "Triathlete"),
            ("Photo logging made macros effortless. Down 9kg without counting anything else.", "Sam Whitfield", "New dad"),
        ],
        faqs=[
            ("Do I need gym equipment?", "No — every plan has a bodyweight variant, and it adapts to whatever you have."),
            ("Which devices are supported?", "Apple Watch, Garmin, Whoop, Oura, and Bluetooth heart-rate straps."),
            ("Can my coach use it?", "Yes — coaches get a dashboard to assign plans and monitor clients."),
            ("Is nutrition tracking included?", "Photo logging, macro targets and a barcode scanner are included on Athlete and Studio."),
        ],
        logos=["RunClub Nord", "Pulse Studio", "Summit CrossFit", "Glow Yoga", "Harbor Strength"],
    ),
    "Legal": dict(
        icon="⚖️", accent="#b45309", accent2="#78350f", audience="legal teams",
        features=[
            ("📄", "Contracts in minutes", "Answer plain-English questions; get a draft built on 10,000+ precedents."),
            ("🔍", "AI clause review", "Flags missing indemnities, bad limitation caps and sneaky auto-renewals."),
            ("✍️", "E-signature", "Court-admissible signing with a full audit trail."),
            ("🗂️", "Obligation tracking", "Every deadline and renewal date extracted and calendared."),
            ("🤝", "Negotiation history", "See how a clause changed across versions — and who pushed."),
            ("🔐", "Privilege preserved", "Bank-grade encryption with role-based access and retention rules."),
            ("🌐", "Multi-jurisdiction", "Templates validated across the US, UK, EU and APAC."),
        ],
        stats=[("10k+", "clause precedents"), ("83%", "faster drafting"), ("120k", "contracts signed monthly"), ("SOC 2", "Type II certified")],
        plans=[("Solo", 29, "For independents and freelancers."), ("Firm", 79, "Per seat. Adds review AI and templates."), ("Corporate", 0, "CLM integrations and custom playbooks.")],
        testimonials=[
            ("Our MSA turnaround went from two weeks to two days.", "Laura Kim", "General Counsel, Meridian SaaS"),
            ("The reviewer caught a liability cap that our team missed twice.", "Robert Mensah", "Partner, Mensah & Vo"),
            ("Freelancers like me finally send contracts that look like we have a legal dept.", "Tania Rossi", "Independent Consultant"),
        ],
        faqs=[
            ("Is this legal advice?", "No — it's drafting and review assistance. You approve everything, and law-firm plans can route to counsel."),
            ("Are the templates jurisdiction-specific?", "Yes, with jurisdiction pickers and localizations maintained by licensed attorneys."),
            ("Can I import existing contracts?", "Yes — bulk import with OCR, auto-extraction of parties, dates and obligations."),
            ("How secure is document storage?", "AES-256 at rest, TLS 1.3 in transit, and EU or US data residency options."),
        ],
        logos=["Meridian SaaS", "Mensah & Vo", "Bright Contracts", "Harbor Legal", "Vertex Compliance"],
    ),
    "Insurance": dict(
        icon="☂️", accent="#0369a1", accent2="#22c55e", audience="policyholders",
        features=[
            ("⚡", "Claims in hours", "Snap photos, get an adjuster AI review, money same week."),
            ("🏷️", "Fair, dynamic pricing", "Telematics and usage data lower premiums for careful people."),
            ("📄", "Plain-language policies", "Every exclusion translated into sentences humans can read."),
            ("🩹", "Coverage gaps, exposed", "We scan your life events and flag what's not covered."),
            ("🔧", "Bundle anything", "Home, auto, travel and gadgets on one renewal date."),
            ("🤖", "24/7 claims bot", "Start a claim at 3am; a human picks it up in the morning."),
            ("🛟", "Disaster fast-track", "Catastrophe mode waives deductibles and pre-approves hotels."),
        ],
        stats=[("48 hrs", "avg. claim payout"), ("4.7★", "claims satisfaction"), ("$310", "avg. annual savings"), ("A-", "AM Best rating")],
        plans=[("Essential", 9, "Per month. Core coverage, instant claims."), ("Complete", 24, "Adds gadgets, travel and liability."), ("Family", 39, "Everything bundled, one deductible cap.")],
        testimonials=[
            ("A pipe burst on Sunday; the claim was approved before Monday coffee.", "Helen Zhao", "Homeowner"),
            ("I finally understand what my policy actually excludes. That's the point.", "David Osei", "Renter"),
            ("Bundling three policies saved us $412 a year and one giant headache.", "Claire Fontaine", "Parent of three"),
        ],
        faqs=[
            ("How are claims paid so fast?", "Photo-based AI assessment pre-approves standard claims; a licensed adjuster reviews anything unusual."),
            ("Are you a real insurer?", "We're a licensed carrier (A- rated) with reinsurance backing, not a broker."),
            ("Can I cancel anytime?", "Yes, monthly plans are cancel- anytime with pro-rated refunds, no fees."),
            ("What isn't covered?", "We publish exclusions in plain language and show them before you buy, not after."),
        ],
        logos=["SafeHarbor", "UrbanNest Insurance", "DriveWise", "FamilyFirst Cover", "EverShield"],
    ),
    "Automotive": dict(
        icon="🚗", accent="#334155", accent2="#f97316", audience="drivers & fleets",
        features=[
            ("📝", "Sell without the lot", "List, inspect and get cash offers from verified dealers."),
            ("📊", "Fleet telemetry", "Fuel, idle time and driver scores across every vehicle."),
            ("⚡", "EV route planning", "Chargers filtered by speed, reliability and live availability."),
            ("🔧", "Mobile mechanics", "Book a vetted tech to your driveway; pay only when fixed."),
            ("🛞", "Maintenance autopilot", "Service reminders based on actual mileage, not guesses."),
            ("🛡️", "History reports", "Accident, ownership and recall data bundled into one trust score."),
            ("💰", "True cost to own", "Depreciation, insurance and fuel projected before you buy."),
        ],
        stats=[("94k", "vehicles sold"), ("1.2M", "fleet miles tracked daily"), ("$1,400", "avg. seller premium"), ("4.8★", "driver rating")],
        plans=[("Driver", 0, "Free for one vehicle."), ("Fleet", 6, "Per vehicle, per month. Telemetry and dispatch."), ("Dealer", 0, "Marketplace fees only, no subscription.")],
        testimonials=[
            ("Sold my sedan for $1,900 over the trade-in offer, without a single test drive.", "Omar Haddad", "Private seller"),
            ("Our 40-van fleet idles 22% less since we could actually see it.", "Bea Novak", "Ops Manager, CityCourier"),
            ("The mobile mechanic fixed my alternator in my office parking lot.", "Tom Riley", "Commuter"),
        ],
        faqs=[
            ("How do cash offers work?", "Dealers bid on your inspected vehicle; you pick the best offer and get paid on pickup."),
            ("Does telemetry need special hardware?", "Most cars 2016+ work through the OBD port or native connected-car APIs."),
            ("Are mobile mechanics vetted?", "Every tech is background-checked, insured and rated after each job."),
            ("Which EVs are supported for routing?", "All major makes, with live charger status from 12 networks."),
        ],
        logos=["CityCourier", "AutoNext", "CarFair", "FleetLine", "DriveHaus"],
    ),
    "Gaming": dict(
        icon="🎮", accent="#7c3aed", accent2="#ec4899", audience="players & creators",
        features=[
            ("🌍", "World builder", "Drag, paint and script levels with friends in real time."),
            ("🏆", "Auto-run tournaments", "Brackets, seeding and prize pools managed for you."),
            ("🎨", "Sprite animator", "Idle, walk and attack cycles generated from a single drawing."),
            ("🗣️", "Party voice", "Crystal-clear voice with music share and clip capture."),
            ("🕹️", "Cross-play SDK", "Ship to web, mobile and Steam with one build."),
            ("📊", "Creator analytics", "Retention, difficulty curves and rage-quit heatmaps."),
            ("🎁", "Season passes", "Battle-pass economy configured, not coded."),
        ],
        stats=[("2.1M", "monthly players"), ("31k", "community worlds"), ("120 fps", "netcode ceiling"), ("0", "uploads needed")],
        plans=[("Player", 0, "Play and create, free forever."), ("Creator", 9, "Per month. Analytics and monetization."), ("Studio", 49, "Per seat. Custom branding and exports.")],
        testimonials=[
            ("Our guild built a co-op campaign over one weekend and 40k people played it.", "Kai Fontaine", "Community creator"),
            ("Tournaments used to take a moderator team. Now they take me and a coffee.", "Lena Fischer", "Esports organizer"),
            ("The rage-quit heatmap told us exactly which level to fix. Retention up 18%.", "Dev Patel", "Indie studio founder"),
        ],
        faqs=[
            ("Can I monetize my worlds?", "Yes — Creator and Studio plans let you sell passes, skins and tip jars, with 80% revenue share."),
            ("What engines can I export to?", "One-click export to web, Unity and Godot projects on Studio plans."),
            ("Is voice chat moderated?", "Yes — real-time moderation, mute controls and reports handled within minutes."),
            ("Does cross-play really just work?", "One build targets web, iOS, Android and Steam with synchronized progression."),
        ],
        logos=["Pixel Harbor", "Guildline", "Nova Arcade", "Byteforge Games", "LevelUp Café"],
    ),
    "Media & Streaming": dict(
        icon="🎬", accent="#dc2626", accent2="#1d4ed8", audience="creators & fans",
        features=[
            ("🎞️", "Everything, one library", "Films, series, podcasts and live channels in a single guide."),
            ("✂️", "Auto-clipping", "Streams become highlights overnight, with captions."),
            ("🎙️", "Podcast studio", "Record, edit and publish with noise removal in the browser."),
            ("📺", "Watch parties", "Synced playback with voice and reactions for 200 friends."),
            ("📈", "Audience analytics", "Know where viewers drop and which clips convert."),
            ("🧠", "Recommendations that listen", "Taste profile you can actually edit and reset."),
            ("💸", "Creator payouts", "Tips, subs and rev-share with transparent dashboards."),
        ],
        stats=[("8M", "hours streamed monthly"), ("140k", "creators paid"), ("<2 s", "stream start time"), ("4K", "on every plan")],
        plans=[("Viewer", 6, "Ad-free viewing, one stream."), ("Creator", 19, "Per month. Studio tools and analytics."), ("Network", 99, "Multi-channel brands and team seats.")],
        testimonials=[
            ("Clipping my 6-hour streams into shorts took a full day. Now it's done before I wake up.", "Riko Tanabe", "Streamer, 90k followers"),
            ("Watch parties replaced our monthly movie club logistics entirely.", "Amelie Dubois", "Film pod host"),
            ("The analytics showed our intro was eating 40% drop-off. Fixed in a day.", "Sasha Meyer", "Podcast producer"),
        ],
        faqs=[
            ("Which devices stream?", "iOS, Android, web, Apple TV, Fire TV, Roku and Chromecast."),
            ("Do uploads have length limits?", "Creator plan allows streams up to 12 hours; clips are unlimited."),
            ("How does revenue share work?", "Creators keep 80% of tips and subscriptions; there are no minimum payout thresholds."),
            ("Can I import my podcast feed?", "Yes — paste your RSS and episodes migrate with artwork preserved."),
        ],
        logos=["Night Owl Radio", "Frame Perfect", "Cinephile Club", "StaticFM", "Reel Good Shows"],
    ),
    "Agriculture": dict(
        icon="🌾", accent="#4d7c0f", accent2="#ca8a04", audience="farmers",
        features=[
            ("🛰️", "Satellite scouting", "Field-by-field stress maps refreshed every three days."),
            ("💧", "Precision irrigation", "Soil moisture sensors decide when each zone drinks."),
            ("📦", "Farm-to-market sales", "List harvests; local buyers bid before you've left the field."),
            ("🐛", "Pest alerts", "Regional outbreak warnings tuned to what you actually grow."),
            ("🚜", "Machine logs", "Every pass, fuel hour and implement tracked automatically."),
            ("🧪", "Soil chemistry", "Lab results, recommendations and application records in one place."),
            ("💵", "Subsidy paperwork", "Grant and insurance forms pre-filled from your field data."),
        ],
        stats=[("4.6M", "acres monitored"), ("-19%", "water usage"), ("+9%", "yield avg"), ("62", "crops supported")],
        plans=[("Smallholder", 0, "Free for up to 5 hectares."), ("Farm", 2, "Per hectare, per month. Sensors and alerts."), ("Co-op", 0, "Group pricing, marketplaces and lending packs.")],
        testimonials=[
            ("We caught a fungal outbreak a week before we'd have seen it walking rows.", "Jan Willem", "3rd-generation grower"),
            ("Water use down a fifth and the corn never looked better.", "Rosa Aguilar", "Farm owner, 240 ha"),
            ("Selling directly to two co-ops doubled our margin on leafy greens.", "Peter Kariuki", "Vegetable farmer"),
        ],
        faqs=[
            ("Does it work without internet in the field?", "Yes — the app caches maps and forms and syncs whenever you get signal."),
            ("Which sensors are supported?", "Most LoRaWAN soil probes; we also sell pre-paired kits."),
            ("Can I add my agronomist?", "Yes — share field views with advisors at no extra seat cost."),
            ("How accurate are satellite stress maps?", "Cloud-free imagery at 10m resolution, validated against ground truth at 90%+ agreement."),
        ],
        logos=["Green Valley Farms", "AgroCentro", "Prairie Gold Co-op", "Sunrise Orchard", "Terra Roots"],
    ),
    "Construction": dict(
        icon="🏗️", accent="#ea580c", accent2="#0891b2", audience="builders",
        features=[
            ("📐", "RFI & submittal flow", "Approvals routed automatically; nothing stalls in an inbox."),
            ("📸", "Daily site logs", "Photo, weather and crew logs auto-compiled into reports."),
            ("🗺️", "Plan markups", "Current revision always on top, with old versions archived."),
            ("👷", "Crew time tracking", "Clock-in by geofence; certified payroll exports itself."),
            ("🧱", "Quantity tracking", "Pour, brick and drywall progress against the estimate in real time."),
            ("🦺", "Safety checklists", "Toolbox talks and incident forms signed on any phone."),
            ("🤝", "Owner transparency", "A live client portal that answers 'how's the project?' by itself."),
        ],
        stats=[("1,900", "active projects"), ("-6%", "cost overruns"), ("3×", "faster closeout"), ("34k", "daily site logs")],
        plans=[("Field", 35, "Per user, per month. Logs, plans and RFIs."), ("Builder", 65, "Per user. Adds budgets and owner portals."), ("Enterprise", 0, "ERP integrations and custom workflows.")],
        testimonials=[
            ("Closeout used to be a shoebox of PDFs. Last project: exported in an afternoon.", "Dave Cummings", "Superintendent, Rockridge Builders"),
            ("RFI turnaround dropped from nine days to two and subs actually thank us.", "Mina Park", "Project Manager, Skyline Commercial"),
            ("The owner portal killed the weekly 'surprise' phone call.", "Ahmed El-Sayed", "Principal, Cornerstone GC"),
        ],
        faqs=[
            ("Does it work offline on site?", "Yes — plans, forms and logs work offline and sync when you hit WiFi."),
            ("Can subs use it for free?", "Yes — unlimited free collaborator seats for subcontractors and owners."),
            ("How do plan revisions work?", "Upload a new set; old versions auto-archive and every markup links to its revision."),
            ("Does it integrate with accounting?", "Procore, QuickBooks, Sage and Viewpoint integrations on Builder and above."),
        ],
        logos=["Rockridge Builders", "Skyline Commercial", "Cornerstone GC", "Ironclad Inc.", "BlueStone Civil"],
    ),
    "Logistics": dict(
        icon="🚚", accent="#1d4ed8", accent2="#0d9488", audience="shippers",
        features=[
            ("🗺️", "Route optimization", "Stops sequenced by traffic, windows and weight — re-optimized hourly."),
            ("📄", "Instant freight quotes", "LTL and FTL rates from 40 carriers in 90 seconds."),
            ("🌡️", "Cold-chain proof", "Temperature logs signed every mile, exportable for audits."),
            ("📦", "Live ETAs", "Predictive arrival times your customers can subscribe to."),
            ("🛳️", "Customs paperwork", "HS codes, duties and docs pre-filled before the border."),
            ("🏭", "Dock scheduling", "Warehouse slots booked without a single email thread."),
            ("🧾", "Audit-proof billing", "Every invoice line reconciled against the actual shipment."),
        ],
        stats=[("680k", "deliveries monthly"), ("-24%", "cost per mile"), ("99.1%", "on-time rate"), ("40+", "carrier network")],
        plans=[("Starter", 99, "Up to 5 vehicles and 500 shipments/mo."), ("Growth", 349, "Adds optimization and customer ETAs."), ("Enterprise", 0, "Dedicated network and custom SLAs.")],
        testimonials=[
            ("Routing alone paid for the platform in the first month.", "Nina Sokolov", "COO, MetroFresh Delivery"),
            ("Quotes that took a day of calls now take 90 seconds.", "Ravi Menon", "Logistics Lead, PartsHive"),
            ("The temperature logs ended our insurance disputes overnight.", "Elena Marin", "QA Director, ChillWorks"),
        ],
        faqs=[
            ("Do drivers need training?", "The driver app is one screen — manifest, navigation, proof of delivery."),
            ("Which carriers are integrated?", "40+ LTL, FTL and parcel carriers with rate and tracking APIs."),
            ("Can customers track deliveries?", "Yes — branded tracking pages with live ETA and proactive delay alerts."),
            ("What hardware is required?", "Nothing beyond phones; optionally ELD and temperature sensors."),
        ],
        logos=["MetroFresh", "PartsHive", "ChillWorks", "CargoBridge", "LastMile Co"],
    ),
    "HR & Recruiting": dict(
        icon="🧑‍💼", accent="#2563eb", accent2="#a855f7", audience="people teams",
        features=[
            ("🤖", "AI shortlists", "Rank 800 applicants against your rubric in minutes."),
            ("📅", "Self-serve scheduling", "Candidates book interviews without a single email."),
            ("🧾", "Payroll on autopilot", "Taxes, benefits and payslips handled before Friday."),
            ("🌱", "Onboarding journeys", "Day-one accounts, swag and paperwork sequenced for you."),
            ("🔄", "Shift marketplace", "Employees swap shifts with rules you set, no group chat."),
            ("📝", "Performance, light", "Lightweight reviews people actually prepare for."),
            ("📊", "Headcount planning", "Model scenarios with comp, taxes and start dates."),
        ],
        stats=[("9 days", "avg. time-to-hire"), ("180k", "paychecks monthly"), ("71%", "less scheduling admin"), ("99.99%", "payroll accuracy")],
        plans=[("Startup", 59, "Per month. Hiring or payroll, pick one."), ("Scaleup", 189, "Per month. Both, plus onboarding."), ("Enterprise", 0, "Multi-country payroll and SSO.")],
        testimonials=[
            ("We went from 400 resumes in an inbox to a ranked shortlist with notes.", "Grace Liu", "Head of Talent, Brightpath Labs"),
            ("Payroll used to be my Friday. Now I forget it's Friday.", "Marc Dubois", "COO, Atelier Nord"),
            ("Shift swaps stopped being a war zone in our group chat.", "Fatima Zahra", "Store Manager, Bloom Café Group"),
        ],
        faqs=[
            ("Which countries does payroll cover?", "US, Canada, UK, EU and 20 more via partners on Enterprise."),
            ("Can candidates apply without an account?", "Yes — one-page applications with resume parsing."),
            ("Does it integrate with Slack/Teams?", "Deeply — approvals, pings and shift swaps live where your team already is."),
            ("Is the AI biased?", "Shortlists are rubric-based, auditable, and we run quarterly third-party bias audits."),
        ],
        logos=["Brightpath Labs", "Atelier Nord", "Bloom Café Group", "NorthStar Staffing", "Hummingbird HR"],
    ),
    "Climate & Energy": dict(
        icon="🌱", accent="#15803d", accent2="#65a30d", audience="households & businesses",
        features=[
            ("☀️", "Solar payoff, calculated", "Roof analysis and bill modeling before any salesperson calls."),
            ("🔌", "Smart load shifting", "Run appliances when power is cheapest and cleanest."),
            ("🌬️", "Real-time footprint", "Emissions tracked from your meter, not estimated yearly."),
            ("🧾", "Tariff detective", "Finds the cheaper utility plan you qualify for, automatically."),
            ("🔋", "Battery orchestration", "Charge when cheap, sell when the grid pays premium."),
            ("🌳", "Verified offsets", "Each project third-party audited with photos from the field."),
            ("🏘️", "Neighborhood challenges", "Block-by-block leaderboards that actually change habits."),
        ],
        stats=[("$384", "avg. annual savings"), ("120 GWh", "clean energy shifted"), ("1.4M", "tonnes CO₂ tracked"), ("96%", "savings accuracy")],
        plans=[("Home", 0, "Free forever for households."), ("Home+", 6, "Adds automation and battery control."), ("Business", 199, "Multi-site reporting and grid programs.")],
        testimonials=[
            ("It moved my EV charging and laundry to off-peak and cut the bill $41 a month.", "Julia Reyes", "Homeowner, Austin"),
            ("Our carbon report for the board used to take a consultant. Now it's a dashboard.", "Felix Brauer", "Sustainability Lead, Kanton Foods"),
            ("The tariff detective found a plan $28/month cheaper. One email, done.", "Nadia Osman", "Renter, Chicago"),
        ],
        faqs=[
            ("Does it work with my utility?", "Yes — we connect read-only to 900+ utilities or via your smart meter."),
            ("Is my energy data private?", "Encrypted, never sold, and used only to optimize your savings."),
            ("How are offsets verified?", "Only Gold Standard or Verra projects, with annual third-party audits."),
            ("Do I need a battery or EV?", "No — most savings come from timing and tariffs alone."),
        ],
        logos=["Kanton Foods", "GreenGrid Homes", "EcoBlock", "Terraview", "SunSide Energy"],
    ),
    "Crypto & Web3": dict(
        icon="⛓️", accent="#b45309", accent2="#0ea5e9", audience="self-custody users",
        features=[
            ("🔐", "Self-custody, human-friendly", "Your keys, encrypted and recoverable with guardians."),
            ("🌉", "One balance, ten chains", "Swap and bridge without juggling five wallets."),
            ("🪙", "Staking, simplified", "Delegate in two taps with slashing-risk disclosed up front."),
            ("🧾", "Tax autopilot", "Every trade, airdrop and fee categorized for your accountant."),
            ("🛡️", "Simulation before signing", "See exactly what a transaction does before it happens."),
            ("🚨", "Real-time alerts", "Drainers and muggings detected before you sign."),
            ("🏛️", "DAO tooling", "Proposals, votes and treasuries with readable receipts."),
        ],
        stats=[("$2.8B", "assets secured"), ("1.1M", "wallets"), ("12", "chains supported"), ("0", "custodied keys")],
        plans=[("Wallet", 0, "Free forever. Swap fees apply."), ("Pro", 9, "Per month. Tax tools and alerts."), ("Treasury", 0, "For DAOs: multisig, policies, reporting.")],
        testimonials=[
            ("I finally understand what I'm signing. That alone is worth it.", "Derek Wu", "DeFi user"),
            ("Bridging used to be four apps and a prayer. Now it's one screen.", "Amara Diallo", "NFT collector"),
            ("Tax autopilot turned 60 hours of spreadsheet hell into an export.", "Tomas Berg", "Ethereum staker"),
        ],
        faqs=[
            ("Do you ever hold my assets?", "Never — keys are encrypted on your devices; we can't move funds even if we wanted to."),
            ("What happens if I lose my phone?", "Social recovery with guardians you choose, or your seed phrase — your choice at setup."),
            ("Which chains are supported?", "Ethereum, L2s, Solana, Polygon, Arbitrum, Optimism, Base, Avalanche and more."),
            ("Is the tax report accepted by accountants?", "Exports match standard formats accepted in the US, UK, DE and 15 other jurisdictions."),
        ],
        logos=["DeFi Collective", "ChainFolk", "Mint Guild", "Proof Society", "Ledger Commons"],
    ),
    "Marketing": dict(
        icon="📣", accent="#e11d48", accent2="#7c3aed", audience="growth teams",
        features=[
            ("🪄", "A month of content, one afternoon", "Plan, draft and schedule 30 posts that still sound like you."),
            ("✉️", "Emails people open", "Subject lines tested against your own past winners."),
            ("🧲", "Funnels that fix themselves", "Every step instrumented; the weak one gets a suggested test."),
            ("🤝", "Referral engines", "Turn customers into a sales force with tracked rewards."),
            ("🎯", "Audience sync", "Segments push to Meta, Google and TikTok automatically."),
            ("📊", "One dashboard", "Ads, email, SEO and social in a single funnel view."),
            ("🧪", "Always-on experiments", "Statistical testing without the statistics degree."),
        ],
        stats=[("+38%", "avg. open-rate lift"), ("14k", "brands growing"), ("5 hrs", "saved weekly"), ("22", "integrations")],
        plans=[("Solo", 19, "One brand, unlimited scheduling."), ("Team", 49, "Adds funnels, referral and audiences."), ("Agency", 149, "Ten brands, white-label reports.")],
        testimonials=[
            ("Content calendar went from a dreaded doc to something I do with coffee on Mondays.", "Zoe Campbell", "Solo marketer"),
            ("The funnel diagnosis found a broken UTM we'd missed for months.", "Hugo Lindqvist", "Growth Lead, Kartell Apps"),
            ("Our referral program now drives 18% of new signups, on autopilot.", "Wei Zhang", "CMO, FreshMart"),
        ],
        faqs=[
            ("Does the AI sound generic?", "It trains on your best-performing copy and tone guide, not the internet's average."),
            ("Can I approve before anything publishes?", "Yes — approval queues with comments on every channel."),
            ("Which platforms are supported?", "Instagram, TikTok, LinkedIn, X, Facebook, YouTube, Mailchimp, Klaviyo and more."),
            ("Is there a free trial?", "14 days on every plan, no card required."),
        ],
        logos=["Kartell Apps", "FreshMart", "Loom & Latte", "Brightside Studio", "Petit Fournier"],
    ),
    "Developer Tools": dict(
        icon="🛠️", accent="#4f46e5", accent2="#0ea5e9", audience="engineering teams",
        features=[
            ("🚀", "Preview every branch", "Full-stack preview deploys with seeded databases, automatically."),
            ("🔁", "Background jobs", "Queues, retries and schedules without babysitting a worker box."),
            ("🧬", "Painless migrations", "Schema changes reviewed, staged and reversible."),
            ("🔭", "Traces, not logs", "One click from a slow request to the exact failing query."),
            ("🔐", "Secrets that rotate", "Encrypted, per-environment, rotated on schedule."),
            ("🧪", "CI that finishes", "Remote caching makes the same tests take a third of the time."),
            ("🤖", "API mocks", "Frontend keeps moving while the backend is still a sketch."),
        ],
        stats=[("p95 45s", "deploy time"), ("3.4M", "builds monthly"), ("68%", "CI time saved"), ("99.99%", "API uptime")],
        plans=[("Free", 0, "Hobby projects, generous limits."), ("Team", 20, "Per seat. Previews and job queues."), ("Enterprise", 0, "VPC peering, SSO and audit logs.")],
        testimonials=[
            ("Our CI bill dropped 60% and engineers stopped dreading main.", "Priya Sharma", "Staff Engineer, Loopline"),
            ("Preview environments ended the 'works on my machine' era for good.", "Jonas Weber", "CTO, Fernstack"),
            ("I found a 400ms N+1 in three clicks that we'd chased for a sprint.", "Marta Nowak", "Backend Lead, Tidepool"),
        ],
        faqs=[
            ("Which frameworks are supported?", "Next.js, Remix, Django, Rails, Go services — anything with a build command."),
            ("Can we self-host?", "Enterprise offers VPC deployment on AWS, GCP and Azure."),
            ("How do preview databases work?", "Each branch gets a seeded copy or branch of your Postgres/MySQL automatically."),
            ("Is there a free tier forever?", "Yes — generous hobby limits with no credit card."),
        ],
        logos=["Loopline", "Fernstack", "Tidepool", "Hexbase", "Kernelworks"],
    ),
    "Hospitality": dict(
        icon="🏨", accent="#9d174d", accent2="#b45309", audience="hotels & venues",
        features=[
            ("🛎️", "Direct bookings first", "A booking engine that pays you instead of the OTAs."),
            ("🗝️", "Contactless check-in", "Digital keys and ID scans; the front desk breathes again."),
            ("🧹", "Housekeeping sync", "Rooms flip to clean-and-ready the moment staff taps."),
            ("📜", "Menu design, automated", "Seasonal menus laid out and priced beautifully from your data."),
            ("💍", "Event command center", "Timelines, vendors and floor plans for every wedding."),
            ("💬", "Guest messaging", "One inbox for SMS, WhatsApp and OTA messages."),
            ("⭐", "Review radar", "Issues surface during the stay — not in a one-star review after."),
        ],
        stats=[("+27%", "direct bookings"), ("8 min", "avg. check-in"), ("4.9★", "guest rating"), ("1,400", "properties live")],
        plans=[("Boutique", 79, "Per month. Up to 20 rooms."), ("Hotel", 199, "Per month. Adds event and F&B modules."), ("Group", 0, "Portfolio pricing and loyalty engine.")],
        testimonials=[
            ("Direct bookings went from 18% to 45% of revenue in a season.", "Élodie Marchand", "Owner, Hôtel du Rivage"),
            ("Check-in queues at 3pm simply stopped existing.", "Ravi Chandran", "GM, Serai Beach Resort"),
            ("Event teams run four weddings a weekend without a binder in sight.", "Carla Mendes", "Events Director, Quinta Bela"),
        ],
        faqs=[
            ("Does it connect to channel managers?", "Yes — Booking.com, Airbnb and Expedia sync two-way."),
            ("Do guests need an app?", "No — digital keys and check-in run in the browser."),
            ("Can housekeeping use it offline?", "Yes — updates sync when staff return to staff WiFi."),
            ("Is there a lock-in contract?", "No — monthly plans, cancel anytime, data exportable."),
        ],
        logos=["Hôtel du Rivage", "Serai Beach Resort", "Quinta Bela", "The Alder House", "Vista Verde Inn"],
    ),
    "Pets": dict(
        icon="🐾", accent="#d97706", accent2="#0d9488", audience="pet parents",
        features=[
            ("📍", "GPS they can't lose", "Collar tracker with geofence alerts to your phone."),
            ("🏥", "Vet records, always", "Vaccines, meds and weight charts in one shareable timeline."),
            ("🥣", "Science-portioned meals", "Feeding plans by breed, age and vet guidance."),
            ("💊", "Med reminders", "Doses logged and the vet notified if one's missed."),
            ("🐶", "Walker network", "Background-checked sitters with GPS walks and notes."),
            ("🧬", "Breed & health insights", "DNA results translated into concrete care advice."),
            ("🐾", "Lost pet mode", "Community alert radius with live map and photo poster."),
        ],
        stats=[("310k", "pets protected"), ("42 min", "avg. lost-pet reunion"), ("4.9★", "parent rating"), ("18k", "vet clinics linked")],
        plans=[("Pet", 6, "Per pet, per month. Health + records."), ("Guardian", 12, "Per pet. Adds GPS tracker + cellular."), ("Household", 19, "Up to 4 pets, everything included.")],
        testimonials=[
            ("Biscuit slipped a fence at a rest stop. The alert found him in 20 minutes.", "Dana Whitfield", "Dog mom"),
            ("Every vet asks which meds, and now I just show them the timeline.", "Oscar Nilsson", "Cat parent ×2"),
            ("Portion plans took 4kg off our beagle. The vet is thrilled.", "Mei Lin", "Beagle owner"),
        ],
        faqs=[
            ("Is the GPS tracker waterproof?", "Yes — IP68 rated, swimmable, with a 10-day battery."),
            ("Can I share records with my vet?", "Yes — a share link gives your clinic read access instantly."),
            ("Which pets are supported?", "Dogs and cats today; birds and small mammals get records-only support."),
            ("What if my pet is lost?", "Lost Pet Mode blasts an alert to app users within a chosen radius with a live map."),
        ],
        logos=["Fetch & Field", "Whisker Clinic", "Pawsome Sitters", "The Happy Hound", "CityCat Vets"],
    ),
}

# (name, sector_key, headline, subhead)
BRANDS = [
    # Fintech
    ("Ledgerly", "Fintech", "Bookkeeping that closes itself", "Ledgerly matches every transaction to your ledger nightly, so the books are basically done before you wake up."),
    ("Paystream", "Fintech", "Instant payouts for modern teams", "Pay contractors and employees in minutes, not pay cycles — with taxes and compliance handled in the background."),
    ("Vaultic", "Fintech", "Bank-grade treasury for startups", "Sweep idle cash into T-bills automatically and see runway, burn and yield on one screen."),
    ("Kitta", "Fintech", "Spend cards your team will actually love", "Issue virtual and physical cards with smart limits, receipts and approvals built in."),
    # Healthcare
    ("Careloop", "Healthcare", "Primary care that fits in your pocket", "Same-day video visits, prescriptions and referrals — one continuous relationship with your care team."),
    ("Medscan", "Healthcare", "AI triage in under 60 seconds", "Patients describe symptoms; Medscan routes urgency, drafts the note and preps the chart before the visit."),
    ("Pulseboard", "Healthcare", "Remote monitoring that actually alerts", "Wearable and device data turned into actionable alerts, with escalation paths your staff trust."),
    ("Dentia", "Healthcare", "Dental practices, finally paperless", "Charts, imaging, recalls and claims in one system designed for the chairside."),
    # Education
    ("Brightpath", "Education", "A personal tutor for every student", "Adaptive lessons meet each learner where they are, with a human teacher always in the loop."),
    ("Quizforge", "Education", "Turn any PDF into a practice exam", "Drop in notes, a chapter or last year's paper; get spaced-repetition quizzes that grade themselves."),
    ("Campusly", "Education", "The LMS students actually open", "Assignments, feedback and grades in a mobile-first app with a 92% weekly active rate."),
    ("Skillstack", "Education", "Job-ready skills in 15 minutes a day", "Micro-courses with real projects and mentor feedback, designed around a work schedule."),
    # E-commerce
    ("Cartloom", "E-commerce", "Checkout that recovers itself", "Abandoned carts get perfectly timed nudges; most stores recover 12% of revenue in month one."),
    ("Shoplyft", "E-commerce", "Launch your store before lunch", "Pick a template, import products, connect payments — selling in under three hours, guaranteed."),
    ("Parcelbee", "E-commerce", "Shipping rates, slashed automatically", "Pre-negotiated carrier rates and label automation that cut shipping costs 20–40%."),
    ("Returnsy", "E-commerce", "Returns your customers won't dread", "Self-serve returns, instant exchanges and refunds that protect margin instead of torching it."),
    # AI & Automation
    ("Promptly", "AI & Automation", "Ship AI features without an ML team", "Production-grade LLM APIs with guardrails, evals and cost control — wired up in an afternoon."),
    ("Copyforge", "AI & Automation", "On-brand copy in every voice", "Trained on your best work, Copyforge drafts emails, ads and posts that pass the sniff test."),
    ("Meetkite", "AI & Automation", "Meetings that write themselves", "Notes, decisions and action items extracted live, then pushed to the tools where work happens."),
    ("Vectorvault", "AI & Automation", "Your knowledge, finally answerable", "Point it at your docs, tickets and wikis; get sourced answers with permissions intact."),
    # Cybersecurity
    ("Watchtower", "Cybersecurity", "Threats stopped before breakfast", "24/7 monitoring with analysts on call — alerts become incidents handled while you sleep."),
    ("Zerokey", "Cybersecurity", "Passwordless, provably", "Passkeys, hardware keys and device trust rolled out to your whole company in a week."),
    ("Redline", "Cybersecurity", "Pen-test coverage, always on", "Continuous offensive testing between formal engagements, with findings your devs can reproduce."),
    ("Phishnet", "Cybersecurity", "Phishing training that sticks", "Realistic simulations and micro-lessons that cut click rates by 90% in six months."),
    # Real Estate
    ("Doorlist", "Real Estate", "Rent collection on autopilot", "ACH and card payments, automatic late fees and instant payouts — tenants never need an account."),
    ("Keyframe", "Real Estate", "Virtual tours that close leases", "Phone-shot walkthroughs, floor plans and staging that convert browsers into applicants."),
    ("Tenantiq", "Real Estate", "Maintenance tickets, resolved faster", "Photo-based requests, vendor bidding and dispatch — tracked to the dollar per door."),
    ("Bricklane", "Real Estate", "Fractional ownership of prime rentals", "Start with $500 and own slices of income-generating buildings, with quarterly payouts."),
    # Food & Beverage
    ("Orderly", "Food & Beverage", "QR ordering that upsells itself", "Guests order and pay at the table while your ticket times drop and average checks rise."),
    ("Fridgechef", "Food & Beverage", "Dinner, from what's already in your kitchen", "Scan your fridge; get recipes ranked by what expires first, diets and skill included."),
    ("Kitchyn", "Food & Beverage", "Ghost kitchens without the guesswork", "Demand forecasts, prep lists and delivery dispatch tuned per menu, per neighborhood."),
    ("Savora", "Food & Beverage", "Reservations, waitlists and tables in sync", "One floor plan for front-of-house, servers and the kitchen — no more double-seating."),
    # Travel
    ("Wanderly", "Travel", "Trips planned in one prompt", "Say where and when; get flights, stays and a day-by-day plan you can actually edit."),
    ("Layover", "Travel", "Long layovers, short adventures", "Turns 6-hour layovers into guided city tours with luggage storage sorted."),
    ("Fareloop", "Travel", "Flight deals before anyone else", "Error fares and price drops for your routes, delivered in minutes with booking links."),
    ("Stayfolio", "Travel", "Vacation rentals, hotel-grade ops", "Dynamic pricing, cleaning dispatch and guest messaging for portfolios of any size."),
    # Fitness & Wellness
    ("Repmate", "Fitness & Wellness", "A coach in your earbuds", "Audio-guided workouts that count reps, correct pace and push exactly hard enough."),
    ("Zenrise", "Fitness & Wellness", "Five minutes to a calmer morning", "Micro-meditations, breathwork and journaling streaks that fit before the coffee's ready."),
    ("Stridex", "Fitness & Wellness", "Running plans that adapt daily", "Sleep, HRV and mileage recalibrate your next workout — PRs without the injury."),
    ("Macroly", "Fitness & Wellness", "Macros tracked from a photo", "Point your camera at the plate; protein, carbs and calories logged in seconds."),
    # Legal
    ("Clausesmith", "Legal", "Contracts drafted in minutes", "Plain-English intake, precedent-backed drafts and e-signature in a single flow."),
    ("Docketly", "Legal", "Case prep without the chaos", "Deadlines, exhibits and depositions organized automatically from your filings."),
    ("Complyharbor", "Legal", "Compliance calendars that run themselves", "Every filing, renewal and policy attestation tracked, assigned and evidenced."),
    ("Notaryze", "Legal", "Notarize documents from your couch", "Video-verified e-notarization in all 50 states, usually in under ten minutes."),
    # Insurance
    ("Shieldpay", "Insurance", "Claims paid in hours, not months", "Photo-based assessment, instant approval for standard claims, money same week."),
    ("Coverly", "Insurance", "Insurance that reads the fine print for you", "Upload any policy; get exclusions, gaps and overlaps explained in plain language."),
    ("Risklens", "Insurance", "Know your risk before it costs you", "Home and auto risk scores with concrete steps that lower your premium."),
    ("Fleetguard", "Insurance", "Fleet coverage priced by the mile", "Telematics-based commercial auto that rewards the safe routes, not the averages."),
    # Automotive
    ("Garagio", "Automotive", "Sell your car without the lot", "Verified dealers bid on your car; free pickup and payment on the same day."),
    ("Fleetwise", "Automotive", "Every vehicle, one dashboard", "Fuel, maintenance, drivers and compliance for fleets of 5 to 5,000."),
    ("Voltroute", "Automotive", "EV routing that never strands you", "Charger-reliable routes with live availability, weather and battery modeling."),
    ("Wrenchcall", "Automotive", "Mechanics who come to you", "Vetted mobile techs for brakes, batteries and diagnostics — in your driveway today."),
    # Gaming
    ("Questforge", "Gaming", "Build worlds with your friends", "Collaborative level design with built-in scripting, publishing and monetization."),
    ("Clashcup", "Gaming", "Tournaments for everyone", "Auto-bracketed competitions for any game, any skill level, with prize pools handled."),
    ("Spritecraft", "Gaming", "Animate characters in minutes", "One drawing becomes idle, walk and attack cycles — exportable to any engine."),
    ("Lobbyly", "Gaming", "Never squad up alone again", "Matchmaking by schedule, skill and vibe, with voice rooms and clip capture built in."),
    # Media & Streaming
    ("Reelmind", "Media & Streaming", "Every film, one subscription", "25,000 curated films and series across every genre, 4K and ad-free."),
    ("Podwave", "Media & Streaming", "Podcasts that grow themselves", "Recording, editing, hosting and cross-promotion — one studio, one feed."),
    ("Clipstream", "Media & Streaming", "Turn streams into clips overnight", "Your 6-hour stream becomes 20 captioned verticals, scheduled and posted."),
    ("Wavelength", "Media & Streaming", "Music for every mood, mixed live", "Adaptive mixes that shift with your heart rate, calendar and time of day."),
    # Agriculture
    ("Fieldnote", "Agriculture", "Scout crops from your phone", "Satellite stress maps, pest alerts and walk-row notes in one offline-ready app."),
    ("Harvestly", "Agriculture", "Sell straight from the farm", "List harvests at 7am; local restaurants and co-ops bid before noon."),
    ("Irrigo", "Agriculture", "Water only where it matters", "Soil sensors and weather models run each zone on its own schedule."),
    ("Herdbook", "Agriculture", "Livestock records, finally simple", "Breeding, health and feed records per animal, synced across the whole team."),
    # Construction
    ("Plancrate", "Construction", "Submittals that don't stall projects", "Automated routing and reminders cut submittal turnaround from weeks to days."),
    ("SiteSync", "Construction", "Every crew, one daily plan", "Morning briefs, task boards and photo logs that supers actually use."),
    ("Buildfolio", "Construction", "Track builds from dirt to keys", "Budgets, schedules and owner updates in one live project view."),
    ("Safetybeam", "Construction", "Site safety, digitized", "Toolbox talks, inspections and incident reports signed on any phone."),
    # Logistics
    ("Routebee", "Logistics", "Last mile, optimized hourly", "Stop sequences recomputed as traffic and orders change — drivers just follow."),
    ("Crateflow", "Logistics", "Freight quotes in 90 seconds", "Compare 40 carriers on price and transit, book and label in one flow."),
    ("Dockside", "Logistics", "Warehouse slots without the emails", "Carriers self-book dock appointments that respect your labor plan."),
    ("Freskeep", "Logistics", "Cold chain you can prove", "Per-mile temperature logs, alerts and audit-ready exports for every load."),
    # HR & Recruiting
    ("Hirely", "HR & Recruiting", "Shortlists by lunchtime", "AI-ranked applicants against your rubric, with structured interview kits attached."),
    ("Onboardly", "HR & Recruiting", "Day one, done right", "Accounts, paperwork, swag and buddy pairing sequenced automatically."),
    ("Paycycle", "HR & Recruiting", "Payroll that never misses Friday", "Taxes, deductions and filings handled; payslips land before the weekend."),
    ("Shiftly", "HR & Recruiting", "Shift swaps without the group chat", "Employees trade shifts under your rules; managers just approve."),
    # Climate & Energy
    ("Solarscore", "Climate & Energy", "Know your roof's solar payoff", "Satellite analysis and bill modeling give payback math before any salesperson calls."),
    ("Carbonkit", "Climate & Energy", "Measure your footprint in a day", "Connect your utilities and accounting; get a board-ready emissions report."),
    ("Wattwise", "Climate & Energy", "Cut your energy bill on autopilot", "Load shifting, tariff switching and battery control — set it and forget it."),
    ("Grovefund", "Climate & Energy", "Forests, funded by spare change", "Round up purchases to plant and protect verified native forests."),
    # Crypto & Web3
    ("Blockloom", "Crypto & Web3", "Self-custody, simplified", "A wallet that recovers gracefully, simulates every transaction and explains what you're signing."),
    ("Yieldport", "Crypto & Web3", "Staking across chains, one view", "Delegate, track rewards and see slashing risk across a dozen networks."),
    ("Mintly", "Crypto & Web3", "Launch a collection this weekend", "Contract templates, allowlists, reveal mechanics and royalties — no Solidity required."),
    ("Chainproof", "Crypto & Web3", "Audit-grade contract reviews", "Static analysis plus human review, with fixes your devs can ship the same day."),
    # Marketing
    ("Funnelio", "Marketing", "Funnels that fix themselves", "Every step instrumented; the leaky one gets a diagnosis and a suggested test."),
    ("Mailbloom", "Marketing", "Email campaigns people open", "Subject lines tested against your history, send times tuned per subscriber."),
    ("Postpilot", "Marketing", "A month of content, one afternoon", "Plan, draft and schedule 30 on-brand posts across every channel."),
    ("Referralloop", "Marketing", "Turn customers into your sales team", "Double-sided rewards, fraud protection and viral loops configured in minutes."),
    # Developer Tools
    ("Deploymint", "Developer Tools", "Preview deploys for every branch", "Full-stack previews with seeded databases and shareable URLs, on every push."),
    ("Queuely", "Developer Tools", "Background jobs without the babysitting", "Queues, retries, schedules and observability — no worker boxes to patch."),
    ("Schemaflow", "Developer Tools", "Database migrations without dread", "Reviewed, staged and reversible schema changes that ship with your code."),
    ("Tracehawk", "Developer Tools", "Find the bug before the user does", "Distributed tracing with one-click paths from slow request to failing query."),
    # Hospitality
    ("Innkeep", "Hospitality", "Direct bookings, fewer commissions", "A fast booking engine, rate parity tools and email capture that beats the OTAs."),
    ("Menucraft", "Hospitality", "Menus that design themselves", "Seasonal menus laid out beautifully from your item data — print and digital."),
    ("Eventide", "Hospitality", "Event planning minus the spreadsheets", "Timelines, vendors and floor plans for weddings and conferences in one place."),
    ("Guestly", "Hospitality", "Five-star stays start at check-in", "Contactless arrival, one guest inbox and issues surfaced before checkout."),
    # Pets
    ("Pawtrack", "Pets", "Know where they roam", "Swim-proof GPS collars with geofence alerts and 10-day battery."),
    ("Vetnote", "Pets", "Vet records in one place", "Vaccines, meds and weights on a shareable timeline every clinic can read."),
    ("Wagpay", "Pets", "Pet care subscriptions that stick", "Grooming, walking and food on one schedule your pets — and calendar — love."),
    ("Whiskerfeed", "Pets", "Meals portioned by science", "Feeding plans from breed, age and vet guidance, with the bowl to prove it."),
]


def slugify(name: str) -> str:
    return name.lower().replace(" ", "").replace("&", "and").replace("+", "plus")

# ---- expansion pack: 25 more sectors / 100 more brands (see data2.py) ----
from data2 import EXTRA_SECTORS, EXTRA_BRANDS  # noqa: E402

SECTORS.update(EXTRA_SECTORS)
BRANDS.extend(EXTRA_BRANDS)

# ---- expansion pack 3: 25 more sectors / 100 more brands (see data3.py) ----
from data3 import EXTRA3_SECTORS, EXTRA3_BRANDS  # noqa: E402

SECTORS.update(EXTRA3_SECTORS)
BRANDS.extend(EXTRA3_BRANDS)

# ---- expansion pack 4+5: 50 more sectors / 200 more brands ----
from data4 import EXTRA4_SECTORS, EXTRA4_BRANDS  # noqa: E402
from data5 import EXTRA5_SECTORS, EXTRA5_BRANDS  # noqa: E402

SECTORS.update(EXTRA4_SECTORS)
SECTORS.update(EXTRA5_SECTORS)
BRANDS.extend(EXTRA4_BRANDS)
BRANDS.extend(EXTRA5_BRANDS)

# ---- expansion packs 6-10: 250 lite sectors / 1000 brands ----
# Lite sectors hand-write the unique parts (name, audience, a few features,
# brands + headlines) and borrow stats/plans/testimonials/FAQs from an
# archetype, so 1000 pages stay varied without 250 hand-built copy banks.
import zlib  # noqa: E402
from archetypes import ARCHETYPES, LOGO_POOL  # noqa: E402
from data6 import LITE6  # noqa: E402
from data7 import LITE7  # noqa: E402
from data8 import LITE8  # noqa: E402
from data9 import LITE9  # noqa: E402
from data10 import LITE10  # noqa: E402

for _lite in (LITE6, LITE7, LITE8, LITE9, LITE10):
    for (_name, _icon, _acc, _acc2, _aud, _arch, _feats, _brands) in _lite:
        assert _name not in SECTORS, f"duplicate sector: {_name}"
        _A = ARCHETYPES[_arch]
        _h = zlib.crc32(_name.encode())
        _fill = lambda s: s.format(audience=_aud, name=_name)  # noqa: E731
        features = list(_feats)
        for emoji, t, d in _A["generic"]:
            features.append((emoji, _fill(t), _fill(d)))
        stats = [(n, _fill(l)) for n, l in _A["stats"]]
        scale = 0.8 + (_h % 5) * 0.2
        plans = []
        for pn, p, blurb in _A["plans"]:
            if isinstance(p, int) and p > 0:
                p = int(round(p * scale / 5.0)) * 5 if p >= 20 else int(round(p * scale))
            plans.append((pn, p, _fill(blurb)))
        testimonials = [(q, n, _fill(r)) for q, n, r in _A["testimonials"]]
        faqs = [(_fill(q), _fill(a)) for q, a in _A["faqs"]]
        logos = [LOGO_POOL[(_h + i * 7) % len(LOGO_POOL)] for i in range(5)]
        SECTORS[_name] = dict(icon=_icon, accent=_acc, accent2=_acc2, audience=_aud,
                              features=features, stats=stats, plans=plans,
                              testimonials=testimonials, faqs=faqs, logos=logos)
        for (_bn, _bh, _bs) in _brands:
            BRANDS.append((_bn, _name, _bh, _bs))
