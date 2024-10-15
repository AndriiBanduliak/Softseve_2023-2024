def Cipher_Zeroes(N):
    # Step 1: Count visible zeros
    visible_zeros = 0

    for char in N:
        if char == '0' or char == '6' or char == '9':
            visible_zeros += 1
        elif char == '8':
            visible_zeros += 2

    M = visible_zeros

    # Step 2: Determine Nicky's points based on M
    if M > 0 and M % 2 == 0:  # M is even and greater than 0
        M -= 1
    elif M % 2 == 1:          # M is odd
        M += 1

    # Step 3: Convert to binary
    return bin(M)[2:]  # Removing the '0b' prefix
