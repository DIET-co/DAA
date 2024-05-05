function KMP(text, pattern):
    failure_table = compute_failure_table(pattern)  // Preprocess the pattern to construct the failure table
    i = 0  // Index for text
    j = 0  // Index for pattern
    while i < length(text):  // Iterate through the text
        if text[i] == pattern[j]:  // If characters match
            if j == length(pattern) - 1:  // If end of pattern reached
                return i - j  // Match found, return starting index of match
            i++  // Move to next character in text
            j++  // Move to next character in pattern
        else:
            if j != 0:  // If a partial match occurred
                j = failure_table[j - 1]  // Adjust pattern index based on failure table
            else:
                i++  // Move to next character in text
    return -1  // Match not found, return -1

function compute_failure_table(pattern):
    failure_table = array of length equal to pattern length  // Initialize failure table
    failure_table[0] = 0  // First value is always 0
    j = 0  // Index for pattern
    for i from 1 to length(pattern) - 1:  // Iterate through pattern
        if pattern[i] == pattern[j]:  // If characters match
            failure_table[i] = j + 1  // Set next value in failure table
            j++  // Move to next character in pattern
        else:
            while j > 0 and pattern[i] != pattern[j]:  // Loop until partial match is found
                j = failure_table[j - 1]  // Adjust pattern index based on failure table
            if pattern[i] == pattern[j]:  // If partial match found
                failure_table[i] = j + 1  // Set next value in failure table
                j++  // Move to next character in pattern
            else:
                failure_table[i] = 0  // No partial match, set value to 0
    return failure_table  // Return failure table
