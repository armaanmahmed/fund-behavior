"""AI stock classifications for 13F analysis."""
# TODO: update with more stocks and possibly refactor classifications

AI_STOCKS = {
    "ai_semiconductors": [
        "NVDA",   # NVIDIA - $4.57T - GPUs, data center accelerators
        "AMD",    # AMD - $350B - MI300X accelerators, ROCm
        "AVGO",   # Broadcom - $1.65T - Custom AI chips (ASICs)
        "TSM",    # TSMC - $1.53T - AI chip manufacturing
        "ASML",   # ASML - $312B - EUV lithography equipment
        "MU",     # Micron - $85B - High-bandwidth memory
        "INTC",   # Intel - $90B - Gaudi accelerators
    ],
    
    "ai_cloud_infrastructure": [
        "MSFT",   # Microsoft - $3.51T - Azure AI, Copilot, OpenAI partnership
        "GOOGL",  # Alphabet - $3.80T - Google Cloud, Gemini, DeepMind
        "AMZN",   # Amazon - $2.5T - AWS Bedrock, Amazon Q, Anthropic
        "ORCL",   # Oracle - $558B - OCI Gen AI, Stargate Project
    ],
    
    "enterprise_ai_platforms": [
        "PLTR",   # Palantir - $417B - AIP, Foundry, Gotham
        "AI"     # C3.ai - $2.5B - Enterprise AI applications
    ],
    
    "ai_enhanced_saas": [
        "CRM",    # Salesforce - $238B - Agentforce, Einstein
        "NOW",    # ServiceNow - $153B - Now Assist, AI Agents
    ],
    
    "ai_data_platforms": [
        "SNOW"   # Snowflake - $77B - Cortex AI, Arctic LLM
    ],
    
    "consumer_ai_applications": [
        "META",   # Meta - $1.66T - Llama, Meta AI, recommendation systems
        "DUOL",   # Duolingo - $8.5B - GPT integration, Birdbrain
        "ADBE",   # Adobe - $190B - Firefly generative AI
    ],
    
    "ai_robotics_autonomy": [
        "TSLA",   # Tesla - $1.48T - FSD, Optimus, Robotaxi
    ],
    
    "ai_hardware_infrastructure": [
        "ANET",   # Arista Networks - $165B - AI data center networking
        "DELL",   # Dell Technologies - $85B - AI servers
        "SMCI",   # Super Micro Computer - $26B - AI server systems
        "AMAT",   # Applied Materials - $145B - Chip manufacturing equipment
        "LRCX",   # Lam Research - $105B - Chip manufacturing equipment
        "KLAC",   # KLA Corporation - $90B - Semiconductor process control
        "QCOM",   # Qualcomm - $175B - Mobile/edge AI chips
    ],
}

# AI transition timeline (year each became "AI stock")
AI_TRANSITION_DATES = {
    "NVDA": "2023-05",   # May 2023 breakout earnings
    "AMD": "2023-12",    # MI300X launch
    "AVGO": "2023",      # Custom AI chip demand surge
    "TSM": "2023",       # AI chip manufacturing demand
    "ASML": "2023",      # AI chip equipment demand
    "MU": "2024",        # HBM demand for AI GPUs
    "INTC": "2023",      # Gaudi accelerator push
    "MSFT": "2023-01",   # $10B OpenAI investment
    "GOOGL": "2023-12",  # Gemini launch (always AI, rebranded)
    "AMZN": "2023-09",   # Bedrock GA + Anthropic
    "ORCL": "2024-06",   # OpenAI infrastructure deal
    "PLTR": "2023-04",   # AIP launch (always AI)
    "AI": "2009",        # Founded as AI company
    "CRM": "2023-03",    # Einstein GPT launch
    "NOW": "2023-09",    # Now Assist launch
    "SNOW": "2024-05",   # Cortex AI GA
    "META": "2023-07",   # Llama 2 open release
    "DUOL": "2023-03",   # GPT-4 integration
    "ADBE": "2023-03",   # Firefly launch
    "TSLA": "2024-04",   # Musk "AI company" declaration
    "ANET": "2023",      # AI data center networking demand
    "DELL": "2023",      # AI server demand
    "SMCI": "2023",      # AI server/cooling demand
    "AMAT": "2023",      # AI chip equipment demand
    "LRCX": "2023",      # AI chip equipment demand
    "KLAC": "2023",      # AI chip equipment demand
    "QCOM": "2023",      # On-device AI push
}

ALL_AI_TICKERS = set().union(*AI_STOCKS.values())