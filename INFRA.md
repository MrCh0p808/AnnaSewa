# AnnaSewa - Story
This file represents the **end-to-end story of AnnaSewa Infrastructure**, showing all components, architecture, workflows, Terraform state handling, provisioning phases, and lifecycle.

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
Imagine AnnaSewa infrastructure as a multi-phase journey:
### *Phase 1* : Builds the foundation (VPC, IGW, subnets, routes).
### *Phase 2* : Brings the essentials (EC2, security groups, SSH keys, elastic IP).

# AnnaSewa Terraform Elaborated: 
```mermaid
flowchart TD
    %% Developer and Repo
    Dev["AnnaSewa Developer"] --> Repo["AnnaSewa Repository"]
    Repo -->|Writes Terraform Code| TFCLI["Terraform CLI"]
    TFCLI --> S3["S3 Bucket: Terraform State"]
    TFCLI --> DDB["DynamoDB: State Locking"]

    %% Phase 1: Networking
    subgraph Phase1 [Phase 1: Networking Foundations]
        VPC["Create VPC"]
        Subnet["Create Subnet(s)"]
        IGW["Create Internet Gateway"]
        RT["Create Route Table"]

        VPC --> Subnet
        VPC --> IGW
        Subnet --> RT
        IGW --> RT
    end

    %% Phase 2: Compute
    subgraph Phase2 [Phase 2: Compute & Access]
        TLS["Generate TLS Key Pair"]
        AWSKey["Upload AWS Key Pair"]
        SG["Create Security Group (22, 80, 443)"]
        EC2["Launch EC2 Instance (App Server)"]
        EIP["Allocate Elastic IP"]

        TLS --> AWSKey
        AWSKey --> EC2
        SG --> EC2
        EIP --> EC2
    end

    %% SSH Access
    PEM["Private Key (.pem)"] -->|ssh -i key.pem| EC2

    %% User Flow
    User["AnnaSewa End User"] -->|HTTP/HTTPS| EIP
    EIP --> EC2

    %% Terraform Lifecycle
    subgraph Workflow [Terraform Workflow]
        Init["terraform init"]
        Plan["terraform plan"]
        Apply["terraform apply"]
        Destroy["terraform destroy"]
        TFCLI --> Init
        TFCLI --> Plan
        TFCLI --> Apply
        TFCLI --> Destroy
    end
```
