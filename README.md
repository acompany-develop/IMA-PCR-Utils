# IMA PCR10 Utils

## Usage

### Calculate PCR10 from IMA log

```bash
# Run on Azure VM with vTPM
# Calculate PCR10 from IMA log:
# /sys/kernel/security/ima/ascii_runtime_measurements
python3 pcr10-calc/main.py
```

### Compare the actual PCR10

```bash
sudo apt update
sudo apt install -y tpm2-tools
```

```bash
sudo tpm2_pcrread sha256:10
```