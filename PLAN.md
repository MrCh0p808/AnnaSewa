# AnnaSewa Terraform Infrastructure – Story
This file represents the **end-to-end story of AnnaSewa Infrastructure**, showing all components, workflows, Terraform state handling, provisioning phases, and lifecycle.

Imagine AnnaSewa infrastructure as a multi-phase journey:
### Phase 1 
Builds the roads and electricity (VPC, IGW, subnets, routes).
### Phase 2 
Brings the house and doors (EC2, security groups, SSH keys, elastic IP).
```mermaid
flowchart TD

    %% Users
    U["AnnaSewa Users"] -->|Access App| LB["Load Balancer (ALB / NLB)"]

    %% Phase 1: Networking
    subgraph Phase1 [Phase 1: VPC & Networking]
        VPC["VPC (CIDR Block)"]
        IGW["Internet Gateway"]
        RT["Route Table"]
        Subnet["Public Subnet(s)"]
        VPC --> IGW
        VPC --> Subnet
        Subnet --> RT
        IGW --> RT
    end

    %% Phase 2: Compute
    subgraph Phase2 [Phase 2: Compute & Security]
        SG["Security Group (22/80/443)"]
        EC2["EC2 Instance (App Server)"]
        EIP["Elastic IP"]
        SG --> EC2
        EC2 --> EIP
    end

    %% Storage / Future
    DB["Database (Future: RDS / DynamoDB)"]

    %% Linking phases
    LB --> EC2
    EC2 --> DB
    Subnet --> EC2
```
# AnnaSewa Terraform Elaborated: 
---

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
