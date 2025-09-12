# 🍲 AnnaSewa — Surplus Food Donation Platform

AnnaSewa (अन्नसेवा) is a mission-driven platform that connects people and organizations with surplus food to underprivileged communities.  
It aims to reduce food waste, fight hunger, and create stronger, more compassionate societies.

---

## 🌍 Why AnnaSewa?

### Hunger Snapshot in India

- **India ranks 105th out of 127 countries** in the **Global Hunger Index (2024)** — classified as *“serious”*.  
- **13.7%** of the population is undernourished.  
- **35.5%** of children under 5 suffer from stunting.  
- **18.7%** of children under 5 are wasted (low weight for height).  
- **2.9%** under-five mortality rate.  

*(Source: [Global Hunger Index 2024](https://www.globalhungerindex.org/india.html))*  

### Why Food Donation Platforms?

- Prevents **food waste** from restaurants, events, and households.  
- Provides **nutritious meals** to the needy.  
- Reduces **environmental impact** (less food in landfills → lower methane emissions).  
- Builds **community resilience** by empowering local food networks.  

---

## 💡 The AnnaSewa Idea

AnnaSewa is designed as a **cloud-native, microservices-based donation platform** where:

- **Donors** (restaurants, households, stores) can list surplus food.  
- **Receivers** (NGOs, shelters, individuals) can request or collect food.  
- **Admins** can monitor donations, impact, and logistics.  
- **Impact tracking** shows meals served, people helped, and food waste reduced.  

---

## 🏗️ Architecture & Tech Stack

| Layer | Technologies |
|-------|--------------|
| **Frontend** | React (Next.js), TailwindCSS |
| **Backend** | Python (FastAPI), REST APIs |
| **Databases** | PostgreSQL (users, donations, reports), DynamoDB (state locks, fast lookups) |
| **Infrastructure** | AWS (EC2, VPC, IAM, S3, RDS, EKS) |
| **IaC** | Terraform (state in S3, lock in DynamoDB) |
| **Containers** | Docker, Kubernetes (EKS) |
| **CI/CD** | GitHub Actions |
| **Security** | JWT Auth, IAM Roles, Security Groups, Secrets Manager |
| **Monitoring** | CloudWatch, Prometheus, Grafana |

---

## 📂 Project Structure

```text
AnnaSewa/
├── infrastructure/           # Terraform scripts for AWS infra
│   ├── main.tf
│   ├── variables.tf
│   ├── outputs.tf
│   └── modules/
│
├── backend/                  # Python FastAPI services
│   ├── auth/                 # Authentication & authorization
│   ├── donation/             # Food donation service
│   ├── distribution/         # Matching donors & receivers
│   ├── impact/               # Analytics & reports
│   └── gateway/              # API gateway / service router
│
├── frontend/                 # React (Next.js) web app
│   ├── components/
│   ├── pages/
│   ├── services/
│   └── styles/
│
├── scripts/                  # Utility scripts (DB migrations, setup)
├── tests/                    # Unit & integration tests
├── docs/                     # Documentation & diagrams
│   ├── architecture.md
│   ├── annasewa-diagram.png
│   └── api-specs.md
│
├── .github/workflows/        # CI/CD pipelines (GitHub Actions)
├── docker-compose.yml        # Local dev environment
├── README.md                 # Project overview
└── LICENSE
```
## 🔑 Key Features

- 👥 **User Management** — Role-based access (Donor, Receiver, Admin)  
- 📦 **Food Donation Listings** — Donors can post surplus food with quantity, expiry, and pickup details  
- 🔒 **Secure APIs** — Authentication (JWT), AWS IAM roles, Secrets Manager  
- 📊 **Impact Dashboard** — Track meals served, food waste prevented, CO₂ emissions saved  
- 🔔 **Notifications** — Email & SMS reminders for donors and receivers  
- 📱 **Responsive Web UI** — Optimized for NGOs, donors, and individuals on any device  
- 🌍 **Scalable Infra** — AWS VPC, EC2, RDS, S3, Terraform-managed infrastructure  
- 📦 **CI/CD** — Automated pipelines with GitHub Actions & Docker  

---

## 🚀 How It Works

1. **Donor Registers Food**  
   - Inputs: food type, quantity, expiry, pickup location.  

2. **AnnaSewa Matches Receiver**  
   - NGOs, shelters, or individuals in need.  

3. **Notification Sent**  
   - Receiver gets alert → confirms pickup.  

4. **Food Delivery / Collection**  
   - Volunteer / NGO picks up food.  

5. **Impact Recorded**  
   - Meals served, waste prevented, analytics updated.  

---

## 🔭 Future Roadmap

- 📱 **Mobile Apps** — Native Android/iOS versions for broader accessibility  
- 🗺️ **Map Integration** — Real-time pickup & delivery tracking  
- 📷 **Image Uploads** — Donors can upload photos of food for verification  
- 🤝 **Partnerships** — Integration with NGOs, delivery services, and local authorities  
- 🤖 **AI Predictions** — Smart demand forecasting & logistics optimization  
- ♻️ **Sustainability Metrics** — Tracking carbon footprint reduction  

---

## 🤝 Contribution

We welcome contributions from developers, NGOs, and organizations passionate about fighting hunger.  

### Steps to Contribute:
1. 🍴 **Fork** this repository  
2. 📥 **Clone** locally and set up the dev environment  
3. 🌱 Create a **feature branch**  
4. ✅ Write tests and ensure linting passes  
5. 🔄 Submit a **Pull Request (PR)** for review  

---

## 📜 License

This project is licensed under the **MIT License**.  
You are free to use, modify, and distribute it as long as the license terms are respected.  

---

## 📈 References

- [Global Hunger Index 2024 – India](https://www.globalhungerindex.org/india.html)  
- [Food Banking & Food Waste Studies](https://www.foodbanking.org/reducing-food-loss-and-waste/)  
- [FAO Report on Hunger & Food Waste](https://www.fao.org/platform-food-loss-waste/en/)  

---

> ✨ *AnnaSewa turns surplus into service, and hunger into hope.* 🍲
