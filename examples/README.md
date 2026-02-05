# Example CLI tools using imapcr10

## Usage

### Common

```shell
python $SCRIPT_PATH [OPTIONS...]
```

or

```shell
$SCRIPT_PATH [OPTIONS...]
```

## pcr10

### Usage

```shell
python pcr10.py [-i $IMA_LOG_PATH] [-a $HASH_ALGORITHM] [-o $OUTPUT_PATH] [-f $OUTPUT_FORMAT]
```

```shell
python pcr10.py [--in $IMA_LOG_PATH] [--hash-algorithm $HASH_ALGORITHM] [--out $OUTPUT_PATH] [--format $OUTPUT_FORMAT]
```

### Options

- `-i, --in`: Path to the IMA log file (default: `/sys/kernel/security/ima/ascii_runtime_measurements`)
- `-a, --hash-algorithm`: Hash algorithm to use for PCR10 calculation: `sha1`, `sha256`, `sha384`, `sha512` (default: `sha256`)
- `-o, --out`: Path to the output file (default: stdout)
- `-f, --format`: Output format: `HEX`, `hex`, `binary` (default: `HEX`)

When using the default input, please run with root privileges in an environment where vTPM is available.

### Example

```shell
# Replay PCR10 from the IMA logs of the current system
python pcr10.py

# Replay PCR10 from the sample IMA log file
python pcr10.py -i ascii_runtime_measurements
```

## boot-aggregate

### Usage

```shell
python boot_aggregate.py -i $PCR_LIST_PATH -s $SELECTOR [-a $HASH_ALGORITHM] [-o $OUTPUT_PATH] [-f $OUTPUT_FORMAT]
```

```shell
python boot_aggregate.py --in $PCR_LIST_PATH --selector $SELECTOR [--hash-algorithm $HASH_ALGORITHM] [--out $OUTPUT_PATH] [--format $OUTPUT_FORMAT]
```

### Required Arguments

- `-i, --in`: Path to the PCR list file (raw blob). The file must be the concatenation of PCR digests for the indices specified by `--selector`, in the same order (each digest size is determined by the selector's hash algorithm).
- `-s, --selector`: PCR selector string: `<hash_algorithm>:all` or `<hash_algorithm>:0,1,2,...` (must include 0 to 9)

### Options

- `-a, --hash-algorithm`: Hash algorithm to use to calculate boot_aggregate: `sha1`, `sha256`, `sha384`, `sha512` (default: `sha256`)
- `-o, --out`: Path to the output file (default: stdout)
- `-f, --format`: Output format: `HEX`, `hex`, `binary` (default: `hex`)

### Example

```shell
# Calculate boot_aggregate from the sample PCR list file
python boot_aggregate.py --in pcr_list.bin -s sha256:0,1,2,3,4,5,6,7,8,9,10,12,14,23
```
