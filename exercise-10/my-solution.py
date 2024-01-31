def findAndReplace(text: str, oldText: str, newText: str):
  if len(text) == len(newText):
    if text == oldText:
      return newText

  first_match_pos = -1
  for x, old_char in enumerate(oldText):
    for y, text_char in enumerate(text):
      if ord(old_char) == ord(text_char):
        first_match_pos = x + y
        break
    if first_match_pos != -1: break
  
  if first_match_pos == -1:
    return text
  
  old_text_in_text = text[first_match_pos:first_match_pos + len(oldText)]
  found_old_text = False
  if old_text_in_text == oldText:
    found_old_text = True
  
  if not found_old_text:
    return

  old_string_head = text[0:first_match_pos]
  old_string_tail = text[first_match_pos + len(newText)::]
  new_string = old_string_head + newText + old_string_tail
  if len(old_string_tail) >= len(newText):
   return findAndReplace(new_string, oldText, newText)
  return new_string

assert findAndReplace('The fox', 'fox', 'dog') == 'The dog'
assert findAndReplace('fox', 'fox', 'dog') == 'dog'
assert findAndReplace('Firefox', 'fox', 'dog') == 'Firedog'
assert findAndReplace('foxfox', 'fox', 'dog') == 'dogdog'
print(findAndReplace('The Fox and fox.', 'fox', 'dog'))
assert findAndReplace('The Fox and fox.', 'fox', 'dog') == 'The Fox and dog.'
print('worked!')