# Define the function
def cigar_party(cigars, is_weekend):
    if not is_weekend and 40 <= cigars <= 60:
        return True
    if is_weekend and 40 <= cigars:
        return True
    else:
        return False

# Call the function
cigar_party(35, False)
