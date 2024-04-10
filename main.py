# Example project suitable for registration with tea Protocol

# Project name
project_name = "tea-protocol-registration"

# Digital wallet addresses of developers or project maintainers
digital_wallet_addresses = {
    "developer1": "0x1234567890abcdef",
    "developer2": "0xabcdef1234567890",
    # Add addresses as needed
}

# Quorum: number of approvals required for any treasury transaction to complete
quorum = 2

def main():
    print("Project successfully registered with tea Protocol")
    print(f"Project name: {project_name}")
    print("Digital wallet addresses of developers or project maintainers:")
    for developer, address in digital_wallet_addresses.items():
        print(f"{developer}: {address}")
    print(f"Quorum: {quorum}")

if __name__ == "__main__":
    main()
