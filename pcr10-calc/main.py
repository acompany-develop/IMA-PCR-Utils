import calculate_pcr10

# Path to IMA log
IMA_LOG_PATH = '/sys/kernel/security/ima/ascii_runtime_measurements'

if __name__ == "__main__":
    pcr_value = calculate_pcr10.get_pcr10_sha256(IMA_LOG_PATH)
    print(f"PCR 10 value: {pcr_value.hex().upper()}")
