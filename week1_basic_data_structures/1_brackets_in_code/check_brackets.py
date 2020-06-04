# python3

def find_mismatch(text):
    opening_brackets_stack = []
    for i, next in enumerate(text, 1):
        if next in "([{":
            opening_brackets_stack.append(next)
            last_unmatched_opening_bracket_index = i
        if next in ")]}":
            if len(opening_brackets_stack) == 0:
                return i
            
            current_match = opening_brackets_stack.pop() + next
            if current_match == "()" or current_match == "[]" or current_match == "{}":
                last_unmatched_opening_bracket_index -= 1
            else:
                return i

    if len(opening_brackets_stack) == 0:
        return "Success"
    else:
        return last_unmatched_opening_bracket_index

def main():
    text = input()
    mismatch = find_mismatch(text)
    # Printing answer, write your code here
    print(mismatch)

if __name__ == "__main__":
    main()
