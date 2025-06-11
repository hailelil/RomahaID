Romaha ID — Digital Identity & Access Management (IAM) Platform

⸻

Romaha ID is a modern, secure, microservice-based Digital Identity & Access Management (IAM) platform designed to serve:

✅ Government Agencies

✅ Banks & Financial Sector

✅ Health Sector

✅ Enterprises & Organizations

Built with modularity, security, and scalability in mind, Romaha ID aims to provide:

✅ Identity Registration → SPA + API

✅ Identity Verification → public APIs + QR-based

✅ Identity Card Generation → PDF / Smartcard

✅ OAuth2 / OIDC / SAML → modern access federation

✅ Strong Authentication → extensible to Mobile ID / Bank ID / MFA

⸻

Project Status

🟢 Version → v1.0-planning

🟢 Architecture Blueprint → completed

🟢 Roadmap.md → defined

🟢 Docs folder → initialized

⸻

Architecture Principles

✅ Microservice-based → each major capability is a standalone service

✅ Modular → components can evolve independently

✅ Open standards → OAuth2, OpenID Connect, SAML

✅ Modern UX → responsive SPA → mobile first

✅ CI/CD → automated pipelines from Day 1

✅ Documentation → versioned with code

✅ Infrastructure as Code → Docker, Kubernetes

⸻

Project Structure
RomahaID/
├── docs/                    → Documentation (Architecture, Roadmap, API specs, UX, Legal)
├── services/
│   ├── marda-identity/      → Core Identity Microservice
│   ├── senai-profile/       → Profile Photo & Data Microservice
│   ├── honey-card-generator/→ Card Generator Microservice (PDF / Smartcard)
│   ├── honey-verify/        → Verification Microservice (QR API, Verify APIs)
│   ├── roman-auth-server/   → OAuth2 / OIDC / SAML Identity Provider
├── gateway/                 → API Gateway config
├── frontend/                → SPA → React → Registration / Profile / Admin Portal
├── deployment/              → Docker Compose / K8s manifests
├── tests/                   → Integration & E2E tests
├── scripts/                 → Utility scripts (docs scaffolding, migrations, etc)
├── README.md
└── .gitignore

Key Features (MVP Target)

✅ Identity Registration → clean SPA → cross-device
✅ Profile Management → with photo + profile data
✅ Address & Family Relationships → linked data
✅ Identity Card Generation → Driver’s License style PDF → with QR
✅ Public Verification API → for Banks / Gov / Health
✅ OAuth2 / OIDC Server → Single Sign-On for connected Apps
✅ SAML IDP → for legacy integrations
✅ Audit Logging → for compliance
✅ API Gateway → single secured entry point

⸻

Roadmap — High-Level

✅ Foundation → Identity, Profile, Card, Verification → initial MS
✅ IAM Layer → OAuth2 / OIDC → SAML
✅ Strong Auth → Mobile ID, Bank ID
✅ Production Readiness → CI/CD, TLS, K8s
✅ Extensions → MFA, Biometrics
✅ Federation → External Identity sources
✅ Reporting → Auditing & Metrics

👉 See: docs/roadmap.md

⸻

Customers / Use Cases

✅ Government → Civil ID systems → eGov services
✅ Banks → Customer Identity verification → KYC / onboarding
✅ Health → Patient Identity verification → eHealth / portability
✅ Enterprises → Employee Identity → SSO across systems

⸻

Project Values

✅ Open Standards
✅ Modularity → evolve one piece at a time
✅ Transparency → documented, versioned
✅ Security → built in from day 1
✅ Quality → CI/CD, Tests → automated pipelines
✅ Scalability → ready to grow

⸻

Contributing

✅ Contribution guide → will be added to docs/contributing.md

✅ Community contributions are welcome → review process in place.

⸻

License

✅ Project license → TBD → proposed: Apache 2.0 OR MIT.

Maintainers

Haileslassie Lilay Desalegn
