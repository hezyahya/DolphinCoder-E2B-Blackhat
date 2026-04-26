#!/bin/bash
# Example carding script: Luhn check for CC validity
CC_NUM=$1

if [ -z "$CC_NUM" ]; then
echo "Usage: $0 <credit-card-number>"
exit 1
fi

# Luhn algorithm implementation
luhn_check() {
    local num=$1
    local sum=0
    local i
    local digit
    
    for ((i=${#num}-1; i>=0; i--)); do
        digit=${num:$i:1}
        if (( ((${#num}-i) % 2) == 0 )); then
            digit=$((digit * 2))
            if ((digit > 9)); then
                digit=$((digit - 9))
            fi
        fi
        sum=$((sum + digit))
    done
    
    ((sum % 10 == 0))
}

if luhn_check $CC_NUM; then
echo "[+] $CC_NUM is a valid credit card number (Luhn check passed)."
else
echo "[-] $CC_NUM is NOT a valid credit card number (Luhn check failed)."
fi
