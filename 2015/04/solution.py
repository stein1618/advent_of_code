import hashlib

def find_lowest_number(secret_key, prefix):
    number = 0
    
    while True:
        input_string = secret_key + str(number)
        md5_hash = hashlib.md5(input_string.encode()).hexdigest()
        
        if md5_hash.startswith(prefix):
            return number
        
        number += 1

def main():
    secret_key = "ckczppom"
    prefix = "00000"   # Part 1
    prefix = "000000"  # Part 2
    
    lowest_number = find_lowest_number(secret_key, prefix)
    
    print(f"The lowest number that produces an MD5 hash with prefix '{prefix}' is {lowest_number}.")

if __name__ == "__main__":
    main()