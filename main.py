import os
from moralis import evm_api

API_KEY = os.environ['api_key']

with open('input.txt', 'r') as file:
    lines = [line.rstrip('\n').rstrip(' ') for line in file]
    for lineIndex in range(len(lines)):
        print(lines[lineIndex])
        params = {
            "address": lines[lineIndex],
            "chain": "bsc"
        }
        result = evm_api.token.get_wallet_token_balances(api_key=API_KEY, params=params)
        print(result)
        with open(f'results{lineIndex+1}.txt', 'w') as f:
            for token in range(len(result)):
                f.write(f"{result[token]['symbol']}: {result[token]['balance']}\n")